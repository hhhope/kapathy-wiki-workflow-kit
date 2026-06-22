# Lore Manual Eval Results

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This file records a fixture-based manual walkthrough of the Lore evaluation corpus.

It is stronger than pure documentation review, but weaker than live agent or multi-session pressure testing.

---

## Scope of this run

Checked manually against:
- `skills/lore/evals/evals.json`
- `skills/lore/evals/fixtures/openspec/`
- `skills/lore/evals/fixtures/wiki/`
- `skills/lore/evals/fixtures/logs/`

Not performed:
- live agent retrieval run
- live OpenSpec apply/archive integration run
- multi-session adversarial pressure test

---

## Results

| Eval id | Category | Result | Notes |
|---|---|---|---|
| `gate-propose-missing` | gate | Pass | Workflow wording requires block when `proposal/design/tasks` are absent |
| `gate-propose-present` | gate | Pass | Fixture change tree has all three required OpenSpec files |
| `retrieval-idempotency-zh` | retrieval | Pass | `index.md` points to `pitfalls/idempotency-keys.md`; callback domain also links to it |
| `retrieval-idempotency-en` | retrieval | Pass | Same path as Chinese retrieval; trigger terms and page summary still align |
| `retrieval-timeout-en` | retrieval | Pass | `payment-retry` domain points to `timeout-fallback`; principle page is also linked |
| `noise-auth-unrelated` | noise | Pass | Fixture corpus has no auth page; payment pages should not be selected for auth as top result if scope filter is respected |
| `absorb-log-project-domain` | absorption | Pass | Sample log clearly maps to `projects/payments-core/domains/payment-retry.md` |
| `absorb-log-principle` | absorption | Pass | Sample log clearly maps to `principles/boundary-first.md` |
| `startup-budget-medium` | startup-budget | Pass | Manual startup set can stay at 6 pages: proposal, design, tasks, overview, payment-retry, timeout-fallback |

---

## Derived manual metrics

### Retrieval

- Similar-task recall sample: 3/3 = `100%`
- Irrelevant-page noise sample: 0/1 = `0%`

These numbers are only for the tiny fixture subset above, not the full target dataset from `TDD-SPEC.md`.

### Absorption

- Accepted sample logs mapped to destinations: 2/2 = `100%`

This proves fixture clarity, not weekly review execution quality.

### Startup budget

- Manual medium scenario page count: `6`

This is within the target P90 budget, but only for the fixture scenario.

---

## Limitations

- Results are based on manual inspection, not an automated or adversarial run
- Recall/noise numbers are too small to treat as production evidence
- Archive blocking is still not exercised against a live OpenSpec archive command

---

## Next stronger step

1. Execute the full query set from `TDD-SPEC.md`
2. Add at least 10 retrieval queries and 10 startup scenarios
3. Record scored before/after results from a live agent run
