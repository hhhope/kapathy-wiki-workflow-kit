---
title: reference-driven-output-calibration / retro
type: retro
canonical_object: reference-driven-output-calibration
artifact_type: retro
language: zh-CN
audience: self
domain: personal-ops
status: active
updated_at: 2026-05-04
ai_generated: true
derived_from:
  - wiki/ops/intelligence-native-organization-intake.md
  - wiki/ops/intelligence-native-organization-h5.html
  - wiki/ops/intelligence-native-organization-handdrawn-h5.html
  - https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w
related_objects:
  - intelligence-native-organization
  - example-driven-capture
  - disagreement-management
  - xiaohongshu-retro-grid-content
  - weixin-reference-wiki-capture
notes_scope: 记录 2026-05-04 围绕 Block intelligence-native organization 材料输出、微信公众号参考、H5 图文纠偏与 skill 沉淀的过程；重点保留用户纠偏压力和可复用方法，不把本轮产物提升为 repo policy。
---

# reference-driven-output-calibration / retro

## Trigger

本轮从用户要求“搜索 Block 这个 CEO 最近写了什么文章”开始，逐步变成一次输出校准：

- 先记录 Jack Dorsey / Roelof Botha 的 `From Hierarchy to Intelligence`
- 再参考微信公众号文章调整文章结构和话术
- 再把文章转成 H5
- 再用用户提供的手绘参考图纠偏 H5
- 最后把两类可复用能力沉淀到 skill

表面上看，这是一次内容生产；实际更重要的是：

> 外部参考不是只提供内容，也提供结构、话术、视觉语法和纠偏标准。

## Source References

主题来源：

- Block / Sequoia：`From Hierarchy to Intelligence`
- 本 repo 记录页：`wiki/ops/intelligence-native-organization-intake.md`

写法参考：

- 微信公众号文章：`AI也有潜意识 而且会传染...`
- URL：https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w

视觉参考：

- 用户本地目录：`C:\Users\yan\Desktop\1`
- 关键参考图：`10.png`
- 该图用于学习视觉语法，不进入 repo，不直接复制图像内容。

## Timeline

### 1. 文章学习阶段

先将 Block / Sequoia 文章整理成 `intelligence-native-organization-intake.md`。

初稿问题：

- 参考链接不完整
- 写法偏口语
- 缺少公众号文章那种强判断、反误读、证据链和行动清单结构

后续修订补上：

- Block / Sequoia 原文链接
- Jack Dorsey 当前官方头衔来源
- 裁员与 AI 背景报道
- 微信公众号文章作为写法参考，而不是主题来源

### 2. H5 初版阶段

先生成了一个 `retro-grid` 风格 H5：

- `wiki/ops/intelligence-native-organization-h5.html`

这个版本解决了“可视化呈现”，但还偏网格卡片和管理汇报。

### 3. 手绘 H5 纠偏阶段

用户指出参考图的知识密度来自大量图示，而不是文字堆叠：

- “不够好你看图片里面有知识密度很多有很多图我们几乎是文字”
- “你和原图对比下，还是少很多图示”
- “不是结论的问题，你再仔细对比原图”

这几次纠偏逐步暴露了错误 framing：

- 不是“结论还不够”
- 不是“多加一些图标”
- 不是“文案再压缩一点”
- 而是 H5 的视觉语法错了

最终重写成手绘教学图方向：

- `wiki/ops/intelligence-native-organization-handdrawn-h5.html`

关键变化：

- 01：气泡 -> 状态简报 -> AI 机器人/问答
- 02：旧组织信息爬楼 vs 新组织状态入模
- 03：剪贴板 -> 靶心，表达“不是问模型，而是给模型下任务”
- 04：五张连线结构卡
- 05：循环迭代图 + 黑底警示
- 06：工具箱、脑、闪电、文档、行动的结尾图示

### 4. Skill 沉淀阶段

用户要求把这次经验融合进小红书 skill，形成两个类型可选。

已写入全局 skill：

- `/home/yan/.codex/skills/xiaohongshu-retro-grid-content/SKILL.md`
- `/home/yan/.codex/skills/xiaohongshu-retro-grid-content/references/html-visual-modes.md`

新增两个 HTML 一图流模式：

- `retro-grid`：网格卡片型，适合数据、对比、矩阵、管理汇报
- `handdrawn-teaching`：手绘教学型，适合概念解释、流程拆解、少文字多图示

随后又新增全局 skill：

- `/home/yan/.codex/skills/weixin-reference-wiki-capture/SKILL.md`

它负责将微信公众号文章从“一次性参考”变成 wiki 学习记录。

## Rejected Framing

本轮被连续否定的 framing 有四个。

### 1. “只是把文章总结好”

实际需要的是：

- 抽取 Block 文章的主张
- 保留来源边界
- 学习微信公众号文章的表达结构
- 不把外部组织设计直接写成 repo policy

### 2. “参考微信公众号文章就是改话术”

实际参考点更广：

- 强判断开头
- 默认假设拆解
- 证据链推进
- 反误读
- 行动清单
- 参考链接完整性

话术只是表层，结构才是关键。

### 3. “H5 多加图标就行”

实际问题是视觉语法。

参考图每段都有一个主视觉动作：

- 气泡到文档到机器人
- 差输入 vs 好输入
- 剪贴板到靶心
- 连线结构卡
- 循环迭代
- 工具箱式结论

如果只加 chips、色块、图标，仍然是文字卡片。

### 4. “补结论就能解决”

用户明确指出“不是结论的问题”。

这说明争点已经从内容判断转移到表达结构：

> 信息是否被图示承载，而不是是否又多写了几条结论。

## What To Reuse

### 微信文章参考的复用方式

以后遇到微信公众号文章作为参考时，应先判断它提供的是哪类参考：

- 内容观点
- 写法结构
- 话术力度
- 证据组织
- 视觉语法
- 读者节奏

不能默认当作“资料来源”或“摘要对象”。

### H5 的两类输出模式

未来小红书 / H5 一图流至少先分两类：

- `retro-grid`：适合信息整理、矩阵、数据、报告
- `handdrawn-teaching`：适合概念解释、方法论、流程拆解、抽象主题

如果用户给手绘参考图，或反复说“太多文字”“图示少”“不像原图”，默认进入 `handdrawn-teaching`。

### 纠偏压力的处理方式

当用户连续指出“不够好”“不是这个问题”“再对比原图”时，不应继续局部修补。

应停下来重判：

- 上一个 framing 是什么
- 用户否定的是内容、结构、语气、视觉，还是目标
- 参考对象真正提供的标准是什么

## What To Adapt

### 对 repo wiki 的适配

本页放在 `wiki/ops`，不是 `wiki/examples`。

原因：

- 这不是一个纯输出样例
- 它包含协作纠偏、外部参考学习、skill 沉淀和后续路由
- 它更像一次输出校准 retro

如果未来要展示“好的手绘 H5 样例”，可以另建 `wiki/examples` 页面，专门摘取视觉结构，不承载本轮分歧过程。

### 对 skill 的适配

这次沉淀没有直接改 repo-local `.codex/skills`，而是写入全局 skill：

- 小红书图文能力属于跨项目复用
- 微信文章参考落 wiki 也不限于本 repo

但这带来一个限制：

- `/home/yan/.codex/skills` 当前不是 git 仓库
- 这些 skill 变更有本地证据文件，但没有 git commit 作为版本锚点

## What Not To Copy

不要复制的东西：

- 不直接复制微信公众号文章内容
- 不把手绘参考图内容照搬到 Block 主题
- 不把 Block 的组织设计文章直接变成 repo AGENTS 或 OpenSpec 规范
- 不把“用户凑活吧”误读成这个模式已经完美，只能说明当前版本可用

## Output Artifacts

本轮主要产物：

- `wiki/ops/intelligence-native-organization-intake.md`
- `wiki/ops/intelligence-native-organization-h5.html`
- `wiki/ops/intelligence-native-organization-handdrawn-h5.html`
- `/home/yan/.codex/skills/xiaohongshu-retro-grid-content/references/html-visual-modes.md`
- `/home/yan/.codex/skills/weixin-reference-wiki-capture/SKILL.md`

相关提交：

- `eabf6de`：记录 intelligence-native organization 文章
- `6f372f8`：补参考链接
- `40c1992`：新增 retro-grid H5
- `1866f1a`：新增 handdrawn H5
- `78eb820`：增强图示密度
- `4a13b4b`：按参考图视觉语法重排 H5

## Current Rule Of Thumb

以后遇到“参考一篇文章/一张图来改输出”，先问或判断这四件事：

1. 参考对象提供的是内容，还是结构？
2. 用户不满的是结论，还是表达载体？
3. 输出应走网格卡片，还是手绘教学？
4. 学到的东西应落 `wiki/examples`、`wiki/ops`，还是 skill？

## Next Step

下一次类似任务，先执行这个顺序：

1. 用 `weixin-reader` 读取微信公众号文章正文
2. 用 `weixin-reference-wiki-capture` 判断它提供的参考类型
3. 如果要做 H5，用 `xiaohongshu-retro-grid-content` 先选择 `retro-grid` 或 `handdrawn-teaching`
4. 如果用户连续纠偏，先写 retro 或更新当前 retro，再继续改产物

这条链路的目标不是让输出更复杂，而是避免把“参考”误读成“再多写一点”。
