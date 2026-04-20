# Personal Ops 总览

这一层不是长期专题知识，而是个人工作流的操作层。

## 页面类型

- `intake`：新输入、新行为、新事件的落地点
- `intake` 也是 `openspec-explore` 的默认留痕容器；进入探索前先创建或更新对应 trace
- `handoff mode`：当会话里同一个北极星反复牵引讨论时，agent 应切换到持续承接，而不是继续当作离散问答
- `example-driven capture`：当外部 repo、README 或聊天例子已经产出可复用学习时，agent 应默认留下 wiki 记录
- `focus-thread`：当前主线与正在推进的关键主题
- `reminder`：待办、提醒、阻塞和 stale 项
- `codex-handoff`：已经成熟到可以交给 Codex 执行的研发任务

## 当前入口

- [主线面板](main-thread.md)
- [提醒面板](reminders.md)
- [项目管理周推进循环](project-management-weekly-loop.md)
- [Codex Handoff 规则](codex-handoff-rules.md)
- [conversation-handoff / method](conversation-handoff-mode.md)
- [例子驱动的 Wiki 留痕](example-driven-wiki-capture.md)
- [分歧管理方法](disagreement-management-method.md)
- [Agent-Readable Wiki Naming Model](agent-readable-wiki-naming-model.md)
- [Agent-Readable Wiki Frontmatter](agent-readable-wiki-frontmatter.md)
- [Agent-Readable Wiki Graph Extraction](agent-readable-wiki-graph-extraction.md)
- [Agent-Readable Wiki Relation Analysis](agent-readable-wiki-relation-analysis.md)
- [Agent-Readable Wiki Semantic Scoring](agent-readable-wiki-semantic-scoring.md)
- [Agent-Readable Wiki Utilization Layer](agent-readable-wiki-utilization-layer.md)
- [Agent-Readable Wiki Runtime Context](agent-readable-wiki-runtime-context.md)
- [Agent-Readable Wiki Runtime Context Source Integration](agent-readable-wiki-runtime-context-source-integration.md)
- [Agent-Readable Wiki Runtime Auto Routing](agent-readable-wiki-runtime-auto-routing.md)
- [Agent-Readable Wiki Context Injection](agent-readable-wiki-context-injection.md)
- [Agent-Readable Wiki Self-Directed Execution](agent-readable-wiki-self-directed-execution.md)
- [分歧管理 Replay Harness](disagreement-management-replay-harness.md)
- [分歧管理 Replay 验证 2026-04-20](disagreement-management-replay-validation-2026-04-20.md)
- [例子驱动留痕运行时验证 2026-04-18](example-driven-capture-runtime-validation-2026-04-18.md)
- [Scope Drift 复盘](scope-drift-retro.md)
- [Agent 治理 gate 缺口复盘 2026-04-18](agent-governance-gate-gap-retro-2026-04-18.md)
- [gstack 与 larksuite CLI 学习复盘 2026-04-18](gstack-lark-learning-retro-2026-04-18.md)
- [Karpathy Skills 学习复盘 2026-04-16](karpathy-skills-learning-retro-2026-04-16.md)

## 样例链路

- [sample-intake](sample-intake.md)
- [sample-explore-trace](sample-explore-trace.md)
- [conversation-handoff / sample](sample-handoff-topic.md)
- [sample-disagreement-retro](sample-disagreement-retro.md)
- [sample-focus-thread](sample-focus-thread.md)
- [sample-reminder](sample-reminder.md)
- [sample-codex-handoff](sample-codex-handoff.md)

## 当前真实记录

- [涅槃项目周推进 intake 2026-04-13](nirvana-weekly-intake-2026-04-13.md)
- [涅槃项目本周跟进提醒 2026-04-13](nirvana-weekly-reminder-2026-04-13.md)
- [Agent 治理 gate 缺口探索 2026-04-18](agent-governance-gate-gap-explore-2026-04-18.md)

## 推荐流转

1. 新材料或新行为先进入 intake。
2. `openspec-explore` 先检查同主题 trace，存在则更新，不存在则新建。
3. 如果用户在当前会话里反复把讨论拉回同一个北极星，agent 进入 `handoff mode`。
4. handoff mode 先维护 north star、constraints、failure modes、preferences、disagreements、open questions 和 repo targets。
5. 如果外部 repo、README 或聊天例子已经产出可复用学习，agent 在同轮默认写 wiki 记录，不等用户再提醒。
6. 如果流程级分歧正在做目标校准，先按“分歧管理方法”保留分歧材料，再判断是否进入 retro、ADR 或 formal spec。
7. explore trace 只负责打开问题，不等于正式 OpenSpec change。
8. 项目管理类周推进材料先走“周推进循环”，再判断是否进入 reminder。
9. 真正需要推进的事项进入 reminder。
10. 明确属于研发执行的待办，再晋升为 Codex handoff。

## 约束

- intake 是入口，不等于主线
- explore trace 是入口，不等于 proposal / design / tasks
- reminder 是动作层，不等于来源页
- Codex handoff 只接收研发任务，不接收泛化待办
