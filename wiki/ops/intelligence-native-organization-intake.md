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

## 0. 核心判断

Block 这篇不是一篇 AI 提效文章，也不只是裁员后的组织解释。

它真正写的是：当 AI 能持续维护公司的状态模型，传统公司里那条"人把信息一级级往上报、再把决策一级级往下传"的路由链，就不再是公司运转的默认骨架。

换句话说：

> 过去的公司把人放在信息链路中间；Block 想把人推到真实世界的边缘，把中间的协调层交给持续更新的系统。

这句话比"取消中层"更准确。

中层不是突然没有价值。失去默认位置的是那种主要靠同步、转发、汇总、对齐、排优先级来维持组织运转的永久中间层。

对这个 repo 来说，可复用的也不是组织裁员，而是另一个问题：

> AGENTS、rules、skills、OpenSpec、wiki、ADR 到底是一套信息路由系统，还是一堆互相复述的提示词？

如果是前者，每一层都要说清楚自己接收什么、阻断什么、升级什么、沉淀什么。如果是后者，文件越写越多，协作越像在穿过一串人工中继站。

## 1. Block 最近写了什么

最相关的一篇署名文章：

- 标题：`From Hierarchy to Intelligence`
- 作者：Jack Dorsey and Roelof Botha
- 日期：2026-03-31
- 官方来源：Block 官网与 Sequoia 官网均有发布

Block 官方 leadership 页当前称 Jack Dorsey 为 `Block Head, Chairman, and cofounder of Block`。外部媒体仍常用 CEO 口径指代。

这篇文章发布前一个月，Block 宣布裁掉 4000 多名员工。Dorsey 在公开 memo / shareholder letter 中把这次调整与 AI 工具、较小且更扁平的团队、以及 intelligence-native company 方向联系起来。

所以它不是单纯观点文。它更像 Block 对外公开的一份组织操作系统草图：公司不再先问"怎么画组织图"，而是先问"系统如何理解公司正在发生什么"。

## 2. 它打穿的默认假设

传统组织默认相信一件事：

> 规模一大，就必须有层级；层级一多，就必须有管理者作为信息中继。

Block 文章不从现代互联网公司讲起，而是从罗马军团讲起。军队、铁路、科学管理、矩阵组织、Spotify squad、Holacracy、Valve 扁平组织，这些例子串起来，其实都在说明同一件事：

> 两千年来，组织创新一直在绕着同一个约束打转：人类的控制幅度有限。

一个人能稳定理解和协调的人数有限。组织要变大，就要加层。层级解决了可控性，也制造了信息损耗：

- 下面的信息被摘要、过滤、变形。
- 上面的决策被解释、转译、延迟。
- 横向协作要等新的同步会、对齐会、优先级会。
- 规模越大，组织越像一条低带宽总线。

Block 的问题是：

> 如果层级原本只是为了解决信息路由，那 AI 能不能替代这部分功能？

这才是文章的锋利处：它把组织结构问题还原成信息流问题。

它不是说人不重要，而是说"人作为默认路由器"这件事开始动摇。

## 3. Block 给出的新结构

Block 没有把 AI 放在旧组织旁边当助手，而是把公司拆成四层。

### 3.1 Capabilities：可组合的金融原语

Capabilities 是底层能力，不是产品界面。

支付、借贷、发卡、银行、BNPL、工资，这些能力背后是监管许可、可靠性、风控、网络效应和长期维护成本。它们不是轻飘飘的抽象能力，而是很难获得、也很难稳定运营的金融基础件。

这层回答的是：公司到底能做什么。

### 3.2 World model：公司理解自己，也理解客户

Block 提了两个 world model。

一个是 `company world model`：公司内部正在发生什么，谁在推进，哪里阻塞，资源在哪里，哪些决策已经发生，哪些问题正在积累。

另一个是 `customer world model`：基于 Cash App、Square 等交易和经营数据，理解客户真实经济行为。

这里最关键的是前者。

Block 是 remote-first，公司每天自然产生大量可机器读取的工作事实：讨论、决策、代码、设计、计划、问题、进度。这些不再只是会议纪要或项目管理副产物，而是系统理解公司的原料。

没有这些 artifact，AI 只能做个人秘书。

有了这些 artifact，AI 才可能变成组织状态层，而不只是更快的秘书。

### 3.3 Intelligence layer：从路线图转向实时组合

传统产品组织靠路线图工作：先猜客户要什么，再排优先级，再组织团队交付。

Block 想要的不是更快地执行路线图，而是让 intelligence layer 直接读取客户现实，组合已有 capabilities，生成解决方案。

如果组合失败，说明能力层有缺口；这个失败信号才进入未来路线图。

这是一处关键反转：

> 不是产品经理先写 roadmap，再让组织执行；而是客户现实先产生信号，系统再暴露能力缺口。

### 3.4 Interfaces：界面只是交付面

Square、Cash App、Afterpay、TIDAL、bitkey、proto 仍然重要，但文章把它们放在最后。

这不是低估界面，而是重新排序价值来源：

> 价值不主要产生在界面里，而是产生在模型、能力和智能组合层里。

## 4. 人的位置怎么变了

Block 最有争议的部分，是对人的重新定位。

传统公司里，智能分散在人和团队里，层级负责把这些智能串起来。

Block 设想的新结构里，系统承载更多上下文和协调，人来到边缘。

边缘不是边缘化。

边缘是模型碰到现实的地方：

- 模型没有品味，人有。
- 模型没有信任关系，人有。
- 模型没有现场感，人有。
- 模型不该独自承担伦理和高风险判断，人要承担。
- 模型遇到新问题时，人要把现实带回来。

因此文章把人的角色收敛成三类：

- `IC`：深度专家，建设和运营 capabilities、world model、intelligence layer、interfaces。
- `DRI`：对某个跨域问题或客户结果负责，可以临时调动多个能力层资源。
- `player-coach`：既做事，也培养人；替代主要靠会议和同步维持存在感的 manager。

真正被挑战的是永久中间层，不是人的判断力。

## 5. 最容易误读的地方

这篇文章最容易被粗暴读成：

> AI 来了，所以管理层没用了。

这个读法会把它读浅。

更准确的条件是：

> 只有当真实工作已经沉淀成高质量 artifact，AI 才可能替代一部分信息路由层。

没有 artifact，就没有 company world model。

没有足够诚实的 customer signal，就没有真实反馈闭环。

没有边界，AI 路由就会变成擅自定案。

所以这篇文章不是在奖励"更少的人"，而是在奖励"更清楚的组织状态"和"更快变深的公司理解"。

## 6. 迁移到本 repo

这篇文章对我们当前的 root/repo governance 讨论，有三个直接启发。

### 6.1 问题不是文件太长，而是信号被多层转发

`AGENTS.md` 长只是表面症状。

更根本的问题是：同一条协作信号在 root AGENTS、repo AGENTS、rules、skills、OpenSpec、wiki 之间反复转述，最后没人知道哪一层有最终解释权。

这就像传统公司里的中层转发链：

- 每层都在解释上一层。
- 每层都加一点自己的判断。
- 每层都声称自己只是帮助理解。
- 最后真正的决策边界消失了。

如果用 Block 的语言说，这不是上下文丰富，而是信息路由系统失真。

### 6.2 行为资产应该像组织层一样分工

比较稳的分工是：

- `root AGENTS`：跨 repo 安全地板、启动入口、硬停边界。
- `repo AGENTS`：repo-specific policy、OpenSpec 触发条件、wiki 路由、交付边界。
- `rules`：按工作类型加载的长期执行约束。
- `skills`：按意图触发的能力合同，保持短入口和渐进披露。
- `OpenSpec`：变更生命周期、任务进度、候选到接受的审查路径。
- `wiki / ADR / retro`：长期记忆、分歧材料、稳定决策。

每层都应该有 `owns / must not own / evidence / promotion path`。

缺这四项，分层就会变成噪声。

### 6.3 AI 可以帮我们路由，但不能替我们定案

Block 的文章强调系统可以替代很多信息路由。

迁移到本 repo，要补一句刹车：

> AI 可以整理、比较、暴露冲突、建议落点；但 candidate 进入 accepted，必须靠 review artifact。

这就是当前设计里最需要守住的边界：

- intake 不是 method。
- design trace 不是 ADR。
- candidate routing table 不是 spec。
- OpenSpec proposal 不是 implementation approval。
- skill trigger draft 不是 runtime behavior。

如果这些边界塌了，AI 不是替代中间层，而是在制造一个更难追责的新中间层。

## 7. 现在该怎么用

### 7.1 本周可用

- 把当前 governance 设计里的核心隐喻从"规则分层"改成"信息路由栈"。
- 检查每层是否都有 `owns / must not own / evidence / promotion path`。
- 把所有 candidate 内容重新标清：它现在只能在哪一层存在，不能升级到哪里。
- 在 `design.md` 里引用这篇文章时，只作为 benchmark signal，不作为规范来源。

### 7.2 这轮不要做

- 不要把 Block 组织设计直接写进 repo `AGENTS.md`。
- 不要把"不需要永久中层"翻译成"不需要人工 review"。
- 不要声称本 repo 已经有 company world model。
- 不要把这篇 intake 直接升级成 ADR、method page 或 OpenSpec requirement。

### 7.3 以后再说

- 如果"信息路由栈"这个框架反复有效，再用新 OpenSpec change formalize。
- 如果要做自动上下文注入或 routing helper，另起 change，不从这篇文章直接获得实现许可。
- 如果要把它提升成 ADR，先证明它解决了两个以上 repo artifact 层之间的真实冲突。

## 8. 对写法参考的学习

用户给的公众号文章不是内容来源，它讲的是 AI 潜意识学习。

它真正值得学的是结构：

- 开头不是"本文总结"，而是直接指出一个行业假设被击穿。
- 中段不是堆概念，而是拆证明链：现象、实验、反驳、后果。
- 结尾不是泛泛感想，而是分层行动清单。
- 参考链接放在正文末尾，读者可以回到原文、论文、解读和讨论。

这页吸收的是这个结构：强判断、默认假设、证据链、反误读、迁移清单、参考链接。内容主题没有迁移。

## 9. 最后留下的问题

Block 原文最后抛出的判断很狠：如果一家公司没有真正难以理解、且每天都在变深的理解，AI 最多只是成本优化故事。

迁移到本 repo，真正该问的也不是：

> Block 怎么用 AI 管公司？

而是：

> 我们能不能把行为资产治理定义成一套可审计的信息路由栈？

这个问题比"AGENTS.md 应该写多长"更根本。

长度只是症状。

真正的问题是：每一层有没有明确的输入、输出、边界、升级路径和证据要求；这些理解有没有随着每次 change、retro、ADR 变深。

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

### 10.3 Repo 内部可能落点

- 当前候选 change：`openspec/changes/decide-root-governance-alignment/design.md`
- 当前候选 trace：`wiki/ops/behavior-asset-governance-design-trace.md`

这些只是可能落点。正式吸收前必须经过 OpenSpec review，不能从本 intake 直接升级成 runtime policy。
