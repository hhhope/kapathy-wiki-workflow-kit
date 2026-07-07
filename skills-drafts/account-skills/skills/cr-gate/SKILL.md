---
name: cr-gate
description: Use only inside cr-agent to produce the final allow, conditional, or blocked CR decision from issues and evidence.
---

Own the final gate conclusion.

Read coverage artifacts; do not re-review code or trust report wording.

Conclusions:

- `allow`
- `conditional`
- `blocked`

Hard rules:

- any open blocking issue => `blocked`
- wrong or stale range metadata => `blocked`
- open diff unit => `blocked`
- open required check => `blocked`
- blocked checker result => `blocked`
- invalid N/A without accepted reason and evidence => `blocked`
- stale checker result after range, config, diff ledger, or agent version change => `blocked`
- wrong baseline => `blocked`
- release range unclear => `blocked`
- feature-branch CR presented as release gate => `blocked`
- mainline direct commit without approval and validation evidence => `blocked`
- production commit not covered by UAT evidence for release CR => `blocked`
- high-risk integration or security change without compatibility and test evidence => `blocked`
- DDL or data repair without rollback or validation evidence => `blocked`
- critical security issue => `blocked`
- missing required reviewer for a triggered high-risk dimension => `blocked` for release CR, otherwise `conditional` but not CR-complete until resolved or waived
- missing quality score rationale => `blocked` for report/gate/full CR: every technical quality score must cite concrete CR-IDs, evidence, or explicit non-applicability
- high-risk release, payment, settlement, MQ, scheduler, report, data-routing, external-integration, or production-operation change without observable runtime signals => `blocked`
- observability evidence is incomplete when it does not cover logs, metrics, traces, dashboards, real-time alerts, report/batch alerts, SLI/SLO or business KPI signals, owner, threshold, routing, and runbook for the changed failure modes
- unmaintainable change boundary => `blocked`: noisy or oversized diffs, mixed generated/manual changes, unclear ownership, hidden profile/config switches, duplicated/dead/complex logic, or rollback/split paths that cannot be audited
- missing maintainability rationale => `conditional` for non-release CR and `blocked` for release/full CR when the report cannot explain change size, ownership, modularity, coupling, duplication, dead code, complexity, test coverage, documentation, config/profile isolation, and rollback/splitability

Do not let report text override this decision.
