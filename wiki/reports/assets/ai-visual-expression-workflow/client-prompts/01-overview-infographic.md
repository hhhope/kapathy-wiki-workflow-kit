---
layer: reports
domain: ai-workflow
---

# 01 总览一图流：AI 作图先拆再画

## 客户端生成设置

- 输出方式：图片模型生成，不要用 SVG、H5、HTML 截图或网页渲染。
- 建议比例：竖版 3:4，也可以 2:3。
- 参考图片路径：`wiki/reports/assets/account-wiki-onepager.png`
- 参考图片角色：只提供手绘质感、版式密度、边框、编号、涂鸦、底部横幅等视觉语法；不要复用旧图的主题、名词或业务内容。
- 内容来源：`wiki/reports/ai-visual-expression-workflow-guide.md` 和 `wiki/adr/0035-visual-reference-style-source-not-content-source.md`

## 生成 Prompt

```text
Create a vertical 3:4 Chinese hand-drawn infographic poster on warm cream paper.
Use an image-model / sketchnote style only. Do not create SVG, HTML, H5, browser
screenshot, wireframe, dashboard, or web page output.

Use the attached reference image only for visual style and layout grammar:
dense one-page hand-drawn teaching poster, thick black marker outline, large
handwritten Chinese title, colored number badges, doodle icons, arrows,
underlines, tape, stars, and a yellow / orange bottom takeaway banner.

Do not reuse the reference image's old topic, old nouns, or old business
content. The content of this new image is only the AI image-generation workflow
below.

Main title: AI 作图先拆再画
Subtitle: 参考图给版式，内容给字段，visual-agent 选路径，图片模型最后出图

Section 01 title: 正确路径
Show a five-step chain with small icons:
参考图 -> 反推版式 Prompt -> 拆内容字段 -> 合成最终 Prompt -> 确认后出图

Section 02 title: Prompt 方法
Main text: 把需求说清楚
Short labels: 版式来源, 业务文字, 禁止元素, 确认字段

Section 03 title: visual-agent
Main text: 把作图类型和路径选对
Short labels: 流程结构图, 海报封面, 知识卡长图, H5/HTML, Hybrid

Section 04 title: 图片模型
Main text: 负责最后画出来
Short labels: 豆包, Codex 图像模型, 手绘质感, 二次修正

Section 05 title: 验收清单
Use check marks:
文字完整, 中文清晰, 版式保留, 禁用元素清干净

Section 06 title: 核心结论
Main text: 先理解图，再组织内容，最后生成图片

Bottom banner:
不要让 AI 猜图；先拆版式，再填内容，再生成。

Keep Chinese text large and readable. Use short labels only. No dense paragraphs.
No generic tech background. No unrelated product, account, payment, wiki, or
knowledge-base content.
```

## 出图后检查

- 标题必须是 `AI 作图先拆再画`。
- 画面主题必须是“AI 作图工作流”，不能漂回参考图旧主题。
- 中文如果大面积错误，直接重生成；不要改成 SVG/H5。
