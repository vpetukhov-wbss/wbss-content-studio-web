---
paths:
  - "src/**/*.html"
  - "src/**/*.scss"
  - "src/**/*.component.ts"
  - "src/**/themes*.ts"
  - "package.json"
---
# Nebular design system

- Use Akveo Nebular Default light theme, Open Sans and Eva outline icons. Verify Angular/Nebular peer dependency compatibility before installing or upgrading.
- Prefer Nebular shell and controls with semantic tokens; app-level board/calendar layouts are custom compositions. No second UI framework for normal layout gaps.
- Preserve the primary-text contrast override from docs/architecture.md. Verify focus, labels, keyboard operation, responsive states and rendered contrast in the browser.
- Do not assume zoneless change detection or the newest Angular syntax is compatible with the pinned Nebular release.
