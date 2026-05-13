# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| positive trigger: Go rule claims best-practice grounding | Source learning records official/GitHub sources, not only article links | `tests.test_go_engineering_security_rules.test_source_learning_records_official_sources_and_global_300_guardrail` |
| positive trigger: user rejects 500-line candidate and chooses 300 | Evidence records Go/Rust/Java `> 300` lines as referenced from global guardrails, not owned by Go rule | `tests.test_go_engineering_security_rules.test_source_learning_records_official_sources_and_global_300_guardrail` |
| negative should-not-trigger: Go rule might duplicate generic threshold | Go rule contains no `500` and no local `> 300` threshold | `tests.test_go_engineering_security_rules.test_go_rule_references_common_rules_instead_of_redefining_generic_limits` |
| official-source promotion: context/interface/layout guidance is Go-specific | Go rule promotes context first argument, no struct-stored context, consumer-side interfaces, and project-layout caution | `tests.test_go_engineering_security_rules.test_go_rule_promotes_official_go_specific_guidance_only` |
| parent gate preserve: user-confirmed stack remains unchanged | Go rule still defaults to Go 1.25.1 + Gin + gin-contrib + validator + GORM + go-redis | `tests.test_go_engineering_security_rules.test_go_rule_exists_with_user_confirmed_stack` |

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, existing `rules/go/engineering-security.md`, `wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md`, `openspec/changes/normalize-go-rule-dedupe-gate/*`, global `~/.codex/AGENTS.md`, Go official module layout docs, Go official CodeReviewComments, Google Go Style Guide, Uber Go Style Guide, and `golang-standards/project-layout`.
- Owns: compressed Go-specific guidance for context propagation, interface placement, Go module layout caution, and official-source grounding.
- References: global `Large-file guardrails`, including current Go/Rust/Java `> 300` line refactor-first threshold; common/global behavior-asset and testing gates.
- Rejects: `500` as a local threshold, any Go-local numeric file-size threshold, fixed Go-local line-length rules, wholesale upstream style-guide copying, and treating `golang-standards/project-layout` as official mandatory policy.

## Replay Evidence

### Positive Trigger Scenario

| Field | Evidence |
|---|---|
| input or situation shape | User asks to solidify Go rule using GitHub/official best practices and confirms 300 instead of 500. |
| trigger condition | The task semantically changes `rules/go/engineering-security.md`, source-learning evidence, and Go-rule tests. |
| expected route | Load Go rule, learning-capture evidence, and behavior-asset prior-art gate before claiming completion. |
| repo-visible artifact | `rules/go/engineering-security.md`, `wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md`, `tests/test_go_engineering_security_rules.py`, and this OpenSpec change. |
| expected output | Future Go work references global large-file guardrails for the 300 threshold and uses official-source-backed Go-specific practices. |
| promotion or non-promotion boundary | Official-source-backed Go-specific points are promoted; generic thresholds remain global references; upstream style guides are not copied wholesale. |
| proof boundary | Tests verify local artifacts and threshold ownership; they do not continuously re-fetch upstream sources for future drift. |

### Negative Should-Not-Trigger Scenario

| Field | Evidence |
|---|---|
| input or situation shape | Non-Go material work, or Go work that only needs generic large-file handling. |
| trigger condition | No Go-specific stack/security/context/interface/layout decision is being made. |
| expected route | Use common/global large-file or testing guidance directly; do not load the Go rule as a generic threshold source. |
| repo-visible artifact | `rules/go/engineering-security.md` states common rule boundaries and no repo-local file length threshold. |
| expected output | No Go-local `500` or `> 300` threshold is invented. |
| promotion or non-promotion boundary | The 300 threshold stays in global guardrails; this change only records that dependency and prevents local duplication. |
| proof boundary | Local tests catch explicit numeric duplication in the Go rule, not every possible paraphrase of generic policy. |

## RED Baseline

- Added tests requiring official/GitHub source evidence and global 300 guardrail evidence.
- `python3 -m unittest tests.test_go_engineering_security_rules -v` failed because the source-learning page did not include Go official/GitHub sources or the `> 300` global guardrail evidence.
- The same RED run also failed because the Go rule had not yet promoted official-source-backed context/interface/layout guidance.
- `python3 scripts/check_behavior_assets.py` failed for this change until `evaluation.md` was added.

## GREEN Result

- `python3 -m unittest tests.test_go_engineering_security_rules tests.test_behavior_asset_prior_art_gate tests.test_behavior_asset_evaluation tests.test_repo_health_check -v`: 21 tests passed.
- `python3 scripts/check_behavior_assets.py`: passed with no behavior-asset drift output.
- `python3 scripts/repo_health_check.py`: passed `draft-skill-runtime-surface`, `skill-evaluation-evidence`, and `behavior-asset-evaluation`.
- `openspec validate solidify-go-rule-official-sources --strict`: change valid; OpenSpec emitted PostHog network flush warnings after validation due restricted network, with exit code 0.
- `git diff --check -- rules/go/engineering-security.md wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md tests/test_go_engineering_security_rules.py openspec/changes/solidify-go-rule-official-sources`: passed.
- `python3 scripts/check_wiki_frontmatter.py`: non-zero from pre-existing taxonomy drift; the edited `wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md` page was not listed in the generated drift report.

## Residual Risks

- External source pages may change after this evaluation; the local rule stores compressed transfer decisions, not a live mirror.
- The global 300 threshold is referenced from loaded root policy and is not owned by this repository.
- Tests prevent explicit `500` and local `> 300` duplication in the Go rule, but subtle generic-policy paraphrases still require review.
