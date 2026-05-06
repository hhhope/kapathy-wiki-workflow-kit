---
title: agent-harness-article-learning / reading-notes
type: learning
canonical_object: agent-harness-article-learning
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: candidate
updated_at: 2026-05-06
ai_generated: true
derived_from:
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
related_objects:
  - example-driven-capture
  - behavior-asset-governance
  - codex-global-agents-md
notes_scope: 外部 agent / harness / eval / managed agents 文章精读。这里只记录学习、
  证据、取舍和候选迁移边界；不直接形成 AGENTS、skill、spec、checklist 或 repo policy。
---

# Agent Harness 文章精读

本页是新开的学习专题，不是 `behavior-asset-governance` 的设计正文。它只回答：

- 每篇文章讲了什么；
- 哪些点对我们有用；
- 有用点的证据在哪里；
- 本地是否采纳、候选、拒绝；
- 若要升级成行为资产，下一步还缺什么证据。

## Evidence Gate

"有用"不等于"立刻写规则"。本页采用同一证据口径：

| 字段 | 含义 |
|---|---|
| source | 文章 URL 和可复核行号 |
| claim | 文章能支撑的窄结论 |
| local usefulness | 对当前 repo / agent 工作方式可能有帮助的原因 |
| status | `accepted` / `candidate` / `rejected` |
| adoption boundary | 不能越过的本地边界 |

## Cross-Article Classification

| 分类 | 文章 | 当前用途 |
|---|---|---|
| Agent-legible repo | OpenAI Harness Engineering | 学习如何让 repo 成为 agent 可读 source of record |
| Workflow selection | Claude workflow patterns | 学习什么时候用 sequential / parallel / evaluator-optimizer |
| Agent loop and tool feedback | Claude Agent SDK | 学习 gather context → act → verify → repeat 的最小闭环 |
| Eval design | Demystifying evals, Diff tool | 学习如何验证行为差异、结果和轨迹 |
| Long-running harness | Effective harnesses, Harness design, Managed Agents | 学习跨 session、评估器、稳定接口与假设过期问题 |

## 1. OpenAI — Harness Engineering

Source: `https://openai.com/index/harness-engineering/`，published 2026-02-11。

文章核心不是"把 AGENTS.md 写短"，而是把工程师工作上移到环境、约束、反馈闭环和 agent-legible repo 设计。它明确说 large instruction manual 会挤占上下文、腐烂、难验证，并主张把 `AGENTS.md` 做成 table of contents，repo docs 做 source of record（L80-L91）。它还强调 repository-local artifacts 是 agent 真正可见的知识（L221-L227），文档本身不足以保持架构一致，需要机械约束和 structural tests（L231-L239），并指出 agent 会复制已有坏模式，漂移需要持续清理而不是偶尔人工 cleanup（L283-L290）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| `AGENTS.md` 应是 map，不是 encyclopedia | L80-L91 | 能解释为什么 root context 治理不能只看单文件行数，而要看默认加载上下文和 source pointer | accepted | 只能作为学习结论；改 root `AGENTS.md` 仍需当前 OpenSpec scope 和验证 |
| repo-local artifact 比聊天 / 外部文档更可被 agent 使用 | L221-L227 | 支持"学习要进 wiki"而不是只留在对话里 | accepted | 不代表所有外部文章都自动新建页面；必须已有可复用学习 |
| 文档不足，关键边界应机械可检 | L231-L239 | 提醒不要把防漂移只写成口号 | candidate | 当前没有 checker / lint 证据，不能升级成强制自动化要求 |
| agent 会复制已有坏模式，漂移会积累 | L283-L290 | 支持定期复盘与差异审查 | candidate | 不在本轮新增 cleanup bot 或后台任务 |

## 2. Anthropic — Scaling Managed Agents

Source: `https://www.anthropic.com/engineering/managed-agents`，published 2026-04-08。

文章核心是把 agent 的 brain 与 hands 解耦：harness 会编码"模型还做不到什么"的假设，而这些假设会随着模型能力变化而过期（L17-L22）。Anthropic 把 session、harness、sandbox 抽象成可替换接口（L23-L25），避免把状态、运行循环和执行环境绑定成不可丢失的 "pet"（L27-L32）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| harness 假设会过期，应被定期质疑 | L17-L22 | 学习页可以把"当前有效"与"长期规则"分开 | accepted | 不把今天的模型弱点固化进 permanent root rule |
| 稳定接口比具体 harness 实现更长寿 | L23-L25 | 支持记录 source / session / evidence / artifact 这些稳定概念 | candidate | 本仓库不设计 managed-agent 平台接口 |
| session / harness / sandbox 解耦提升恢复和调试性 | L27-L32 | 可作为 future runtime architecture 的参考 | candidate | 当前只是知识学习，不改执行架构或权限模型 |

## 3. Claude — Common Workflow Patterns

Source: `https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them`，published 2026-03-05。

文章把 workflow 定义为给 agent 自主性加结构、checkpoint 和边界，而不是替代 agent 的判断（L278-L285）。它区分 sequential、parallel、evaluator-optimizer 三类，并明确每类都有成本收益权衡（L286-L299）。它还提醒：如果一个 agent 就能可靠完成，就不要强拆成 workflow；只在自然依赖或可靠性需要时拆分（L307-L319）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| workflow 是给自主性加边界，不是替代自主性 | L278-L285 | 帮助区分"学习过程"和"治理规则"两层 | accepted | 不自动创建新 workflow 资产 |
| 默认从最简单 pattern 开始 | L286-L299 | 防止一上来加 parallel agents / evaluator loop | accepted | 只有可测 latency 或 quality gap 才升级 |
| sequential 适合天然依赖链，单 agent 能做就别拆 | L307-L319 | 指导文章精读先用逐篇顺序流 | accepted | 不把顺序流写成全局硬规则 |
| parallel 适合独立任务和多维 review | L322-L339 | 可作为后续多文章交叉复核候选 | candidate | 本轮不启用子 agent；没有明确并行收益证据 |

## 4. Claude — Building Agents with the Claude Agent SDK

Source: `https://claude.com/blog/building-agents-with-the-claude-agent-sdk`，published 2025-09-29。

文章把 Claude Agent SDK 的基本循环说成 `gather context -> take action -> verify work -> repeat`（L290-L296），强调 agent 需要像人一样有文件、命令、lint、debug 等工具（L276-L281）。它还把可靠性建立在具体反馈上：规则、视觉反馈、LLM judge 各有适用场景和成本（L350-L379）；改进 agent 要看失败样本，问它是否缺信息、规则、工具或 eval set（L380-L388）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| agent loop 是 gather context / act / verify / repeat | L290-L296 | 可作为学习记录的基本检查顺序 | accepted | 不把 SDK 文章直接升级成 repo policy |
| 具体反馈优先于抽象鼓励 | L350-L360 | 支持每个有用点必须绑定 evidence | accepted | 不新增 lint / judge，除非有本地测试需求 |
| 视觉任务需要视觉反馈 | L361-L370 | 对未来 HTML / report QA 有用 | candidate | 当前文章学习不做 UI 验证 |
| LLM judge 有成本和鲁棒性限制 | L375-L379 | 防止滥用 evaluator | accepted | 不能把另一模型意见当最终 proof |
| 失败分析要问缺信息、规则、工具还是 eval set | L380-L388 | 可作为后续 agent 行为诊断框架 | candidate | 还未在本仓库形成正式 checklist |

## 5. Anthropic — A Diff Tool for AI

Source: `https://www.anthropic.com/research/diff-tool`，published 2026-03-13。

文章讨论的是模型行为 diff，不是工程 diff 工具。可迁移的学习是：全量审计未知风险成本太高，diff 能把注意力引向变化区域（L18-L23）；但 diff 不是银弹，只是 high-recall screening，需要后续验证（L23-L24）。结论再次强调关注行为差异可以更聪明地审计变化（L67-L71）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| 不要每次从头审计全量语料，先看变化 | L18-L23 | 支持 review 关注 changed behavior 和 evidence delta | accepted | 不能用 diff 代替语义判断 |
| diff 只是 high-recall screening，不是结论 | L23-L24 | 防止把"发现差异"误当"找到问题" | accepted | 后续仍需本地证据和人工判断 |
| 行为差异是有限注意力的优先入口 | L67-L71 | 对跨版本 agent / rule / skill review 有用 | candidate | 当前没有自动行为 diff 工具 |

## 6. Anthropic — Harness Design for Long-Running Application Development

Source: `https://www.anthropic.com/engineering/harness-design-long-running-apps`，published 2026-03-24。

文章用前端应用生成实验说明：长任务中，context anxiety、self-evaluation 偏乐观、主观质量难打分都会让单 agent 失败（L24-L34）。解决方式是 planner / generator / evaluator 分工、每个 sprint 定义 testable behaviors（L96-L97），并用 evaluator 按 contract criteria 跑 Playwright、产出具体 fail（L115-L122）。后半段更重要：harness 很容易变重，每个组件都编码了模型做不到的假设，应一个组件一个组件地删减并观察影响（L126-L138）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| 自评偏乐观，复杂任务需要外部评价视角 | L31-L34 | 解释为什么关键验证可用另一个 reviewer | candidate | 不默认启用 evaluator agent |
| testable behavior contract 能让评价更具体 | L96-L97, L115-L120 | 可用于未来高风险输出验收 | candidate | 本轮不新增 contract 模板 |
| evaluator 需要调参，人类校准不可省 | L121-L122 | 防止把 LLM judge 当可靠权威 | accepted | evaluator 输出只能是证据之一 |
| harness 组件会过期，应逐个删减并测影响 | L126-L138 | 支持渐进式而非无限增殖 | accepted | 不在学习页里决定删哪个资产 |

## 7. Anthropic — Demystifying Evals for AI Agents

Source: `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents`，published 2026-01-09。

文章给了 agent eval 的词汇和路线图：task、trial、grader、transcript、outcome、evaluation harness 各自不同（L30-L36）。对 research agents，质量要看 groundedness、coverage、source quality，并常需要与专家判断校准（L199-L205）。对 computer-use agents，必须在真实或 sandboxed 环境里看结果，而不仅看过程（L206-L210）。从零开始做 eval 时，建议先从真实失败和手工检查中收集 20-50 个任务（L222-L232），任务规格要清楚，grader 检查项必须在题面里可见（L234-L237），并用隔离环境减少噪声（L242-L249）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| eval 要区分 task / trial / grader / transcript / outcome / harness | L30-L36 | 给学习和验证讨论提供准确词汇 | accepted | 不把词汇表变成正式 spec |
| research eval 要看 groundedness / coverage / source quality | L199-L205 | 直接适用于本次文章精读质量 | accepted | 当前仍是人工 wiki 证据，不是自动 eval |
| computer-use eval 看真实或 sandboxed outcome | L206-L210 | 指导未来 UI / browser 任务验证 | candidate | 本轮不运行 GUI eval |
| 初始 eval 可从真实失败和手工检查开始 | L222-L232 | 可用于后续把 drift 案例转成 fixture | candidate | 尚未建立 20-50 样本集 |
| ambiguous task 会污染 eval | L234-L237 | 支持先澄清"学习 vs 治理" | accepted | 不把所有模糊都升级成流程规则 |
| trial 环境应隔离，避免共享状态污染 | L242-L249 | 对后续自动测试有用 | candidate | 当前 wiki 学习不涉及运行环境 |

## 8. Anthropic — Effective Harnesses for Long-Running Agents

Source: `https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents`，published 2025-11-26。

文章的问题定义很贴近长会话：agent 跨多个 context window 工作时，新 session 没有记忆，compaction 不够，容易半路留下未记录状态或过早宣告完成（L19-L30）。Anthropic 的方案是 initializer agent 建 `init.sh`、progress file 和初始 git commit，后续 coding agent 每轮只做增量并留下结构化更新（L31-L34）。文章还强调 git commit 和 progress file 能让 agent 恢复状态（L60-L61），显式要求端到端测试能减少"标记完成但功能不可用"（L62-L70），每轮开始先读路径、日志、progress 和基础测试（L71-L101）。

| claim | evidence | local usefulness | status | adoption boundary |
|---|---|---|---|---|
| 长任务失败常来自跨 session 记忆断裂和过早完成 | L19-L30 | 支持每次中断后必须看 git/log/artifact | accepted | 本页不改全局 AGENTS |
| progress file + git commit 是恢复机制 | L31-L34, L60-L61 | 支持 repo-visible trace 和小步提交 | accepted | 不强制所有非代码学习都提交每个小节 |
| 基础端到端测试比只看代码更能防止假完成 | L62-L70 | 对应用开发验证有用 | candidate | 当前文章学习只需 source/evidence 检查 |
| session 启动应先 get bearings | L71-L101 | 支持恢复时先查 pwd/git/progress | accepted | 已有 root / repo 规则覆盖，不重复新增规则 |

## Current Accepted Learnings

这些是本页当前认为可以复用、但仍不直接升级成规则的学习结论：

1. Agent 可用的知识必须 repo-visible、可检索、可恢复；聊天里的结论不是稳定资产。
2. `AGENTS.md` 类入口更适合作 map，而不是把所有细节常驻加载。
3. 工作流复杂度要从 simplest viable pattern 开始，只有可测收益时才升级。
4. 验证必须看 outcome、source quality、changed behavior 和恢复证据，不只看文本是否自洽。
5. evaluator / LLM judge 有价值，但需要人类校准，不能作为单独权威。
6. harness / workflow / rule 里的每个组件都编码模型能力假设，必须允许随着模型变化被删减。

## Candidate Only

以下学习尚不能升级：

- 自动 doc-gardening / cleanup bot：有外部证据，但本仓库没有运行 demo。
- parallel agents / evaluator-optimizer loop：有模式说明，但当前学习任务未证明需要并行。
- 自动 behavior diff 工具：diff 思想有用，但尚无本地工具或样本集。
- 20-50 个 eval dataset：方向成立，但当前还没有本地样本收集。
- session / harness / sandbox 平台解耦：架构思想成立，但超出本仓库当前工具边界。

## Rejected Moves

- 不把这些文章作为 `behavior-asset-governance` 正文补丁。
- 不把文章句子直接写进 root `AGENTS.md`、repo `AGENTS.md`、skill 或 spec。
- 不因为文章提到 evaluator 就新增 evaluator agent。
- 不因为文章提到 harness 就新建自动 harness。
- 不用"外部大厂这么做"替代本地 RED/GREEN、demo、git 对照或运行证据。

## Next Step

如果后续要把某条学习升级成行为资产，必须另开明确任务，并补足以下至少一种证据：

- 本地 RED/GREEN fixture；
- demo 或命令 / 手工回放记录；
- git-like 项目对照；
- 明确的 before / after behavior delta。
