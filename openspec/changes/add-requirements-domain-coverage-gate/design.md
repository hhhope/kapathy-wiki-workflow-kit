# Design

## Scope

This change upgrades requirements readiness from "domain model and story
mapping exist" to "domain model, domain coverage, lifecycle stories, and
observable acceptance coverage are all reviewable." It is a requirements
workflow gate/template change.

The implementation should remain scoped to requirements case generation,
checking, rendering, worker guidance, and OpenSpec handoff output. It should not
rewrite the taxonomy model itself unless a small non-semantic field is needed to
represent coverage decisions.

## Case Shape

New taxonomy v2 cases should include a top-level `domain_coverage` or
equivalent machine-readable list. Each item should identify:

- `subdomain`
- `coverage_type`: `primary`, `required_payment`, `conditional_payment_in_scope`,
  `adjacent_agent_service`, `light_coverage`, `out_of_scope`, or `follow_up`
- `contexts`
- `aggregate_roots`
- `user_story_ids`
- `acceptance_function_ids`
- `review_note`

The rendered markdown should expose the same information in a readable
`## Domain Coverage` section before roles and stories.

## Story Contract

Each strict-mode user story should keep existing fields and add coverage fields:

- `domain_refs`
- `context_refs`
- `aggregate_refs`
- evidence anchor

The checker should verify that every referenced value is known in the active
taxonomy or explicitly recorded as a candidate/follow-up term. User stories
should not be considered complete only because they have `role_ref`, `want`,
and `benefit`.

## Acceptance Contract

Each strict-mode acceptance function should keep existing fields and add a type
or equivalent coverage classification:

- `state_change`
- `handoff`
- `failure_path`
- `evidence`

An acceptance function may cover more than one story, but it must still be
observable and evidence-anchored.

The checker should verify:

- state-changing aggregate lifecycles have at least one `state_change`
  acceptance function
- every `domain_model.context_handoffs` item has at least one `handoff`
  acceptance function or a documented `light_coverage` / `follow_up`
  explanation
- known failure paths surfaced by the source or taxonomy trigger rules have
  `failure_path` acceptance
- auditable payment, ledger, reconciliation, settlement, and payout flows have
  `evidence` acceptance

## Coverage Gate

Add `domain_coverage_gate` to the checker result. The final hard gate should
pass only when all three gates pass:

- `domain_model_gate`
- `domain_coverage_gate`
- `requirement_delivery_gate`

The gate should not require full expansion of every taxonomy context by default.
Instead, every required/in-scope subdomain or context must be either covered or
explicitly classified:

- `full_coverage`: has story and acceptance coverage
- `light_coverage`: has minimal story/acceptance coverage plus reason
- `out_of_scope`: excluded with reason
- `follow_up`: deferred with reason and next action

Silent absence should block readiness.

## Worker Updates

Update worker guidance so generation naturally produces coverage-aware cases:

- `req-domain-analysis`: emits coverage obligations from taxonomy examples,
  trigger rules, and confirmed user scope.
- `req-scope`: maps role obligations to case-local roles and preserves owner
  gaps as open questions.
- `req-stories`: writes lifecycle stories for domain objects and contexts, not
  only owner-oriented stories.
- `req-acceptance`: writes observable state-change, handoff, failure-path, and
  evidence acceptance functions.
- `req-agent`: reports `domain_coverage_gate` before allowing handoff.

## Handoff Output

OpenSpec draft generation should include the coverage summary so reviewers can
see how each requirement maps back to taxonomy domains and contexts. Draft
generation should still require `requirements_ready`; it should not create
drafts from cases with coverage blockers.

## Compatibility

Legacy or compatibility-mode cases may remain readable with the existing gate.
Strict taxonomy v2 cases should require the new coverage contract. Existing
historical cases do not need batch migration unless selected as golden samples.

## Proof Boundary

Implementation proof should include RED/GREEN checker tests, a rendered case
template check, and at least one golden sample based on
`agent-subscription-payment`. Passing unit tests prove checker/template
behavior; they do not prove future agents will always choose good domain
coverage without human review.
