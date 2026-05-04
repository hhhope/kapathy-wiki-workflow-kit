---
title: intelligence-native-organization / intake
type: intake
canonical_object: intelligence-native-organization
artifact_type: intake
language: zh-CN
audience: self
domain: personal-ops
period: evergreen
confidence: medium
status: active
updated_at: 2026-05-04
ai_generated: true
source_type: external-article
derived_from:
  - https://block.xyz/inside/from-hierarchy-to-intelligence
  - https://sequoiacap.com/article/from-hierarchy-to-intelligence/
  - https://investors.block.xyz/governance/leadership/default.aspx
  - https://www.pbs.org/newshour/amp/economy/ai-is-key-driver-behind-layoffs-at-fintech-company-block-ceo-says
  - https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w
related_objects:
  - behavior-asset-governance
  - agents-governance-drift
notes_scope: 记录 Jack Dorsey / Roelof Botha 关于 intelligence-native organization 的外部文章学习，并参考微信公众号文章的表达结构做二次整理。这里只保留可复用信号和边界，不把文章主张直接转成 repo policy、AGENTS 规则、skill 或 OpenSpec requirement。
---

# intelligence-native-organization / intake

## 0. 一句话

Block 这篇文章真正值得记的，不是"AI 会让公司裁掉中层"。

它戳穿的是另一个更底层的默认假设：

> 公司必须靠人类层级来路由信息。

Jack Dorsey 和 Roelof Botha 的说法是：如果 AI 能持续维护公司自己的 `world model`，那公司就不必继续把管理层当作信息传输管道。管理层过去做的很多事，不是"领导力"，而是慢速路由、摘要、同步、对齐、转发。

这对本 repo 有用的地方也不在组织裁员，而在行为资产治理：

> root AGENTS、repo AGENTS、rules、skills、OpenSpec、wiki、ADR，本质上也都是信息路由层。问题不是多写一条规则，而是每一层到底负责传什么、挡什么、升级什么。

## 1. 他最近写了什么

最相关的一篇署名文章：

- 标题：`From Hierarchy to Intelligence`
- 作者：Jack Dorsey and Roelof Botha
- 日期：2026-03-31
- 来源：Block 官网与 Sequoia 官网均有发布

Block 官方 leadership 页当前称 Jack Dorsey 为 `Block Head, Chairman, and cofounder of Block`。外部媒体仍常用 CEO 口径指代。

这篇文章发布前一个月，Block 宣布裁掉 4000 多名员工。Dorsey 在公开 memo / shareholder letter 中把这次调整与 AI 工具、较小且更扁平的团队、以及 intelligence-native company 方向联系起来。这个背景让文章不只是观点文，而是 Block 正在公开押注的一套组织操作系统。

## 2. 它为什么刺耳

传统管理层级有一个听起来很正当的解释：

- 组织大了，需要经理知道团队发生了什么。
- 团队多了，需要一层层同步信息。
- 方向复杂了，需要有人做优先级协调。
- 规模继续扩大，就需要更清晰的汇报线和控制幅度。

Block 文章把这套说法翻译成更冷的语言：

> 层级是人类认知限制下的信息路由协议。

这句话一旦成立，管理层级就不再天然神圣。它只是旧技术条件下的必要中介。

文章的核心推理是：

1. 过去两千年，军队、铁路、现代公司都在用层级解决大规模协调。
2. 层级的约束来自人类 span of control：一个人能稳定管理的人有限。
3. 层级越多，信息流越慢，决策越失真。
4. AI 第一次提供了替代协调层的可能：它可以持续读取 artifacts，维护公司状态模型，并主动组合资源。

它不是在说"每个人加一个 copilot"。

它在说：

> AI 不只是提高原结构的效率，而是可能替换原结构里最核心的信息协调功能。

## 3. Block 的模型

文章把 intelligence-native company 拆成四层。

### 3.1 Capabilities

能力不是产品界面，而是底层金融原语：支付、借贷、发卡、银行、BNPL、工资等。

这些能力难获得、难维护、有合规和可靠性要求，但它们不是最终价值的全部。

### 3.2 World model

Block 说它需要两个 world model：

- `company world model`：理解公司内部正在发生什么，谁在做什么，哪里被卡住，资源怎么分配。
- `customer world model`：从 Cash App、Square 等交易数据中理解客户真实经济行为。

文章里最关键的判断是：Block 是 remote-first，公司工作天然留下大量可机器读取 artifacts。决策、讨论、代码、设计、计划、问题和进展，都是 world model 的原料。

### 3.3 Intelligence layer

intelligence layer 负责把 capabilities 组合成具体方案。

传统模式是产品经理先规划路线图，再让团队开发。

Block 设想的是：客户现实产生信号，intelligence layer 发现需求，直接组合已有能力；如果组合失败，失败本身就变成未来路线图。

### 3.4 Interfaces

Square、Cash App、Afterpay、TIDAL、bitkey、proto 是交付界面。

文章把界面降级了：界面重要，但价值不主要在界面里，而在模型和智能层里。

## 4. 人还剩什么角色

文章没有说人消失，而是把人推到"边缘"。

边缘指模型碰不到现实的地方：

- 判断
- 直觉
- 品味
- 伦理
- 信任关系
- 新场景
- 高风险决策

因此它把人的角色归纳成三类：

- `IC`：深度专家，围绕能力、模型、智能层和界面建设。
- `DRI`：对跨域问题或客户结果负责，按问题调动资源。
- `player-coach`：既做事也培养人，替代主要负责信息路由的传统 manager。

最刺耳的一句是：不需要永久性的中层管理层。

但对本 repo 更有用的改写是：

> 不需要把每一层都变成永久规则层。

## 5. 对本 repo 的可复用信号

### 5.1 行为资产治理也是信息路由问题

我们现在讨论 root AGENTS、repo AGENTS、rules、skills、OpenSpec、wiki、ADR，看起来像是在讨论"规则放哪"。

其实更准确的问题是：

- 哪一层负责入口判断？
- 哪一层负责安全硬停？
- 哪一层负责触发式能力？
- 哪一层负责 change lifecycle？
- 哪一层负责长期记忆？
- 哪一层只记录候选，不能升级成规则？

Block 文章提醒我们：层级不是目标，信息流才是目标。

### 5.2 artifact 比聊天记忆可靠

Block 的 company world model 建在 artifacts 上。

对应到本 repo，可依赖的上下文也应该来自：

- `PROJECT.md`
- OpenSpec `proposal.md / design.md / tasks.md / evaluation.md`
- wiki intake / retro / method / ADR
- git status / git log
- 明确的 source links

不应该来自"我记得刚才好像说过"。

### 5.3 AI 可以路由，但不能擅自定案

这篇文章容易被误读成"AI 接管协调"。

放到本 repo，必须加一道边界：

> AI 可以整理、路由、比较、暴露冲突，但不能把 candidate 自动升级成 accepted。

这正好对应当前 root/repo governance 设计里的问题：候选规则、review 状态、accepted spec、runtime policy 必须分层。

### 5.4 不要把更多提示词误认为更好的组织

如果每遇到一个问题就往 AGENTS、rules、skills 里塞一段话，本质上是在复制旧层级的毛病：更多转发、更多解释、更多上下文负担。

更好的方向是：

- root AGENTS 做跨 repo 安全地板和入口卡片
- repo AGENTS 做 repo-specific policy
- rules 做 work-type 约束
- skills 做 triggered capability
- OpenSpec 做 change lifecycle
- wiki / ADR 做 durable memory

每层只拥有自己该拥有的语义。

## 6. 不能照搬的地方

- Block 是公司组织设计，不是 agent governance 标准。
- "取消中层管理"不能翻译成"取消人工 review"。
- Block 有交易数据和客户闭环，本 repo 没有这种高频 customer world model。
- Block 设想的是持续运行系统，本 repo 目前是 markdown + git + OpenSpec，不应 overclaim 自动上下文注入或 runtime autonomy。
- 文章的裁员语境不适合作为本 repo 的正面行动模板，只能作为组织结构案例背景。

## 7. 如果要用，只抽两条

现在最稳的抽法：

1. **层级存在是因为信息路由困难。**
   行为资产分层也必须围绕信息流和责任边界设计，而不是围绕"哪里还能塞规则"设计。

2. **AI 可以增强路由，不等于获得决定权。**
   候选材料必须经过 review artifact 才能进入 spec、AGENTS、rules 或 skills。

其他更强的说法，比如 mini-AGI、取消管理层、world model 自动协调，暂时只作为外部案例，不进入 repo policy。

## 8. 后续落点

如果继续用于当前 root/repo governance 设计评审，建议只作为 benchmark / design-review 输入，最多进入：

- `openspec/changes/decide-root-governance-alignment/design.md`
- `wiki/ops/behavior-asset-governance-design-trace.md`

不要从本 intake 直接落到：

- repo `AGENTS.md`
- root `AGENTS.md`
- `rules/`
- `.codex/skills/`
- OpenSpec requirement

下一步如果要正式吸收，应该先问一个更窄的问题：

> 这篇文章能不能支持我们把行为资产治理定义成"信息路由栈"？

如果答案是能，再走 OpenSpec review。否则它只保留为外部案例。
