# Design

## Scope

This change improves the readable requirements case template. It is a
requirements workflow output change, not a taxonomy or product-domain change.

Implementation should stay inside:

- `scripts/requirements_case.py`
- focused tests for requirements case rendering
- this OpenSpec change's evaluation evidence

The checker already owns machine readiness. This change adds a human review
layer that explains the judgments behind the machine references.

## Review Output Shape

Rendered strict taxonomy v2 cases should include structured review JSON for
domain coverage and stories. The rendered output should make these fields visible
before machine case data:

- `review_judgment`
- `taxonomy_refs`
- `acceptance_functions`
- `gate_closure`
- `eval_plan`

The review output should not replace the existing summary lines. It should add a
review block that reviewers can read without expanding the machine JSON.

## Review Judgment Contract

Each review block should explain:

- `coverage_decision`: `full_story`, `light_coverage`, `out_of_scope`, or
  `follow_up`
- `business_meaning`
- `why_this_domain`
- `first_release_scope`
- `out_of_scope`
- `future_work`
- `reviewer_question`

When source case data does not provide these fields, rendering may derive a
conservative fallback from existing domain coverage, story, acceptance, and
review-note fields. The fallback must be explicit that it is derived from case
coverage metadata, not a new product decision.

## Taxonomy Reference Contract

Each rendered taxonomy reference should include both an ID and a plain-language
meaning. At minimum:

- domains explain the subdomain responsibility
- contexts explain the bounded-context responsibility
- aggregates explain the business object whose lifecycle is covered

Known meanings may be derived from
`requirements/config/requirements-taxonomy.yaml` when available. If a meaning
cannot be derived, the output should still include a conservative fallback such
as `Meaning not provided in case data`.

## Gate Closure Contract

The readable block should connect human review back to machine gates:

- `domain_model_gate`: what the domain model declares
- `domain_coverage_gate`: which coverage mappings close the taxonomy references
- `requirement_delivery_gate`: which story and acceptance fields make the
  requirement deliverable
- `human_review_gate`: what the reviewer must decide

This is explanatory output. The existing checker remains the source of pass/fail
truth.

## Eval Contract

Evaluation must include both machine and human-readability checks:

- RED: old compressed output lacks `review_judgment`, `taxonomy_refs`,
  `gate_closure`, and `eval_plan`.
- GREEN: new output includes the review block and keeps existing machine case
  data unchanged.
- Human review fixture: a payment transaction story must be understandable from
  the rendered review block without relying only on raw tags.

## Compatibility

Existing cases without review metadata should still render. The generated review
block may use derived defaults, and the machine data must round-trip unchanged.

Historical markdown files do not need batch migration. Regenerating a case with
the updated renderer is enough to receive the review block.

## Proof Boundary

Tests can prove the template includes review judgments and eval scaffolding.
They cannot prove every future judgment is correct. Correctness still depends on
the requirements agent, checker output, and human review.
