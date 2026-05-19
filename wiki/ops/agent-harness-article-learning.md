---
title: agent-harness-article-learning / reading-notes
type: learning
canonical_object: agent-harness-article-learning
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
domain: agent-harness
layer: ops
ops_area: learning-capture
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
  - https://mp.weixin.qq.com/s/-nXD7gp75SHeZHHhTh3lNw
related_objects:
  - learning-capture-routing
  - example-driven-capture
  - behavior-asset-governance
  - codex-global-agents-md
notes_scope: 外部 agent / harness / eval / managed agents 文章精读。按
  learning-capture -> article reference module 记录
  route、source grounding、admission gate、评分、结构化意译、可迁移学习和
  promotion boundary；不直接形成 AGENTS、skill、spec、checklist 或 repo
  policy。
---

# Agent Harness 文章精读

本页按 `.codex/skills/learning-capture/` 的 article reference module
返工。它不是
`behavior-asset-governance` 的设计正文，也不是规则发布页。

本页只做六件事：

1. 记录 learning-capture route：这是 article-shaped source learning。
2. 先做 admission gate：source access、source class、source grounding、local objective、copyright boundary。
3. 先给每篇文章打分，决定是否值得精读。
4. 保留 source-first reading notes：问题、方法、证据类型、适用前提、没有证明什么。
5. 对值得迁移的点做 evidence gate：source / claim / evidence / local usefulness / adoption boundary / status。
6. 明确哪些内容只是 candidate，不能直接写进 `AGENTS.md`、skill、spec 或 archive-ready 结论。

## Learning Capture Route

| Field | Value |
|---|---|
| Domain Skill | `learning-capture` |
| Module | article-shaped source -> `references/article.md` |
| Article Reference | `learning-capture/references/article.md` |
| Source Kind | article / blog / engineering post / research post / WeChat reference |
| User Intent | agent / harness / eval / managed-agents 外部文章精读与本地可迁移学习 |
| Non-Goal | 不做新闻摘要、raw fetch、自动 crawler、规则发布或治理正文补丁 |
| Repo Target | `wiki/ops` reading-notes |

## Admission Gate

| Gate | Result | Reason |
|---|---|---|
| Source access | pass | 9 个来源均有 URL；微信来源通过 `weixin-reader` 处理过。 |
| Source class recorded | pass | 官方工程 / 研究文章标为 primary source；微信文章标为 structure reference / secondary interpretation。 |
| Source grounding preserved | pass | 本页保留 section-level source map、line references 和 evidence notes；不保存全文快照。 |
| Local objective exists | pass | 目标是学习 agent-first harness / workflow / eval 方法，并抽取本仓库候选实践。 |
| Copyright boundary workable | pass | 本页使用结构化意译和短 source map，不保存全文原文或全文翻译。 |

## Original Source Grounding

Source artifact type: `source map with line references`。本页不保存 full
verbatim article text，不保存 full verbatim translation；官方文章以章节 / 行号
映射作为 source grounding，微信文章仅作为结构参考。

| Source | Source Class | Source Artifact | Grounding Status |
|---|---|---|---|
| OpenAI Harness Engineering | primary source | source map + line references | pass |
| Claude Common Workflow Patterns | primary source | source map + line references | pass |
| Claude Agent SDK | primary source | source map + line references | pass |
| Anthropic Diff Tool | primary source / research | source map + line references | pass |
| Anthropic Managed Agents | primary source | source map + line references | pass |
| Anthropic Harness Design | primary source | source map + line references | pass |
| Anthropic Demystifying Evals | primary source | source map + line references | pass |
| Anthropic Effective Harnesses | primary source | source map + line references | pass |
| 微信 Agent 架构选型 | structure reference / secondary interpretation | `weixin-reader` + section map | pass for structure, not primary technical evidence |

## Scoring Summary

Access date: 2026-05-06.

| Article | Source Class | Artifact | Score | Decision | Hard Cap | Reason |
|---|---|---|---:|---|---|---|
| Harness Engineering | primary source | source map | 95 | deep-read | none | 一手工程文章，直接回答 agent-legible repo、`AGENTS.md`、source of record 和 drift 问题。 |
| Common Workflow Patterns | primary source | source map | 91 | deep-read | none | 一手 workflow pattern 文章，能约束 sequential / parallel / evaluator 的选型，不只是概念介绍。 |
| Building Agents with Claude Agent SDK | primary source | source map | 88 | deep-read | none | 一手 SDK 文章，给出 agent loop、tool feedback、eval 改进方法。 |
| A Diff Tool for AI | primary source / research | source map | 76 | deep-read | none | 研究向文章，本地相关性较窄，但对 changed-behavior review 很有迁移价值。 |
| Scaling Managed Agents | primary source | source map | 83 | deep-read | none | 架构向文章，对稳定接口、harness 假设过期、session/sandbox 分离有帮助。 |
| Harness Design for Long-Running Apps | primary source | source map | 88 | deep-read | none | 实验/产品经验结合，适合学习长任务 generator/evaluator 分工和 harness 简化原则。 |
| Demystifying Evals for AI Agents | primary source | source map | 93 | deep-read | none | 直接给 eval 词汇、样本、grader、outcome/trajectory 边界，和本地验证方法强相关。 |
| Effective Harnesses for Long-Running Agents | primary source | source map | 90 | deep-read | none | 直接命中长会话、中断恢复、progress artifact、基础测试与交接问题。 |
| Agent 架构选型（微信） | structure reference / secondary interpretation | section map | 79 | deep-read as reference-shape | max 80 | 二次解读 Claude workflow 文章；技术观点回原文验证，主要学习四问法、场景矩阵和演进叙事。 |

Score band result: 全部达到 75+，但微信文章只作为 structure / method reference，不作为 primary technical evidence。

## Score Detail Matrix

说明：下表是按新版 scorecard 对既有总分做的回溯拆分，用于让分数可审计；它不是新的
外部证据来源。

| Article | Provenance /20 | Evidence /25 | Local Gain /25 | Transfer /15 | Verification /15 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Harness Engineering | 20 | 25 | 25 | 13 | 12 | 95 |
| Common Workflow Patterns | 20 | 23 | 24 | 13 | 11 | 91 |
| Building Agents with Claude Agent SDK | 20 | 22 | 23 | 12 | 11 | 88 |
| A Diff Tool for AI | 19 | 21 | 18 | 10 | 8 | 76 |
| Scaling Managed Agents | 20 | 21 | 20 | 11 | 11 | 83 |
| Harness Design for Long-Running Apps | 20 | 23 | 22 | 12 | 11 | 88 |
| Demystifying Evals for AI Agents | 20 | 24 | 24 | 13 | 12 | 93 |
| Effective Harnesses for Long-Running Agents | 20 | 23 | 23 | 13 | 11 | 90 |
| Agent 架构选型（微信） | 15 | 17 | 21 | 14 | 12 | 79 |

## Cross-Article Classification

| 分类 | 文章 | 学习对象 |
|---|---|---|
| Agent-legible repo | OpenAI Harness Engineering | repo 如何成为 agent 可读 source of record |
| Workflow selection | Claude workflow patterns, 微信结构参考 | 单 agent、skills、workflow、多 agent 的选型问题 |
| Agent loop and tool feedback | Claude Agent SDK | gather context -> act -> verify -> repeat |
| Eval and diff | Demystifying evals, Diff tool | 如何评 outcome、trajectory、source quality、behavior delta |
| Long-running harness | Effective harnesses, Harness design, Managed Agents | 跨 session 恢复、evaluator、稳定接口、假设过期 |

## 1. OpenAI — Harness Engineering

### Source

| Field | Value |
|---|---|
| Title | Harness engineering: leveraging Codex in an agent-first world |
| URL | `https://openai.com/index/harness-engineering/` |
| Author / Publisher | OpenAI |
| Published At | 2026-02-11 |
| Accessed At | 2026-05-06 |
| Source Type | article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 95 / deep-read |

### Reading Draft

**Problem.** 文章要解决的是 agent-first 开发里“模型越来越能写代码，但环境、约束、反馈和 repo 可读性跟不上”的问题。它把工程师的工作从直接写代码上移到 harness 设计：让 agent 能拿到正确上下文、使用正确工具、留下可验证 artifact。

**Method.** 核心方法是把 repo 变成 agent-legible source of record。`AGENTS.md` 不应承载百科式长规则，而应更像入口地图；真正的知识应落在 repo-local docs、tests、scripts 和结构化 artifact 中。文章还强调：文档本身不够，关键边界要靠 mechanical constraints 和 structural tests 防漂移。

**Evidence type.** OpenAI 工程经验和平台实践；可复核段落包括 `AGENTS.md` 作为目录/地图的建议（L80-L91）、repo-local artifact 的重要性（L221-L227）、文档不足与机械约束（L231-L239）、agent 复制既有模式导致漂移积累（L283-L290）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| `AGENTS.md` guidance | 常驻指令入口应指路，而不是把所有操作细节塞进默认上下文。 | L80-L91 |
| Repo as source of record | agent 真正能稳定复用的是 repo 内可检索 artifact，不是聊天记忆。 | L221-L227 |
| Docs are insufficient | 单靠文档很容易被绕过，关键约束要能被测试或结构性检查捕捉。 | L231-L239 |
| Drift accumulates | agent 会复制已有坏模式；若 repo 中坏样例可见，漂移会继续放大。 | L283-L290 |

**Applicability Conditions.** 适用于 agent 经常进入同一 repo、需要跨 session 恢复、或者规则/知识开始挤占默认上下文的场景。

**What It Does Not Prove.** 它不证明“短文件一定更好”，也不证明所有约束都要自动化；它证明的是 agent 可见环境和反馈闭环比单纯堆 prompt 更重要。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| OpenAI L80-L91 | `AGENTS.md` 类入口应像 map，不像 encyclopedia。 | 一手工程建议 | 支持 root/context 治理看 loaded context 和 source pointer，不只看行数。 | 改 root `AGENTS.md` 仍需当前 OpenSpec scope 和验证。 | accepted |
| OpenAI L221-L227 | repo-local artifact 比聊天结论更可复用。 | source-of-record 段落 | 支持文章学习必须落 wiki，而不是留在聊天。 | 不代表每个链接都建页；需有可复用学习。 | accepted |
| OpenAI L231-L239 | 关键边界需要机械可检。 | mechanical constraints / tests 段落 | 提醒未来不要把防漂移只写成口号。 | 当前没有 checker demo，不能升级成自动化要求。 | candidate |
| OpenAI L283-L290 | agent 会复制已有模式，坏样例会导致漂移。 | drift / replication 段落 | 支持定期复盘、删除诱导性坏样例。 | 本轮不新增 cleanup bot。 | candidate |

## 2. Claude — Common Workflow Patterns

### Source

| Field | Value |
|---|---|
| Title | Common workflow patterns for AI agents and when to use them |
| URL | `https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them` |
| Author / Publisher | Claude / Anthropic |
| Published At | 2026-03-05 |
| Accessed At | 2026-05-06 |
| Source Type | article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 91 / deep-read |

### Reading Draft

**Problem.** 文章要解决的是“什么时候让一个 agent 自主做，什么时候加 workflow，什么时候拆并行或 evaluator”的架构选型问题。

**Method.** 它把 workflow 看作给 agent 自主性加 checkpoint 和边界的结构，而不是替代智能。文章区分 sequential、parallel、evaluator-optimizer，并强调按任务依赖、可靠性、成本、延迟选择，而不是因为架构高级就使用。

**Evidence type.** Claude 产品/工程经验和 pattern catalog；关键段落包括 workflow 作用（L278-L285）、三类 workflow 的成本收益（L286-L299）、sequential 的适用条件（L307-L319）、parallel 的独立任务和多视角场景（L322-L339）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Workflow purpose | workflow 是边界和检查点，不是把 agent 变成脚本。 | L278-L285 |
| Pattern tradeoffs | sequential、parallel、evaluator 都有成本，不能默认越复杂越好。 | L286-L299 |
| Sequential | 如果步骤天然依赖，顺序流比多 agent 更稳。 | L307-L319 |
| Parallel | 独立任务或多视角评审适合并行。 | L322-L339 |

**Applicability Conditions.** 适用于任务边界和依赖关系能说清的场景；如果单 agent 能可靠完成，不应硬拆 workflow。

**What It Does Not Prove.** 它不证明多 agent 是默认目标，也不证明 evaluator loop 应该常驻；它只提供选型条件。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Claude L278-L285 | workflow 是给 agent 自主性加边界。 | workflow framing | 区分学习、执行、验证，不把所有事情都固化成规则。 | 不自动创建新 workflow。 | accepted |
| Claude L286-L299 | 复杂 workflow 只有在收益超过成本时才值得。 | pattern tradeoff | 防止一上来 parallel agents / evaluator loop。 | 需要可测 latency 或 quality gap 才升级。 | accepted |
| Claude L307-L319 | 能画出依赖链时，sequential 足够。 | sequential pattern | 指导文章返工先逐篇顺序处理。 | 不写成全局硬规则。 | accepted |
| Claude L322-L339 | parallel 适合独立任务或多视角评估。 | parallel pattern | 可用于后续多文章交叉 review。 | 当前未启用子 agent；先不升级。 | candidate |

## 3. Claude — Building Agents with the Claude Agent SDK

### Source

| Field | Value |
|---|---|
| Title | Building agents with the Claude Agent SDK |
| URL | `https://claude.com/blog/building-agents-with-the-claude-agent-sdk` |
| Author / Publisher | Claude / Anthropic |
| Published At | 2025-09-29 |
| Accessed At | 2026-05-06 |
| Source Type | article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 88 / deep-read |

### Reading Draft

**Problem.** 文章关注如何构建能在真实环境中行动的 agent，而不是只会回复文本的模型调用。

**Method.** 它把 agent loop 定义成 gather context、take action、verify work、repeat，并强调工具、文件、命令、lint、debug 反馈对 agent 可靠性的重要性。改进 agent 时要看失败样本，判断缺的是信息、规则、工具还是 eval set。

**Evidence type.** SDK 产品实践和设计经验；关键段落包括工具需求（L276-L281）、agent loop（L290-L296）、具体反馈机制（L350-L379）、失败分析问题集（L380-L388）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Tools | agent 需要能读写文件、运行命令、得到 lint/debug 反馈。 | L276-L281 |
| Loop | agent 可靠性来自 context、action、verification 的循环。 | L290-L296 |
| Feedback | 规则、视觉反馈、LLM judge 都是反馈工具，但适用边界不同。 | L350-L379 |
| Improvement | 失败后要问缺信息、规则、工具还是 eval。 | L380-L388 |

**Applicability Conditions.** 适用于需要 agent 实际操作 repo、文件、命令和验证的场景。

**What It Does Not Prove.** 它不证明某个 SDK 是本仓库必须采用的工具，也不证明 LLM judge 可以替代人工校准。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Claude SDK L290-L296 | agent loop 是 context -> action -> verify -> repeat。 | SDK loop 段落 | 作为文章学习和执行任务的基本闭环。 | 不直接升级成 repo policy。 | accepted |
| Claude SDK L350-L360 | 具体反馈比抽象鼓励更有用。 | feedback 段落 | 支持每个学习点必须有 evidence。 | 不新增 lint/judge，除非本地需要。 | accepted |
| Claude SDK L361-L370 | 视觉任务需要视觉反馈。 | visual feedback 段落 | 未来 HTML/report QA 可复用。 | 当前文章学习不做 UI 验证。 | candidate |
| Claude SDK L375-L379 | LLM judge 有成本和鲁棒性边界。 | evaluator caveat | 防止把另一个模型意见当最终 proof。 | judge 只能是证据之一。 | accepted |
| Claude SDK L380-L388 | 改进 agent 要看失败样本和缺口类型。 | failure-analysis 段落 | 可作为 agent 行为诊断框架。 | 尚未形成正式 checklist。 | candidate |

## 4. Anthropic — A Diff Tool for AI

### Source

| Field | Value |
|---|---|
| Title | A diff tool for AI |
| URL | `https://www.anthropic.com/research/diff-tool` |
| Author / Publisher | Anthropic Research |
| Published At | 2026-03-13 |
| Accessed At | 2026-05-06 |
| Source Type | research article |
| Retrieval Method | Web |
| Source Class | primary source / research |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 76 / deep-read |

### Reading Draft

**Problem.** 文章要解决模型行为变化难以审计的问题。传统 eval 更擅长抓已知风险，未知行为差异需要另一种高召回筛查方式。

**Method.** 它提出行为 diff 思路：不是从头审计所有行为，而是比较变化前后，把注意力集中到差异上，再由人或后续检查判断重要性。

**Evidence type.** 研究工具介绍；关键段落包括 eval 难覆盖未知风险（L18-L23）、diff 只是 screening 不是结论（L23-L24）、关注行为差异以优化审计注意力（L67-L71）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Known vs unknown risks | 传统 eval 适合已知风险；未知变化需要 diff。 | L18-L23 |
| Screening boundary | diff 只能提示差异，不等于判断差异好坏。 | L23-L24 |
| Attention routing | 有限审计注意力应先看变化区域。 | L67-L71 |

**Applicability Conditions.** 适用于版本前后行为变化、规则/skill 修改前后比较、或模型输出变化审查。

**What It Does Not Prove.** 它不证明 diff 可以代替 eval，也不证明本仓库已经有自动行为 diff 能力。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Anthropic Diff L18-L23 | 不要每次从头审全量，先看变化。 | known/unknown risk 段落 | 支持 review changed behavior 和 evidence delta。 | 不能用 diff 代替语义判断。 | accepted |
| Anthropic Diff L23-L24 | diff 是 high-recall screening。 | caveat 段落 | 防止把“发现差异”当成“找到问题”。 | 后续仍需人工/本地证据。 | accepted |
| Anthropic Diff L67-L71 | 行为差异是注意力入口。 | conclusion 段落 | 对跨版本 rule/skill review 有用。 | 当前无自动工具。 | candidate |

## 5. Anthropic — Scaling Managed Agents

### Source

| Field | Value |
|---|---|
| Title | Scaling Managed Agents: Decoupling the brain from the hands |
| URL | `https://www.anthropic.com/engineering/managed-agents` |
| Author / Publisher | Anthropic Engineering |
| Published At | 2026-04-08 |
| Accessed At | 2026-05-06 |
| Source Type | engineering article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 83 / deep-read |

### Reading Draft

**Problem.** 文章讨论 agent 平台如何避免把模型、harness、执行环境、状态和 sandbox 绑定成难维护系统。

**Method.** 它主张把 brain 和 hands 解耦：session、harness、sandbox 用稳定接口连接。这样当模型能力提升或执行假设过期时，可以替换 harness 或执行层，而不是重写整个系统。

**Evidence type.** Anthropic agent runtime / platform 架构经验；关键段落包括 harness 假设会过期（L17-L22）、稳定接口抽象（L23-L25）、状态/运行循环/执行环境不应绑定成 pet（L27-L32）、session/harness/sandbox 的隔离价值（L35-L43）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Stale assumptions | harness 里常藏着“模型做不到”的假设，这些假设会过期。 | L17-L22 |
| Stable interfaces | session、harness、sandbox 之间应靠稳定接口协作。 | L23-L25 |
| Recovery | 不把状态和执行环境绑定死，系统才可恢复、可调试。 | L27-L32 |
| Isolation | 隔离有助于凭证、安全和失败恢复。 | L35-L43 |

**Applicability Conditions.** 适用于构建 agent 平台、长期运行环境或跨任务状态管理。

**What It Does Not Prove.** 它不证明本仓库应立即设计 managed-agent 平台；当前只能迁移“假设会过期、接口要稳定”的判断。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Anthropic Managed L17-L22 | harness 假设会过期。 | stale-assumption 段落 | 防止把当前模型弱点写成永久规则。 | 不直接改 root/skill。 | accepted |
| Anthropic Managed L23-L25 | 稳定接口比实现细节更长寿。 | interface 段落 | 支持 source/session/evidence/artifact 这类稳定概念。 | 不设计平台接口。 | candidate |
| Anthropic Managed L35-L43 | session/harness/sandbox 分离提升恢复和隔离。 | isolation 段落 | 对未来运行架构有参考价值。 | 当前不改权限/沙箱架构。 | candidate |

## 6. Anthropic — Harness Design for Long-Running Application Development

### Source

| Field | Value |
|---|---|
| Title | Harness design for long-running application development |
| URL | `https://www.anthropic.com/engineering/harness-design-long-running-apps` |
| Author / Publisher | Anthropic Engineering |
| Published At | 2026-03-24 |
| Accessed At | 2026-05-06 |
| Source Type | engineering article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 88 / deep-read |

### Reading Draft

**Problem.** 文章描述长任务应用开发中 agent 容易自评过乐观、上下文焦虑、质量标准不稳定的问题。

**Method.** 它使用 planner / generator / evaluator 分工。planner 定义 sprint 和 testable behaviors；generator 生成应用；evaluator 按 contract criteria 用 browser/test 工具检查。文章最后提醒 harness 不应无限增殖，每个组件都编码模型能力假设，应逐个删减并观察效果。

**Evidence type.** Anthropic 前端应用生成实验和 harness 设计经验；关键段落包括问题定义（L24-L34）、testable behaviors（L96-L97）、evaluator logs 和 granular criteria（L115-L122）、harness 组件会过期并应简化（L126-L138）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Failure mode | 长任务里 agent 常高估自己完成质量。 | L24-L34 |
| Planner contract | planner 要把目标拆成可测试行为。 | L96-L97 |
| Evaluator | evaluator 用具体 criteria 和日志让失败可行动。 | L115-L122 |
| Harness simplification | harness 不是越多越好，组件要能删减。 | L126-L138 |

**Applicability Conditions.** 适用于复杂、长时间、主观质量高、需要外部评估的开发任务。

**What It Does Not Prove.** 它不证明每个任务都需要 evaluator，也不证明本仓库应新增 evaluator agent。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Anthropic Harness Design L31-L34 | 自评偏乐观，复杂任务需要外部评价。 | failure 段落 | 支持高风险变更用 review/evaluation。 | 不默认启用 evaluator agent。 | candidate |
| Anthropic Harness Design L96-L122 | testable behavior contract 让评价更具体。 | planner/evaluator 段落 | 可用于未来高风险输出验收。 | 当前不新增模板。 | candidate |
| Anthropic Harness Design L121-L122 | evaluator 需要人类校准。 | tuning caveat | 防止 LLM judge 权威化。 | evaluator 输出只是证据之一。 | accepted |
| Anthropic Harness Design L126-L138 | harness 组件会过期，应逐个删减。 | simplification 段落 | 支持渐进式治理，不无限增殖。 | 不在本页决定删资产。 | accepted |

## 7. Anthropic — Demystifying Evals for AI Agents

### Source

| Field | Value |
|---|---|
| Title | Demystifying evals for AI agents |
| URL | `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents` |
| Author / Publisher | Anthropic Engineering |
| Published At | 2026-01-09 |
| Accessed At | 2026-05-06 |
| Source Type | engineering article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 93 / deep-read |

### Reading Draft

**Problem.** 文章要解决的是 agent eval 容易概念混乱：到底评 task、trial、trajectory、transcript、outcome 还是 grader。

**Method.** 它先定义 eval 词汇，再按 research agents、computer-use agents 等场景说明 eval 应该看什么。它强调从真实失败和手工检查开始收集样本；任务规格要清楚；grader 检查项必须能从题面或输出中判断；运行环境要隔离。

**Evidence type.** Anthropic eval 工程方法；关键段落包括 eval 术语（L30-L36）、research agent 的 groundedness/coverage/source quality（L199-L205）、computer-use outcome（L206-L210）、从真实失败开始收集样本（L222-L232）、任务规格清晰性（L234-L237）、隔离环境（L242-L249）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Eval vocabulary | task、trial、grader、transcript、outcome、harness 不是一回事。 | L30-L36 |
| Research eval | 研究型任务要看 groundedness、coverage、source quality。 | L199-L205 |
| Computer-use eval | 操作型 agent 要看环境中的实际结果。 | L206-L210 |
| Dataset start | 先从真实失败和人工检查收集样本。 | L222-L232 |
| Task clarity | 模糊任务会污染 eval。 | L234-L237 |
| Isolation | trial 环境应隔离，避免共享状态污染。 | L242-L249 |

**Applicability Conditions.** 适用于需要验证 agent 工作质量、文章学习质量、UI 操作结果、跨 session 恢复结果的场景。

**What It Does Not Prove.** 它不证明必须马上建立 20-50 个样本集，也不证明自动 grader 可以替代人工验收。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Anthropic Evals L30-L36 | eval 词汇必须区分。 | vocabulary 段落 | 避免把 harness、grader、outcome 混用。 | 不独立写成 spec。 | accepted |
| Anthropic Evals L199-L205 | research eval 要看 groundedness / coverage / source quality。 | research-agent 段落 | 直接适用于文章精读质量。 | 仍是人工 wiki 证据，不是自动 eval。 | accepted |
| Anthropic Evals L206-L210 | computer-use eval 看真实或 sandboxed outcome。 | computer-use 段落 | 指导未来 UI/browser 验证。 | 本轮不运行 GUI eval。 | candidate |
| Anthropic Evals L222-L232 | 初始 eval 可从真实失败开始。 | dataset 段落 | 可把 drift 案例转 fixture。 | 尚未建立样本集。 | candidate |
| Anthropic Evals L234-L237 | 模糊任务会污染 eval。 | task clarity 段落 | 支持先澄清学习 vs 治理。 | 不把所有模糊都升级成流程规则。 | accepted |

## 8. Anthropic — Effective Harnesses for Long-Running Agents

### Source

| Field | Value |
|---|---|
| Title | Effective harnesses for long-running agents |
| URL | `https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents` |
| Author / Publisher | Anthropic Engineering |
| Published At | 2025-11-26 |
| Accessed At | 2026-05-06 |
| Source Type | engineering article |
| Retrieval Method | Web |
| Source Class | primary source |
| Source Artifact Type | source map + line references |
| Source Artifact Path / Note | 本节 Structured Translation Notes 和 Evidence Notes |
| Score | 90 / deep-read |

### Reading Draft

**Problem.** 文章解决长会话 agent 的恢复和交接问题：context window 会重置，新 session 没有前文记忆，agent 容易过早宣告完成或留下不可恢复状态。

**Method.** Anthropic 的方案是 initializer 建启动脚本、progress file 和初始 commit；后续 agent 每轮读 progress、日志、测试，再做增量更新。git commit 和 progress file 共同形成恢复机制；基础端到端测试防止“看起来完成但不可用”。

**Evidence type.** Anthropic 长任务 harness 经验；关键段落包括长会话失败模式（L19-L30）、initializer/progress/commit（L31-L34）、git/progress 恢复（L60-L61）、端到端测试防假完成（L62-L70）、每轮 get bearings（L71-L101）。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Long-session failure | session 重置会让 agent 丢状态、假完成。 | L19-L30 |
| Initializer | 用启动脚本、progress file、commit 建恢复入口。 | L31-L34 |
| Recovery | git commit 和 progress file 是恢复锚点。 | L60-L61 |
| E2E tests | 基础端到端测试比只看代码更能防假完成。 | L62-L70 |
| Bearings | 每轮开始先读路径、日志、progress、测试。 | L71-L101 |

**Applicability Conditions.** 适用于跨轮、跨 context、长时间执行的代码/文档/治理任务。

**What It Does Not Prove.** 它不证明每个小学习动作都要 init.sh 或每步 commit；它证明的是长任务需要恢复 artifact。

### Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Anthropic Effective L19-L30 | 长任务失败常来自 session 断裂和假完成。 | problem 段落 | 支持中断后查 git/log/artifact。 | 不改全局 AGENTS。 | accepted |
| Anthropic Effective L31-L34, L60-L61 | progress file + git commit 是恢复机制。 | initializer/recovery 段落 | 支持 repo-visible trace 和小步提交。 | 不强制非代码学习每小节提交。 | accepted |
| Anthropic Effective L62-L70 | 基础 E2E 防假完成。 | testing 段落 | 对应用开发验证有用。 | 当前文章学习只做 source/evidence 检查。 | candidate |
| Anthropic Effective L71-L101 | session 启动应先 get bearings。 | startup 段落 | 支持恢复时先查 pwd/git/progress。 | 已有 root/repo 规则覆盖，不重复新增。 | accepted |

## 9. 微信参考 — Agent 架构选型

### Source

| Field | Value |
|---|---|
| Title | Agent架构选型：好架构都是逼出来的 |
| URL | `https://mp.weixin.qq.com/s/-nXD7gp75SHeZHHhTh3lNw` |
| Author / Publisher | tiny / 微信公众号 |
| Published At | 2026-04-15 |
| Accessed At | 2026-05-06 |
| Source Type | WeChat article |
| Retrieval Method | `weixin-reader` |
| Source Class | structure reference / secondary interpretation |
| Source Artifact Type | section map via `weixin-reader` |
| Source Artifact Path / Note | 本节 Structured Translation Notes；技术主张回 Claude 原文验证 |
| Score | 79 / deep-read as reference-shape |

### Reading Draft

**Problem.** 这篇文章要把 Claude workflow pattern 的架构选择讲成业务决策问题：单 agent、skills、workflow、多 agent 不是技术炫技，而是被控制度、复杂度、资源和专业度逼出来的选择。

**Method.** 它采用“四问法”：控制度、问题域复杂度、资源约束、领域专业度。之后用四种架构场景表和演进案例解释为什么应从简单方案开始，逐步升级。

**Evidence type.** 二次解读和结构化表达，原文技术依据指向 Claude workflow pattern 和 Anthropic report。它的价值主要是表达结构、读者引导和选型框架，不是 primary technical evidence。

**Structured Translation Notes.**

| Section | Paraphrased Meaning | Evidence Notes |
|---|---|---|
| Four questions | 用控制度、复杂度、资源、专业度把架构选择从抽象讨论拉回业务约束。 | 微信正文 01-04 |
| Architecture matrix | 单 agent、串行、并行、多 agent 各自有适用场景。 | 微信正文 05 |
| Evolution narrative | 架构升级来自真实瓶颈，而不是预先追求复杂。 | 微信正文 06 |
| Skills option | 多领域问题不一定要多 agent，单 agent + skills 可能足够。 | 微信正文 04 |

**Applicability Conditions.** 适合作为中文学习页的表达结构参考：先用问题框架组织读者，再给矩阵和演进路径。

**What It Does Not Prove.** 它不替代 Claude 原文；所有技术主张要回到 Claude workflow pattern 或 Anthropic report 验证。

### Transferable Learning

| Source   | Claim                         | Evidence       | Local Usefulness                  | Adoption Boundary           | Status    |
| -------- | ----------------------------- | -------------- | --------------------------------- | --------------------------- | --------- |
| 微信 01-04 | 架构选型可先问四个业务约束问题。              | 文章结构           | 可复用到中文 wiki 学习页和决策说明。             | 技术判断仍回官方原文验证。               | accepted  |
| 微信 05    | 场景矩阵比散点总结更容易学会。               | 四架构矩阵          | 改善本页 cross-article synthesis 的表达。 | 不照搬文字或图片。                   | accepted  |
| 微信 06    | 架构演进应被瓶颈推动。                   | 演进案例           | 支持“先简单，再升级”的学习表达。                 | 案例是说明性，不作为本仓库证据。            | candidate |
| 微信 04    | 单 agent + skills 是多领域问题的中间选项。 | skills section | 直接回应“是否一遇到问题就多 agent/新 skill”。    | 仍需结合 Claude 原文和本地 evidence。 | candidate |

## Current Accepted Learnings

1. Agent 可用知识必须 repo-visible、可检索、可恢复；聊天里的结论不是稳定资产。
2. `AGENTS.md` 类入口更适合作 map，而不是把所有细节常驻加载。
3. 工作流复杂度要从 simplest viable pattern 开始，只有可测收益时才升级。
4. 对文章学习而言，claim/evidence 表只是 transfer extraction；精读必须先有 source-first reading draft。
5. 验证要看 outcome、source quality、changed behavior 和恢复证据，不只看文本是否自洽。
6. evaluator / LLM judge 有价值，但需要人类校准，不能作为单独权威。
7. harness / workflow / rule 里的每个组件都编码模型能力假设，必须允许随着模型变化被删减。
8. 中文学习材料可学习结构和表达，但技术主张必须回到 primary source。

## Candidate Only

- 自动 doc-gardening / cleanup bot：有外部证据，但本仓库没有运行 demo。
- parallel agents / evaluator-optimizer loop：有模式说明，但当前学习任务未证明需要并行。
- 自动 behavior diff 工具：diff 思想有用，但尚无本地工具或样本集。
- 20-50 个 eval dataset：方向成立，但当前还没有本地样本收集。
- session / harness / sandbox 平台解耦：架构思想成立，但超出本仓库当前工具边界。
- 单 agent + skills 的架构选型表：适合继续学习，但不能替代本地 routing evidence。

## Rejected Moves

- 不把这些文章作为 `behavior-asset-governance` 正文补丁。
- 不把文章句子直接写进 root `AGENTS.md`、repo `AGENTS.md`、skill 或 spec。
- 不因为文章提到 evaluator 就新增 evaluator agent。
- 不因为文章提到 harness 就新建自动 harness。
- 不把微信二次解读当 primary technical evidence。
- 不用"外部大厂这么做"替代本地 RED/GREEN、demo、git 对照或运行证据。

## Next Action

如果后续要把某条学习升级成行为资产，必须另开明确任务，并补足以下至少一种证据：

- 本地 RED/GREEN fixture；
- demo 或命令 / 手工回放记录；
- git-like 项目对照；
- 明确的 before / after behavior delta。
