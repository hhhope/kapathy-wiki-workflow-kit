# HTML One-Pager Template

Use this reference when the user asks to turn an article, Feishu document,
report, governance idea, learning note, or abstract framework into a visual
one-flow HTML page.

Before drafting, select the HTML visual mode from [html-visual-modes.md](html-visual-modes.md):

- `retro-grid`: structured grid/cards, metrics, matrices, comparison blocks
- `handdrawn-teaching`: hand-drawn teaching poster, concrete visual actions, more diagrams than text

## Output target

Produce one self-contained HTML file:

- inline CSS only
- no build step
- no framework dependency
- easy to open locally and screenshot vertically

## Structural default

For `retro-grid`, use this section order unless the source material strongly suggests another grouping:

1. Hero
2. Core metrics grid
3. Scale / capability section
4. Cost / usage section
5. Risk / warning section
6. Final conclusion footer

## Visual rules

Shared rules:

- Beige base background
- Pink / blue / yellow / mint section blocks
- Thick black borders and drop-shadow-like offset blocks
- At least one black-background warning section with white text
- Screenshot-friendly vertical rhythm

For `retro-grid`:

- Strong grid rhythm
- Large numeric anchors
- Minimal decorative motifs: stickers, checkerboards, arrows, stars

For `handdrawn-teaching`:

- Each section has a concrete visual object or action
- Use flows, loops, comparison scenes, connected cards, clipboards, targets, tools, robots, documents, speech bubbles, and warning notes
- Text supports the drawing; it must not become a restyled article dump

## Content rules

- Extract 5-8 strongest message blocks from the source
- Prioritize numbers, dates, totals, rankings, thresholds, or concrete examples
- Compress paragraphs into punchy infographic lines
- Use short headings and dense bullet groups
- Keep one big conclusion sentence near the top
- Keep one management or action-oriented conclusion near the end

## Layout recommendations

- Use a centered page wrapper with a max width around 1100-1300px
- Use CSS grid for sections
- Prefer 3-column or 4-column metric blocks
- Mix large quote cells with denser list cells
- Make the first screen visually decisive

## Avoid

- Generic dashboard UI look
- Thin neutral cards without personality
- Long article-style paragraphs
- External assets unless the user explicitly requests them
- Multi-file split unless requested

## Suggested naming

If the user gives no file name, prefer:

- `{topic_slug}_visual_onepager.html`
- `{topic_slug}_retro_pop_flow.html`
- `{topic_slug}_xiaohongshu_flow.html`

## Minimum QA

Before finalizing:

- verify the page has one clear thesis in the hero
- verify at least 3 numeric anchor blocks are visible
- verify at least one black-background warning block exists
- verify the HTML is standalone and readable on desktop
- verify the page still looks intentional when screenshotted as a long image
