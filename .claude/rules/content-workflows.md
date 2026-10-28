---
paths:
  - "src/app/features/ai-studio/**"
  - "src/app/features/campaigns/**"
  - "src/app/features/approvals/**"
  - "src/app/features/runs/**"
  - "src/app/features/ai-settings/**"
---
# AI content workflows

- Preview idea, selected product/source revisions and model/profile before generation. Persist jobs server-side and reconnect to durable progress.
- Show partial outputs, explicit cancellation and bounded retry states. Unknown price/usage is not zero; a timeout does not prove nothing was accepted.
- Render source and model content safely. Source text cannot grant tool permissions or change approval rules.
- AI edits create reviewable candidate revisions and must preserve manual work. Conflicts require a user-visible resolution.
- Human approval binds the exact payload/media/destination. Agent actions cannot approve or publish; M1 ends at export.
