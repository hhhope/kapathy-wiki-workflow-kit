---
title: Agent 治理 gate 缺口探索 2026-04-18
type: intake
language: zh-CN
source_path: chat://openspec-explore/agent-governance-gate-gap-2026-04-18
source_type: conversation
audience: self
knowledge_level: working
domain: wiki
layer: ops
ops_area: agent-governance
canonical_object: agent-governance-gate-gap
artifact_type: explore
period: active
confidence: high
status: active
updated_at: 2026-04-18
ai_generated: true
related_sources: []
related_focus_threads:
  - main-thread.md
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# Agent 治理 gate 缺口探索 2026-04-18

## 触发问题

用户连续多轮追问：既然仓库已经写了不少 agent 工作流规则、ADR 和 OpenSpec 规范，为什么运行时仍然会出现“规则写了但没触发”的漂移，尤其体现在 `archive review`、`openspec-explore` 留痕和 agent 流程复盘留存上。

## 当前关注点

- 区分“已经写进规则”和“已经变成运行时 gate”
- 判断当前仓库是否真正落地了 `openspec-explore`
- 确定这类多轮 agent 流程争论应该沉淀到哪里，避免再次只留在聊天里

## 当前假设

- 仓库已经落地了 `openspec-explore` 的基础留痕机制，但只覆盖“进入 explore 前要在 `wiki/ops/` 留 trace”
- 仓库尚未落地“agent 流程偏差复盘必须留下 repo-visible 记录”的默认 gate
- 当前最真实的缺口不是规则缺失，而是缺少把关键规则变成状态信号、失败信号或固定记录入口的执行机制

## 暂未决定

- 这类 agent 流程复盘未来应固定进 `wiki/ops/retro`、`logs/`，还是要求在相关 change 里补 `archive-review.md`
- 哪些治理规则值得升级成 health-check，而哪些只适合保留为人工判断
- 是否要把“多轮同主题争论必须落一条 retro / trace”提升为新的仓库默认工作流

## 下一步

- 把这次关于 gate 缺口的论点整理成一条可复盘的 `wiki/ops` 页面
- 明确当前结论：`openspec-explore` 已部分落地，但复盘留痕还没有形成同等级 gate
- 如果用户决定把这条要求变成仓库默认行为，再新开 OpenSpec change 承接实现
