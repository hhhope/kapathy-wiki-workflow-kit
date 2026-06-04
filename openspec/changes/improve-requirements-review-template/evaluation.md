# Evaluation

## Pressure Scenarios

- A payment transaction story with correct `domains`, `contexts`, and
  `aggregates` must not render as labels only.
- A reviewer must be able to see why a coverage item is considered a full
  first-release story, what the taxonomy references mean, what gates close, and
  how to evaluate the output.
- Regenerating an existing case must preserve machine case data so the
  requirements checker still passes.

## RED Baseline

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case` failed before
  implementation.
- Expected failure:
  `AssertionError: '## Reviewable Coverage' not found`.
- The old output rendered only compressed lines such as
  `domains=payment_transaction; contexts=...; aggregates=...` and did not
  include `review_judgment`, taxonomy `meaning`, `gate_closure`, or `eval_plan`.

## GREEN Result

- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case` passed:
  6 tests.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_case tests.test_requirements_domain_coverage_gate tests.test_requirements_openspec_draft`
  passed: 13 tests.
- `PYTHONPATH=. python3 scripts/check_requirements_case.py wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md --repo-root . --format markdown`
  passed with `requirements_ready`, `Hard gate passed: True`, and no blockers.
- `openspec validate improve-requirements-review-template --strict` passed. The
  CLI printed a PostHog DNS flush error after validation; validation itself
  reported `Change 'improve-requirements-review-template' is valid`.
- `PYTHONPATH=. python3 scripts/check_behavior_assets.py` returned non-zero
  because unrelated `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
  is missing required evaluation sections, replay evidence, and prior-art
  dedupe evidence. This is an existing repo-wide behavior-asset checker blocker
  outside this change's file set.

## Re-render Evidence

- Regenerated
  `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`
  from its machine case data using the updated renderer.
- The rendered case now includes `## Reviewable Coverage` with structured JSON
  containing `review_judgment`, `taxonomy_refs`, `acceptance_functions`,
  `gate_closure`, and `eval_plan`.
- The regenerated case still passes the requirements checker.

## Behavior Replay

- Situation shape: a strict taxonomy v2 case has technically correct domain
  coverage references, but reviewers cannot understand the judgment from labels
  alone.
- Trigger condition: `render_requirements_case_markdown()` renders a package
  with domain coverage.
- Expected route or stop behavior: the readable output includes review JSON
  before roles/stories, while machine case data remains unchanged.
- Repo-visible artifact for future agents:
  `scripts/requirements_review_template.py`,
  `scripts/requirements_case.py`, and this OpenSpec change.
- Expected output: reviewers can inspect business meaning, taxonomy meanings,
  first-release scope, deferred work, gate closure, and eval expectations.
- Promotion boundary: this proves template output is reviewable; it does not
  prove that every future generated judgment is domain-correct.

## Residual Risks

- The fallback meanings are intentionally conservative and most precise for the
  payment transaction refs covered by the pressure test.
- Human review is still required for whether a story should be `full_story`,
  `light_coverage`, `out_of_scope`, or `follow_up`.
- Historical case files are not batch migrated; only the selected
  `agent-subscription-payment` sample was regenerated.
