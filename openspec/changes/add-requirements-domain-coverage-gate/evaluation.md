# Evaluation

## Pressure Scenarios

- Valid strict DDD case with `domain_model`, roles, stories, and acceptance mappings but no domain coverage must be blocked.
- User stories without `domain_refs`, `context_refs`, or `aggregate_refs` must be blocked.
- Acceptance functions without `coverage_types` must be blocked, including missing state-change, handoff, failure-path, and evidence surfaces.
- OpenSpec draft generation must preserve Domain Coverage and refuse coverage-blocked cases.
- Repo-local req worker skills must mention the new coverage contract without replacing checker authority.

## RED Baseline

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_domain_coverage_gate` failed because `domain_coverage_gate` did not exist and a no-coverage case still returned `requirements_ready`.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case` failed because `build_requirements_case_package()` did not accept `domain_coverage`.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_openspec_draft` failed because generated draft files did not include `Domain Coverage`.
- `PYTHONPATH=. python3 -m unittest tests.test_req_agent_skills` failed because req worker skills did not mention `domain_coverage_gate`, coverage obligations, lifecycle refs, or acceptance coverage types.

## GREEN Result

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_domain_coverage_gate` passed.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case` passed.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_openspec_draft` passed.
- `PYTHONPATH=. python3 -m unittest tests.test_req_agent_skills` passed.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_domain_coverage_gate tests.test_requirements_case tests.test_requirements_openspec_draft tests.test_requirements_ddd_readiness_gate tests.test_requirements_checker_gate tests.test_requirements_analysis_agent tests.test_req_agent_skills` passed: 51 tests.
- `PYTHONPATH=. python3 scripts/check_requirements_ddd_taxonomy.py --taxonomy requirements/config/requirements-taxonomy.yaml` passed.
- `python3 -m scripts.check_requirements_case wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md` passed with `domain_model_gate`, `domain_coverage_gate`, and `requirement_delivery_gate`.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md` passed with `blocking_count=0`.
- `openspec validate add-requirements-domain-coverage-gate --strict` passed; the CLI also printed a PostHog DNS flush error after validation.
- `python3 scripts/check_behavior_assets.py` returned non-zero because unrelated `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md` is missing required evaluation sections and prior-art evidence. This result is preserved here as an existing repo-wide behavior-asset checker blocker outside this change's file set.

## Behavior Replay

- Situation shape: a strict taxonomy v2 requirements case has a confirmed `domain_model` and delivery mappings but omits domain coverage.
- Trigger condition: `scripts/check_requirements_case.py` runs with `strict=True` and taxonomy version 2.
- Expected route or stop behavior: checker returns `domain_coverage_gate.passed=false`, final hard gate fails, and `req-handoff` must not create an OpenSpec draft.
- Repo-visible artifact for future agents: `scripts/requirements_domain_coverage.py`, `.codex/skills/req-agent/SKILL.md`, `.codex/skills/req-handoff/SKILL.md`, and this OpenSpec change.
- Expected output: blockers identify missing domain coverage, story lifecycle refs, or acceptance coverage types.
- Promotion boundary: the gate enforces reviewability of requirements cases; it does not prove implementation design, API, DDL, or release correctness.

## Prior-Art / Common-Rule Dedupe

- Scanned `AGENTS.md`, `PROJECT.md`, `openspec/specs`, `wiki/adr`, `wiki/ops`, repo-local req skills, and common/global rule paths for `domain_coverage`, `domain coverage`, `domain_model_gate`, and `requirement_delivery_gate`.
- Existing assets owned OpenSpec lifecycle, wiki frontmatter, behavior-asset evaluation, and the prior `domain_model_gate` / `requirement_delivery_gate` readiness surface.
- No existing behavior asset owned strict taxonomy v2 `domain_coverage_gate` semantics or required story/acceptance lifecycle coverage fields.
- This change owns the new requirements-domain coverage behavior. It references existing behavior-asset evaluation and OpenSpec lifecycle gates without restating generic git, testing, or taxonomy-frontmatter rules.

## Residual Risks

- Coverage quality still depends on human review; passing tests only prove that required fields and observable coverage classes are present.
- Failure-path detection is intentionally heuristic and currently keyed to known recovery/payment contexts and aggregates.
- Historical cases are not batch migrated; compatibility behavior remains scoped to strict taxonomy v2 gates and selected golden samples.
