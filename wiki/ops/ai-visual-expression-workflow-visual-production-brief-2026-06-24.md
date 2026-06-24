---
layer: ops
domain: ai-workflow
ops_area: report-quality
canonical_object: ai-visual-expression-workflow
artifact_type: visual-production-brief
title: AI visual expression workflow visual production brief 2026-06-24
status: active
created_at: 2026-06-24
updated_at: 2026-06-24
derived_from:
  - wiki/reports/ai-visual-expression-workflow-guide.md
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/assets/account-wiki-runtime-card.png
  - wiki/reports/assets/account-wiki-validation-card.png
---

# AI 作图表达工作流 visual production brief

## Route

Use image-model / hybrid visual production, not HTML screenshot production.

Historical reference:

- `account-wiki-onepager.png`: vertical dense one-page hand-drawn overview.
- `account-wiki-runtime-card.png`: horizontal flow teaching card.
- `account-wiki-validation-card.png`: horizontal 2x2 method / validation card.

Shared visual grammar:

- warm cream paper
- thick black marker border
- large handwritten Chinese title
- colored number badges
- hand-drawn objects, arrows, underlines, stars, and warning notes
- yellow / orange bottom takeaway banner
- short readable Chinese labels, no paragraph blocks

Boundary:

- Do not use HTML/H5 screenshots as final visual output.
- Do not force the three cards into one identical layout.
- If generated Chinese is inaccurate, treat the result as image-model draft and
  repair through hybrid deterministic text overlay in a follow-up.

## Asset 01: 总览一图流

Reference style: `account-wiki-onepager.png`.

Format: vertical 2:3 or 3:4 hand-drawn one-page infographic.

Title: `AI 作图先拆再画`

Subtitle: `参考图给版式，内容给字段，visual-agent 选路径，图片模型最后出图`

Sections:

1. `01 正确路径`: show the five-step chain:
   `参考图 -> 反推版式 Prompt -> 拆内容字段 -> 合成最终 Prompt -> 确认后出图`.
2. `02 Prompt 方法`: say `把需求说清楚`, with labels:
   `版式来源`, `业务文字`, `禁止元素`, `确认字段`.
3. `03 visual-agent`: say `把作图类型和路径选对`, with labels:
   `流程结构图`, `海报封面`, `知识卡长图`, `H5/HTML`, `Hybrid`.
4. `04 图片模型`: say `负责最后画出来`, with labels:
   `豆包`, `Codex 图像模型`, `手绘质感`, `二次修正`.
5. `05 验收清单`: show check marks:
   `文字完整`, `中文清晰`, `版式保留`, `禁用元素清干净`.
6. `06 核心结论`: `先理解图，再组织内容，最后生成图片`.

Bottom banner:

`不要让 AI 猜图；先拆版式，再填内容，再生成。`

Prompt:

```text
Create a vertical 2:3 Chinese hand-drawn infographic poster on warm cream paper,
in a classroom sketchnote style. Use thick black marker outlines, a large
handwritten Chinese title banner, colored section labels 01-06, doodle icons,
arrows, underlines, tape, stars, and a yellow bottom takeaway banner. The layout
should resemble a dense one-page hand-drawn teaching poster, not a webpage.

Main title: AI 作图先拆再画
Subtitle: 参考图给版式，内容给字段，visual-agent 选路径，图片模型最后出图

Section 01 title: 正确路径
Show a five-step chain with icons:
参考图 -> 反推版式 Prompt -> 拆内容字段 -> 合成最终 Prompt -> 确认后出图

Section 02 title: Prompt 方法
Text: 把需求说清楚
Short labels: 版式来源, 业务文字, 禁止元素, 确认字段

Section 03 title: visual-agent
Text: 把作图类型和路径选对
Short labels: 流程结构图, 海报封面, 知识卡长图, H5/HTML, Hybrid

Section 04 title: 图片模型
Text: 负责最后画出来
Short labels: 豆包, Codex 图像模型, 手绘质感, 二次修正

Section 05 title: 验收清单
Show check marks:
文字完整, 中文清晰, 版式保留, 禁用元素清干净

Section 06 title: 核心结论
Text: 先理解图，再组织内容，最后生成图片

Bottom banner: 不要让 AI 猜图；先拆版式，再填内容，再生成。

Use readable Chinese, short labels only, no English except Prompt, visual-agent,
H5/HTML, Hybrid, Codex. No generic tech background. No HTML screenshot style.
```

## Asset 02: 正确路径知识卡

Reference style: `account-wiki-runtime-card.png`.

Format: 16:9 horizontal hand-drawn teaching card.

Title: `正确路径怎么跑`

Subtitle: `不是直接出图，而是先拆版式、再填内容、再确认生成`

Four visual panels:

1. `01 参考图`: image card + magnifier, labels `比例`, `分区`, `卡片`, `图标`.
2. `02 版式 Prompt`: paper scroll / signpost, labels `结构`, `风格`, `模块位置`.
3. `03 内容字段`: drawer / table, labels `标题`, `模块`, `底部信息`, `禁止项`.
4. `04 确认后出图`: stamp + picture output, labels `先审 Prompt`, `再生成`, `再验收`.

Bottom sentence:

`不是让模型直接画，而是先把“图怎么表达”说清楚。`

Prompt:

```text
Create a 16:9 Chinese hand-drawn teaching card on warm cream paper with a thick
black marker border. Use four large rounded panels connected left to right by
hand-drawn arrows, colored number badges 01-04, doodle icons, marker
underlines, and a blue/yellow bottom sentence strip. The style should match a
hand-drawn workflow teaching card.

Main title: 正确路径怎么跑
Subtitle: 不是直接出图，而是先拆版式、再填内容、再确认生成

Panel 01 title: 参考图
Icon: small image card with magnifier
Bullet labels: 比例, 分区, 卡片, 图标

Panel 02 title: 版式 Prompt
Icon: paper scroll or road sign
Bullet labels: 结构, 风格, 模块位置

Panel 03 title: 内容字段
Icon: drawer or table with labeled cards
Bullet labels: 标题, 模块, 底部信息, 禁止项

Panel 04 title: 确认后出图
Icon: approval stamp plus generated picture
Bullet labels: 先审 Prompt, 再生成, 再验收

Bottom sentence: 不是让模型直接画，而是先把“图怎么表达”说清楚。

Keep all Chinese large and readable. No dense paragraphs. No HTML screenshot
look. Do not make it a tech dashboard.
```

## Asset 03: 推荐方法知识卡

Reference style: `account-wiki-validation-card.png`.

Format: 16:9 horizontal 2x2 hand-drawn method card.

Title: `作图方法怎么选`

Subtitle: `Prompt 说清楚，visual-agent 选对路，图片模型画出来`

Four modules:

1. `01 Prompt 方法`: icon `sticky notes`, bullets:
   `版式来源`, `业务文字`, `确认字段`.
2. `02 visual-agent`: icon `branch road sign`, bullets:
   `流程结构`, `海报封面`, `知识卡长图`, `H5/HTML`, `Hybrid`.
3. `03 图片模型`: icon `brush + sparkle image`, bullets:
   `豆包`, `Codex 图像模型`, `手绘质感`.
4. `04 验收清单`: icon `clipboard + magnifier`, bullets:
   `文字完整`, `中文清晰`, `禁用元素清干净`.

Bottom sentence:

`Prompt 解决说清楚，visual-agent 解决选对路，图片模型解决画出来。`

Prompt:

```text
Create a 16:9 Chinese hand-drawn method card on warm cream paper, thick black
marker border, large handwritten title, red/blue/green/orange colored module
frames, 2x2 layout, big number badges 01-04, one doodle icon per module, and a
yellow bottom takeaway banner. Match a hand-drawn validation/method card style.

Main title: 作图方法怎么选
Subtitle: Prompt 说清楚，visual-agent 选对路，图片模型画出来

Module 01 title: Prompt 方法
Icon: sticky notes and pencil
Bullets: 版式来源, 业务文字, 确认字段

Module 02 title: visual-agent
Icon: branching road sign
Bullets: 流程结构, 海报封面, 知识卡长图, H5/HTML, Hybrid

Module 03 title: 图片模型
Icon: brush plus glowing image
Bullets: 豆包, Codex 图像模型, 手绘质感

Module 04 title: 验收清单
Icon: clipboard plus magnifier
Bullets: 文字完整, 中文清晰, 禁用元素清干净

Bottom banner: Prompt 解决说清楚，visual-agent 解决选对路，图片模型解决画出来。

Use readable Chinese, short labels, no extra claims, no generic tech poster
style, no HTML screenshot look.
```
