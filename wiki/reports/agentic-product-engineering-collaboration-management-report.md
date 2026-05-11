---
artifact_type: report
title: AI Agent 时代，产研协作从人力流水线走向人机作业系统
canonical_object: agentic-product-engineering-collaboration
status: draft
audience: mixed-management
created: 2026-05-11
derived_from:
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
---

# AI Agent 时代，产研协作从人力流水线走向人机作业系统

> 给混合管理层的判断：AI agent 对产研最大的影响，不是让某个工程师写代码更快，而是把软件工程从“人按流程排队交付”改造成“人定义目标、系统调度 agent、产研共同审查结果”的作业系统。

## 1. 这不是工具升级，是作业模式升级

过去的软件工程默认是人力流水线。

产品提出需求，设计补交互，工程排期实现，QA 测试，CI/CD 发布，问题再回流。工具可以提高效率，但每个环节仍然依赖人把上下文带到下一步。

AI agent 进入后，变化不是“代码写得更快”这么简单。真正的变化是：需求、设计、issue、spec、PR、测试、日志、知识库开始变成 agent 可以读取、执行、回写的工作对象。

OpenAI 的 Symphony 把 Linear 这样的项目管理板变成 coding agents 的控制面。每个 open task 都可以映射到 agent workspace，agent 持续运行，人审查结果。OpenAI 文章里最关键的不是 500% PR 增长，而是他们把工程瓶颈从“代码速度”重新定义为“人类注意力和上下文切换”。

这对管理层意味着一件事：不能只采购 AI 编码工具。要重新设计产研作业系统。

## 2. 公司样本正在收敛到同一个方向

| 公司类型 | 样本 | 看到的变化 |
|---|---|---|
| AI 厂 | OpenAI Codex / Symphony | issue tracker 成为 agent control plane；人从 session 管理者变成目标、边界、评审负责人 |
| AI 厂 | Anthropic Claude Code | 工程、产品、设计、数据、法律、营销都开始把 agent 当作可执行工作界面 |
| 支付 / 金融科技 | Block | 大规模 monorepo 先做 AI-readiness：AGENTS.md、HOWTOAI、skills、AI review、CI/CD、共享 recipes |
| 云商 | AWS Q / Kiro / Frontier Agents | agent 进入开发、测试、review、重构、升级、安全、SRE、云运营 |
| 传统软件平台 | GitHub Copilot coding agent | issue 指派给 agent，agent 在 GitHub Actions 环境里工作，提交 draft PR，人 review |
| 工作管理平台 | Atlassian Jira / Rovo Dev | backlog、PRD、Jira issue、code plan、PR 连接成 agentic SDLC |
| IDE / 开发平台 | JetBrains Central | agentic software development 被定义为跨 IDE、CLI、pipeline、协作工具的分布式生产系统 |

它们表面上卖的是不同产品，底层共识很接近：

1. agent 不能停留在个人 IDE 里。
2. agent 必须接入真实产研对象：issue、PR、CI、日志、知识库、权限和环境。
3. 人的角色不消失，但上移到目标定义、边界设定、判断、审查和系统设计。
4. 管理层要治理的不是“员工能不能用 AI”，而是“agent 工作是否可控、可审、可复用、可度量”。

## 3. 新的产研协作对象：ticket、spec、PR、eval、wiki

AI agent 时代，管理层要重新看这些对象。

| 对象 | 旧角色 | 新角色 |
|---|---|---|
| Ticket / Issue | 需求记录和排期对象 | agent 工作入口、状态机、调度单元 |
| Spec / PRD | 给人读的需求文档 | agent 可执行的目标、边界、验收标准 |
| PR | 工程交付结果 | agent 输出包、人机审查面、反馈回路 |
| Test / Eval | 发布前质量检查 | agent 自证、回归验证、自动修复入口 |
| Wiki / Docs | 知识沉淀 | agent 上下文系统、组织记忆、规则索引 |
| CI / Logs | 工程基础设施 | agent 可读的验证和故障定位信号 |

管理层真正要问的问题是：这些对象现在能不能被 agent 读懂、执行、校验、回写。

如果不能，AI 只能停留在个人效率工具。
如果能，产研组织才开始进入人机协同作业系统。

## 4. 产研分工会怎么变

### 产品

产品不只是写需求给工程排期，而是把需求拆成 agent 可执行的工作对象。

产品要更清楚地写出：

- 目标用户和场景
- 验收标准
- 不做什么
- 优先级和取舍
- 需要人确认的判断

在 OpenAI Symphony 模式里，PM 和设计可以直接发起 feature request，agent 返回 review packet，甚至包含真实产品里的演示。这会缩短从想法到可评审结果的距离。

### 设计

设计不只是交 Figma，而是把交互意图、状态、边界和例外场景交给 agent。

Anthropic 的案例里，产品设计团队用 Claude Code 把 mockup 转成可运行原型，也用它发现 error states 和复杂逻辑流。设计开始从静态稿变成“可运行假设”的发起者。

### 工程

工程不再只靠手写代码体现价值。

工程的高价值工作会转向：

- 架构边界
- repo legibility
- agent-readable docs
- build/test/eval harness
- 安全和权限
- review 规则
- 判断复杂问题
- 把失败沉淀成 guardrail / skill / lint / test

OpenAI Harness Engineering 的关键判断是：当 agent 执行代码后，工程团队的主业变成设计环境、指定意图、构建反馈循环。

### QA / 测试 / 平台

QA 不再只是末端验收。

测试、日志、CI、可观测性、浏览器驱动、截图、回放，都变成 agent 自我验证和人类审查的基础设施。AWS、GitHub、OpenAI、Block 都在强调 agent 要能运行测试、读日志、看 CI、修失败，而不是只提交代码。

### 管理者

管理者不再只管人力排期。

管理者要管：

- 哪些工作可以进入 agent 队列
- 谁能发起 agent 工作
- agent 可以改什么、不能改什么
- 什么必须人审
- 什么指标证明有效
- agent 失败后是人工修，还是补规则和工具

这是管理对象的变化：从管理人执行，变成管理人机作业系统。

## 5. 成熟组织不是先追求全自动，而是先做可控协作

这些公司没有走向同一个“全自动写代码”口号。更成熟的方向是可控协作。

| 能力 | 为什么重要 |
|---|---|
| 明确入口 | agent 从 issue、ticket、spec、PR comment、CLI task 进入，而不是到处临时聊 |
| 隔离环境 | 每个任务有 workspace / branch / cloud env，避免污染主线 |
| 人类审查 | PR、review packet、approval、branch protection 保留人的判断权 |
| 自动验证 | agent 能跑测试、看 CI、读日志、修失败 |
| 知识系统 | repo docs、AGENTS.md、skills、wiki、rules 让 agent 读得到组织规则 |
| 权限和审计 | 管理层能看谁发起、agent 做了什么、花了多少、结果如何 |
| 失败回流 | agent 做错不是单点返工，而是补 guardrail、skill、lint、test |

JetBrains Central 把这个问题说得很直接：代码生成已经不是唯一瓶颈，真正挑战是让结果对齐意图，并管理 agent-driven work 带来的运行复杂度和成本。

## 6. 对我们的启发：先做一条 30-60 天试点链路

不要一开始做“全公司 AI 转型”。

先选一条产研链路，把它跑成闭环。

建议试点对象：

> 从需求 / 文章 / 会议材料进入，到 spec / wiki / issue，再到 agent 产出草稿或代码改动，最后由人审查、修正、沉淀规则。

试点目标不是“agent 替代工程师”，而是验证这套作业模式：

1. 需求是否能变成 agent 可执行任务。
2. agent 是否能产出可审查结果。
3. 人审查时是否更聚焦于判断和边界，而不是机械实现。
4. 失败是否能回流成规则、skill、测试、wiki，而不是下次重犯。
5. 产研负责人是否能看见吞吐、质量、成本、风险。

## 7. 建议的 30-60 天试点方案

### 第 1 阶段：定义控制面

选择一个入口，不要多个入口一起上。

可选入口：

- Jira / Linear / GitHub issue
- OpenSpec change
- repo wiki + task queue

最低要求：

- 每个任务有目标
- 有验收标准
- 有非目标
- 有判断归属
- 有人审查节点

### 第 2 阶段：定义 agent 可做和不可做

先让 agent 做低风险高重复工作：

- 阅读材料并产出结构化摘要
- 生成初稿
- 修改文档
- 补测试
- 修小 bug
- 运行检查
- 生成 review packet

先不要让 agent 自动做：

- 未确认的产品判断
- 架构大改
- 安全敏感改动
- 生产发布
- 跨系统数据写入

### 第 3 阶段：建立审查和回流

每次 agent 输出后，都要问：

- 结果是否服务原目标
- 哪些判断是 agent 自己做的
- 哪些地方需要人确认
- 失败是 prompt 问题、上下文问题、测试问题、权限问题，还是任务本身不清楚
- 下次应该补 wiki、skill、lint、test，还是调整流程

### 第 4 阶段：管理层看指标

不要只看“节省了多少小时”。

更重要的指标：

- 从需求到可评审结果的时间
- agent 输出一次通过率
- 人审查耗时
- 返工原因分类
- 重复失败是否下降
- 知识是否写回
- 哪些角色可以独立发起工作
- 哪些任务仍必须人工完成

## 8. 最后判断

AI agent 时代的软件工程，不会简单变成“更快写代码”。

它会变成一种新的作业系统：

```text
业务目标 / 产品意图
  -> spec / issue / wiki / acceptance criteria
  -> agent execution
  -> PR / draft / review packet
  -> human judgment
  -> tests / guardrails / skills / docs
  -> next run gets better
```

管理层真正要建设的，是这个循环。

谁能更早把产研知识、工程规则、验收标准、测试、日志、权限和审查机制变成 agent 可读可执行的系统，谁就能把 AI 从个人效率工具升级为组织级生产力。

## Sources

- OpenAI, [An open-source spec for Codex orchestration: Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)
- OpenAI, [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- Anthropic / Claude, [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)
- Block Engineering, [AI-Assisted Development at Block](https://engineering.block.xyz/blog/ai-assisted-development-at-block)
- AWS, [Amazon Q Developer](https://aws.amazon.com/q/developer/)
- AWS, [Frontier agents](https://aws.amazon.com/ai/frontier-agents/)
- GitHub, [GitHub Copilot: Meet the new coding agent](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/)
- Atlassian, [Rovo Dev in Jira](https://www.atlassian.com/blog/company-news/rovo-dev-in-jira)
- JetBrains, [Introducing JetBrains Central](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)
