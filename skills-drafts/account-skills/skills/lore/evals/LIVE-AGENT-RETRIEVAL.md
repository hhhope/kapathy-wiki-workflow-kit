# Lore Live Agent Retrieval Run

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This file records live retrieval passes performed in the current session against:
- the original tiny fixture corpus
- the expanded pressure corpus

Method:
- read `skills/lore/evals/fixtures/wiki/index.md`
- follow the Lore retrieval rule
- select only the most relevant pages
- answer the prompt from those pages

Limits:
- single-session run only
- no blinded evaluator
- corpus-wide scoring still comes from `PRESSURE-RESULTS.md`

---

## Case: `retrieval-idempotency-zh`

Prompt:
`支付回调重复通知时如何避免重复入账？`

Pages read:
- `fixtures/wiki/index.md`
- `fixtures/wiki/projects/payments-core/domains/callback-processing.md`
- `fixtures/wiki/pitfalls/idempotency-keys.md`

Answer:
- Core page: `pitfalls/idempotency-keys.md`
- Supporting page: `projects/payments-core/domains/callback-processing.md`
- Retrieval outcome: repeated callbacks must derive a stable idempotency key, verify dedupe before mutation, and keep write paths idempotent.

Verdict:
- Pass

---

## Case: `retrieval-idempotency-en`

Prompt:
`How should repeated payment callbacks avoid duplicate ledger writes?`

Pages read:
- `fixtures/wiki/index.md`
- `fixtures/wiki/projects/payments-core/domains/callback-processing.md`
- `fixtures/wiki/pitfalls/idempotency-keys.md`

Answer:
- Core page: `pitfalls/idempotency-keys.md`
- Supporting page: `projects/payments-core/domains/callback-processing.md`
- Retrieval outcome: repeated payment callbacks should be deduped with a stable provider-event key before any ledger mutation is attempted.

Verdict:
- Pass

---

## Case: `retrieval-timeout-en`

Prompt:
`How should retry workers call notification providers when timeout and fallback matter?`

Pages read:
- `fixtures/wiki/index.md`
- `fixtures/wiki/projects/payments-core/domains/payment-retry.md`
- `fixtures/wiki/pitfalls/timeout-fallback.md`
- `fixtures/wiki/principles/boundary-first.md`

Answer:
- Core pages: `pitfalls/timeout-fallback.md`, `principles/boundary-first.md`
- Supporting page: `projects/payments-core/domains/payment-retry.md`
- Retrieval outcome: retry workers must set explicit timeouts, define fallback behavior, and stay within approved external boundaries.

Verdict:
- Pass

---

## Case: `noise-auth-unrelated`

Prompt:
`Frontend login session refresh bug in auth flow.`

Pages read:
- `fixtures/wiki/index.md`

Answer:
- No strong matching lore page in the payment fixture corpus
- Suggested next step: query auth-specific wiki pages instead of reusing payment pages

Verdict:
- Pass

---

## Summary

- Similar-task recall sample: `3/3`
- Irrelevant-page noise sample: `0/1`
- Live-session retrieval behavior matches the expected fixture routing

---

## Pressure corpus representative cases

These cases use the expanded pressure corpus under `skills/lore/evals/pressure/wiki/`.

## Case: `similar-zh-04`

Prompt:
`设计里新增外部依赖前应该先看什么边界？`

Pages read:
- `pressure/wiki/index.md`
- `pressure/wiki/principles/boundary-first.md`

Answer:
- Core page: `principles/boundary-first.md`
- Retrieval outcome: before adding a new external dependency, confirm ownership boundaries and define explicit timeout and fallback behavior.

Verdict:
- Pass

---

## Case: `cross-01`

Prompt:
`Settlement replay and payment callback both risk duplicate writes. What shared pattern applies?`

Pages read:
- `pressure/wiki/index.md`
- `pressure/wiki/pitfalls/idempotency-keys.md`
- `pressure/wiki/projects/payments-core/domains/callback-processing.md`
- `pressure/wiki/projects/settlements-core/domains/reconciliation.md`

Answer:
- Core page: `pitfalls/idempotency-keys.md`
- Supporting pages:
  - `projects/payments-core/domains/callback-processing.md`
  - `projects/settlements-core/domains/reconciliation.md`
- Retrieval outcome: both replayed settlement inputs and repeated payment callbacks should be treated as idempotent events guarded by a stable dedupe key before mutation.

Verdict:
- Pass

---

## Case: `noise-zh-01`

Prompt:
`前端登录态刷新循环怎么查？`

Pages read:
- `pressure/wiki/index.md`
- `pressure/wiki/projects/auth-core/domains/session-refresh.md`

Answer:
- Core page: `projects/auth-core/domains/session-refresh.md`
- Retrieval outcome: this is an auth/session-refresh problem and should stay in auth scope rather than loading payment retry or callback pages.

Verdict:
- Pass

---

## Case: `edge-01`

Prompt:
`worker retry and login refresh both mention timeout; for payment worker timeout what page should be loaded first?`

Pages read:
- `pressure/wiki/index.md`
- `pressure/wiki/pitfalls/timeout-fallback.md`
- `pressure/wiki/principles/boundary-first.md`

Answer:
- Core page: `pitfalls/timeout-fallback.md`
- Supporting page: `principles/boundary-first.md`
- Retrieval outcome: even when timeout appears in multiple domains, payment worker timeout should route to external-call timeout/fallback guidance first, then to the boundary rule.

Verdict:
- Pass

---

## Pressure-corpus session summary

- Representative categories covered in-session:
  - similar-task retrieval
  - cross-domain retrieval
  - auth/noise separation
  - ambiguous timeout edge case
- Full corpus measured result remains in `PRESSURE-RESULTS.md`:
  - similar-task recall: `12/12 = 100%`
  - irrelevant-page noise: `0/8 = 0%`
