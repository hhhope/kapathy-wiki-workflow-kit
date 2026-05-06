---
title: agent-harness-article-learning / intake
type: intake
canonical_object: agent-harness-article-learning
artifact_type: intake
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: candidate
updated_at: 2026-05-06
ai_generated: true
related_objects:
  - example-driven-capture
  - behavior-asset-governance
derived_from:
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
notes_scope: agent / harness / eval / managed agents 外部文章精读专题的目录入口。
  本页记录要学什么、为什么学、怎么读；不承载逐篇结论，也不把文章结论直接升级成
  AGENTS、skill、spec 或 repo policy。
---

# agent-harness-article-learning / intake

## Trigger Question

用户要求对一组 agent / harness / eval / managed agents 文章逐篇精读，并指出：

- 这是新开的学习专题，不是继续塞进既有 behavior-asset governance 框架；
- 当前动作是学习，不是治理；
- 所谓"有用"必须走已确认的证据约束；
- `intake` 应该像目录，先说明要学什么，而不是直接替代精读页。

## Learning Directory

本专题要学的是 agent-first 工作方式里的可迁移工程经验，而不是给现有治理框架找
背书。

| 学习方向 | 文章 | 主要问题 |
|---|---|---|
| Agent-legible repo | OpenAI Harness Engineering | agent 能读懂的 repo 应该长什么样？ |
| Workflow selection | Claude workflow patterns | sequential / parallel / evaluator-optimizer 何时值得用？ |
| Agent loop and tool feedback | Claude Agent SDK | agent 的最小闭环和反馈机制是什么？ |
| Behavior diff | Anthropic Diff Tool | 如何只看变化，而不是每次从头审计？ |
| Managed agent architecture | Anthropic Managed Agents | 哪些 harness 假设会过期，稳定接口是什么？ |
| Long-running harness design | Anthropic Harness Design | 长任务里 planner / generator / evaluator 如何分工？ |
| Agent eval design | Anthropic Demystifying Evals | agent eval 应该评 outcome、trajectory 还是 rubric？ |
| Long-running session recovery | Anthropic Effective Harnesses | 跨 context/session 的恢复和进度交接怎么做？ |

## Reading Method

文章学习分两层，不能混成一张表。

第一层是**读懂文章**，每篇至少回答：

- 这篇文章要解决什么问题？
- 它的方法、架构或流程是什么？
- 它给出的证据是什么类型：实验、案例、运行日志、产品经验、研究结果？
- 它的适用前提是什么？
- 它没有证明什么？

第二层是**抽取可迁移点**。只有当文章里某个点可能影响本仓库或个人 agent
工作方式时，才进入证据门：

| 字段 | 角色 |
|---|---|
| source | 来源定位字段：URL、发布时间、可复核段落 / 行号 |
| claim | 从文章中抽出的窄结论，不是文章全文摘要 |
| evidence | 支撑 claim 的原文位置或文章里的实验 / 案例 |
| local usefulness | 为什么这个点可能对我们有用 |
| adoption boundary | 不能直接迁移、不能升级成规则的边界 |
| status | 当前迁移状态：`accepted` / `candidate` / `rejected` |

所以这六个字段**不是学习要点本身**。它们是把学习要点变成可审计候选项时的
元数据。真正的学习要点仍然是：问题、方法、证据、适用前提、不可迁移边界。

## Open Questions

- 逐篇精读是否需要继续拆成每篇独立页面，还是当前专题页分节足够？
- 哪些 `candidate` 后续值得做本地 RED/GREEN 或 demo？
- 是否要把现有 pre-SOP 精读页逐篇补成新模板：评分、结构化翻译笔记、证据门和
  promotion boundary。

## Next Step

文章学习 SOP 已经固化到
`.codex/skills/article-learning-capture/`，逐篇精读初版落在
[agent-harness-article-learning.md](agent-harness-article-learning.md)。后续同类文章
学习先走 skill 的 scorecard 和 wiki template；若要把某条学习升级成行为资产，
需要另开明确任务，并补本地 RED/GREEN、demo、git 对照或 before / after behavior
delta。
