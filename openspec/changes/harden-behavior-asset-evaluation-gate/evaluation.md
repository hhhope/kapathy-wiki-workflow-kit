# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| positive trigger: active semantic skill change lacks `evaluation.md` | `check_behavior_assets.py` reports `missing_evaluation` error | `tests.test_behavior_asset_evaluation.test_missing_evaluation_for_skill_change_is_error` |
| negative should-not-trigger: grandfathered active change predates this rollout | Checker skips configured grandfathered change instead of forcing historical cleanup | `tests.test_behavior_asset_evaluation.test_grandfathered_active_change_is_not_rechecked` |
| parent gate preserve: active behavior change mentions parent gate, route, publish, sync, or reader-facing output | Evaluation must show parent gate preservation evidence | `tests.test_repo_health_check.test_reports_pass_for_skill_change_with_valid_evaluation_md` |
| structural anti-drift: `Agent Intent Routing` duplicates the High-Frequency Skills route table | Checker reports `route_table_ownership_drift` error | `tests.test_behavior_asset_evaluation.test_route_table_ownership_drift_is_error` |
| health-check integration: route table drift exists in a temp repo | `repo_health_check.py` reports `FAIL behavior-asset-evaluation` | `tests.test_repo_health_check.test_reports_fail_for_agent_intent_route_table_drift` |
| reviewer finding: evaluation omits positive trigger case | Checker reports `missing_positive_scenario` error | `tests.test_behavior_asset_evaluation.test_missing_positive_scenario_is_error` |
| reviewer finding: routing proof only asserts required wording was present | Checker reports `shallow_text_evidence` error | `tests.test_behavior_asset_evaluation.test_shallow_text_exists_evidence_is_error` |

## Replay Evidence

| Replay Field | Evidence |
|---|---|
| input or situation shape | Semantic skill edit, skill reference edit, or `AGENTS.md` runtime route, hard stop, parent gate, publish/sync, or future runtime behavior change. |
| trigger condition | Active OpenSpec change references covered behavior-asset markers or current `AGENTS.md` contains configured route ownership drift. |
| expected route, stop, refusal, or boundary behavior | Future agent runs `python3 scripts/check_behavior_assets.py` before claiming behavior-asset completion; error-severity drift blocks completion claims. |
| repo-visible artifact a future agent should read | `AGENTS.md`, `wiki/config/behavior-asset-evaluation.yaml`, `scripts/check_behavior_assets.py`, `scripts/repo_health_check.py`, and this OpenSpec change. |
| expected output or non-output | Checker emits terminal output plus `/tmp/behavior-asset-evaluation-report.json` and `/tmp/behavior-asset-evaluation-report.md`; it does not silently pass shallow evidence. |
| promotion or non-promotion boundary | This is repo-local governance only. It does not promote rules to root `AGENTS.md` or team lore. |
| proof boundary | Tests and checker prove local structural and evidence requirements. They do not prove every future AI client will load repo guidance. |

## RED Baseline

- `python3 -m unittest tests.test_repo_health_check -v` failed 6/6 after tests were updated because `repo_health_check.py` still returned only two checks.
- `python3 scripts/check_behavior_assets.py` initially reported `missing_evaluation` for this change.
- The same checker initially also flagged earlier active changes. That exposed a rollout-boundary issue: the first checker version would force historical cleanup on active changes that predated this gate.
- Existing Agent Intent Routing contained a second route table under `Minimum routes` before Task 4.

## GREEN Result

- `python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check -v` passed 10 tests after health-check integration and rollout scoping.
- `python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check tests.test_agent_intent_routing tests.test_public_report_quality_gate -v` passed 24 tests after final evaluation closeout.
- `python3 scripts/check_behavior_assets.py` passed with no error-severity behavior asset drift after this file was added.
- `python3 scripts/repo_health_check.py` reported `PASS draft-skill-runtime-surface`, `PASS skill-evaluation-evidence`, and `PASS behavior-asset-evaluation`.
- Final review found two enforcement gaps: incomplete required replay fields and missing positive/shallow-evidence checks. After repair, `python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check -v` passed 12 tests, including positive-scenario and shallow-text-evidence RED cases.
- `AGENTS.md` now keeps `High-Frequency Skills` as the single runtime skill routing table and compresses `Agent Intent Routing` into pre-action classification guidance.
- `wiki/config/behavior-asset-evaluation.yaml` owns detailed evaluation vocabulary and configured grandfathered active changes for the first rollout.

## Residual Risks

- Text-level checks can still miss subtle semantic drift.
- Manual replay records can be incomplete.
- Archived changes are not scanned by default.
- Grandfathered active changes avoid first-rollout cleanup pressure but should not be used for new behavior-asset changes.
- Weak replay evidence remains warn-level in the first rollout.
