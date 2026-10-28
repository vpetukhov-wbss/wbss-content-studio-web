# API and trust boundary

No API schema or running server contract is implemented yet. This document states requirements, not existing routes.

The browser submits an idea, product/source identifiers, selected channels, model/profile configuration and an expected revision. The server authorizes the workspace, resolves allowed immutable inputs, validates the model capabilities and budgets, persists the run and returns a durable identifier. Progress and results must survive navigation or reconnection; UI cancellation is an explicit server operation.

The server is authoritative for identity, workspace membership, credentials, rate/budget limits, source access, version checks, approvals, export access and publication. Never send Anthropic credentials directly from the browser. Render source/generated content as untrusted data and preserve Angular sanitization.

Use typed request/response contracts with stable error codes and actionable validation/conflict responses. Unknown pricing stays unknown. A timed-out request may already have been accepted; retries need server-supported duplicate-request semantics. Client-side disabling alone does not prevent duplicate work.

Only publish reviewed DTOs, synthetic fixtures and documentation. A future OpenAPI snapshot must exclude internal/admin-only operations, real hostnames, credentials and real customer examples. Do not commit a fabricated schema to imply an API is available.

Contract changes must coordinate frontend and backend versions, compatibility windows and consumer tests. Changing UI code cannot grant agent permission to approve content or publish to a social account.
