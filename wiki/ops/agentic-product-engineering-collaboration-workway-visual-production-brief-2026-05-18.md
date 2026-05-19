---
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
canonical_object: agentic-product-engineering-collaboration-workway-visual-production
artifact_type: visual-production-brief
title: agentic-product-engineering-collaboration workway visual production brief 2026-05-18
type: visual-production-brief
language: zh-CN
status: active
created_at: 2026-05-18
updated_at: 2026-05-18
ai_generated: true
derived_from:
  - wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
  - wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md
related_objects:
  - public-report-quality-gate
  - knowledge-article-visual
  - infographic-onepager
  - imagegen
notes_scope: 记录 H5 工作方式重写版本的章节配图脚本和图片模型 / hybrid 输出边界。
---

# agentic-product-engineering-collaboration workway visual production brief 2026-05-18

## Purpose And Route

This brief turns the H5 section visual request into repo-visible production
scripts before any image executor runs. It is the control artifact for six
standalone section visuals, not a final image-quality claim.

Route:

1. `public-report-quality-gate` owns reader-facing intent, output shape, review
   boundary, and evidence boundary.
2. `knowledge-article-visual` owns the article-level visual package and the
   progression across the H5.
3. `infographic-onepager` owns each per-image teaching-card or one-page script.
4. `imagegen` is the final bitmap executor only after scripts exist.

## Existing Visual Inspection Summary

Inspected existing local references:

- `wiki/reports/agentic-collaboration-images/02-company-dumbbell.png`
- `wiki/reports/agentic-collaboration-images/ai-collaboration-operating-system-onepager.png`
- `wiki/reports/agentic-collaboration-images/04-operating-system.png`
- `wiki/reports/agentic-collaboration-images/05-agent-loop.png`

Grammar to preserve:

- warm cream paper texture
- thick black marker outer border
- large handwritten Chinese title
- colored number badge at the top-left or section anchor
- boxed modules with marker outlines
- doodle icons, arrows, underlines, tape, stars, and small warning notes
- bottom takeaway banner in yellow/orange marker style
- readable Chinese text with short labels, not paragraph blocks

Wording and visual debt to replace:

- Replace the English `Review Packet` label with direct Chinese wording such as
  `验证证据` or `可审查证据`; avoid turning it into a new opaque noun.
- Do not reuse the old metrics strip as a section-02 proof surface. Metrics such
  as commits, logs, specs, and ADR belong later in the evidence section.
- Avoid old generic diagrams when the section now needs split-account-core
  content, AI work graph nodes, role evidence, and writeback boundaries.
- Do not create decorative no-text editorial images. Each image must carry a
  section-level argument.

## Article-Level Visual Package

The package contains six assets requested for sections 02, 03, 04, 06, 08, and
09. Use horizontal 16:9 teaching-card format by default; section 03 may remain a
vertical one-pager if the final composition needs the full operating-system map.

1. `workway-02-local-overload.png` - 分账核心说明: 信息密度压穿传统协作.
   This image opens the local case: 9 docs, 6 designs, 3 notes, about 90k words,
   16 meetings, and daily reports still leave drift, inconsistency, one-person
   bottlenecks, and cross-team friction. The relief is an AI work graph.
2. `workway-03-operating-system.png` - 先用一张图看清: 重塑作业方式.
   This image gives the H5's scan-first model: AI is not a tool; it connects
   intent, knowledge, plans, tools, evidence, and writeback while human judgment
   remains central.
3. `workway-04-capability-layers.png` - AI capability layers.
   This image decomposes the system into eyes/intent, knowledge/code archaeology,
   plan simulation, hands/tool execution, and feedback/writeback. It must show
   the difference between general models and vertical knowledge/interfaces.
4. `workway-06-technical-route.png` - Technical route.
   This image shows one real chain: prototype -> multi-option evaluation ->
   Spec/ADR -> tool execution -> real verification -> writeback/memory layers.
   It is not a platform-stack chart.
5. `workway-08-work-graph.png` - Complex demand becomes AI-participating work
   graph.
   This image names the graph nodes: requirement card, knowledge links,
   方案评估, execution env, evidence, owner judgment, and failure writeback.
6. `workway-09-evidence-system.png` - Engineering changes from delivery pipeline
   to evidence-driven collaboration.
   This image contrasts old waterfall with the new evidence loop and shows how
   product, RD, test, PM, and owner roles collaborate.

Progression through the article:

- Section 02 proves the pain is local and concrete, not abstract AI strategy.
- Section 03 gives the total operating-system lens.
- Section 04 decomposes the AI capabilities without losing the human judgment
  boundary.
- Section 06 turns the model into a technical route that can be piloted.
- Section 08 converts the workflow into an AI-participating work graph.
- Section 09 closes with the engineering-collaboration change and evidence
  system.

## Per-Image Infographic Scripts

### workway-02-local-overload.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: 16:9 horizontal teaching card.

Title: 分账核心不是缺资料

Subtitle: 信息密度压穿传统协作

Layout: left metrics stack, middle bottleneck, right work graph relief.

Panels/modules:

1. `资料很多`: `9 需求`, `6 详设`, `3 纪要`, `约 9 万字`, `16 场会议`, `每日进度`.
2. `仍会漂移`: `口径不一`, `状态过期`, `接口反复确认`.
3. `一号位卡点`: `历史需求`, `代码考古`, `上线风险`.
4. `AI 工作图`: `需求`, `代码`, `接口`, `问题`, `owner`, `风险`.

Bottom sentence: 问题不是没有信息，而是没有共同维护的全局工作图。

Image prompt:

```text
Create a 16:9 Chinese hand-drawn teaching card on warm cream paper, thick black
marker border, large handwritten title, blue number badge "02", colored boxed
modules, doodle icons, arrows, and a yellow bottom takeaway banner.

Main title: 分账核心不是缺资料
Subtitle: 信息密度压穿传统协作

Left panel title: 资料很多
Show short metric labels: 9 需求, 6 详设, 3 纪要, 约 9 万字, 16 场会议, 每日进度.

Middle panel title: 仍会漂移
Show a stressed owner icon with labels: 口径不一, 状态过期, 接口确认, 风险压身.

Right panel title: AI 工作图
Show connected nodes: 需求, 代码, 接口, 问题, owner, 风险.

Bottom banner: 问题不是没有信息，而是没有共同维护的全局工作图。
Use readable Chinese, no dense paragraphs, no English labels.
```

### workway-03-operating-system.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: vertical one-pager is allowed if it preserves the scan-first operating
system map; otherwise use 16:9 horizontal teaching card.

Title: 不是 AI 工具

Subtitle: 是重塑产研作业方式

Layout: central human judgment circle, surrounding operating-system loop.

Panels/modules:

1. `意图`: `原话`, `目标`, `非目标`.
2. `知识`: `文档`, `代码`, `会议`, `测试`.
3. `方案`: `多路径`, `反方`, `风险`.
4. `工具`: `repo`, `数据`, `截图`, `日志`.
5. `证据`: `真实验证`, `验证证据`.
6. `写回`: `规则`, `ADR`, `ops`, `知识库`.

Bottom sentence: 不是多一个聊天入口，而是让工作对象可追踪、可验证、可写回。

Image prompt:

```text
Create a Chinese hand-drawn infographic in the same warm cream paper style,
thick black marker border, large handwritten title, colored numbered tags,
boxed modules, doodle icons, arrows, and a yellow bottom takeaway banner.
Prefer vertical one-page composition if needed for a full loop.

Main title: 不是 AI 工具
Subtitle: 是重塑产研作业方式

Center: 人的判断
Surrounding loop modules:
01 意图: 原话 / 目标 / 非目标
02 知识: 文档 / 代码 / 会议 / 测试
03 方案: 多路径 / 反方 / 风险
04 工具: repo / 数据 / 截图 / 日志
05 证据: 真实验证 / 验证证据
06 写回: 规则 / ADR / ops / 知识库

Bottom banner: 不是多一个聊天入口，而是让工作对象可追踪、可验证、可写回。
Keep Chinese large and readable.
```

### workway-04-capability-layers.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: 16:9 horizontal teaching card.

Title: AI 放大人的判断

Subtitle: 通用模型负责推演，垂直知识保存经验

Layout: five capability layers from left to right, with human judgment above and
vertical knowledge/interface base below.

Panels/modules:

1. `眼睛 / 意图`: `原话`, `歧义`, `验收`.
2. `知识考古`: `历史`, `代码`, `接口`.
3. `方案推演`: `多方案`, `反方`, `评分`.
4. `手脚 / 工具`: `repo`, `DB`, `截图`.
5. `反馈写回`: `证据`, `失败`, `规则`.

Bottom sentence: 人负责目标和取舍，AI 放大判断依据。

Image prompt:

```text
Create a 16:9 Chinese hand-drawn teaching card with warm cream paper, thick
black marker border, large handwritten title, purple number badge "04", boxed
modules, doodle icons, arrows, and a yellow bottom takeaway banner.

Main title: AI 放大人的判断
Subtitle: 通用模型负责推演，垂直知识保存经验

Five horizontal capability boxes:
01 眼睛/意图: 原话, 歧义, 验收
02 知识考古: 历史, 代码, 接口
03 方案推演: 多方案, 反方, 评分
04 手脚/工具: repo, DB, 截图
05 反馈写回: 证据, 失败, 规则

Show a base strip: 垂直知识库 + 真实接口.
Show a top marker label: 人的判断在中心.
Bottom banner: 人负责目标和取舍，AI 放大判断依据。
No corporate dashboard style.
```

### workway-06-technical-route.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: 16:9 horizontal teaching card.

Title: 先跑通一条真实链路

Subtitle: 不是搭平台，是让复杂需求可追踪、可比较、可验证

Layout: one chain across the page with six steps and a writeback layer beneath.

Panels/modules:

1. `原型`: `真实需求`, `可点开`.
2. `多方案`: `快上`, `稳妥`, `长期`, `不做`.
3. `Spec / ADR`: `边界`, `取舍`, `验收`.
4. `工具执行`: `代码`, `数据`, `截图`.
5. `真实验证`: `API`, `DB`, `权限`, `日志`.
6. `写回记忆`: `测试`, `规则`, `ops`, `知识库`.

Bottom sentence: 每一步都要把判断变成可试、可证、可写回的对象。

Image prompt:

```text
Create a 16:9 Chinese hand-drawn technical route card on warm cream paper,
thick black marker border, large handwritten title, colored badge "06",
boxed step chain, doodle arrows, and a yellow bottom takeaway banner.

Main title: 先跑通一条真实链路
Subtitle: 不是搭平台，是让复杂需求可追踪、可比较、可验证

Draw one real chain, not a platform stack:
01 原型: 真实需求 / 可点开
02 多方案: 快上 / 稳妥 / 长期 / 不做
03 Spec/ADR: 边界 / 取舍 / 验收
04 工具执行: 代码 / 数据 / 截图
05 真实验证: API / DB / 权限 / 日志
06 写回记忆: 测试 / 规则 / ops / 知识库

Bottom banner: 每一步都要把判断变成可试、可证、可写回的对象。
Keep labels short and readable.
```

### workway-08-work-graph.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: 16:9 horizontal teaching card.

Title: 复杂需求变成工作图

Subtitle: AI 连接上下文，人做判断

Layout: old way on the left, AI-participating work graph in the center, owner
judgment and writeback on the right.

Panels/modules:

1. `旧方式`: `开会`, `翻材料`, `追状态`.
2. `工作图节点`: `需求卡`, `知识链接`, `方案评估`, `执行环境`, `证据`.
3. `人做判断`: `目标`, `边界`, `优先级`, `上线取舍`.
4. `失败写回`: `风险`, `测试`, `规则`, `知识库`.

Bottom sentence: 会议不再同步全部信息，而是处理冲突和待判断问题。

Image prompt:

```text
Create a 16:9 Chinese hand-drawn teaching card with warm cream paper, thick
black marker border, large handwritten title, green number badge "08",
boxed modules, connected graph nodes, doodle icons, arrows, and a yellow bottom
takeaway banner.

Main title: 复杂需求变成工作图
Subtitle: AI 连接上下文，人做判断

Left small panel: 旧方式
Labels: 开会 / 翻材料 / 追状态

Center graph: 工作图节点
Nodes: 需求卡, 知识链接, 方案评估, 执行环境, 证据

Right panel: 人做判断
Labels: 目标, 边界, 优先级, 上线取舍

Bottom-right mini panel: 失败写回
Labels: 风险, 测试, 规则, 知识库

Bottom banner: 会议不再同步全部信息，而是处理冲突和待判断问题。
No decorative-only illustration.
```

### workway-09-evidence-system.png

Output mode: hybrid preferred. Direct image model is acceptable only if the
Chinese text is readable.

Format: 16:9 horizontal teaching card.

Title: 从交付流水线到证据协作

Subtitle: 软件工程交付的不只是代码，而是可判断的证据链

Layout: old waterfall on the left, new evidence loop in the center, role map on
the right.

Panels/modules:

1. `旧流水线`: `需求`, `开发`, `测试`, `上线`.
2. `新证据环`: `意图`, `知识`, `方案`, `执行`, `验证`, `写回`.
3. `证据类型`: `真实 DB`, `API`, `权限`, `截图`, `日志`.
4. `角色协作`: `产品`, `研发`, `测试`, `PM`, `owner`.

Bottom sentence: 目标人定，过程可委托，结果可审计。

Image prompt:

```text
Create a 16:9 Chinese hand-drawn teaching card on warm cream paper, thick black
marker border, large handwritten title, red/orange number badge "09", boxed
modules, doodle icons, arrows, and a yellow bottom takeaway banner.

Main title: 从交付流水线到证据协作
Subtitle: 软件工程交付的不只是代码，而是可判断的证据链

Left panel: 旧流水线
Flow: 需求 -> 开发 -> 测试 -> 上线

Center loop: 新证据环
Nodes: 意图, 知识, 方案, 执行, 验证, 写回

Evidence strip: 真实 DB, API, 权限, 截图, 日志

Right role map: 产品, 研发, 测试, PM, owner

Bottom banner: 目标人定，过程可委托，结果可审计。
Use short readable Chinese labels and the same hand-drawn grammar.
```

## Quality Checklist

- Chinese text is readable at H5 desktop and mobile sizes.
- No image prompt, production note, or route language leaks into the H5 body.
- Visual grammar matches the existing warm paper / marker / badge / boxed-module
  style.
- Every image carries a section argument; no decorative-only image is accepted.
- Existing visuals have been inspected before scripting replacements.
- Final files are saved under
  `wiki/reports/agentic-collaboration-images/`.
- Later desktop and mobile visual QA must check nonblank render, aspect ratio,
  text overlap, style drift, and image placement in the H5.

## Proof Boundary

This brief is script and routing evidence. It does not prove final generated
asset quality, Chinese text correctness in bitmap output, H5 embedding quality,
mobile readability, or share-ready status.
