---
layer: reports
domain: ai-workflow
---

# 02 正确路径知识卡：正确路径怎么跑

## 客户端生成设置

- 输出方式：图片模型生成，不要用 SVG、H5、HTML 截图或网页渲染。
- 建议比例：横版 16:9。
- 参考图片路径：`wiki/reports/assets/account-wiki-runtime-card.png`
- 参考图片角色：只提供横向流程卡、手绘箭头、编号面板、底部提示条等视觉语法；不要复用旧图的主题、名词或业务内容。
- 内容来源：`wiki/reports/ai-visual-expression-workflow-guide.md` 和 `wiki/adr/0035-visual-reference-style-source-not-content-source.md`

## 生成 Prompt

```text
Create a 16:9 Chinese hand-drawn workflow teaching card on warm cream paper.
Use image-model output only. Do not create SVG, HTML, H5, browser screenshot,
wireframe, dashboard, or web page output.

Use the attached reference image only for visual style and layout grammar:
horizontal hand-drawn process card, thick black marker border, four large panels
connected left to right by hand-drawn arrows, colored number badges, doodle
icons, marker underlines, and a blue / yellow bottom sentence strip.

Do not reuse the reference image's old topic, old nouns, or old business
content. The content of this new image is only the image-generation workflow
below.

Main title: 正确路径怎么跑
Subtitle: 不是直接出图，而是先拆版式、再填内容、再确认生成

Panel 01 title: 参考图
Icon: small picture card with magnifier
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

Bottom sentence:
不是让模型直接画，而是先把“图怎么表达”说清楚。

Keep all Chinese text large and readable. Avoid dense paragraphs. No unrelated
product, account, payment, wiki, or knowledge-base content.
```

## 出图后检查

- 标题必须是 `正确路径怎么跑`。
- 必须是 4 个横向流程面板，不要变成海报或仪表盘。
- 中文如果大面积错误，直接重生成；不要改成 SVG/H5。
