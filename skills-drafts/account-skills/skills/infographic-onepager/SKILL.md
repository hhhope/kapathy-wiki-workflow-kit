---
name: infographic-onepager
description: Use when a Chinese infographic, horizontal teaching card, vertical one-page poster, SVG/HTML visual layout, image-generation prompt, or chapter-supporting visual is requested for a topic, article, workflow, project summary, capability map, or reference visual.
---

# Infographic Onepager

Create a Chinese visual explanation that matches the content density: either a
high-density one-page infographic or a focused horizontal teaching card.

## Core Rule

Do not start with image generation. First compress the content into a poster
script. Compression is not permission to choose the output mode for the user.

Visual output mode is user-owned. When the requested visual could be delivered as
H5/HTML, deterministic SVG/HTML, direct image model, or hybrid overlay, ask for
the mode before implementation unless the user has already clearly chosen one.

Then choose:

- image-generation prompt for quick visual drafts
- direct image generation when requested, chosen, or when the user rejects H5/SVG
  output quality
- SVG/HTML exported to PNG/SVG when the user chooses exact/editable deterministic
  rendering or an external delivery constraint requires it
- hybrid image-background plus deterministic text overlay when the user wants
  image-model aesthetics and accurate Chinese

Never switch from requested images to H5/HTML without saying that HTML is being
used as a deterministic image renderer and exporting an actual image asset.
Dense Chinese is a risk note, not a silent override of an explicit image-model
request.

## Default Style

For dense one-page posters, default to `reference-10`:

- vertical 2:3 or 3:4 poster
- white or warm paper background
- thick black marker outlines
- playful handwritten Chinese title banner
- colored numbered section labels
- six stacked sections
- doodle icons and simple arrows
- pastel blue / orange / green / purple / pink accents
- large readable Chinese text

For chapter visuals, default to horizontal teaching-card style:

- 16:9 landscape layout
- white or warm paper background
- thick black marker outlines
- large handwritten Chinese title and short subtitle
- 2-4 numbered panels, lanes, comparison blocks, or step chains
- one icon per panel, arrows only where they explain flow
- bottom takeaway sentence

## Format Decision

Choose the content format and output mode before writing the prompt or
SVG/HTML:

| Signal | Use |
|---|---|
| Big topic, full framework, dense article, complete workflow | Vertical one-page infographic |
| Chapter illustration, section header visual, or supporting visual for a narrow section | Horizontal teaching card |
| Chapter has many claims, evidence boundaries, or role/action mapping | Vertical chapter one-page infographic |
| User wants a lightweight supporting visual instead of a dense full-summary poster | Horizontal teaching card |
| Multi-page article set | Separate page-specific visuals; do not collapse everything into one poster |
| Feishu-facing, formal, exact Chinese text, or editable result | Treat as a text-accuracy constraint. Ask the output-mode fork unless the user already chose deterministic SVG/HTML. |
| User chooses image-model output or explicitly confirms image generation | Prompt/direct image generation or hybrid. Dense Chinese is a risk note, not permission to silently switch to deterministic layout. |
| User rejects H5/SVG quality or asks why image generation was not used | Stop the deterministic route. Use direct image generation or hybrid unless the user explicitly chooses H5/SVG again. |
| Choice between image model, H5/HTML, SVG/HTML, and hybrid is unclear | Ask before generating or editing files with the four-mode fork. |

## Output Mode Fork

Ask with four concrete choices when the mode is not already clear:

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

## Integration With knowledge-article-visual

When called from `knowledge-article-visual`:

1. Treat the total summary as a vertical one-page infographic.
2. Treat each article section as either:
   - a horizontal teaching card if it has one clear claim and 2-4 panels, or
   - a vertical chapter one-pager if it has dense claims, evidence boundaries,
     metrics, or role/action mapping.
3. Return a script and prompt or an exported visual asset path for every visual.
4. Do not use topic-specific templates unless the source material provides that
   topic.

## Generic Six-Section Poster Skeleton

Use this structure unless the source requires another sequence:

1. `01 基础概念`
   - Define the topic in one sentence.
   - Show input -> system -> output with simple icons.

2. `02 为什么重要`
   - Contrast the old way and the better way.
   - Use a small VS comparison.

3. `03 本质`
   - Explain the deeper operating principle.
   - Use one anchor metaphor or model.

4. `04 核心结构`
   - Show the 3-6 essential building blocks.
   - Use boxed modules, not paragraphs.

5. `05 运行方法`
   - Show how to operate, improve, or iterate it.
   - Use a loop, checklist, responsibility map, or step chain.

6. `06 边界结论`
   - Summarize capability and boundary.
   - End with one large golden sentence.

## Generic Fill Template

```text
Title:
[一张图读懂 X / X 的作业系统 / X 方法论]

Subtitle:
[用一句话说清读者为什么要看]

01 基础概念
[X 是什么？]
- [定义]
- [输入 / 中间层 / 输出]
- [它不是什么]

02 为什么重要
[为什么现在重要？]
- [旧方式的问题]
- [新方式的变化]
- [读者会损失或获得什么]

03 本质模型
[X 的本质是什么？]
- [模块 1]
- [模块 2]
- [模块 3]

04 运行方法
[X 如何跑起来？]
- [步骤 1]
- [步骤 2]
- [步骤 3]

05 已有信号 / 观察指标
[怎么判断它有效？]
- [指标或案例 1]
- [指标或案例 2]
- [指标或案例 3]

06 边界结论
[不要过度承诺什么？]
- [边界 1]
- [边界 2]
- [下一步]

Bottom:
[一句大号金句]
```

## Topic-Specific Examples

Do not hardcode any topic example as the default. If a domain example is useful,
derive it from the user's source material and label it as an example. Account Wiki
is just one possible topic, not the default template.

## Copy Compression Rules

- Main title: no more than 18 Chinese characters when possible.
- Section heading: one short question or phrase.
- Bullet: one idea per line.
- Avoid long paragraphs inside cards.
- If exact text is too long, compress before prompt generation.
- Preserve boundaries and evidence claims.
- Do not make future capabilities sound completed.

## Image Prompt Pattern

Use this for direct image generation:

```text
Create a vertical 2:3 Chinese hand-drawn infographic poster, inspired by a
sketchnote educational poster style: white paper background, thick black marker
outlines, playful handwritten title banner, colored numbered section tags,
doodle icons, rounded content boxes, readable Chinese text, pastel blue/orange/
green/purple/pink accents.

Topic: [topic]

Main title banner:
[title]
Subtitle:
[subtitle]

Use six horizontal stacked sections, each section with a colored number label on
the left and simple illustrations.

Section 01 label: [label]
Heading: [heading]
Visual: [visual idea]
Bullets:
- [short bullet]
- [short bullet]
- [short bullet]

[repeat sections 02-06]

Bottom golden sentence:
[one sentence]

Design requirements:
- Match a hand-drawn classroom sketchnote poster style.
- Thick black borders, large readable Chinese typography, doodle icons, pastel
  section labels, and school-note feeling.
- Keep Chinese text crisp and legible.
- No tiny text, no overlap, no distorted characters.
- Do not include QR code, watermark, real person portrait, or unrelated logos.
```

## Horizontal Teaching-Card Prompt Pattern

Use this for chapter-supporting visuals:

```text
Create a 16:9 Chinese hand-drawn teaching card, warm white paper background,
thick black marker outlines, large handwritten title, short subtitle, colored
number circles, doodle icons, pastel blue/orange/green/purple accents, crisp
readable Chinese text.

Topic: [topic]
Title:
[short title]
Subtitle:
[short subtitle]

Layout:
- [2-4 panels / two lanes / comparison blocks / step chain]
- Each panel has one icon and 1-2 short bullets.
- Use arrows only where they explain flow.

Panels:
1. [panel title] — [icon idea] — [short bullets]
2. [panel title] — [icon idea] — [short bullets]
3. [panel title] — [icon idea] — [short bullets]
4. [optional panel title] — [icon idea] — [short bullets]

Bottom takeaway:
[one sentence]

Requirements:
- Keep it landscape, not a vertical poster.
- Do not force six sections.
- Do not copy the reference subject matter; reuse only layout language,
  density, hierarchy, and hand-drawn style.
- No tiny text, overlap, QR code, watermark, portrait, or unrelated logos.
```

## SVG / HTML Pattern

Use SVG/HTML when the user chooses deterministic rendering, explicitly confirms
deterministic handling for dense exact Chinese, or needs editable output:

- one full-height poster container or one 16:9 card container
- fixed title, section, and bottom sentence zones
- explicit typography sizes
- no background images behind text
- exportable with Playwright screenshot

Minimum verification:

- expected section count is present
- title and bottom sentence are present
- screenshot is non-empty
- obvious text overflow is absent

## Anti-Patterns

- Starting from a generic product one-pager layout when the reference style is a
  hand-drawn learning poster.
- Making a dark hero section by default.
- Turning a requested image into H5 without exporting an image.
- Treating a PNG exported from HTML/SVG as image-model output.
- Turning a requested chapter card into a full vertical onepager.
- Inflating a low-information visual into six sections just because the skill
  name says onepager.
- Switching from requested image generation to H5/HTML because Chinese text is
  dense without asking or confirming the mode change.
- Copying long article paragraphs directly into the poster.
- Treating image generation as final proof when Chinese text is dense.
- Hardcoding Account Wiki or any other domain as the default template.
- Adding QR code, watermark, portrait, or brand marks unless requested.
- Letting icons overlap Chinese text.

## Final Response

Return:

1. what was generated or changed
2. the poster script, prompt, or output file path
3. verification performed
4. known limitations, especially text accuracy if pure image generation was used
