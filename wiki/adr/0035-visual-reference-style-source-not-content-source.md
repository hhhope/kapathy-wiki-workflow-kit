---
layer: adr
domain: none
canonical_object: visual-reference-source-boundary
artifact_type: adr
---

# ADR-0035 Visual Reference Source Is Style Source, Not Content Source

## Status

Accepted

## Context

During visual production for the AI visual expression Feishu article, the user
asked for three hand-drawn knowledge-card images based on the article content
and referenced prior hand-drawn outputs as style history.

The agent drifted twice:

1. It first chose a deterministic HTML/SVG screenshot route without asking or
   preserving the requested visual-output mode.
2. It then over-corrected by treating historical Account Wiki images as a
   production anchor. The historical images were only style and layout
   references, but the agent allowed the task framing to drift toward the
   reference artifact's source object.

The user rejected a proposed fix that would add explicit prompt bans such as
`No Account Wiki`, `no wiki pages`, `no Obsidian`, or `no source entries`.
That style of fix is brittle: it names the accidental contaminant rather than
fixing the underlying source-role confusion.

## Decision

For visual production with reference images, distinguish source roles before
prompting or generation:

- **Content source**: the current article, Feishu draft, markdown, oral brief,
  or user-provided material that owns the message.
- **Style source**: prior images or references that only provide layout,
  composition, palette, texture, density, and visual grammar.
- **Executor**: image model, hybrid overlay, SVG/H5 renderer, whiteboard, or
  other production tool.

Reference images used as style sources must not become semantic content
sources.

The correction should not be an over-specific negative prompt that lists the
previous artifact's nouns. Instead, the visual brief must explicitly map:

1. what each output image communicates,
2. which current content section it comes from,
3. which style reference only supplies visual grammar,
4. which route is selected (`image_model`, `hybrid`, deterministic SVG/H5, or
   another route),
5. what must be verified after generation.

If the user asks for historical style, name the style features, not the old
artifact's topic, as the reference:

- vertical dense one-page poster
- horizontal workflow teaching card
- horizontal 2x2 method / validation card
- warm cream paper
- thick black marker border
- colored number badges
- doodle icons and arrows
- bottom takeaway banner

Do not present generated output as complete until the output format and intent
route have been explicitly respected and the result has been visually checked.

## Consequences

- Visual briefs must separate content source, style source, and executor before
  image generation.
- `visual-agent` should later be updated to enforce this source-role boundary
  for reference-image-driven requests.
- Historical artifacts can still be used, but only for visual grammar unless
  the user explicitly asks to reuse their content.
- Prompt fixes should avoid brittle lists of forbidden legacy nouns unless the
  generated image actually contains those unwanted nouns and a targeted repair
  pass is needed.
- For the current task, image regeneration should use the Feishu article
  sections as content source and the three historical hand-drawn images only as
  layout/style references.
