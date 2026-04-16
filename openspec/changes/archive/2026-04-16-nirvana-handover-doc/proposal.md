## Why

The Nirvana project handover needs to be turned into an actionable document for the incoming account engineering owner, not just a summary of weekly reports. The key goal is to make risks, unfinished items, scope drift, and acceptance status explicit against both the M3.1 baseline and recent weekly commitments.

Without a structured handover document, the incoming owner will inherit scattered facts from weekly reports and product planning spreadsheets, which makes gaps, stalled work, and acceptance boundaries easy to miss.

## What Changes

- Create a handover document for the incoming account engineering owner of the Nirvana project.
- Extract milestone, module, owner, status, risk, and testing facts from the provided weekly report and product launch spreadsheets.
- Organize the handover using two baselines:
  - M3.1 full-scope target
  - recent weekly-report commitments
- Make explicit:
  - unfinished items
  - current risks
  - scope drift
  - item-level acceptance status
  - first-week alignment checklist
- Publish the document to Feishu as the primary delivery medium.

## Capabilities

### New Capabilities
- `nirvana-handover-doc`: Create and publish a structured Nirvana project handover document for the incoming account engineering owner.

### Modified Capabilities

None.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/nirvana-handover-doc/`.
- Adds a local markdown handover draft in the repo for traceability and reuse.
- Produces a Feishu document based on the local draft.
- Uses the two Excel files under `/mnt/c/Users/yan/Desktop/nirvana/` as primary evidence sources.
