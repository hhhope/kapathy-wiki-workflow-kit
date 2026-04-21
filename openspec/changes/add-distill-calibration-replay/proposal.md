## Why

The repository now has a `distill` page for `agents-governance-drift` plus a
separate calibration retro that explains why parts of that distill overstate
the current level of agreement.

Right now that calibration is still narrative. The user explicitly asked
whether the recommendations had gone through TDD, and the answer was no.

The next smallest useful step is to add a bounded executable replay contract
for `distill` calibration, so the repository can fail structurally when a
calibration record does not preserve:

- which parts are session facts
- which parts are only candidate governance models
- which words overclaim current agreement
- what weaker wording would keep the page honest

## What Changes

- Define a replay contract for `agents-governance-drift` distill calibration
- Add an executable checker script for the calibration record
- Add one example replay record for the current 2026-04-21 distill dispute
- Publish a repo-visible replay harness page and a first validation note

## Capabilities

### New Capabilities

- `agents-governance-drift-distill-calibration-replay`: The repository SHALL
  provide an executable replay contract for validating distill-calibration
  evidence.

### Modified Capabilities

- `disagreement-management-method`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/add-distill-calibration-replay/`
- Adds one repo-local checker script, one example JSON record, and one unit
  test file
- Adds repo-visible harness and validation pages under `wiki/ops/`
