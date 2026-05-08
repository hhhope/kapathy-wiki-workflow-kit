## Why

The Account Wiki article set reached a failed review state after reference
readback. The previous five-article packet had been synced to Feishu as an
audit draft, but the gate review later corrected the quality decision to
`INVALID` because the linked reference articles and visual requirements were
not fully mapped.

The remaining local drafts are still too thin for release:

- the runtime page explains a path table but not the actual operating flow
- the validation/cases page summarizes evidence without concrete replay and
  readback data
- the current visual file covers overview-style cards only and does not provide
  dedicated runtime or validation/cases visuals
- the current infographic workflow guidance does not explicitly protect
  multi-page Account Wiki article sets from collapsing into one generic
  onepager

## What Changes

- Repair the local Account Wiki article set before any Feishu write.
- Add runtime and validation/cases visuals based on the reference style
  language rather than copying the reference images.
- Update the public report gate review with corrected reference, learning,
  visual, split, evidence, and replay decisions.
- Add behavior proof for any skill change before treating it as complete.
- Keep Feishu sync out of scope until local drafts and evidence pass.

## Impact

- A future agent should see the failed packet as frozen, not review-ready.
- Runtime and validation/cases drafts should become concrete enough to review
  locally.
- Visual proof should distinguish missing final artwork from completed local
  diagram assets.
- Any `infographic-onepager` skill adjustment must include RED/GREEN evidence
  before being relied on.

## Non-Goals

- Do not update or publish Feishu documents in this change.
- Do not archive the already-complete quality-gate changes as part of this
  repair.
- Do not promote one-off Account Wiki wording into global behavior policy.
