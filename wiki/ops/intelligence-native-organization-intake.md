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

## 0. 这页要学什么

这页不是普通摘要。

这页要学的是：Block 那篇 `From Hierarchy to Intelligence` 为什么值得放进我们的行为资产治理讨论里。

结论先放前面：

> Block 文章真正刺穿的，不是"公司可以裁掉中层"，而是"公司必须靠人类层级来路由信息"这个默认假设。

迁移到本 repo，就是另一句话：

> AGENTS、rules、skills、OpenSpec、wiki、ADR 不是越多越好；它们是一套信息路由栈。每一层必须知道自己传什么、挡什么、升级什么。

## 1. 参考文章的结构学到什么

用户给的公众号文章是写法参考，不是内容来源。它讲的是 AI 潜意识学习，但结构值得借。

它的结构大概是：

1. **先给一个让人坐直的判断。**
   不是先铺背景，而是直接说行业默认假设被打穿了。

2. **解释为什么这个判断吓人。**
   不是泛泛说"很重要"，而是指出它挑战了哪条常用工作流。

3. **用实验或机制拆开证明链。**
   读者能看到：现象是什么、怎么证明、为什么不是误判。

4. **把反驳先替读者问出来。**
   比如"会不会只是过滤不干净"。好文章不是只讲自己对，而是封住最自然的反驳路径。

5. **最后落到行动清单。**
   按紧迫度分层：本周做什么、本月做什么、以后跟什么。

6. **给参考链接。**
   让读者可以回到原文、论文、解读和讨论，而不是只相信二手总结。

这页按这个结构重写 Block 文章：不是平铺摘要，而是抓默认假设、证据链、可迁移动作和参考链接。

## 2. Block 最近写了什么

最相关的一篇署名文章：

- 标题：`From Hierarchy to Intelligence`
- 作者：Jack Dorsey and Roelof Botha
- 日期：2026-03-31
- 官方来源：Block 官网与 Sequoia 官网均有发布

Block 官方 leadership 页当前称 Jack Dorsey 为 `Block Head, Chairman, and cofounder of Block`。外部媒体仍常用 CEO 口径指代。

这篇文章发布前一个月，Block 宣布裁掉 4000 多名员工。Dorsey 在公开 memo / shareholder letter 中把这次调整与 AI 工具、较小且更扁平的团队、以及 intelligence-native company 方向联系起来。这个背景让文章不只是观点文，而是 Block 正在公开押注的一套组织操作系统。

## 3. 为什么这篇文章刺耳

传统公司有一个听起来很合理的解释：

- 组织大了，需要经理知道团队发生了什么。
- 团队多了，需要一层层同步信息。
- 方向复杂了，需要有人做优先级协调。
- 规模继续扩大，就需要更清晰的汇报线和控制幅度。

Block 文章把这套解释翻译成更冷的语言：

> 层级是人类认知限制下的信息路由协议。

这句话一旦成立，管理层级就不再天然神圣。它只是旧技术条件下的必要中介。

文章真正的推理链是：

1. 过去两千年，军队、铁路、现代公司都靠层级解决大规模协调。
2. 层级的约束来自人类 span of control：一个人能稳定管理的人有限。
3. 层级越多，信息流越慢，决策越失真。
4. AI 第一次提供了替代协调层的可能：它可以持续读取 artifacts，维护公司状态模型，并主动组合资源。

它不是在说"每个人加一个 copilot"。

它是在说：

> AI 不只是提高原结构的效率，而是可能替换原结构里最核心的信息协调功能。

## 4. Block 的证据链

### 4.1 Capabilities

Block 不是从界面开始讲，而是从能力开始讲。

底层能力包括支付、借贷、发卡、银行、BNPL、工资等。这些能力难获得、难维护、有合规和可靠性要求，是金融科技公司的硬地基。

### 4.2 World model

Block 说它需要两个 world model：

- `company world model`：理解公司内部正在发生什么，谁在做什么，哪里被卡住，资源怎么分配。
- `customer world model`：从 Cash App、Square 等交易数据中理解客户真实经济活动。

这里最关键的是 company world model。

Block 是 remote-first，公司工作天然留下大量可机器读取 artifacts：讨论、决策、代码、设计、计划、问题、进展。这些不是会议后的附属材料，而是 intelligence-native company 的原料。

### 4.3 Intelligence layer

intelligence layer 负责把 capabilities 组合成具体方案。

传统模式是产品经理先规划路线图，再让团队开发。

Block 设想的是：客户现实产生信号，intelligence layer 发现需求，直接组合已有能力；如果组合失败，失败本身就变成未来路线图。

### 4.4 Interfaces

Square、Cash App、Afterpay、TIDAL、bitkey、proto 是交付界面。

文章把界面降级了：界面重要，但价值不主要在界面里，而在模型和智能层里。

## 5. 最容易误读的地方

这篇文章很容易被读成：

> AI 来了，所以中层没用了。

这个读法太粗。

更准确的读法是：

> 如果一个组织已经把真实工作沉淀成高质量 artifacts，AI 才可能替代一部分信息路由层。

没有 artifacts，就没有 company world model。

没有 world model，AI 只能当个人助手。

没有清晰边界，AI 路由就会变成擅自定案。

所以这篇文章对本 repo 的启发，不是"减少人"，而是：

> 减少无主语、无边界、无证据的规则层。

## 6. 对本 repo 的迁移

### 6.1 行为资产治理也是信息路由问题

我们现在讨论 root AGENTS、repo AGENTS、rules、skills、OpenSpec、wiki、ADR，看起来像是在讨论"规则放哪"。

其实更准确的问题是：

- 哪一层负责入口判断？
- 哪一层负责安全硬停？
- 哪一层负责触发式能力？
- 哪一层负责 change lifecycle？
- 哪一层负责长期记忆？
- 哪一层只记录候选，不能升级成规则？

Block 文章提醒我们：层级不是目标，信息流才是目标。

### 6.2 artifact 比聊天记忆可靠

Block 的 company world model 建在 artifacts 上。

对应到本 repo，可依赖的上下文也应该来自：

- `PROJECT.md`
- OpenSpec `proposal.md / design.md / tasks.md / evaluation.md`
- wiki intake / retro / method / ADR
- git status / git log
- 明确的 source links

不应该来自"我记得刚才好像说过"。

### 6.3 AI 可以路由，但不能擅自定案

这篇文章容易被误读成"AI 接管协调"。

放到本 repo，必须加一道边界：

> AI 可以整理、路由、比较、暴露冲突，但不能把 candidate 自动升级成 accepted。

这正好对应当前 root/repo governance 设计里的问题：候选规则、review 状态、accepted spec、runtime policy 必须分层。

### 6.4 不要把更多提示词误认为更好的组织

如果每遇到一个问题就往 AGENTS、rules、skills 里塞一段话，本质上是在复制旧层级的毛病：更多转发、更多解释、更多上下文负担。

更好的方向是：

- root AGENTS 做跨 repo 安全地板和入口卡片
- repo AGENTS 做 repo-specific policy
- rules 做 work-type 约束
- skills 做 triggered capability
- OpenSpec 做 change lifecycle
- wiki / ADR 做 durable memory

每层只拥有自己该拥有的语义。

## 7. 行动清单

### 7.1 现在就能用

- 把当前 root/repo governance 设计里的核心对象改写成"信息路由栈"，不要只写成"规则分层"。
- 检查每一层是否有清楚的 `owns / must not own / evidence / promotion path`。
- 对所有 candidate 内容加显式边界：只能进入 design / intake / trace，不能直接进入 spec / AGENTS / rules / skills。
- 在 `design.md` 里保留这篇文章作为 benchmark 输入，而不是 normative source。

### 7.2 这轮不要做

- 不要把 Block 的组织设计直接写进 repo `AGENTS.md`。
- 不要把"取消中层管理"改写成"取消人工 review"。
- 不要声称本 repo 已经有 company world model 或自动上下文注入。
- 不要把这篇 intake 直接升级成 ADR 或 method page。

### 7.3 以后再说

- 如果后续多次用到"信息路由栈"这个框架，再考虑在 OpenSpec change 里正式定义。
- 如果要吸收到 behavior-asset governance，应先做 review：它支持哪些原则，不支持哪些原则。
- 如果要做运行时工具，必须另起 OpenSpec；这篇文章不能作为直接实现许可。

## 8. 不能照搬的地方

- Block 是公司组织设计，不是 agent governance 标准。
- Block 有交易数据和客户闭环，本 repo 没有这种高频 customer world model。
- Block 设想的是持续运行系统，本 repo 目前是 markdown + git + OpenSpec。
- 裁员语境不适合作为本 repo 的正面行动模板，只能作为组织结构案例背景。

## 9. 最后留下的问题

如果以后继续吸收这篇文章，真正应该问的不是：

> Block 怎么用 AI 管公司？

而是：

> 我们能不能把行为资产治理定义成一套可审计的信息路由栈？

这个问题比"AGENTS.md 应该写多长"更根本。

长度只是症状。

真正的问题是：每一层有没有明确的输入、输出、边界、升级路径和证据要求。

## 10. 参考链接

### 10.1 主要来源

- Block 原文：`From Hierarchy to Intelligence`
  - https://block.xyz/inside/from-hierarchy-to-intelligence
- Sequoia 同文发布页：`From Hierarchy to Intelligence`
  - https://sequoiacap.com/article/from-hierarchy-to-intelligence/
- Block leadership：Jack Dorsey 当前官方头衔
  - https://investors.block.xyz/governance/leadership/default.aspx
- PBS/AP 背景报道：Block layoffs and AI rationale
  - https://www.pbs.org/newshour/amp/economy/ai-is-key-driver-behind-layoffs-at-fintech-company-block-ceo-says

### 10.2 写法参考

- 微信公众号文章：`AI也有潜意识 而且会传染...`
  - https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w

本页借鉴的是它的结构：强判断开头、默认假设拆解、证据链、反误读、行动清单、参考链接。内容主题没有迁移。

### 10.3 Repo 内部可能落点

- 当前候选 change：`openspec/changes/decide-root-governance-alignment/design.md`
- 当前候选 trace：`wiki/ops/behavior-asset-governance-design-trace.md`

这些只是可能落点。正式吸收前必须经过 OpenSpec review，不能从本 intake 直接升级成 runtime policy。
