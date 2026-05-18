---
title: multi-system branch spec explore
layer: ops
type: intake
language: zh-CN
source_path: chat://openspec-explore/multi-system-branch-spec-2026-05-12
source_type: conversation
audience: self
knowledge_level: working
domain: product-engineering-collaboration
ops_area: workflow-trace
canonical_object: multi-system-branch-spec
artifact_type: explore
period: active
confidence: medium
status: active
updated_at: 2026-05-12
ai_generated: true
related_sources: []
related_focus_threads: []
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# multi-system branch spec explore

## 触发问题

用户要调研：一个业务需求同时对应多个系统和多个项目时，branch 和 spec 文档
应该怎么组织，避免总需求、各系统实现、跨项目联调和验收边界混在一起。

## 当前关注点

- 一个需求是否应该只有一个总 spec，还是每个系统都有子 spec。
- 多系统代码分布在多个 repo 或多个项目时，branch 是按需求切还是按系统切。
- 总控文档如何记录业务目标、跨系统契约、依赖顺序和验收矩阵。
- 各系统 spec 如何保留自己的实现、测试、迁移和发布边界。
- 如何避免执行计划、项目计划、子系统任务清单变成互相竞争的多套进度账本。

## 当前假设

- 推荐采用“一个需求总控 + 多个系统子变更”的结构。
- 总控 spec 管业务意图、跨系统契约、接口时序、发布依赖和整体验收。
- 子 spec 管单个系统或单个 repo 内的实现范围、任务、验证和回滚。
- branch 应尽量和代码归属一致；跨 repo 需求不应该强行制造一个物理大 branch。

## 已确认事实

- 本仓库 `PROJECT.md` 声明 OpenSpec owns change lifecycle and implementation progress。
- 现有 `add-product-status-contract` change 展示了 proposal/design/tasks 的基础分工。
- 现有 `clarify-openspec-superpowers-overlay` change 记录过一个关键边界：OpenSpec
  `tasks.md` 应保持唯一进度和完成账本，执行 overlay 不能产生第二套 task ledger。
- 本仓库分支命名已经存在 `feat/<change-topic>`、`chore/<change-topic>` 等按变更主题命名的模式。

## 已确认边界

- 本页是探索 trace，不是正式 OpenSpec proposal。
- 不改变仓库默认 branch 或 OpenSpec 规则。
- 如果后续要固化为团队规范，应另开 OpenSpec change。

## 下一步

- 给出跨系统需求的推荐模型：总控 change + 系统子 change。
- 明确什么时候用一个 spec、什么时候拆多个 spec。
- 明确 branch 命名、任务账本、验收矩阵和发布联调的边界。
