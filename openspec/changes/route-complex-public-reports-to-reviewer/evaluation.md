## RED Baseline

Date: 2026-05-08

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Complex report requires reviewer before drafting | `public-report-quality-gate` has hard gates but no escalation rule for multi-page, reference-shaped, scored, or drift-corrected public materials. | FAIL |
| Template choice is treated as a user fork point | The Account Harness Wiki repair proceeded after proposition/gate checks without presenting 2-3 candidate templates for user selection. | FAIL |
| Scoring distinguishes schema check from quality score | Evaluation evidence used an `awk` total of 100 to prove rubric consistency, but the process did not explicitly prevent treating that as draft-quality proof. | FAIL |
| Heavy review logic stays out of the runtime skill | Existing fixes kept adding responsibilities to `public-report-quality-gate`; no separate reviewer role exists. | FAIL |
| Reviewer role remains manual | No repo-local reviewer template exists, so there is no explicit manual/non-auto-spawn boundary. | FAIL |

## GREEN Result

To be filled after implementation.

## Residual Risks

To be filled after implementation.
