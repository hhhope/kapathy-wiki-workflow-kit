# Design: visual-agent routing

## Entry Model

`visual-agent` is a controller skill, modeled after the existing `cr-agent` and
`wiki-medical-agent` pattern:

- it is a normal user-facing entry point;
- it classifies intent and state before work starts;
- it routes to bounded worker skills;
- it reports allowed and blocked actions explicitly;
- it does not own worker-specific rendering prompts or implementation details.

## Mode Decision

The controller exposes four production modes:

- `svg`: deterministic, editable, precise diagrams and text-safe Chinese labels.
- `h5_html`: interactive or scrollable report pages, explainers, and dashboards.
- `image_model`: visual richness, illustration, or bitmap-first output where
  exact text layout is less important.
- `hybrid`: image-model visual assets plus deterministic text/layout overlay.

The route can be chosen by explicit user preference or by content shape. If
both are absent or conflict, the controller must present a mode fork instead of
silently choosing.

## Worker Routing

`visual-agent` routes rather than renders:

- Reader-facing report/H5/share outputs first preserve
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Article/report visual packages route to `knowledge-article-visual`.
- Single-card or one-page infographic requests route to `infographic-onepager`.
- Fund-flow, business-flow, sequence, state, and Mermaid-like diagrams route to
  `svg-flow-diagram`.
- System, deployment, integration, and technical topology diagrams route to
  `architecture-diagram`.
- H5 one-page visual boards can route to `visual-knowledge-onepager` when that
  external skill is available.
- Direct bitmap generation routes to `imagegen` only after the controller has
  established mode, source, and prompt/script boundaries.
- Whiteboard-specific edits route to `lark-whiteboard` when the user asks for
  Feishu whiteboard work.

## Response Shape

Normal responses include:

- `Intent`
- `Visual Case`
- `Content Shape`
- `Output Mode`
- `State`
- `Allowed Action`
- `Blocked Action`
- `Next Action`
- `Evidence`

The fields mirror the CR and medical controller designs while using visual
domain terms.

## Boundaries

The controller must not:

- bypass public report quality gates for reader-facing output;
- treat `imagegen`, browser, Feishu, or whiteboard tools as planning owners;
- claim visual quality without screenshot/readback or equivalent verification;
- replace specialized SVG, H5, one-page infographic, or architecture workers;
- promote article examples or one-off conversation preferences into global
  rules without OpenSpec and behavior evidence.
