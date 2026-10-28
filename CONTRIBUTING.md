# Contributing

Start from a focused issue and read [CLAUDE.md](CLAUDE.md). Keep changes small and record relevant behaviour and API compatibility. Respect Angular/Nebular compatibility and existing version pins; do not introduce framework migrations or another UI library incidentally.

Run `python3 scripts/check_claude_setup.py` and `git diff --check`. Once the application exists, run its documented type/template, lint, test and build checks appropriate to the change. Report exact results and skipped checks. Use synthetic fixtures; no real credentials, customer sources or production exports in issues, commits or test data.

Imported Claude setup files are adapted from a pinned upstream version. Review changes deliberately and preserve attribution; do not blindly run an overwrite installer. Contributions are provided under the repository's [MIT license](LICENSE).
