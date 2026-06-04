# enforce-req-agent-design-hard-gates

## Why

The agent subscription payment case exposed a reusable workflow gap: a
requirements case can be ready for product review and OpenSpec handoff while
still lacking the product-owned materials needed for detailed design. If this
distinction stays only in one case file, future `req-agent` runs can repeat the
same mistake by treating `requirements_ready` as permission to infer current
state, business rule parameters, or system boundaries.

## What Changes

- Add default detailed-design hard gates to new requirements case packages.
- Teach the requirements checker to report design hard-gate readiness
  separately from requirement hard-gate readiness.
- Update `req-agent` so normal future requirements work blocks detailed design
  until product clarifies:
  - current-state material package
  - business rule position table
  - system boundary contract table
- Add tests and evaluation evidence that prove the behavior is enforced.

## Out of Scope

- Changing the DDD taxonomy vocabulary.
- Blocking `requirements_ready` solely because detailed-design materials are
  missing.
- Generating full API, DDL, or detailed design artifacts.
- Reworking existing completed `req-agent` lifecycle architecture.

