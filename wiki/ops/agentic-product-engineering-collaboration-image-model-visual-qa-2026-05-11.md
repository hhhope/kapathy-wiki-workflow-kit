---
artifact_type: visual-qa
title: agentic-product-engineering-collaboration / image-model visual qa
canonical_object: agentic-product-engineering-collaboration
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
created: 2026-05-11
status: partial
derived_from:
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/agentic-visual-assets-v2/00-total-infographic.png
  - wiki/reports/agentic-visual-assets-image-model/00-total-infographic-image-model.png
---

# Image-Model Visual QA

## Decision

The SVG/Playwright route under `wiki/reports/agentic-visual-assets-v2/` should
not be treated as final visual output. It is a programmatic draft and still
looks like stacked SVG/H5 cards.

The image-model anchor at
`wiki/reports/agentic-visual-assets-image-model/00-total-infographic-image-model.png`
is the correct direction for the total infographic. The four chapter cards in
the same directory now follow the same image-model route.

## Why The SVG Route Failed

- Six modules repeat the same empty card structure.
- Icons decorate but do not explain relationships.
- Arrows are isolated and do not form real flows.
- There is too much blank space and too little visual density.
- The result reads like a slide outline, not a standalone teaching poster.

## Why The Image-Model Anchor Is Better

- It uses a six-section long-poster structure close to the Account Wiki
  reference.
- Each section is a small explanation graphic, not just a bullet card.
- The dumbbell, bridge, operating-system chain, review loop, and people section
  are drawn as visual objects.
- The bottom golden sentence works as a real visual conclusion.

## Remaining Checks

- Verify Chinese text for typos or model-introduced wording drift.
- Decide whether exact publication text should be overlaid deterministically.
- Review whether the chapter-card labels should be renumbered or accepted as
  image-model draft labels.
- Update `report-gate-review` only after all five visuals are reviewed.

## Image-Model Files

| File | Status | Note |
|---|---|---|
| `00-total-infographic-image-model.png` | better direction | Closest to `account-wiki-onepager.png`; six-section dense poster. |
| `01-industry-debate-card-image-model.png` | draft | Strong visual metaphor; text needs review. |
| `02-company-dumbbell-card-image-model.png` | draft | Correct dumbbell/bridge metaphor; text needs review. |
| `03-operating-system-card-image-model.png` | draft | Strong old-to-new transformation; generated label says `04`, needs review if used as chapter 03. |
| `04-reviewable-loop-card-image-model.png` | draft | Correct loop/rollback metaphor; generated label says `05`, needs review if used as chapter 04. |
