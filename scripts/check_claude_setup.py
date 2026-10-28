"""Check this repository's constrained Claude metadata and local references.

Uses Python's standard library. Frontmatter intentionally supports the simple
scalar/list format checked into these repos, rather than arbitrary YAML.
This is a structural check, not a Claude session or application build.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(path, message):
    errors.append(f'{path.relative_to(ROOT)}: {message}')


def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        fail(path, 'missing frontmatter')
        return {}
    header = text[4:].split('\n---\n', 1)[0]
    values, current = {}, None
    for line in header.splitlines():
        if not line.strip():
            continue
        item = re.fullmatch(r'  - (.+)', line)
        if item and current and isinstance(values[current], list):
            try:
                values[current].append(json.loads(item[1]))
            except ValueError:
                fail(path, 'list entries must be JSON-compatible quoted strings')
            continue
        field = re.fullmatch(r'([a-zA-Z][a-zA-Z-]*):\s*(.*)', line)
        if not field:
            fail(path, 'unsupported or malformed frontmatter line')
            continue
        current, value = field.groups()
        if current in values:
            fail(path, f'duplicate key {current}')
        if not value:
            values[current] = []
        elif value.startswith('"'):
            try:
                values[current] = json.loads(value)
            except ValueError:
                fail(path, f'invalid quoted value for {current}')
        else:
            values[current] = value
    return values


for required in ['CLAUDE.md', 'AGENTS.md', '.claude/setup.json', 'docs/claude-setup.md',
                 'third_party/ai-engineering-setups/LICENSE']:
    if not (ROOT / required).is_file():
        errors.append(f'Missing required setup file: {required}')

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    if not text.endswith('\n'):
        fail(path, 'missing final newline')
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s)]+)\)', text):
        parsed = urlsplit(target.strip('<>'))
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        dest = (path.parent / unquote(parsed.path)).resolve()
        if not dest.is_relative_to(ROOT) or not dest.exists():
            fail(path, f'invalid local link {target}')
    if '.claude' in path.parts:
        for reference in re.findall(r'`((?:knowledge|templates)/[^`\n]+\.md)`', text):
            if not (ROOT / reference).is_file():
                fail(path, f'missing repository-root reference {reference}')

for path in ROOT.rglob('*.json'):
    if '.git' in path.parts:
        continue
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, UnicodeError) as exc:
        fail(path, str(exc))

skills = list((ROOT / '.claude/skills').glob('*/SKILL.md'))
agents = list((ROOT / '.claude/agents').glob('*.md'))
rules = list((ROOT / '.claude/rules').glob('*.md'))
for path in skills + agents:
    data = frontmatter(path)
    expected = path.parent.name if path.name == 'SKILL.md' else path.stem
    if data.get('name') != expected or not re.fullmatch('[a-z0-9-]+', expected):
        fail(path, 'name must match its skill directory or agent filename')
    if not isinstance(data.get('description'), str) or not data['description'].strip():
        fail(path, 'missing description')
    if path in agents:
        tools = {x.strip() for x in str(data.get('tools', '')).split(',') if x.strip()}
        if not tools or not tools <= {'Read', 'Grep', 'Glob', 'Edit', 'Write', 'Bash'}:
            fail(path, 'missing or unsupported explicit tool list')
        if any(role in expected for role in ['auditor', 'reviewer', 'architect']):
            if not tools <= {'Read', 'Grep', 'Glob'}:
                fail(path, 'advisory reviewer must have read-only tools')

for path in rules:
    if not path.read_text(encoding='utf-8').startswith('---\n'):
        continue
    data = frontmatter(path)
    paths = data.get('paths')
    if set(data) != {'paths'} or not isinstance(paths, list) or not paths:
        fail(path, 'scoped rule must have a nonempty paths list')
    elif any(not isinstance(p, str) or p.startswith('/') or '..' in p.split('/') for p in paths):
        fail(path, 'rule paths must be relative repository globs')

metadata = ROOT / '.claude/setup.json'
if metadata.is_file():
    try:
        setup = json.loads(metadata.read_text(encoding='utf-8'))
        if not re.fullmatch('[0-9a-f]{40}', setup.get('sourceCommit', '')):
            fail(metadata, 'upstream commit must be pinned')
        for item in setup.get('sourceFiles', []):
            path = (ROOT / item['path']).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                fail(metadata, f'missing imported file {item["path"]}')
        for key, actual in [('skills', len(skills)), ('agents', len(agents)), ('rules', len(rules))]:
            if setup.get('installedCounts', {}).get(key) != actual:
                fail(metadata, f'{key} inventory differs from installed setup')
    except (ValueError, KeyError) as exc:
        fail(metadata, str(exc))

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'OK: Claude setup, {len(skills)} skills, {len(agents)} agents, {len(rules)} rules; local references and JSON')
