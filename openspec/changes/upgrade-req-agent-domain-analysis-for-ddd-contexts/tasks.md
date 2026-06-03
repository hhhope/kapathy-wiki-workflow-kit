# Tasks

- [x] 1. Add OpenSpec requirements for DDD req-agent domain analysis.
- [x] 2. Add failing tests for DDD domain analysis output and actor/obligation split.
- [x] 3. Implement taxonomy v2 domain analysis output in `requirements_analysis_agent`.
- [x] 4. Update req-domain-analysis / req-scope guidance with behavior evidence.
- [x] 5. Run focused requirements analysis tests and checker compatibility tests.
- [x] 6. Run behavior asset validation and OpenSpec validation.
- [x] 7. Record verification results and proof boundary.

## Verification

- RED baseline:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent` -> failed because analysis output had no `domain_model` or `actors`.
  - `rg -n "actors|role_obligations|domain_model|bounded_contexts|fact owner|subscription_owner|user-story actors" .codex/skills/req-domain-analysis/SKILL.md .codex/skills/req-scope/SKILL.md` -> no matches.
- GREEN:
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent` -> passed, `Ran 3 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent tests.test_requirements_analysis_agent` -> passed, `Ran 15 tests`.
  - `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent tests.test_requirements_analysis_agent tests.test_requirements_ddd_readiness_gate tests.test_requirements_checker_gate` -> passed, `Ran 38 tests`.
  - `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml` -> valid.
  - `openspec validate upgrade-req-agent-domain-analysis-for-ddd-contexts --strict` -> valid.
    The command exited 0; the trailing PostHog DNS flush error is telemetry-only.
  - `wc -l scripts/requirements_ddd_analysis.py` -> `297`, under the Python
    large-file threshold.

## Behavior Asset Validation

- `python3 scripts/check_behavior_assets.py` -> non-zero because unrelated
  active change `initialize-llm-wiki-seed-repo` is missing behavior-asset
  evaluation sections and replay fields.
- No error was reported for
  `upgrade-req-agent-domain-analysis-for-ddd-contexts`.

## Proof Boundary

This change proves local DDD domain-analysis output and repo-local worker skill
guidance for separating actors from role obligations. It does not prove every
historical requirement case can pass strict taxonomy v2 readiness, and it does
not mutate the taxonomy skeleton.
