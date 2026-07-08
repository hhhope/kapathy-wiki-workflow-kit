---
name: visual-knowledge-onepager
description: Use when the user wants to turn a concept, article, report, governance idea, learning note, or abstract framework into a dense visual one-pager, H5, long infographic, Xiaohongshu-style carousel, retro-grid knowledge card, or screenshot-friendly single-file HTML.
---

# Visual Knowledge One-Pager

Turn dense knowledge into a visual artifact: a one-page H5, long infographic,
retro-grid knowledge card, hand-drawn teaching poster, or Xiaohongshu-style
carousel. Xiaohongshu is one visual mode, not the skill identity.

## Must-Do Rules

- For carousel outputs, ask for 3 inputs first: topic, 1-2 sentence description, image count.
- For carousel outputs, do not start drafting before the user provides all 3 inputs.
- If the user asks for H5, HTML, 一图流, visual explanation, or a one-pager and already provides a source, topic, metaphor, or target idea, use the HTML one-pager branch instead of forcing carousel intake.
- Must keep each image aligned to exactly 1 core theme.
- Must design each image with 6-7 grid modules, not 4-5.
- Must keep every module specific: include numbers, brands, parameters, tiers, scenarios, or pitfalls.
- Must include 1 black-background warning module with white text in every image.
- Must ask for user confirmation before generating final image prompts or images.
- For HTML one-pagers, must output a single self-contained HTML file unless the user asks for a multi-file webpage.
- For HTML one-pagers, must choose or ask the user to choose one visual mode: `retro-grid` or `handdrawn-teaching`.
- If live platform trends materially matter and browsing is available, search first; if not, say the trend extraction is inferred rather than verified.

## Intent Routing

| User intent | Output path |
| --- | --- |
| Concept / governance idea / abstract framework -> H5 or 一图流 | Use the HTML one-pager branch |
| 小红书多图内容 / 干货拆图 | Follow the carousel workflow |
| Image-generation handoff or prompt request | Generate one image prompt per image after confirmation |
| 根据文章/飞书文档做一图流 HTML | Skip image-count splitting, choose an HTML visual mode, and produce one single-file HTML infographic |

## Workflow

### Step 1: Intake

Default branch: multi-image Xiaohongshu carousel.

Always begin by asking for exactly these 3 items:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 请提供以下信息，我将为你生成爆款干货内容：

1️⃣ 主题：你想要制作的干货主题是什么？
2️⃣ 简短描述：用1-2句话描述核心要点或目标受众
3️⃣ 图片数量：希望生成多少张图片？（3-10张）

⚠️ 图片数量 = 核心主题数量
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Do not compress or paraphrase this intake unless the user explicitly asks for a shorter version.

If the user instead gives a concrete source artifact such as:

- an article
- a Feishu doc summary
- a local HTML/article file
- “根据这个文章做一图流 HTML”

then switch to the HTML one-pager branch below.

### Step 1B: HTML one-pager branch

Choose this branch when the user explicitly wants:

- 一图流
- HTML 长图
- H5 视觉解释页
- 概念解释图
- 治理目标可视化
- 根据文章/文档做 HTML
- 单页信息图网页

For this branch:

- infer the topic from the source material
- infer the audience from the request if possible
- do not force the 3-question intake if the source and target form are already clear
- ask the user to choose `retro-grid` or `handdrawn-teaching` when neither the prompt nor reference material implies a mode
- infer `handdrawn-teaching` when the user provides a hand-drawn reference, says the output is too text-heavy, or asks for more diagrams and concrete visual objects
- infer `handdrawn-teaching` for abstract concepts, governance models, metaphors, operating principles, and mental models unless the user asks for a dense grid
- infer `retro-grid` when the user asks for Swiss grid, modular cards, data blocks, comparison matrices, or management-report style density
- extract the strongest 5-8 data-backed message blocks from the source
- produce a single-file HTML with embedded CSS
- keep the layout screenshot-friendly and vertically scannable
- use the selected visual mode rather than a generic dashboard

### Step 2: Research and extraction

If browsing is available and helpful, search for recent Xiaohongshu high-engagement examples, headline patterns, pain points, and list structures related to the topic.

Collect these signals:

- Common framing angles
- Repeated pain points or decision mistakes
- Useful numbers, specs, thresholds, price bands, or brand examples
- Comparison dimensions that can become grid modules

If browsing is not available, proceed with best-effort domain synthesis and explicitly state that no live Xiaohongshu verification was done.

### Step 3: Value distillation

Distill the topic into high-value dry content using three filters:

- Practical: directly helps the reader choose, compare, avoid mistakes, or decide faster
- Scarce: includes concrete numbers, standards, models, brands, or thresholds
- Pain-point driven: answers what people most often get wrong, overspend on, or misunderstand

### Step 4: Split into image themes

Map the requested image count to the same number of core themes.

For each image, build 6-7 grid modules. Use this default split:

- Grid 1: options / brands / categories
- Grid 2: numeric standards / thresholds / tiers
- Grid 3: scenario comparison
- Grid 4: identification methods / selection techniques
- Grid 5: recommendation or fit matrix
- Grid 6: warning / pitfall block with black background
- Grid 7: optional quick-check or summary block

Use 4-character Chinese labels when possible for each grid title.

### Step 5: Draft the content

For each image, output:

- Core theme
- Main title
- Subtitle
- Grid-by-grid content assignment
- Data points or parameters inside each module
- Suggested illustration objects for the final image prompt

When drafting, load [references/content-template.md](references/content-template.md).

### Step 5B: Draft the HTML one-pager

For the HTML branch:

- convert the source article into one vertically scrolling infographic page
- organize the page into a hero plus 3-6 grid sections
- keep the same high-contrast Xiaohongshu palette: beige base, pink/blue/yellow/mint blocks, thick black borders
- include at least one black-background warning section
- favor numbers, summary tables, short bullets, and large conclusion cells
- if using `handdrawn-teaching`, make every section contain a concrete visual action or object, not only abstract boxes
- keep it as one self-contained HTML file with inline CSS

When drafting the HTML structure, load [references/html-onepager-template.md](references/html-onepager-template.md).
When selecting the HTML visual mode, load [references/html-visual-modes.md](references/html-visual-modes.md).

### Step 6: Confirm before image generation

After the written content is ready, stop and ask the user to confirm with an
explicit image-generation handoff. Do not treat draft approval as permission to
generate final images unless the user confirms that handoff.

Only after confirmation should you generate image prompts or images.

When generating image prompts, load [references/image-prompt-template.md](references/image-prompt-template.md).

For the HTML branch, do not stop for image confirmation unless the user asked for both content draft and HTML separately. If the user explicitly requested HTML output, generate the HTML directly.

## Output Shape

Default output order:

1. Topic summary and audience assumption
2. Image-by-image outline
3. Full written content for each image
4. A short confirmation message asking whether to proceed to image generation
5. After confirmation, one image prompt per image

For the HTML branch:

1. Brief summary of what was extracted from the source article
2. One self-contained HTML file
3. Short note on where the strongest data blocks were placed

## Quality Bar

Before finalizing written content, check:

- Every image has 6-7 modules
- Every module is anchored to a unique grid cell
- At least one warning cell uses black background / white text in the prompt spec
- No image feels sparse or generic
- Numeric support is present wherever possible
- The visual language is retro pop art plus Swiss-grid order, not generic pastel infographic style

Before finalizing HTML output, also check:

- the file is fully self-contained
- the page can be screenshotted as one long visual
- the top section communicates the thesis in one screen
- sections alternate color blocks with clear black outlines
- the page is not just a restyled article dump; it must read like an infographic
- the selected visual mode is visible in structure, not only in colors or copy

## Failure Modes

- If the topic is too broad, narrow it into decision-oriented subthemes instead of producing vague advice.
- If the user asks for fewer than 3 or more than 10 images, ask them to choose a number inside the range.
- If the topic lacks hard numbers, use structured comparison and scenario logic, and clearly label heuristic recommendations as heuristic.
- If the user wants direct image prompts immediately, still collect the 3 intake inputs first unless they are already present in the conversation.
- If the user wants HTML based on an article, do not route them into the multi-image confirmation flow by default.
