# Draft Results — first rollout slice drafts

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This evaluation scores the draft rewrite set against the same RED scenarios used in the baseline.

Scoring:

- `Pass` = scenario dimension is satisfied well enough for first rollout
- `Partial` = improved but not complete
- `Fail` = still not good enough for the agent-memory contract

## Scenario matrix

| Scenario | Primary draft pages | Hit-rate | First-load readability | Boundary clarity | Mixed-language compatibility | Verdict |
|---|---|---|---|---|---|---|
| RED-01 | draft domain target pattern represented by overview + pitfall contract | Pass | Pass | Partial | Partial | Partial |
| RED-02 | account-team-efficiency overview + pitfall + domain pattern | Pass | Pass | Pass | n/a | Pass |
| RED-03 | draft account-team-efficiency overview | Pass | Pass | Pass | n/a | Pass |
| RED-04 | draft migration contract for durable pages | Pass | Pass | Partial | n/a | Partial |
| RED-05 | draft principle / pitfall / overview pattern | Pass | Pass | n/a | Partial | Partial |
| RED-06 | draft index + account-skills overview | Pass | Pass | Pass | Pass | Pass |
| RED-07 | draft admin-scope pitfall | Pass | Pass | Pass | n/a | Pass |
| RED-08 | draft evidence package in this change | Pass | Partial | Partial | Partial | Partial |

## Totals

| Dimension | Result |
|---|---|
| Hit-rate | `8 Pass / 0 Partial / 0 Fail` |
| First-load readability | `7 Pass / 1 Partial / 0 Fail` |
| Boundary clarity | `5 Pass / 3 Partial / 0 Fail` |
| Mixed-language compatibility | `1 Pass / 3 Partial / 0 Fail` |

## Interpretation

### What improved

- first-load readability improved materially because the drafts now expose `Applies When`, `Not For`, `Top Facts` or `Top Checks`, and `Load Next`
- boundary clarity improved because neighboring pages can now be rejected or sequenced more deliberately
- hit-rate did not regress while page shape became more retrieval-first

### What improved only partially

- mixed-language compatibility improved from accidental routing toward explicit routing aids via `Aliases`
- this is still not full bilingual support
- the current drafts now prove a minimal routing-aid hypothesis, not full mixed-language interpretation completeness

## Self-justification notes

This is why the drafts are worth keeping even though they are not "complete":

1. They improve the weakest baseline dimension: first-load readability.
2. They improve page-boundary clarity without sacrificing hit-rate.
3. They make mixed-language incompleteness more visible instead of hiding it behind good routing luck.

That is a valid GREEN step for the page-contract hypothesis, while language support remains an explicit follow-up.
