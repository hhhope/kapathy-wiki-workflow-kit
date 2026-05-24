---
title: team-knowledge-dev-workflow-lease-drift / source-learning
type: learning
canonical_object: team-knowledge-dev-workflow-lease-drift
artifact_type: source-learning
language: zh-CN
audience: agent
knowledge_level: working
layer: ops
domain: ai-workflow
ops_area: learning-capture
status: active
confidence: candidate
updated_at: 2026-05-24
ai_generated: true
derived_from:
  - /mnt/d/cloud/team-knowledge/team-knowledge/logs/20260524-092808-yan-dev-workflow-lease-drift-p4m8.md
notes_scope: 相邻仓库漂移日志学习记录。本文只记录可复用的工作流教训和采用边界，
  不把来源提升为仓库规则、OpenSpec 需求或行为资产。
---

# Team Knowledge 开发工作流 Lease 漂移 / 来源学习

## 来源

- 来源类型：例子型漂移日志。
- 来源主题：Team Knowledge 的需求开发协作与完成检查流程。
- 可复用能力类型：结构、边界、证据。
- 路由模块：`learning-capture` 的 example/reference 路线。
- 主题锚点：相邻 Team Knowledge 工作流；作为 report-wiki 工作流治理和未来
  agent 协作讨论的候选学习保留。

## 学到了什么

这份日志真正有价值的对象，不是 Team Knowledge 那个具体功能本身，而是一次
brainstorming 偏离用户目标之后的纠偏模式：

- 继续设计前，先明确写出漂移原因。
- 把有吸引力的外部参考和真正的设计中心分开。
- 发明新抽象前，先把新概念重新锚定到已有表、迁移、页面和生命周期表面。
- 保住用户的页面级要求，而不是只把后端机制讲完整。
- 在 brainstorming 转成 OpenSpec design 前，先冻结修正后的范围。

## 复用什么

| 学习点 | 本地用途 |
|---|---|
| 外部参考边界 | 把 Multica 这类例子只当作边界启发，不让它变成依赖或设计中心。 |
| 既有模型锚定 | 提出 `WorkTarget`、lease、run、binding 等概念前，先映射到项目已有数据结构。 |
| 页面级需求找回 | 后端工作流可以是对的，但如果没有建模核心页面/工作台体验，仍然会错过用户目标。 |
| 可信证据门禁 | 完成声明应依赖已链接的运行时证据，而不是某个人或工具自称完成。 |
| stale/conflict 状态 | 分支、提交、内容哈希、策略或映射变化后，已有证据应变 stale，而不是静默保持绿色。 |

## 修改什么

- 不把 Team Knowledge 的具体表名作为规则导入本仓库。
- 只把它作为工作流设计和漂移纠偏的过程学习，不作为 report-wiki 运行时行为要求。
- 把经验改写成通用设计习惯：当一个工作流有面向用户的生命周期表面时，数据模型、
  API、评估和页面信息架构必须同时留在修正后的范围内。

## 没有形式化什么

- 没有修改 `AGENTS.md`、skills、rules、OpenSpec specs 或 ADR。
- 没有主张本仓库需要 claim/lease 语义。
- 没有主张未来 report-wiki 材料工作流要实现 Git 或 MR readiness 检查。
- 没有提出 archive-ready 或 behavior-trigger 声明。

## 本地价值

以后做工作流设计 review 时，如果 agent 从一个漂亮的架构类比出发，但还没有锚定
当前仓库的真实数据模型、已接受生命周期和核心页面表面，这条记录可以作为提醒。

它也给 brainstorming 漂移识别提供了一个简短检查表：

1. 外部参考是不是变成了中心？
2. 设计是不是先发明名字，再回头读已有运行时事实？
3. 后端机制是不是挤掉了用户要求的 UI/工作台形态？
4. 实现开始前，缺失设计区是否已经列出来？
5. “提交检查”和“完成”是否被分开？

## 采用边界

采用的是纠偏模式，不是 Team Knowledge 的功能形态。若未来要晋升为仓库级行为，
需要新的 OpenSpec change 和行为回放证据；这条记录只能证明该模式帮助总结了一次
相邻仓库的漂移纠偏。

## 下一步

后续 review 工作流设计时，把它作为候选参考。如果同样的漂移模式在本仓库再次出现，
通过正常 workflow-governance 路径更新或晋升这条学习，不要直接修改行为资产。
