---
layer: reports
domain: ai-workflow
---

# 03 推荐方法知识卡：作图方法怎么选

## 客户端生成设置

- 输出方式：图片模型生成，不要用 SVG、H5、HTML 截图或网页渲染。
- 建议比例：横版 16:9。
- 参考图片路径：`wiki/reports/assets/account-wiki-validation-card.png`
- 参考图片角色：只提供 2x2 方法卡、手绘边框、编号模块、图标和底部结论条等视觉语法；不要复用旧图的主题、名词或业务内容。
- 内容来源：`wiki/reports/ai-visual-expression-workflow-guide.md` 和 `wiki/adr/0035-visual-reference-style-source-not-content-source.md`

## 生成 Prompt

```text
Create a 16:9 Chinese hand-drawn method card on warm cream paper. Use
image-model output only. Do not create SVG, HTML, H5, browser screenshot,
wireframe, dashboard, or web page output.

Use the attached reference image only for visual style and layout grammar:
2x2 hand-drawn method card, thick black marker border, large handwritten title,
red / blue / green / orange module frames, big number badges 01-04, one doodle
icon per module, and a yellow bottom takeaway banner.

Do not reuse the reference image's old topic, old nouns, or old business
content. The content of this new image is only the image-generation method
selection workflow below.

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

Bottom banner:
Prompt 解决说清楚，visual-agent 解决选对路，图片模型解决画出来。

Keep Chinese text large and readable. Use short labels only. No extra claims.
No unrelated product, account, payment, wiki, or knowledge-base content.
```

## 出图后检查

- 标题必须是 `作图方法怎么选`。
- 必须是 2x2 方法卡，不要变成流程图或网页。
- 中文如果大面积错误，直接重生成；不要改成 SVG/H5。
