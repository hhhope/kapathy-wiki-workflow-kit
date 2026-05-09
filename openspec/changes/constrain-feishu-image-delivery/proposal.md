## Why

The Account Wiki repair showed a delivery gap: generated chapter images can be
valid local assets, and Feishu image insertion can return image tokens and
read-back logs, while the resulting image-bearing Feishu document still freezes
Codex or the Feishu client.

The current `public-report-quality-gate` asks at image/H5 and Feishu sync
fork-points, but it does not yet make "local image assets" and "Feishu image
insertion" separate default routes. Future agents may still treat user approval
for a Feishu draft as approval to insert images, or treat image-token read-back
as delivery-quality proof.

## What Changes

- Update `public-report-quality-gate` so visual generation remains expected for
  reader-facing reports, but Feishu image insertion is not the default delivery
  route.
- Require explicit user approval plus client-risk acceptance before any Feishu
  image insertion.
- Record that image tokens and read-back logs are audit evidence only, not proof
  of client usability.
- Add pressure-scenario and gate-review artifact guidance for text-only Feishu
  drafts with local asset paths.

## Impact

- Updates `.codex/skills/public-report-quality-gate/`.
- Adds spec and evaluation evidence for Feishu image-delivery boundaries.
- Does not modify existing Feishu documents.
- Does not create an ADR; this is a skill/runtime constraint, not yet a new
  cross-change stable decision beyond existing ADR-0009 explore-trace behavior.

## Non-Goals

- Do not remove existing image blocks from Feishu.
- Do not generate more Account Wiki images in this change.
- Do not change `openspec-explore` behavior.
- Do not promote this into global/root guidance.
