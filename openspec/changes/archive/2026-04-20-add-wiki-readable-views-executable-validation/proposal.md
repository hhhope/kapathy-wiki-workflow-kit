## Why

`wiki-readable-views` has been implemented and archived, but it does not yet have
the kind of TDD and pressure-test evidence the user explicitly asked for.

Current gap:

- the readable views exist
- the change has verification and archive review
- but there is no executable validation contract proving the reading-layer
  bundle is structurally present and index-linked

The smallest follow-up is to add executable validation for the readable views
themselves.

## What Changes

- Define a bounded executable validation contract for `wiki-readable-views`
- Add a checker script for the reading-view bundle
- Add an example validation record
- Add an evaluation artifact with RED baseline, GREEN result, and residual risks
- Publish a short repo-visible harness page

## Capabilities

### New Capabilities

- `wiki-readable-views-validation`: The repository SHALL provide executable
  validation for the readable-view bundle.

### Modified Capabilities

- `wiki-readable-views`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/add-wiki-readable-views-executable-validation/`
- Adds one repo-local validation script and one example validation record
- Adds one harness page under `wiki/ops/`
