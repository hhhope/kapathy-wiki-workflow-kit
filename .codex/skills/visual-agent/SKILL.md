---
name: visual-agent
description: Use when the user asks in formal or casual language to make, draw, add, polish, convert, or generate a visual artifact, including diagrams, H5 visual pages, knowledge cards, infographics, image-model output, visual assets, or SVG/H5/image/hybrid mode choices.
---

# Visual Agent

Runtime card for visual production. Load this before any visual worker or image
tool.

## Trigger

Use for any request to create, add, improve, transform, or choose a visual
deliverable. Casual wording counts: "弄个图", "画一下", "整张图", "做成卡片",
"配几张图", "图像化一下", and similar phrasing are examples, not a closed list.

Do not use only because the wording is casual; a visual deliverable must be
requested.

## Response

Start visual work with a compact route block:

```text
- `Using visual-agent`
- `Intent`
- `Visual Case`
- `Content Shape`
- `Output Mode`
- `State`
- `Allowed Action`
- `Blocked Action`
- `Next Action`
- `Evidence`
```

If the block lacks `Using visual-agent`, treat the response as a controller
bypass unless the user is debugging another visual skill.

## Modes

- `svg`: exact structure, editable diagram, reliable Chinese labels, fund/account
  flows, architecture, tables, or compliance text.
- `h5_html`: interactive or scrollable explainer, dashboard, or browser-verified
  report page.
- `image_model`: visual richness, illustration, cover, or bitmap-first output
  where exact text is not the source of truth.
- `hybrid`: image-model visual layer plus deterministic text/layout overlay.

If the user did not choose a mode and the content does not strongly choose one,
ask this fork before production: `SVG`, `H5/HTML`, `Image model`, `Hybrid`.

Do not default casual or ambiguous visual requests to H5/HTML, SVG, browser
screenshots, or deterministic cards just because they are easier to render or
safer for Chinese text. If the user rejects prior H5/SVG-like output or asks for
image-model-like quality, treat `image_model` or `hybrid` as the active route
pressure until they choose deterministic SVG/H5.

## Routes

Named visual workers are child routes, not entry points, unless the user is
debugging that worker.

- Reader-facing report/H5/share/Feishu visual:
  `public-report-quality-gate -> visual-agent -> child worker`.
- Article or multi-section visual package: `knowledge-article-visual`.
- Single card, poster, long image, or per-image script: `infographic-onepager`.
- Flow, process, state, payment/fund/account sequence: `svg-flow-diagram`.
- System, deployment, integration, topology, pipeline: `architecture-diagram`.
- Direct bitmap generation: `imagegen` only after mode, source, prompt/script,
  and verification boundary are set.
- Feishu whiteboard: `lark-whiteboard`.

## Stops

- Do not claim visual quality without screenshot/readback or equivalent visual
  verification.
- Do not insert generated images into Feishu or whiteboards without explicit
  user approval.
