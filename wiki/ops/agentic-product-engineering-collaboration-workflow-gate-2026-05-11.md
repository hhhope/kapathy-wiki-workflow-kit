---
artifact_type: workflow-gate
title: agentic-product-engineering-collaboration / workflow gate
canonical_object: agentic-product-engineering-collaboration
layer: ops
domain: product-engineering-collaboration
ops_area: workflow-trace
created: 2026-05-11
status: active
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/ops/agentic-product-engineering-collaboration-split-execution-2026-05-11.md
---

# Workflow Gate

## Current Gate

Do not continue by repairing H5. Do not sync Feishu. Do not claim the current
PNG files are final visuals.

Current report status remains `INVALID` because Reference, Paragraph Drift,
Judgment Ownership, and Visual gates are still `PARTIAL`, and Publish is `FAIL`.

## Execution Order

1. Confirm split execution route.
2. Produce Visual Production Brief.
3. Produce Article Evidence Matrix.
4. Generate or redraw five standalone visuals.
5. Inspect image outputs against the reference grammar.
6. Update report gate review.
7. Only then consider H5 embedding.
8. Feishu remains out of scope until all hard gates pass and the user explicitly
   approves writing.

## Inputs And Outputs

| Step | Input | Output | Acceptance |
|---|---|---|---|
| Route confirmation | handoff, report gate, three reference images, visual skills | split execution plan | It is clear which track owns what and where to stop. |
| Visual brief | reference images, current failed visuals, article claims | five image scripts | Every visual states claim, metaphor, format, objects, route, and QA. |
| Evidence matrix | source map, broad scan, timeline, podcast/video pool, report | chapter evidence matrix | Each chapter has claim, load-bearing sources, boundary, hard-source gaps. |
| Image generation/redraw | visual brief + evidence matrix | five local image assets | Standalone PNG/SVG files, not H5 substitutes. |
| Visual QA | five images + reference grammar | pass/fail notes | Thumbnail structure, readable Chinese, no H5/PPT screenshot feel. |
| Gate update | image QA + evidence matrix | updated report gate review | Visual Gate can move only with evidence; otherwise overall remains `INVALID`. |
| H5 embedding | passed images + explicit decision | H5 using approved images | H5 embeds or links images; it does not replace image delivery. |
| Feishu | passed report gate + explicit approval | Feishu draft/write | Text-only by default; image insertion requires separate approval. |

## Anti-Drift Rules

- A request for `图`, `出图`, `图片`, `图片模型`, `知识卡`, `一图流`, or
  `章节配图` must produce or prepare standalone visual assets.
- HTML may be used as a deterministic renderer or overlay tool only when it
  exports actual image assets.
- Do not treat current `agentic-visual-assets/*.png` as final quality.
- Do not continue article polishing while the visual route is unresolved.
- Do not call the source pool `全网`.
- Do not hard-quote podcasts/videos without transcript capture.

## Visual-Specific Stops

| Visual | Stop If | Required Correction |
|---|---|---|
| Word cloud / heat map | It is static decoration. | Make it source-backed: category, dispute axis, source route, or click target. |
| Timeline | It is only a pretty date line. | Show monthly discussion movement, counts, and source boundary. |
| Dumbbell | It is two circles plus text. | Draw execution objects, governance objects, and a load-bearing middle bridge. |
| Agent loop | It is a horizontal module chain. | Draw loop arrows, agent queue, review packet, replay trail, writeback, and human gate. |
| Evidence table | It just lists links. | Show what each source class can and cannot prove. |

## Feishu Boundary

Feishu is blocked until hard gates pass and the user approves. Default Feishu
output is text-only with local image paths or captions. Image insertion is a
separate external operation because API read-back does not prove client-side
usability.
