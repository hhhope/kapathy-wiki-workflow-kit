---
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
artifact_type: runtime-replay
title: agentic-product-engineering-collaboration / tool-executor-bypass-drift
canonical_object: agentic-product-engineering-collaboration-tool-executor-bypass-drift
related_objects:
  - public-report-quality-gate
  - knowledge-article-visual
  - infographic-onepager
  - imagegen
derived_from:
  - docs/superpowers/specs/2026-05-18-tool-executor-bypass-visual-routing-design.md
  - docs/superpowers/plans/2026-05-18-tool-executor-bypass-visual-routing.md
  - openspec/changes/harden-tool-executor-bypass-routing/tasks.md
  - wiki/ops/visual-output-routing-drift-explore-2026-05-11.md
validates:
  - openspec/changes/harden-tool-executor-bypass-routing
created: 2026-05-18
---

# agentic-product-engineering-collaboration / tool-executor-bypass-drift

## Trace Purpose

This record preserves the 2026-05-18 route drift that happened during the
Agentic Product Engineering Collaboration H5 visual work.

It is a repo-visible drift trace and route-repair evidence for the active
OpenSpec change `harden-tool-executor-bypass-routing`. It is not a publish
review, visual QA result, or proof that every future client will auto-route
correctly.

## Original User Intent

The user wanted to update H5 report visuals for
`agentic-product-engineering-collaboration` by using the existing article visual
grammar and the correct skill route.

The intended output was not generic illustration. It needed to follow the
existing H5/report visual language:

- warm paper background
- thick black marker outlines
- large handwritten Chinese headings
- colored number badges
- boxed modules and arrows
- doodle-style icons
- bottom takeaway banners
- section-level visual assets that could later be embedded into the H5

The request was delivery-sensitive because it affected a reader-facing H5/share
draft, so the parent workflow should have been the public report gate.

## Drift Evidence

The response drifted by treating `imagegen` as the main route owner after the
user mentioned image-model output.

Observed drift:

- It generated generic, low-text illustrations instead of report-specific
  information graphics.
- It skipped `public-report-quality-gate`, even though the target was a
  reader-facing H5/share report.
- It skipped `knowledge-article-visual`, which should own article-level visual
  series structure.
- It skipped `infographic-onepager`, which should compress each visual into a
  card or one-page script before generation.
- It did not inspect existing H5 visuals before producing new assets.
- It did not use the existing visual scripts or visual production route as the
  control path.
- It treated the low-level image-generation tool as sufficient workflow
  authority, instead of as the final executor.

The failure was not "image generation was available". The failure was that the
route jumped to an executor before the workflow that owns intent, output shape,
review, and evidence had run.

## Rejected Fixes

Rejected fix: add a brittle trigger-word list to `AGENTS.md` or root rules.

Reason: the problem is not one missing phrase such as `图片模型`, `生图`, or
`章节配图`. A trigger-word patch would remain fragile and would push
repo-specific delivery behavior into the wrong layer.

Rejected fix: make direct `imagegen` the workflow owner for H5 visuals.

Reason: `imagegen` can produce bitmap candidates, but it does not own the
reader, article argument, visual grammar, existing-artifact inspection,
per-image compression, public review boundary, or evidence ledger.

## Corrected Framing

Low-level tools are executors.

Delivery-sensitive outputs must first pass the workflow that owns:

- intent
- output shape
- review boundary
- evidence boundary
- publication or share-readiness claims

For this incident, `public-report-quality-gate` owns the outer route because the
target is a reader-facing H5/share report. Visual production then delegates down
the stack instead of bypassing it.

## Correct Route

Correct route:

`public-report-quality-gate -> knowledge-article-visual -> infographic-onepager -> imagegen`

Route responsibilities:

| Layer | Responsibility |
|---|---|
| `public-report-quality-gate` | Own the reader-facing report boundary, article intent contract, visual gate, review/evidence boundary, and publish/share readiness claims. |
| `knowledge-article-visual` | Own the article-level visual series and decide how the H5 sections become a coherent visual package. |
| `infographic-onepager` | Own per-image compression: horizontal teaching-card or one-page infographic script, format, layout, and prompt/rendering decision. |
| `imagegen` | Act as the bitmap executor after the route, visual grammar, and per-image scripts exist. |

This route does not forbid image generation. It makes image generation the final
executor under the public-report and visual-planning workflows.

## Evidence Boundary

This record proves only that the drift was identified and that the corrected
route was recorded in the repository.

It does not prove:

- every future client will automatically load the right skill
- generated visuals will match the H5 grammar without visual QA
- the H5 is review-ready or share-ready
- direct image-model Chinese text will be reliable
- share zip regeneration is included

Future behavior still depends on agents loading and following the repo
instructions, skill text, OpenSpec change artifacts, and pressure scenarios.

## Next Action

Next action for the active change:

1. Update `public-report-quality-gate` with the tool-executor-bypass
   anti-pattern.
2. Add pressure scenarios that fail direct executor routing and pass the
   corrected parent-route chain.
3. Produce the H5 visuals through the corrected route:
   `public-report-quality-gate -> knowledge-article-visual ->
   infographic-onepager -> imagegen`.
4. Inspect the generated or assembled visual assets against the existing H5
   grammar before embedding or claiming visual quality.
