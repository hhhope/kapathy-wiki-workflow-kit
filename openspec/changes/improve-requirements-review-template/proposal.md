# Proposal

## Why

The requirements domain coverage gate now proves that strict taxonomy v2 cases
carry domain, context, aggregate, story, and acceptance mappings. The remaining
gap is human reviewability.

The `agent-subscription-payment` case exposed the problem: fields such as
`domains=payment_transaction`, `contexts=payment_intent_context`, and
`aggregates=payment_attempt` are accurate, but the readable case output compresses
them into technical labels. A reviewer cannot easily see what each taxonomy
reference means, why the case classifies a story as full first-release coverage,
what is deferred, or how to evaluate that the template is understandable.

The acceptance granularity is good. The template needs to expose the agent's
judgment and the review/eval contract around that judgment.

## What Changes

- Add a review-oriented requirements case output shape for strict taxonomy v2
  cases.
- Render domain coverage, user stories, and acceptance functions with structured
  review JSON that includes business meaning, taxonomy meanings, scope boundary,
  future work, reviewer question, and gate closure.
- Preserve existing machine case data and checker semantics.
- Add tests that fail against the old compressed output and pass only when the
  review output is explicit enough for human audit.
- Record RED/GREEN evaluation evidence for the template behavior.

## What Does Not Change

- Does not change the requirements taxonomy vocabulary.
- Does not change `domain_model_gate`, `domain_coverage_gate`, or
  `requirement_delivery_gate` pass/fail semantics.
- Does not implement the Agent subscription payment product.
- Does not generate OpenSpec drafts automatically from requirements cases.
- Does not migrate all historical case files.

## Source Evidence

- `wiki/ops/requirements-cases/2026-06-02-160000-agent-subscription-payment.md`
- `scripts/requirements_case.py`
- `scripts/requirements_domain_coverage.py`
- `openspec/changes/add-requirements-domain-coverage-gate/*`
