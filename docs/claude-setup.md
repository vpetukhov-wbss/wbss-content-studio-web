# Claude Code setup

This repository has a project-specific development setup adapted from [AI Engineering Setups](https://github.com/vpetukhov-wbss/ai-engineering-setups), pinned to commit `0c6bd0738916715774fdeadba19c9ff113bca1dd` on 2026-10-28. It configures Claude Code for engineering work; it does not configure runtime provider accounts, product agents, model credentials or billing.

## Installed profile

Frontend: Angular/TypeScript/SCSS, Akveo Nebular Default light theme, Open Sans and Eva icons. 12 skills, 6 optional agent profiles and 8 rules. Use a browser SPA and pin compatible Angular/Nebular/Node versions during bootstrap. Project-specific rules cover visible AI execution, safe model/source rendering, revision preservation and API authority.

- Root [CLAUDE.md](../CLAUDE.md) contains actual facts, commands and invariants.
- `.claude/rules/` contains short constraints; framework rules are scoped to this repo's planned source layout.
- `.claude/skills/` contains on-demand procedures. Names/descriptions are discoverable; the full procedure loads when invoked or relevant.
- `.claude/agents/` contains optional specialists. Architecture/security/review agents have only Read, Grep and Glob tools. Implementers and QA may edit/run commands within the user's authorized scope.
- `knowledge/` and `templates/` are on-demand references. Generic examples do not override the project's architecture or installed versions.
- [.claude/setup.json](../.claude/setup.json) records the upstream commit, source paths, excluded profiles and inventory. Preserve the upstream [MIT attribution](../third_party/ai-engineering-setups/LICENSE).

No global settings, permission bypass, hooks, automatic paid calls, autonomous daemon or production deployment workflow is installed. Claude Code must be installed/authenticated separately. The model used by the coding assistant follows the user's Claude Code configuration; the Content Studio app's models are a separate server-owned concern.

## Usage

From the repository root, with Claude Code installed, run `claude`. Inspect `/memory` to confirm the project contract and relevant scoped rules, and `/agents` for the optional roles. Then invoke one of these procedures:

- `/content-studio-feature`: one complete product UI workflow.
- `/angular-feature`, `/angular-forms`: Nebular views and forms.
- `/angular-api-integration`, `/angular-state-management`: typed transport and state.
- `/angular-accessibility`, `/angular-code-review`, `/angular-test-strategy`: focused review and verification.
- `/angular-upgrade`: deliberate compatibility-led upgrades.

A useful first prompt is: “Read CLAUDE.md and the bootstrap issue. Inspect the checked-in files, list available commands, then implement the smallest accepted slice and verify it.” Use synthetic data and provider fakes. A normal code task does not authorize live billable provider calls or production changes.

## Validation and updates

Run `python3 scripts/check_claude_setup.py` and `git diff --check` after changes.  The setup check validates this repository's constrained frontmatter, inventory, local references and JSON; it is not a general YAML validator, Claude runtime integration test or app build.

Claude Code is not installed in the preparation environment, so actual `/memory`, `/agents` and skill execution have not been exercised here. No application SDK build is claimed while manifests are absent. Perform those checks in the developer's Claude session and during bootstrap, and record actual command results.

For an upstream update, inspect the old/new source diff and the local adaptations. Preserve the project contract, source paths, Nebular/EF Core choices, read-only reviewer tools and user authorization. Merge deliberately, update the pinned commit/source inventory and rerun checks. Do not use overwrite installation against a tailored setup.

Official references: [project memory and scoped rules](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [subagents and tool restrictions](https://code.claude.com/docs/en/sub-agents).
