# Lore E2E Fixture Results

Date: 2026-04-13
Branch: `feat-lore-wiki-openspec`

Command:

```bash
sh skills/lore/evals/run-e2e-fixture.sh
```

Purpose:
- prove one local end-to-end path from OpenSpec apply gate
- through Lore retrieval and weekly review absorption
- into archive gate satisfaction

Observed result:

```text
STEP | apply gate with full change docs
ALLOW | apply gate satisfied
STEP | retrieval sample
TOP | projects/payments-core/domains/callback-processing.md, pitfalls/idempotency-keys.md
STEP | weekly review absorbs logs
ABSORB | 20260411-090000-yan-payment-retry-gap-a1b2.md -> projects/payments-core/domains/payment-retry.md
ABSORB | 20260411-091500-yan-shared-boundary-gap-c3d4.md -> principles/boundary-first.md
STEP | archive gate after review
ALLOW | archive gate satisfied
SUMMARY | e2e fixture passed
```

Interpretation:

- The local fixture command surface now supports a minimal but complete path:
  - apply gate
  - retrieval of a relevant lore page
  - weekly-review style absorption
  - archive gate after reviewed markers
- This is stronger than isolated gate checks, but still not a production OpenSpec CLI or live multi-session rollout.
