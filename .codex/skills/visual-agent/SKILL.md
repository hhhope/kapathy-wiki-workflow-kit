---
name: visual-agent
description: Use when the user asks for 制图, 出图, 配图, visual routing, knowledge cards, infographic pages, H5 visual pages, SVG diagrams, image-model output, or a choice between SVG, H5/HTML, direct image generation, and hybrid visual production.
---

# Visual Agent

Use this as the normal user-facing controller for visual production requests in
this repo. It is modeled after the `cr-agent` and `wiki-medical-agent`
controller pattern: classify first, expose state, route to bounded workers, and
do not become the renderer itself.

## Response Contract

Every normal response MUST show these fields when routing or executing visual
work:

- `Intent`
- `Visual Case`
- `Content Shape`
- `Output Mode`
- `State`
- `Allowed Action`
- `Blocked Action`
- `Next Action`
- `Evidence`

Keep the fields compact. Use `Blocked Action: none` only when the route is ready.

## Intent Classes

- `mode_fork`: user wants help choosing SVG, H5/HTML, image-model, or hybrid.
- `article_visual_package`: reader-facing report, Feishu article, H5 share page,
  or multi-section visual package.
- `single_infographic`: one card, one poster, one long image, one teaching page,
  or one-page summary.
- `flow_svg`: payment flow, fund flow, account flow, process, state, sequence,
  Mermaid-like source, or other deterministic flow diagram.
- `architecture_diagram`: system architecture, interface architecture,
  deployment, topology, data pipeline, or component relationship diagram.
- `h5_onepager`: interactive/scrolling HTML visual board or one-page H5.
- `image_generation`: bitmap-first illustration, cover, style exploration, or
  image prompt execution.
- `whiteboard_visual`: Feishu whiteboard creation or editing.
- `status_or_review`: user asks what visual skill or route should be used.

## Output Modes

- `svg`: exact structure, editable diagram, reliable Chinese labels, fund/account
  flows, architecture, tables, or compliance text.
- `h5_html`: interactive or scrollable report page, dashboard-like explanation,
  long-form H5, or browser-verifiable visual artifact.
- `image_model`: visual richness, illustration, mood, cover art, or bitmap-first
  exploration where exact text is not the source of truth.
- `hybrid`: image-model asset plus deterministic text/layout overlay. Prefer
  this when image quality and Chinese/text accuracy both matter.
- `prompts_only`: user only asks for image prompts or art direction.
- `ask_human`: no explicit preference and source shape does not strongly select
  a mode.

## Mode Decision Rules

Honor an explicit user preference unless it conflicts with the source material.
If preference and content conflict, state the tradeoff and offer a deterministic
or hybrid alternative before production.

If no preference is given, choose from strong content evidence:

- Mermaid, sequence, fund flow, process flow, state machine, compliance process,
  or architecture-like material -> `svg`.
- Reader-facing H5, share page, interactive explainer, or report/dashboard
  material -> `h5_html` or `hybrid`.
- Article visual package or multiple section images -> `article_visual_package`
  first, then choose mode.
- Single poster, one-page graphic, teaching card, or long image -> `single_infographic`
  first, then choose mode.
- Visual style, cover image, illustration, or atmosphere-first request ->
  `image_model` or `hybrid`.

If neither preference nor content shape is decisive, ask a bounded fork:

1. `SVG`: precise, editable, text-safe.
2. `H5/HTML`: interactive, scrollable, browser-verifiable.
3. `Image model`: higher visual richness, weaker exact Chinese text control.
4. `Hybrid`: generated visual assets with deterministic text and layout.

## Worker Routing

Route to the smallest bounded worker that owns the next action:

- Reader-facing H5/share/report/Feishu visual output: load
  `.codex/skills/public-report-quality-gate/SKILL.md` first.
- Article or report visual package: use `knowledge-article-visual`.
- Single infographic, one-card summary, poster, or per-image script: use
  `infographic-onepager`.
- Business flow, payment flow, fund flow, state, process, or Mermaid sequence:
  use `svg-flow-diagram`.
- System architecture, deployment, topology, technical integration, or data
  pipeline: use `architecture-diagram`.
- H5/HTML one-page visual board: use `visual-knowledge-onepager` if available;
  otherwise use the repo's frontend/H5 workflow under the public-report gate.
- Direct bitmap execution: use `imagegen` only after source, mode, prompt/script,
  and verification boundary are established.
- Feishu whiteboard work: use `lark-whiteboard`.

## Hard Boundaries

- Do not bypass the public-report quality gate for reader-facing artifacts.
- Do not copy detailed prompts or implementation rules from worker skills into
  this controller.
- Do not treat `imagegen`, browser tools, Feishu tools, or whiteboard tools as
  planning owners; they are executors after route selection.
- Do not claim visual quality without screenshot/readback or equivalent
  verification when a visual artifact is produced.
- Do not insert generated images into Feishu or whiteboards without explicit
  user approval.
- Do not create global skill behavior from a single example; keep this route
  repo-local unless a separate migration is approved.

## Evidence Notes

When explaining a route, cite the source signal: user preference, content shape,
target medium, text-density risk, verification need, or named worker. If the
route is blocked, ask only for the missing source or preference.
