# Frontend architecture

This is the public frontend repository. The selected .NET API and background AI execution are developed separately; source separation does not imply backend microservices. This repo owns UI, browser state, typed API consumption and public, synthetic examples. The backend owns persistence, secrets, authorization and execution.

## Selected direction

- Angular, TypeScript and SCSS, with compatible Angular/Nebular/Node versions pinned during bootstrap.
- Akveo Nebular Default light theme, Open Sans and Eva outline icons.
- Browser SPA with lazy feature routes. Prefer local signals/computed for synchronous state and RxJS for asynchronous streams where supported by the selected versions.
- Planned application paths: `src/app/core/`, `src/app/features/`, `src/app/shared/ui/`, `src/environments/`, `e2e/`. They do not exist yet.
- Feature boundaries: AI Studio, products/context, sources/assets, content board, campaign editor, agent settings, run history, approval/export and later calendar.
- No SSR, module federation or global state framework initially. Record an ADR before adding them for a measured requirement.

## Nebular integration

Use `nb-layout`, `nb-sidebar` and `nb-menu` for the shell; `nb-card`, `nbButton`, `nbInput`, `nb-select`, `nb-tabset`, `nb-alert`, `nb-checkbox` and `nb-icon` for controls. Product/content cards, evidence panels, board columns and weekly scheduling are application compositions, not built-in Kanban/scheduler controls.

Keep primary button fill at `#3366ff`; use primary-600 (`#274bdb`) for normal-size primary text on pale primary surfaces. Use semantic theme tokens and verify the actual browser contrast, focus and disabled states. Do not copy Figma coordinates as fixed page positioning.

## Dependency and delivery boundary

The frontend depends only on a reviewed public API contract and synthetic fixtures; it must build and test without a checkout of private server source or live provider credentials. Coordinate breaking contracts through a versioned schema and consumer tests once the API exists. The initial authentication and local-development connection are implementation decisions; do not invent endpoints or claim integration before verification.
