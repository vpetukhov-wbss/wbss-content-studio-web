---
name: content-studio-feature
description: "Implement a Content Studio frontend workflow with Nebular UI, typed API boundaries, visible AI steps and preserved revisions."
---

# Content Studio frontend feature

1. Read repository CLAUDE.md, docs/ui.md, docs/api-boundary.md and the relevant issue. Confirm actual installed versions and the API contract; identify any unimplemented backend dependency explicitly.
2. Use angular-feature, angular-forms and angular-api-integration procedures as needed. Compose Nebular controls around the smallest complete user task.
3. For generation/rewrite, expose selected context/model and durable progress; preserve unsaved/manual work, cancellation and version conflicts. Only a human approval of an exact revision can authorize export or later publishing.
4. Cover the relevant loading, empty, invalid, denied, failed, cancelled and conflicting states. Use synthetic fixtures and test the observable failure paths and browser accessibility.
5. Run only repository-defined available checks. Report what works, what was verified and any contract/backend behaviour still unimplemented. Update docs with the actual commands once bootstrap exists.
