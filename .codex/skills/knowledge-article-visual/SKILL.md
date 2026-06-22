---
name: knowledge-article-visual
description: Use when a Chinese reader-facing knowledge article, visual card series, infographic set, or generated visual asset is requested for a knowledge topic, method, workflow, report, project summary, or article learning.
---

# Knowledge Article Visual Skill

## Core Principle

This skill owns article-level visual series. It must not stop at a restyled
article or H5 block when the requested deliverable is a standalone visual asset,
card set, infographic set, generated image, or chapter-supporting visual.

Visual output mode is user-owned. When the requested visual could be delivered as
H5/HTML, deterministic SVG/HTML, direct image model, or hybrid overlay, ask for
the mode before implementation unless the user has already clearly chosen one.
Do not use dense Chinese, formal review, or editability as a silent reason to
override an explicit image-model request.

Correct order:

1. Clarify or infer the real topic, reader, argument, and output form.
2. Select or confirm the visual output mode.
3. Structure the article into four progressive visual sections.
4. Decide whether each section is a knowledge card or a full one-page infographic.
5. Use `infographic-onepager` for the per-image format, layout, and mode-specific
   prompt/rendering decision.
6. Produce the requested visual artifacts in the chosen mode: image prompts,
   direct image generation, deterministic SVG/HTML images, or hybrid
   visual-background plus text overlay.
7. Inspect for Chinese text accuracy, overlap, style drift, and readability.
8. Iterate or record limitations.

## Intent Routing

| User intent | Required route |
|---|---|
| Chinese article plus visual package | Create article outline, four visual sections, four card/infographic scripts, and one total infographic script. Confirm the visual output mode before generating files. |
| Existing H5/article needs standalone visual assets | Do not only edit H5 text. Ask the output-mode fork if the user has not chosen; then produce standalone visual assets in the chosen mode and optionally embed/link them in H5. |
| A chapter has dense concepts, many claims, or many evidence boundaries | Route that chapter to `infographic-onepager` as a one-page infographic. |
| A chapter is narrow, illustrative, or supports a section heading | Route that chapter to `infographic-onepager` as a horizontal teaching card. |
| User chooses image-model output or explicitly confirms image generation | Use direct image generation or hybrid mode. Dense Chinese is a risk note, not permission to silently fall back to deterministic SVG/HTML. |
| User rejects H5/SVG quality or asks why image generation was not used | Stop the deterministic route. Use direct image generation or hybrid mode unless the user explicitly chooses H5/SVG again. |
| Dense Chinese text, Feishu-facing, formal review, or exact wording required | Present the output-mode fork with the text-accuracy tradeoff. Use deterministic SVG/HTML only when the user chooses exact/editable rendering or an external constraint requires it. |
| Output form is unclear between image model, H5/HTML, SVG/HTML, and hybrid | Ask once with the four-mode fork before implementation; do not silently choose H5 or SVG. |

## Required Inputs

Ask for or infer:

- Topic
- Target audience
- Core argument
- Problem to solve
- Key examples or cases
- Desired tone
- Desired visual style
- Output mode: H5/HTML, deterministic SVG/HTML, direct image model, hybrid overlay, prompts only, or PNG exports

If enough context already exists, state the assumptions and proceed.

## Load

- Visual style: `references/visual_style_guide.md`
- Four-card templates: `references/card_templates.md`
- One-page infographic template: `references/one_page_infographic_template.md`
- Final check: `references/quality_checklist.md`
- For every final visual format decision, also load `infographic-onepager`.

## Output Modes

### Mode 0: Output Mode Fork

Use when the user asks for visuals and the mode has not been chosen.

Ask with four concrete choices:

1. H5/HTML: fastest for interactive or article-like reading, but not image-model
   quality.
2. SVG/HTML deterministic image: best for exact Chinese and editability, but can
   look like a rendered layout.
3. Direct image model: best for visual quality and hand-drawn texture, but Chinese
   text may need correction.
4. Hybrid: image-model background or composition plus deterministic Chinese text;
   default when the user wants image-model aesthetics and reliable Chinese.

If the user already chose image-model output, explicitly confirmed image
generation, or complained that the result is H5/SVG, skip the fork and choose
direct image model or hybrid.

### Mode A: Content + Visual Prompt Mode

Use when the user asks for planning or prompts only.

Output:

1. Topic diagnosis
2. Article title options
3. Four-part article outline
4. Four visual-card or chapter-infographic scripts
5. One high-density total infographic script
6. One prompt per visual
7. Quality checklist

### Mode B: Direct Image Generation Mode

Use when image generation is available and the user asks to run images, chooses
image model, or rejects H5/SVG output quality.

Process:

1. Generate Slide 1 first as the style anchor.
2. Use Slide 1 as the style reference for Slides 2-4 and the total infographic.
3. Keep the same background, title style, card style, color system, doodles,
   spacing, and handwriting style.
4. Inspect the image. If Chinese text is broken, report the issue and switch to
   Mode D unless the user explicitly chooses deterministic-only Mode C.

### Mode C: Deterministic Layout Image Mode

Use when the user chooses deterministic/editable/exact rendering, or when an
external delivery constraint requires exact Chinese text.

Process:

1. Build SVG/HTML with all Chinese text as real text.
2. Export each visual to PNG or SVG.
3. Verify nonblank render, no obvious overflow, readable hierarchy, and consistent
   style.
4. Treat the exported PNG/SVG as the image deliverable, not as a draft H5 section.

### Mode D: Hybrid Image Model + Text Overlay

Use when the user wants image-model aesthetics and the card has dense Chinese,
or when direct image generation produces broken text. Prefer this over silently
falling back to H5/SVG after an image-model request.

Process:

1. Generate a low-text or text-free illustration/background with the image model.
2. Add exact Chinese text using SVG/HTML, Figma, PPT, Canva, or PIL.
3. Export and verify final PNG/SVG.

## Article Structure

The article should usually have four progressive sections:

1. Core experience / misconception
2. Structural model / framework
3. Iteration path / operating change
4. Deeper principle / reusable SOP

Each section must include:

- Section title
- Core claim
- Explanation
- Example or contrast
- Summary sentence
- Visual-card or infographic assignment

## Visual Series Structure

Default series:

1. Card 1: Core experience or misconception
2. Card 2: Structural model
3. Card 3: Iteration path or operating change
4. Card 4: Deeper principle or SOP
5. Total infographic: high-density summary

If a section is too dense for a 16:9 card, promote that section to its own
one-page infographic. Do not squeeze dense text into tiny cards.

## Visual Style Guide

The visual style should resemble a hand-drawn educational sketchnote poster.

Mandatory:

- 16:9 horizontal layout for normal cards
- Vertical 2:3 or 3:4 for total one-page infographics
- Warm cream paper texture
- Hand-drawn marker / colored-pencil feel
- Big black Chinese title
- Orange / blue / green / purple highlights
- Rounded hand-drawn cards
- Doodle arrows, tape, underlines, spark marks
- Bottom takeaway banner
- Clear whitespace and safe margins

Avoid:

- Corporate PPT style
- Flat SaaS dashboard style
- Dense spreadsheet-like layout
- Tiny Chinese text
- Overlapping text and icons
- Inconsistent card shapes
- Treating a visual prompt as proof of final image quality

## Layout Rules

For normal cards:

- Main title: 1 line
- Subtitle: 1 line
- 2-4 panels or lanes
- Each panel: 1 icon plus 1-2 short bullets
- Bottom takeaway: 1 sentence

For high-density one-page infographics:

- Up to 5 main modules
- Each module no more than 4 bullets
- Up to 2 support modules
- One clear bottom golden sentence

## Standard Four-Card Template

### Card 1: Core Experience

Purpose: Explain the key misconception and correct path.

Layout:

- Top title
- Subtitle
- Old vs new comparison banner
- 3-4 step cards across the middle
- Bottom takeaway

### Card 2: Structural Model

Purpose: Explain a framework or architecture.

Layout:

- Three large cards or two poles plus a bridge
- Arrows between objects
- Boundary / warning note
- Bottom takeaway

### Card 3: Iteration Path

Purpose: Explain how the system or behavior changes over time.

Layout:

- Decision banner
- Old state vs new state
- Version or maturity steps
- Measurement / observation block
- Bottom takeaway

### Card 4: Deeper Principle

Purpose: Explain the reusable operating principle.

Layout:

- Center principle ribbon
- Two scenarios or one loop
- One warning block
- One concrete next action
- Bottom takeaway

## Prompt Handoff

When generating prompts, use `infographic-onepager` prompt patterns:

- Vertical one-page poster for the total infographic or dense chapter.
- Horizontal teaching card for chapter-supporting visuals.

When the user explicitly asks to run images, do not stop at prompts. When direct
image generation is unavailable or text accuracy becomes risky, report the
constraint and ask or confirm before changing modes.

## Quality Checklist

- Core argument is clear.
- Four sections are progressive.
- Each visual has one main claim.
- Examples are concrete.
- Chinese text is readable.
- Cards use one consistent style system.
- Icons support meaning and do not cover text.
- Bottom takeaway exists.
- If image generation distorts Chinese, report the issue and prefer hybrid mode
  unless the user explicitly chose deterministic-only output.

## Final Response Format

Return:

1. What visual artifacts were generated
2. File paths or prompts
3. Verification performed
4. Known limitations, especially Chinese text quality or image-model text risk
