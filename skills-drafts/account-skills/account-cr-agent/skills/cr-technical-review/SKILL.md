---
name: cr-technical-review
description: Use only inside cr-agent as the main technical reviewer path for correctness, robustness, security, architecture, data, integration, observability, tests, and debt.
---

Coordinate technical CR and emit normalized findings into `cr-issues`.

This is the main technical reviewer path. `cr-evidence` is only supporting evidence and must not replace this review.

Dimensions:

- `cr-correctness`: business logic, state transitions, branch coverage, boundaries, nulls, regressions.
- `cr-robustness`: exceptions, timeouts, retries, fallbacks, idempotency, concurrency, partial failure, cleanup.
- `cr-security`: authn/authz, sensitive data, secrets, encryption/decryption, key material, logging, injection, token handling.
- `cr-architecture`: responsibility boundaries, change size, ownership, modularity, coupling, duplication, dead code, complexity, oversize files, abstraction fit, local patterns, config/profile isolation, rollback/splitability.
- `cr-data`: transactions, locks, isolation, pagination, consistency, DDL, rollback, data repair, validation SQL.
- `cr-integration`: external APIs, channel protocols, compatibility, config contracts, environment drift, old/new coexistence.
- `cr-observability`: logs, metrics, traces, dashboards, real-time alerts, report/batch alerts, SLI/SLO or business KPI signals, trace context, error messages, diagnosis usefulness, owner, threshold, routing, and runbook.
- `cr-testability`: unit, integration, regression, compatibility, performance, and failure-path evidence.
- `cr-tech-debt`: new or exposed debt, blocking status, deferral, owner, due date, and follow-up.

Use installed domain review skills when available. If a required reviewer skill is missing, record a missing review dependency.

Review completeness:

- Include Sonar-style code smells such as dead code, oversized classes, confusing
  names, unbounded methods, duplicated flow, and overly broad controller entry points.
- Include security and business-risk findings when the diff touches external
  callbacks, auth, sensitive logging, account/payment/settlement state, or
  upstream/downstream contracts.
- Include observability findings when changed failure modes cannot be detected
  through logs, metrics, traces, dashboards, real-time alerts, report/batch
  alerts, SLI/SLO or business KPI signals, and named owner/runbook paths.
- Include maintainability findings when change size, ownership, modularity,
  coupling, duplication, dead code, complexity, config/profile isolation,
  rollback/splitability, tests, or documentation make future review or rollback
  unsafe.
- Do not stop at only the first blocking issue. Continue scanning triggered
  dimensions and emit technical debt, bad smells, security, testability, and
  business-risk findings into `cr-issues`.
- If a real Sonar or security scan was not run, record that as missing evidence
  through `cr-evidence`; do not present static reading as scan proof.
