## Why

The repository now has a formal `live-conversation-reanchor-gate` policy and a RED/GREEN evaluation note, but that proof is still narrative.

The user explicitly asked for executable TDD rather than another round of descriptive validation. The gap is:

- the gate is documented
- the RED baseline is documented
- the GREEN behavior is documented
- but there is no executable replay contract that can fail structurally when the gate evidence is missing

The next smallest useful step is to add an executable replay harness for the re-anchor gate itself.

## What Changes

- Define a replay contract for `live-conversation-reanchor-gate`
- Add an executable checker script for the replay record
- Add at least one example replay record covering the current drift dispute
- Publish a short repo-visible harness page that explains the proof boundary

## Capabilities

### New Capabilities

- `live-conversation-reanchor-gate-replay`: The repository SHALL provide an executable replay contract for validating re-anchor-gate evidence.

### Modified Capabilities

- `live-conversation-reanchor-gate`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-reanchor-gate-executable-replay/`
- Adds one repo-local validation script and one example replay record
- Extends repo-visible validation guidance in `wiki/ops/`
