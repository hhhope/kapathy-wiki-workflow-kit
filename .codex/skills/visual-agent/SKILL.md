---
name: visual-agent
description: Use when the user asks in formal or casual language to make, draw, add, polish, convert, or generate a visual artifact, including diagrams, H5 visual pages, knowledge cards, infographics, image-model output, visual assets, or SVG/H5/image/hybrid mode choices.
---

# Visual Agent

Runtime card for visual production. Load this before any visual worker or image
tool.

## Trigger

Trigger on visual-deliverable intent, not on fixed phrases.

Use this skill when the requested output is meant to be seen as a designed,
spatial, graphical, image-like, or browser-rendered artifact. This includes
requests to create, transform, polish, choose the medium for, or add visual
presentation to content.

Classify the intent by role:

- Visual artifact requested: diagram, map, card, poster, cover, image,
  illustration, infographic, chart, whiteboard, H5/HTML visual page, screenshot,
  slide-like page, layout, asset set, or visual package.
- Visual transformation requested: turn text/data/notes/process/source material
  into something visual, scannable, spatial, interactive, shareable, or
  presentation-ready.
- Visual decision requested: choose between SVG, H5/HTML, image model, hybrid,
  screenshot, generated image, or another visual medium.
- Visual repair requested: improve composition, visual hierarchy, readability,
  image quality, rendering, layout, labels, or visual consistency.

Casual, incomplete, or shorthand language still triggers when the intended
deliverable is visual. Do not require the user to say "visual", "diagram",
"SVG", "H5", or any exact keyword.

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

A reference PNG, screenshot, poster, cover, or "similar image" request is
image-mode pressure, not strong evidence for deterministic rendering. Do not
start HTML/CSS/SVG/browser-screenshot production for that request unless the
user explicitly chooses deterministic output after the mode fork.

## Source Roles

For reference-image-driven visual work, map source roles before prompt/script
generation:

- content source: current article, draft, markdown, oral brief, or user input
  that owns the message.
- style source: reference images that only provide layout, composition, palette,
  texture, density, and visual grammar unless the user explicitly asks to reuse
  their content.
- executor: image model, hybrid overlay, deterministic renderer, whiteboard, or
  another production tool.

The route or visual brief must state what each output communicates, which
current content section it comes from, which style source only supplies visual
grammar, the selected route, and what must be verified after generation. Do not
repair source-role confusion with brittle forbidden-noun lists unless an actual
generated output already drifted and needs a targeted repair pass.

## Delivery Capability

Before promising repo-local image files for `image_model` or image-model visual
layers, verify that delivery is possible through an exposed artifact export/path
or a usable image-generation API credential. Codex login tokens are not OpenAI
Platform image API keys unless image-generation scope is verified.

If the current runtime can only show a chat `Generated Image` artifact and
cannot expose a local file, do not claim file generation. Produce client-mode
prompt markdown or an equivalent prompt package with reference image paths,
source-role map, copyable prompt, and verification checklist.

## Routes

Named visual workers are child routes, not entry points, unless the user is
debugging that worker.

Before naming a child worker in `Next Action`, verify that the child skill is
available in the current runtime. If it is not available, do not pretend to
route to it; keep ownership in `visual-agent`, ask the mode fork or state the
missing worker in `Blocked Action`.

Bundled visual workers in this repository:

- Article visual packages and card series: `knowledge-article-visual`.
- Single poster, long image, teaching card, or per-image script:
  `infographic-onepager`.
- Dense concept one-pager, governance visual, H5/HTML long infographic, or
  carousel-style knowledge visual: `visual-knowledge-onepager`.
- Flow, process, state, payment/fund/account sequence: `svg-flow-diagram`.
- Service interaction order, call sequence, or Mermaid sequence diagram:
  `sequence-diagram`.
- System architecture, infrastructure, security, integration, topology, or
  deployment diagram: `architecture-diagram`.
- Frontend visual polish, dashboard UX, chart/widget/icon/layout quality, or UI
  visual repair: `frontend-visual-governor`.
- Management-facing Gantt, capability map, roadmap/milestone visual, or weekly
  project update H5/HTML brief: `project-weekly-report-gantt-map`.
- Feishu whiteboard output: `lark-whiteboard`.

Runtime/system routes:

- When routed by `atlas`, preserve Atlas visual anchors. Do not compress
  approved per-section visuals into a generic visual package without user
  approval, and verify the visual proof task rather than layout alone.
- Direct bitmap generation or image-model visual layer: `imagegen` only when the
  current runtime provides the image tool/skill, and only after mode, source,
  prompt/script, and verification boundary are set.
- Reader-facing reports, H5/share pages, Feishu-facing visuals, or public
  materials: preserve `public-report-quality-gate` when the host runtime
  provides it, then route through `visual-agent` to the selected visual worker.

Use this route matrix after the mode decision:

- Knowledge article visuals, multi-section visual packages, card series,
  article-learning visuals, or report visual asset sets:
  `knowledge-article-visual`.
- Single infographic, one-page poster, long image, horizontal teaching card,
  screenshot-friendly HTML, carousel-like visual, or image prompt/script:
  `infographic-onepager`.
- Dense retro-grid one-pager, Xiaohongshu-style carousel, governance concept
  card, or abstract framework visual: `visual-knowledge-onepager` when present.
- Flow, process, state, payment/fund/account sequence, Mermaid sequence source,
  or information/fund flow: `svg-flow-diagram`.
- Service interaction order, call sequence, or Mermaid sequence diagram
  authoring before final visual conversion: `sequence-diagram` when present.
- System architecture, infrastructure, security, integration, topology,
  deployment, component relationship, or technical architecture diagram:
  `architecture-diagram`.
- Frontend visual polish, dashboard UX, chart/widget/icon/layout quality, or
  existing UI visual repair: `frontend-visual-governor`.
- Management-facing Gantt, capability map, roadmap/milestone visual, or weekly
  project update H5/HTML brief: `project-weekly-report-gantt-map`.
- Feishu whiteboard output: `lark-whiteboard`.
- Direct bitmap generation or image-model visual layer: runtime/system
  `imagegen`.

## Stops

- Do not claim visual quality without screenshot/readback or equivalent visual
  verification.
- Do not insert generated images into Feishu or whiteboards without explicit
  user approval.
