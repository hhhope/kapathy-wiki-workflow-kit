## Context

The incoming owner is the account engineering lead, and the handover must prioritize operational takeover rather than project storytelling. The user explicitly wants the document to clarify:
- risks
- unfinished items
- scope drift within the current handover scope
- acceptance status against the full milestone target

The available evidence comes from two local spreadsheets:
- `涅槃焕新周报.xlsx`
- `涅槃产品上架梳理.xlsx`

The document must be written in Chinese and published to Feishu, with the repo keeping a markdown source-of-truth draft.

## Goals / Non-Goals

**Goals:**
- Produce a takeover-oriented handover document for the account engineering owner.
- Use a dual-baseline method:
  - M3.1 full target as the strategic baseline
  - recent weekly-report commitments as the tactical baseline
- Include item-level acceptance status for relevant modules and functions.
- Surface what needs active follow-up, not just what is already complete.
- Create a local markdown draft and push the same content into Feishu.

**Non-Goals:**
- Rebuild the entire Nirvana project history.
- Create a management-facing status report as the primary output.
- Normalize every spreadsheet inconsistency or missing owner field.
- Automatically infer missing facts without marking them as pending confirmation.

## Decisions

### Decision: Use a dual-baseline structure
The document will evaluate progress and gaps against:
- M3.1 full-scope target
- latest weekly-report commitments

This separates long-term scope drift from short-term delivery drift.

### Decision: Use a two-layer document structure
Top section:
- takeover summary for the incoming account owner

Bottom section:
- item-level acceptance and drift matrix

This keeps the document readable while still preserving detail.

### Decision: Use module-and-item granularity
The document will cover the modules visible in the evidence and relevant to takeover:
- product shelf / launch
- product enablement
- transaction / protocol payment
- profit sharing
- account
- gateway
- testing and joint-debug stages

Each relevant item will be labeled with current status and acceptance state.

### Decision: Preserve uncertainty explicitly
If an owner, completion state, or acceptance basis is not fully derivable from the spreadsheets, the document will mark it as `待确认` instead of guessing.

## Risks / Trade-offs

- [Risk] Spreadsheet data mixes planning, actual status, and future intent. → Mitigation: separate evidence by baseline and mark uncertain items.
- [Risk] The account owner handover can be polluted by too much cross-module detail. → Mitigation: keep the summary focused on takeover-critical items and move detail into the matrix.
- [Risk] Some acceptance states are implied rather than explicitly declared. → Mitigation: use `待验收` / `待确认` when evidence is incomplete.
- [Risk] Feishu publishing may fail because of auth or permission issues. → Mitigation: keep a local markdown draft as the durable source and retry publication once auth is confirmed.

## Migration Plan

1. Create OpenSpec artifacts for the handover document change.
2. Extract the key facts from the two spreadsheets.
3. Draft the local markdown handover document.
4. Verify the structure against the requested takeover focus.
5. Publish the document to Feishu.

## Open Questions

- Whether the account owner should explicitly inherit cross-module coordination items or only account-owned execution items.
- Which items the user considers the top 5 highest-risk takeover misses if later refinement is needed.
