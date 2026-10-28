# Content Studio Web

Open-source Angular and Akveo Nebular frontend for an AI-assisted content workspace. Turn an idea and selected product sources into channel drafts, follow the agents' work, edit the result and approve an exact revision for export.

**Status:** repository-specific Claude Code setup and implementation specifications. The Angular application and runtime integrations are not implemented yet. There is no runnable demo or live AI connection in this repository.

## Product flow

1. **AI Studio:** enter the idea, select product, sources, language, channels and model configuration.
2. **Agent progress:** follow Planner → Writer → Reviewer, inspect partial outputs and cancel work.
3. **Campaign editor:** edit manually or request an AI rewrite; retain saved revisions and review findings.
4. **Approval and export:** approve the exact payload and export text/Markdown/JSON. Social publishing is a later milestone.

The API backend is a separate component. Provider keys, business rules, permissions and execution stay on the server. Open-source UI code does not grant API or account access.

## Work with Claude Code

With Claude Code installed separately:

```bash
git clone https://github.com/vpetukhov-wbss/wbss-content-studio-web.git
cd wbss-content-studio-web
python3 scripts/check_claude_setup.py
claude
```

In Claude Code, inspect `/memory`, then use `/content-studio-feature`, `/angular-feature`, `/angular-api-integration` or `/angular-code-review` for the relevant task. Configuration is derived from [AI Engineering Setups](https://github.com/vpetukhov-wbss/ai-engineering-setups) and adapted to this repository. It configures the development assistant; it does not connect the product to Claude's API.

## Documentation

| Document | Purpose |
| --- | --- |
| [Engineering contract](CLAUDE.md) | Facts, commands and development constraints |
| [Architecture](docs/architecture.md) | Angular/Nebular structure and source ownership |
| [UI flows](docs/ui.md) | Screens, AI interaction and required states |
| [API boundary](docs/api-boundary.md) | Server authority and frontend compatibility |
| [Claude setup](docs/claude-setup.md) | Rules, skills, agents, provenance and updates |
| [Contributing](CONTRIBUTING.md) | Small changes and verification |
| [Security](SECURITY.md) | Public examples and responsible reporting |

Track implementation in [frontend bootstrap](https://github.com/vpetukhov-wbss/wbss-content-studio-web/issues/1), [AI Studio and agent progress](https://github.com/vpetukhov-wbss/wbss-content-studio-web/issues/2), and [campaign editing and approval](https://github.com/vpetukhov-wbss/wbss-content-studio-web/issues/3).

The first implementation task pins compatible Angular, Nebular and Node versions, configures the theme/font/icon pack and proves an actual production build. Application commands will be documented after they have been run.

## License

[MIT](LICENSE). Imported Claude engineering material retains its upstream attribution in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Nebular, Open Sans and Eva retain their respective licenses when dependencies/assets are added.
