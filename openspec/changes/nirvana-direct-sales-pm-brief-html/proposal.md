## Why

当前涅槃一期材料已经有交接稿、PM 复盘稿和零散汇报页，但表达口径仍然混杂了交接语言、分析语言和项目管理语言，导致在直销模式下一期复盘和向领导汇报时，无法直接回答“承诺了什么、现在做到哪里、最小可交付路径是什么、资源上要什么”。同时，现有内容没有形成高对比、高信息密度的单页 HTML 展示，难以支撑现场汇报。

## What Changes

- 将直销模式下一期的项目材料统一成项目管理语言，围绕“产品承诺接口、对客最小路径、当前能力覆盖、关键时间节点、当前约束、资源诉求、待拍板事项”重构 PM 汇报稿。
- 基于现有 `nirvana-handover-account-owner.md`、`nirvana-phase1-pm-review.md` 和参考 H5，沉淀一版可直接用于领导汇报的直销一期管理主稿。
- 新增一版高对比、高信息密度的单页 HTML 汇报页，突出“承诺范围 vs 当前可交付范围”“主链路 vs 运营/BM/分账耦合”“时间节点 vs 资源动作”的对比关系。
- 将现有泛化的 `gap` 话术替换为项目管理口径，如“当前偏差”“未闭环项”“交付约束”“资源配置约束”“需管理层拍板事项”。

## Capabilities

### New Capabilities
- `nirvana-direct-sales-pm-brief`: 以直销模式下一期为范围，输出可直接用于复盘和领导汇报的 PM 管理主稿，覆盖承诺接口、最小路径、能力覆盖、时间节点、当前约束、资源诉求和决策事项。
- `nirvana-direct-sales-html-brief`: 基于 PM 管理主稿生成高对比、高信息密度、适合投屏汇报的单页 HTML 视图。

### Modified Capabilities

## Impact

- Affected content:
  - `wiki/reports/nirvana-phase1-pm-review.md`
  - `wiki/reports/nirvana-phase1-leadership-brief.md`
  - `wiki/reports/index.md`
  - new HTML artifact for direct-sales leadership review
- Affected systems:
  - OpenSpec change artifacts for the nirvana direct-sales reporting workflow
  - report wiki management-facing reporting outputs
- No external API or runtime dependency changes; impact is limited to reporting artifacts and their presentation layer.
