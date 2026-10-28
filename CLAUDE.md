# Content Studio Web — engineering contract

## Repository facts

Public MIT-licensed Angular frontend for Content Studio. This repository currently contains the Claude engineering setup and implementation specifications. There is no Angular application, package manifest, lockfile, installed UI library or running AI integration yet.

Selected UI: Angular, TypeScript, SCSS, Akveo Nebular Default light theme, Open Sans and Eva outline icons. Pin a mutually compatible Angular/Nebular/Node combination before using version-specific APIs. Start with a browser SPA, feature-oriented lazy routes and local signals/computed where the selected Angular version supports them; use RxJS for asynchronous streams and cancellation.

The backend is developed separately. It owns identity/workspace authorization, AI/provider keys, model capability checks, budgets, immutable revisions, approval and publishing. This client consumes an explicit versioned HTTP contract; client guards and buttons are not authorization boundaries. See [architecture](docs/architecture.md), [API boundary](docs/api-boundary.md) and [UI flows](docs/ui.md).

## Available commands

```bash
python3 scripts/check_claude_setup.py
git diff --check
```

No npm/build/test commands exist yet. The frontend bootstrap issue must pin the toolchain, add and execute real lint/typecheck/test/build commands, then update this file. Setup validation does not prove an application build or a live Claude call.

## Code and UI constraints

- Prefer focused standalone features and separate meaningful `.ts`, `.html`, `.scss` and test files. Respect installed versions and existing conventions.
- Use Nebular controls and theme tokens; compose board columns, evidence panels and a weekly calendar within the app. Do not add another component library for ordinary layout needs.
- Use typed API responses and forms. Classify state ownership; preserve manual/unsaved edits and handle version conflicts explicitly. Add a global state library only for a concrete need.
- Keep all browser-delivered configuration public-safe. Never place API keys, OAuth secrets, production exports, customer files or privileged tokens in the bundle or examples.
- Render user/source/model text safely; preserve Angular sanitization. Check real keyboard focus, labels, contrast and responsive states.
- Show the AI idea/context/model before generation, visible Planner/Writer/Reviewer progress, partial results, cancellation and actionable failures. Model IDs and allowed options come from validated server configuration.
- AI rewrites produce candidate revisions. Accepting a candidate must preserve history and respect expected versions; payload changes require fresh approval.
- M1 ends at reviewed text/Markdown/JSON export. Calendar/publishing is M2, analytics and extra providers are M3. A video script is not a finished video; unknown cost is not zero.
- Keep KISS/YAGNI. No module federation, SSR, microservices or framework migration without an evidenced problem and a recorded decision.

## Workflow and skills

Read the issue, contract, current files and relevant rules before editing. Use `/angular-feature` for a feature, `/angular-api-integration` for HTTP/auth, `/angular-forms` for forms, `/angular-state-management` for state, `/angular-accessibility` for UX review, `/angular-test-strategy` for risk-based tests and `/angular-code-review` for a read-only review. `/content-studio-feature` ties these to the product workflow. Agent profiles are optional helpers; reviewers are read-only.

Before completing a change run available checks and relevant application checks once they exist. Report executed results, skipped checks and material limitations. Honor existing task authorization; routine reads, reversible edits and checks do not require repeated confirmation. Production releases, destructive data operations, credential changes and billable live calls need explicit authorization.

## Setup maintenance

This setup is adapted from [ai-engineering-setups](https://github.com/vpetukhov-wbss/ai-engineering-setups), pinned in [.claude/setup.json](.claude/setup.json). Project facts and ADRs govern over generic knowledge. Read [Claude setup](docs/claude-setup.md) for usage, selected profiles, source attribution and safe updates. Never overwrite local adaptations with an upstream installer blindly.
