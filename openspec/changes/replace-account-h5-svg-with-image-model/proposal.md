# Proposal: Replace Account H5 SVG Visuals With Image Model Outputs

## Why

The current account-group onboarding H5 still uses manually drawn SVG-derived
PNG visuals for the main diagrams. The user requested that the corresponding
SVG visuals all be produced through the image model instead of continuing with
hand-authored SVG diagram assets.

## What Changes

- Generate image-model bitmap replacements for the five SVG-derived H5 visuals:
  - account capability map;
  - account system architecture;
  - account core chain;
  - Nirvana / active project entry map;
  - technical planning fishbone roadmap.
- Save generated bitmap assets under
  `wiki/reports/assets/account-group-onboarding-h5/`.
- Update the H5 image references to use the image-model outputs.
- Keep existing section order, headings, and account-domain explanations.
- Update the gate review with image-model prompts, asset paths, and
  verification evidence.

## Out of Scope

- Feishu sync or image insertion.
- Creating new source SVG diagrams.
- Rewriting account-domain copy beyond image alt/reference updates.
- Exposing credentials, internal URLs, personal contacts, QR codes, or access
  instructions.

## Impact

- H5 visuals move from SVG-authored diagram PNGs to image-model generated PNGs.
- Existing SVG assets may remain in the repository as historical editable
  references, but the H5 should not rely on them for the current displayed
  visuals.
