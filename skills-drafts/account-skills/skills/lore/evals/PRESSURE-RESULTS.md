# Lore Pressure Results

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This file records the second-pass corpus-driven pressure run for retrieval, weekly review, and startup-budget metrics.

## Summary

| Metric | Result | Target | Verdict |
|---|---:|---:|---|
| Similar-task recall | 12/12 = `100%` | `>= 80%` | Pass |
| Irrelevant-page noise | 0/8 = `0%` | `<= 20%` | Pass |
| Log absorption success | 8/8 = `100%` | `>= 90%` | Pass |
| `absorbed-to` completion | 8/10 = `80%` | weekly review metrics required | Pass |
| Startup context budget P50 | `4` pages | `3-4` | Pass |
| Startup context budget P90 | `6` pages | `<= 6` | Pass |

## Weekly review metrics block

- reviewed logs: `10`
- absorbed logs: `8`
- discarded logs: `2`
- `absorbed-to` completion rate: `80%`
- absorption success rate: `100%`
- destination page types: `{'domain': 3, 'principle': 2, 'pitfall': 2, 'overview': 1}`

## Retrieval sample details

| Query id | Category | Top results | Hit | Noisy |
|---|---|---|---|---|
| `similar-zh-01` | similar | `projects/payments-core/domains/callback-processing.md, projects/payments-core/overview.md` | Pass | No |
| `similar-zh-02` | similar | `projects/payments-core/domains/payment-retry.md, principles/boundary-first.md, projects/payments-core/overview.md` | Pass | No |
| `similar-zh-03` | similar | `projects/settlements-core/overview.md, pitfalls/idempotency-keys.md, projects/settlements-core/domains/reconciliation.md` | Pass | No |
| `similar-zh-04` | similar | `principles/boundary-first.md` | Pass | No |
| `similar-zh-05` | similar | `projects/payments-core/domains/callback-processing.md, projects/payments-core/overview.md` | Pass | No |
| `similar-en-01` | similar | `projects/payments-core/domains/callback-processing.md, pitfalls/idempotency-keys.md` | Pass | No |
| `similar-en-02` | similar | `projects/payments-core/domains/payment-retry.md, pitfalls/timeout-fallback.md, principles/boundary-first.md` | Pass | No |
| `similar-en-03` | similar | `projects/settlements-core/domains/reconciliation.md, pitfalls/idempotency-keys.md, projects/settlements-core/overview.md` | Pass | No |
| `cross-01` | similar | `pitfalls/idempotency-keys.md, projects/payments-core/domains/callback-processing.md, projects/settlements-core/domains/reconciliation.md` | Pass | No |
| `cross-02` | similar | `pitfalls/timeout-fallback.md, principles/boundary-first.md, projects/auth-core/overview.md` | Pass | No |
| `noise-zh-01` | noise | `projects/auth-core/domains/session-refresh.md, projects/auth-core/overview.md` | n/a | Pass |
| `noise-zh-02` | noise | `projects/auth-core/domains/session-refresh.md` | n/a | Pass |
| `noise-zh-03` | noise | `projects/auth-core/overview.md` | n/a | Pass |
| `noise-zh-04` | noise | `projects/auth-core/overview.md, pitfalls/session-refresh-loop.md` | n/a | Pass |
| `noise-zh-05` | noise | `projects/auth-core/domains/session-refresh.md, projects/auth-core/overview.md` | n/a | Pass |
| `noise-en-01` | noise | `projects/auth-core/overview.md` | n/a | Pass |
| `noise-en-02` | noise | `projects/auth-core/overview.md, pitfalls/session-refresh-loop.md, projects/auth-core/domains/session-refresh.md` | n/a | Pass |
| `noise-en-03` | noise | `projects/auth-core/overview.md` | n/a | Pass |
| `edge-01` | edge | `pitfalls/timeout-fallback.md, principles/boundary-first.md, projects/auth-core/overview.md` | Pass | No |
| `edge-02` | edge | `pitfalls/idempotency-keys.md, projects/settlements-core/overview.md, projects/settlements-core/domains/reconciliation.md` | Pass | No |

## Startup budget distribution

- scenario count: `10`
- page counts: `[3, 3, 4, 4, 4, 4, 5, 6, 6, 6]`
- P50: `4`
- P90: `6`
- max: `6`

## Interpretation

- Retrieval recall and noise now have a measured corpus instead of a tiny walkthrough only.
- Weekly review now has a mandatory metrics block, not only page diffs.
- Startup-budget evidence is based on 10 scenarios, not one medium example.
