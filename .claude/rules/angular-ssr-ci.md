---
paths:
  - "angular.json"
  - "package.json"
  - "src/**/server.ts"
  - "src/**/app.config.server.ts"
  - ".github/workflows/**"
  - "Dockerfile*"
---
# Browser SPA and deployment
- Start with a browser SPA. SSR/SSG, a Node server and module federation are not selected; introduce them only for an evidenced need and an ADR.
- Keep browser-only APIs behind platform checks; avoid serialization of secrets and leaking authenticated private HTML through shared caches.
- Define hydration, reverse proxy trusted header policy, CSP, asset caching, client routing fallback and environment-specific config.
- CI: lockfile install, lint, type/templates checks, unit tests, production build, targeted E2E and vulnerability/license policy.
- No deployment claims without actual environment verification; no unattended production release without approval.
