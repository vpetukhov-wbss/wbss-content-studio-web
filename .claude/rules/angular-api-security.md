---
paths:
  - "src/app/**/data-access/**/*.ts"
  - "src/app/**/auth/**/*.ts"
  - "src/app/**/*interceptor*.ts"
  - "src/app/**/*guard*.ts"
  - "src/environments/**"
---
# Integration and security
- Type contracts based on backend OpenAPI or explicit domain-facing DTOs. Avoid `any` responses and silent shape coercion.
- Centralize common transport behavior in HttpClient interceptors; avoid unnecessary auth token rotation machinery in UI components.
- Authorization must be enforced server-side; route guards are for navigation experience.
- Prefer secure cookies/BFF or standards-based auth flows as appropriate; avoid long-lived secrets in browser bundles/localStorage.
- Protect against XSS, CSRF/XSRF, open redirect and SSRF (server); review CORS and credential policies.
- Do not bypass sanitization or use dangerous HTML APIs without rigorous review.
