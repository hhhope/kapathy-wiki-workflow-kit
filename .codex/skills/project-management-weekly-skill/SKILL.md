---
name: project-management-weekly-skill
description: Use when the user asks about 项目管理, 周报, 里程碑, 风险, 甘特图, 项目推进, or provides weekly project-management materials that need structured weekly outputs
---

# Project Management Weekly Skill

## Overview

把项目管理输入统一变成固定周推进输出，不要只写自由发挥式总结。

核心原则：
- 先判断输入类型，再决定输出类型
- 周材料必须保留来源，不允许只留结论
- reminder 不等于 Codex handoff

## When to Use

适用于这些场景：

- 用户说“项目管理”
- 用户给周报、排期、风险清单、里程碑、甘特图、测试推进表、问题追踪表
- 用户要看本周进展、偏移、风险、下周动作
- 用户要把项目管理材料落到 wiki 并持续归档

不适用于：

- 纯研发实现任务
- 只改单个接口或代码文件
- 没有项目推进上下文的普通会议纪要

## Fixed Outputs

处理项目管理输入时，必须先判断本轮需要哪些输出：

1. `source`
   - 原始周报、排期、风险表、测试表等来源页
2. `html/source companion`
   - 如果存在 `html`、甘特图预览、能力地图等可视化周视图，单独做来源页
   - 如果用户明确要求“更新图”“更新 html”“更新 preview”，并且原文件可编辑，必须更新原始视图文件本体，不能只同步 wiki
3. `intake`
   - 抽取本周判断：进展、偏移、风险、下周动作
4. `reminder`
   - 把本周必须跟进的动作单独落出来
5. `codex handoff candidate`
   - 只判断是否成熟，不要默认直接升级

## Required Extraction

每次至少判断并输出这些信息：

- `milestone`
- `this_week_progress`
- `drift`
- `risks`
- `next_actions`
- `owner`
- `codex_handoff_candidate`

如果有额外材料，再补：

- `html_view_summary`
- `capability_map_signal`
- `technical_construction_signal`

## Escalation Rules

停留在 `reminder` 的情况：

- 主要是对单、排期、边界确认
- owner 还没定
- 验收标准不清楚
- 还不是明确研发任务

可以进入 `Codex handoff candidate` 的前提：

- 已明确是研发任务
- 目标、上下文、影响范围清楚
- 可以写最小验收口径

## Repo Pattern

当前 repo 的参考链路：

- 规则页：
  - [项目管理周推进循环](../../../wiki/ops/project-management-weekly-loop.md)
- 示例来源：
  - [涅槃项目周报 2026-04-13](../../../wiki/sources/nirvana-weekly-2026-04-13.md)
  - [涅槃项目周视图 2026-04-13](../../../wiki/sources/nirvana-weekly-view-2026-04-13.md)
- 示例 ops：
  - [涅槃项目周推进 intake 2026-04-13](../../../wiki/ops/nirvana-weekly-intake-2026-04-13.md)
  - [涅槃项目本周跟进提醒 2026-04-13](../../../wiki/ops/nirvana-weekly-reminder-2026-04-13.md)

## Output Order

默认顺序：

1. 先确认原始材料位置
2. 再建或更新 `source`
3. 如果有周视图，再建 `html/source companion`
   - 如果周视图文件本体需要更新，先改原文件，再同步来源页和周结论
4. 再写 `intake`
5. 再写 `reminder`
6. 最后只判断要不要进入 `Codex handoff candidate`

## Common Mistakes

- 只写总结，不保留来源页
- 把 `html` 周视图混进普通周报，不单独存档
- 用户要求更新周视图时，只改 wiki，不改原始 `html/h5/preview`
- 直接把项目管理待办升级成 Codex 任务
- 忽略 owner、偏移和风险，只写进展百分比
- 改甘特图时间轴时，没有检查每一行的月份格数量和视觉对齐，导致主线错位

## Quick Check

处理完后至少自查这 5 个问题：

- 有来源页吗？
- 如果用户要求改图，原始 `html/h5/preview` 本体改了吗？
- 有本周偏移判断吗？
- 有风险吗？
- 有下周动作吗？
- 有 owner 和 handoff 判断吗？

如果本轮改了甘特图/周视图，再额外检查：

- 时间轴月份列数量是否一致
- 每条主线的 bar cell 数量是否与时间轴对齐
- `M2-M3` 这类跨阶段主线有没有因为空格缺失而视觉错位
