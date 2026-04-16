---
name: material-collaboration-defaults
description: Use when the user drops meeting notes, weekly materials, reports, attachments, preview html, or other source files and expects Codex to process them without repeated workflow confirmation.
---

# Material Collaboration Defaults

## Overview

把用户刚投递进仓库的材料继续处理成可读结果，不要停在占位 intake 或重复确认整套流程。

核心原则：

- 默认先处理材料，再提问
- `source` 不能只留占位文本，必须补可读中文结论
- 同一批材料按增量处理，不重复全量重做
- 只有在输出路径真实分叉时，才问一次

## When to Use

适用于这些场景：

- 用户把会议纪要、逐字稿、周报、附件、飞书导出、截图、`html/preview` 文件放进仓库
- 用户说“你去处理”“整理一下”“归档一下”“帮我看这些材料”
- 用户没有显式写步骤，但明显期望 Codex 主动完成整理

不适用于：

- 纯代码实现任务
- 已经明确指定只做单一步骤，比如“只建 source 占位页”

## Default Processing Chain

收到材料后，默认按这个顺序执行：

1. 判断是新材料还是已整理材料的补充
2. 建或更新 `source`
3. 补真正的中文摘要、关键结论、风险、待办
4. 判断是否需要 `ops` 层输出
5. 如果材料已经接近面向受众的交付物，再判断是否进入 `reports`

除非用户明确说“只 intake”，否则不要停在仅有占位文本的草稿。

## Output Rules

### 1. Source 是默认必做项

- 会议纪要、逐字稿、周报、附件、导出文档都先进入 `source`
- `source` 页面至少要有：
  - 中文摘要
  - 关键结论
  - 风险或争议点
  - 待跟进事项

### 2. Ops 不是默认跳过项

如果材料中已经出现明确动作、owner、截止时间、阻塞项，默认继续补：

- `intake`
- 必要时 `reminder`
- 只有成熟到研发执行边界时才升 `codex-handoff`

### 3. Reports 是条件输出

只有材料已经明显面向受众，或者用户明确要汇报稿时，才进入 `reports`。

### 4. Visual / HTML 是一次性确认项

如果材料里存在 `html / preview / h5 / gantt` 这类可视化产物：

- 默认先整理 wiki 层来源和结论
- 如果当前请求没有明确说要更新可视化文件本体，必须问一次：
  - 只同步 wiki 结论
  - 还是同时更新原始 `html/h5/preview`

不要把这个问题扩展成整套流程确认；只问这个输出分叉点。

## Incremental Rules

- 先识别哪些 `source_path` 已经整理过
- 已有结论时，默认增量补充，不整页重写
- 新材料比旧材料更完整时，更新摘要并保留原有链接关系
- 不要每次全量重跑整个 `inbox/`

## Repo Pattern

当前 repo 的固定约束：

- [AGENTS.md](../../../AGENTS.md)
- [ADR-0006](../../../wiki/adr/0006-formal-project-local-skills-over-drafts.md)
- [ADR-0007](../../../wiki/adr/0007-retire-draft-skills-as-runtime-surface.md)

## Ask-Once Boundaries

只有下面这些情况才需要问用户：

- 是否要产出或修改 `html/h5/preview`
- 同一材料可能进入多个互斥交付物，且成本差异明显
- 现有页面结论与新材料直接冲突，无法安全覆盖
- 需要做超出当前材料整理范围的研发执行

下面这些情况不要问：

- 是否先建 `source`
- 是否要补中文摘要
- 是否要抽动作项
- 是否要做增量而不是全量

## Common Mistakes

- 只生成“待补充”占位页就结束
- 把 intake 当成整理完成
- 每批新材料都重新扫全仓
- 明明只有一个输出分叉点，却把整套流程重新问一遍
- 用户给了会议纪要，却不提炼结论、风险和待办
