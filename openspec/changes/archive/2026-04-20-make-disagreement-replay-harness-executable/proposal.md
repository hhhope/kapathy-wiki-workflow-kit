## Why

The repository already has:

- a formal disagreement-management method
- replay / harness validation pages
- runtime routing and archive-review integration

But the replay harness is still only a wiki template.

That means future validation still depends on a human remembering:

- which fields are mandatory
- which pass conditions matter
- what should count as an invalid replay record

The next step is not broader automation. It is a narrower move:

make the replay harness executable enough to validate a structured replay record.

## What Changes

- Add an executable replay-harness checker for disagreement-management validation.
- Define a minimal machine-checkable replay record shape.
- Add at least one sample replay record and run the checker against it.
- Update harness documentation to show how to use the executable checker.

## Capabilities

### Modified Capabilities

- `disagreement-management-method`

## Impact

- Adds a new OpenSpec change under `openspec/changes/make-disagreement-replay-harness-executable/`.
- Publishes a script-based checker under `scripts/`.
- Adds at least one sample replay record for verification.
