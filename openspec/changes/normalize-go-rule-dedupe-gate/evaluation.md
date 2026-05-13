# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| positive trigger: new behavior-asset change touches `rules/*` or `AGENTS.md` without prior-art dedupe evidence | `check_behavior_assets.py` reports `missing_prior_art_dedupe` | `tests.test_behavior_asset_prior_art_gate.test_missing_prior_art_dedupe_is_error_for_rule_change` |
| negative should-not-trigger: the same change records scanned sources, owns, references, and rejects | Prior-art gate does not emit `missing_prior_art_dedupe` | `tests.test_behavior_asset_prior_art_gate.test_prior_art_dedupe_section_satisfies_rule_change_gate` |
| Go rule normalization: external article suggests a generic file-size limit | Go rule references global `Large-file guardrails` and does not define a local threshold | `tests.test_go_engineering_security_rules.test_go_rule_references_common_rules_instead_of_redefining_generic_limits` |
| Go service work still needs the confirmed stack | Go rule keeps Go 1.25.1 + Gin + gin-contrib + validator + GORM + go-redis | `tests.test_go_engineering_security_rules.test_go_rule_exists_with_user_confirmed_stack` |
| `go tool fix` question remains migration-scoped | Rule keeps `go tool fix` out of daily lint/format workflow | `tests.test_go_engineering_security_rules.test_go_tool_fix_is_migration_scoped_not_daily_lint` |

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, `openspec/specs/behavior-replay-gate/spec.md`, `openspec/specs/skill-evaluation-evidence/spec.md`, `openspec/changes/harden-behavior-asset-evaluation-gate/*`, existing `rules/go/engineering-security.md`, `wiki/config/behavior-asset-evaluation.yaml`, `~/.codex/AGENTS.md`, and `~/.codex/rules/common/development-workflow.md`.
- Owns: repo-local behavior-asset prior-art evidence gate; Go-specific stack, Gin/GORM/Redis, concurrency/resource lifecycle, and `go tool fix` boundaries.
- References: global large-file guardrails, global/root git discipline, common testing policy, and existing behavior-asset evaluation flow.
- Rejects: article-derived generic file-size thresholds, framework rankings, and broad documentation/testing workflow rules as Go-local hard rules.

## Replay Evidence

### Positive Trigger Scenario

| Field | Evidence |
|---|---|
| input or situation shape | An active OpenSpec change semantically modifies `rules/*`, `.codex/skills/*`, or `AGENTS.md`. |
| trigger condition | Change text includes configured behavior-asset markers and is not listed as a prior-art grandfathered change. |
| expected route | `python3 scripts/check_behavior_assets.py` reads `wiki/config/behavior-asset-evaluation.yaml`, inspects the change `evaluation.md`, and requires the prior-art dedupe section. |
| repo-visible artifact | `AGENTS.md`, `wiki/config/behavior-asset-evaluation.yaml`, `scripts/check_behavior_assets.py`, `rules/go/engineering-security.md`, and this OpenSpec change. |
| expected output | Missing prior-art evidence emits `ERROR missing_prior_art_dedupe`; present evidence allows the checker to proceed to other behavior-asset checks. |
| promotion or non-promotion boundary | Go-specific rules can be promoted into `rules/go`; generic engineering constraints are referenced from common/global rules instead of duplicated. |
| proof boundary | Tests prove structural enforcement and the Go-rule generic-threshold boundary. They do not prove semantic overlap for every future rule domain. |

### Negative Should-Not-Trigger Scenario

| Field | Evidence |
|---|---|
| input or situation shape | Ordinary wiki/source/report work that does not touch behavior assets, or grandfathered active changes from before this rollout. |
| trigger condition | No configured behavior-asset marker appears, or the change is listed in `prior_art_dedupe.grandfathered_changes`. |
| expected route | The prior-art dedupe gate does not force unrelated material work through rule ownership evidence. |
| repo-visible artifact | `wiki/config/behavior-asset-evaluation.yaml` records the covered markers and grandfathered rollout boundary. |
| expected output | No `missing_prior_art_dedupe` entry is emitted for unrelated or grandfathered changes. |
| promotion or non-promotion boundary | Historical completed changes are not rewritten only to satisfy the new section requirement. |
| proof boundary | Grandfathering prevents rollout churn; it also means older evaluations may not document this newer dedupe framing. |

## RED Baseline

- Added `tests/test_behavior_asset_prior_art_gate.py` before changing the checker.
- `python3 -m unittest tests.test_behavior_asset_prior_art_gate -v` failed because missing prior-art dedupe evidence produced no checker entry.
- `python3 scripts/check_behavior_assets.py` then failed for this new change until `evaluation.md` was added, confirming the behavior-asset gate was active for the change itself.

## GREEN Result

- `python3 -m unittest tests.test_behavior_asset_prior_art_gate -v`: passed.
- `python3 -m unittest tests.test_go_engineering_security_rules -v`: passed.
- `python3 -m unittest tests.test_behavior_asset_prior_art_gate tests.test_go_engineering_security_rules tests.test_behavior_asset_evaluation tests.test_repo_health_check -v`: 19 tests passed.
- `python3 scripts/check_behavior_assets.py`: passed with no behavior-asset drift output.
- `python3 scripts/repo_health_check.py`: passed `draft-skill-runtime-surface`, `skill-evaluation-evidence`, and `behavior-asset-evaluation`.
- `openspec validate normalize-go-rule-dedupe-gate --strict`: change valid; OpenSpec emitted PostHog network flush warnings after validation due restricted network, with exit code 0.
- `git diff --check -- AGENTS.md rules/go/engineering-security.md wiki/config/behavior-asset-evaluation.yaml scripts/check_behavior_assets.py tests/test_behavior_asset_prior_art_gate.py tests/test_go_engineering_security_rules.py openspec/changes/normalize-go-rule-dedupe-gate`: passed.

## Residual Risks

- The dedupe checker is intentionally structural. It enforces recorded ownership decisions but does not compute semantic overlap automatically.
- Grandfathered active changes can lack the new prior-art section; this avoids historical churn but leaves older evidence less complete.
- Go rule normalization references global files that live outside this repo; future machines still need those global rules available or an equivalent local bootstrap.
