## RED Baseline

Date: 2026-05-11

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Public report gate requires article intent before judging drift | `SKILL.md` has reference, split, voice, narrative, visual, and publish gates but no Article Intent Contract. | FAIL |
| Complex drafts receive section and paragraph drift diagnostics | `scorecard.md` scores the whole article but has no section or paragraph drift matrix. | FAIL |
| Agent judgment is separated from user-owned conclusions | Existing gates block invented metrics but do not block the agent silently choosing the main line, stance, conclusion, or priority. | FAIL |
| Hard failure can still provide diagnostic scores without a false total | Existing rules only say scorecard `INVALID`; they do not preserve diagnostic paragraph scores for repair. | FAIL |
| Reviewer performs reverse outline before scoring | `.codex/agents/public-report-reviewer.md` checks proposition and hard gates but does not reverse-outline paragraphs before score evidence. | FAIL |

Command:

```bash
python3 -m unittest tests.test_public_report_quality_gate
```

Result: `FAILED (failures=5)`.

## GREEN Result

Date: 2026-05-11

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Public report gate requires article intent before judging drift | `.codex/skills/public-report-quality-gate/SKILL.md` now requires an Article Intent Contract for complex, scored, reference-shaped, or drift-corrected drafts. | PASS |
| Complex drafts receive section and paragraph drift diagnostics | `references/scorecard.md` and `references/gate-review-artifact.md` define Section And Paragraph Drift Review fields and 0-5 diagnostic drift scores. | PASS |
| Agent judgment is separated from user-owned conclusions | `SKILL.md` and `scorecard.md` define Judgment Ownership Gate and explicitly preserve the rule that process can be delegated, but judgment cannot. | PASS |
| Hard failure can still provide diagnostic scores without a false total | `scorecard.md` and `gate-review-artifact.md` keep the overall score `INVALID` while allowing diagnostic paragraph scores for repair. | PASS |
| Reviewer performs reverse outline before scoring | `.codex/agents/public-report-reviewer.md` now runs reverse outline, paragraph drift actions, and judgment ownership before score evidence. | PASS |
| Regression scenarios cover the user-stated failure mode | `pressure-scenarios.md` includes paragraph drift and judgment replay cases for agent-owned conclusions, pretty paragraphs changing decisions, reference opinions becoming local conclusions, and invalid overall score with diagnostics. | PASS |

Command:

```bash
python3 -m unittest tests.test_public_report_quality_gate
```

Result: `OK` with 5 tests.

## Residual Risks

- This change provides skill and reviewer behavior evidence, not automated
  article-quality enforcement.
- Paragraph drift scoring is still manual judgment. The artifact makes the
  judgment observable; it does not remove the need for user review.

## Verification

| Check | Result |
|---|---|
| Focused behavior test | PASS — `python3 -m unittest tests.test_public_report_quality_gate` ran 5 tests. |
| Full unit suite | PASS — `python3 -m unittest discover -s tests` ran 64 tests. |
| Change validation | PASS — `openspec validate add-public-report-paragraph-drift-gate --strict` returned valid. |
| Full OpenSpec validation | PASS — `openspec validate --all` returned 49 passed, 0 failed. |
| Whitespace check | PASS — `git diff --check` returned no output. |

PostHog telemetry flush printed DNS errors after OpenSpec commands. The
OpenSpec validation commands exited successfully; the telemetry flush is not
part of repository validation.
