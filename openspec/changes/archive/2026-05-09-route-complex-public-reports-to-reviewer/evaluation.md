## RED Baseline

Date: 2026-05-08

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Complex report requires reviewer before drafting | `public-report-quality-gate` has hard gates but no escalation rule for multi-page, reference-shaped, scored, or drift-corrected public materials. | FAIL |
| Template choice is treated as a user fork point | The Account Harness Wiki repair proceeded after proposition/gate checks without presenting 2-3 candidate templates for user selection. | FAIL |
| Scoring distinguishes schema check from quality score | Evaluation evidence used an `awk` total of 100 to prove rubric consistency, but the process did not explicitly prevent treating that as draft-quality proof. | FAIL |
| Heavy review logic stays out of the runtime skill | Existing fixes kept adding responsibilities to `public-report-quality-gate`; no separate reviewer template exists. | FAIL |
| Reviewer role remains manual | No repo-local reviewer template exists, so there is no explicit manual/non-auto-spawn boundary. | FAIL |

## GREEN Result

Date: 2026-05-08

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Complex report requires reviewer before drafting | `.codex/skills/public-report-quality-gate/SKILL.md` now routes complex reader-facing materials to reviewer when at least two escalation signals are true; `references/reviewer-routing.md` defines the six signals. | PASS |
| Template choice is treated as a user fork point | `.codex/agents/public-report-reviewer.md` requires 2-3 candidate templates, fit/risk notes, a recommendation, and user selection unless the user already selected explicitly. | PASS |
| Scoring distinguishes schema check from quality score | `references/reviewer-routing.md` marks schema arithmetic as invalid draft-quality proof; `.codex/agents/public-report-reviewer.md` requires score only after all hard gates pass. | PASS |
| Heavy review logic stays out of the runtime skill | The runtime skill adds only routing and one reference link; reviewer details live in `.codex/agents/public-report-reviewer.md` and `references/reviewer-routing.md`. | PASS |
| Reviewer role remains manual | `.codex/agents/public-report-reviewer.md` says not to treat the file as an automatic sub-agent trigger and to spawn only when the user explicitly asks for delegation. | PASS |
| Account Harness Wiki failure replay | `references/pressure-scenarios.md` now includes reviewer-routing replay cases for missing reviewer step, silent template choice, false 100 score, and auto-spawn boundary. | PASS |
| Skill authoring gate | `SKILL.md` stays compact at 75 lines, keeps a trigger-only description, and `pressure-scenarios.md` contains 9 should-trigger and 4 should-not-trigger cases. | PASS |
| OpenSpec validation | `openspec validate route-complex-public-reports-to-reviewer --strict` passes. | PASS |
| Whitespace validation | `git diff --check` passes. | PASS |

## Residual Risks

- This is a manual routing and reviewer role. It does not prove automatic
  runtime dispatch across future sessions.
- The change is not retroactive proof that the already-written Feishu document
  is publication-ready.
- Reviewer routing can block missing template choice and false scoring, but it
  does not generate local metrics by itself.
- Sub-agent delegation still requires explicit user permission; the default
  behavior is to load and apply the role template in the current agent.
