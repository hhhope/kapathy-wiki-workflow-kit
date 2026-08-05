---
layer: ops
domain: public-report-output
ops_area: workflow-trace
canonical_object: rd-digital-employee-profile-v1-h5-structure-reanchor
artifact_type: drift-reanchor
derived_from:
  - docs/superpowers/specs/2026-08-05-rd-digital-employee-profile-h5-design.md
  - wiki/ops/rd-digital-employee-profile-v1-2026-08-05.md
---

# 研发数字员工画像 H5 章节结构重锚

## 时间

2026-08-05

## 触发

用户确认白色滚动叙事 H5 后，进一步明确章节不能只做概念摘要和能力展示，必须完整回答：

1. Agent 是什么、由什么组成。
2. 研发 Agent 是什么。
3. 同业研发 Agent 已有哪些形态，以及和人的分工。
4. 研发数字员工的定位和必要条件。
5. 身份卡、行为特征和能力雷达。
6. 员工定级。
7. 使用场景。
8. 如何考核。
9. 用一个研发任务还原数字员工的一天。

## 原设计偏差

原设计把同业图谱、人机分工、身份卡、行为特征、使用场景、考核体系和完整任务回放压缩过多，容易形成“概念解释 + 能力清单”，不足以支撑画像作为岗位模型。

## 重锚后的主线

`Agent 基础 → 研发 Agent 专业化 → 同业与人机边界 → 数字员工岗位化 → 画像 → 定级 → 场景 → 考核 → 一天回放`

## 受保护目标

- 先定义对象，再呈现画像。
- 同业部分只使用新鲜度核验后的官方来源，不用二手文章替代产品现状。
- 人机分工贯穿岗位定位、定级和任务回放，不单独停留在口号。
- 每章使用适合该关系的横向图，而不是机械复用同一时间轴。
- “数字员工的一天”必须调用前文所有概念：Orchestration、SOP、状态机、权限、Gate、恢复、审计和考核。

## 下一步

更新设计文档并再次确认；确认后进入实现计划，不在旧章节结构上继续制作。

## 边界

本记录是一次内容结构重锚，不改变仓库默认工作流、不创建 OpenSpec 变更，也不把画像 V1.0 提升为组织制度。
