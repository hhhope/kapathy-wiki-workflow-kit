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

## 0. 摘要

Jack Dorsey 与 Roelof Botha 在 `From Hierarchy to Intelligence` 中提出的核心观点是：传统组织层级主要承担信息路由和协调职能；当 AI 能够持续维护公司运行状态模型时，这部分职能不一定继续依赖永久性管理层级。

这篇文章不应被简单理解为"AI 替代中层"。更准确的理解是：

> 组织结构的核心约束正在从"人类管理幅度"转向"系统是否能准确理解公司和客户的实时状态"。

对本 repo 的可复用启发也不在组织裁员，而在行为资产治理：

> `AGENTS.md`、`rules`、`skills`、OpenSpec、wiki、ADR 应被视为一套信息路由与决策升级系统。每一层都需要明确输入、输出、边界、证据要求和升级路径。

本页只记录外部文章学习和迁移假设，不直接形成 repo policy、root policy、skill 规则或 OpenSpec requirement。

## 1. 来源

主要文章：

- 标题：`From Hierarchy to Intelligence`
- 作者：Jack Dorsey and Roelof Botha
- 日期：2026-03-31
- 发布：Block 官网与 Sequoia 官网

背景信息：

- Block 官方 leadership 页当前称 Jack Dorsey 为 `Block Head, Chairman, and cofounder of Block`。
- 文章发布前，Block 宣布裁员 4000 多人。公开报道显示，Dorsey 将这次组织调整与 AI 工具、扁平化团队和 intelligence-native company 方向联系起来。

写法参考：

- 用户提供的微信公众号文章 `AI也有潜意识 而且会传染...` 被用作结构参考。参考的是写法：强判断开头、默认假设拆解、证据链、反误读、行动清单和参考链接；内容主题不迁移。

## 2. 原文主张

### 2.1 层级是一种信息路由机制

文章从罗马军团、普鲁士总参谋部、美国铁路组织图、科学管理、矩阵组织和互联网公司的组织实验谈起。这些例子服务于一个共同判断：

> 传统组织结构是在有限沟通能力和有限管理幅度下形成的信息路由机制。

组织规模扩大后，个人无法直接理解所有上下文，因此组织引入层级、职能、汇报线和管理者。层级提升了可控性，但也带来信息延迟、压缩和失真。

原文关注的不是"层级是否好"，而是：

> 如果层级主要解决信息路由问题，那么当 AI 能够承担一部分路由和协调工作时，组织结构是否需要重新设计？

### 2.2 AI 不是附加在旧结构上的效率工具

文章区分了两种 AI 使用方式：

- 把 AI 当作 productivity enhancer：在现有组织结构中提高个人产出。
- 把公司重构为 intelligence-native organization：让 AI 成为公司理解自身、理解客户、组合能力和协调工作的基础层。

Block 选择讨论的是第二种。

## 3. Block 的四层模型

### 3.1 Capabilities

Capabilities 是可组合的底层金融能力，包括支付、借贷、发卡、银行、BNPL、工资等。

这些能力不是界面功能，而是受监管、可靠性、风控、网络效应和长期运营约束的基础能力。它们定义了公司可以提供哪些解决方案。

### 3.2 World model

文章提出两个 world model：

- `company world model`：理解公司内部的决策、讨论、代码、设计、计划、问题、进度和资源状态。
- `customer world model`：基于交易和经营数据，理解客户与商户的经济行为。

对本文学习最重要的是 `company world model`。Block 是 remote-first，工作天然留下大量可机器读取的 artifact。文章认为，这些 artifact 可以成为系统理解组织状态的输入。

如果没有稳定 artifact，AI 只能辅助个体任务；只有当组织活动被持续记录、结构化和引用时，AI 才可能承担更高层级的协调职能。

### 3.3 Intelligence layer

Intelligence layer 负责把 capabilities 组合为面向具体客户和具体时刻的解决方案。

传统产品组织通常先制定 roadmap，再组织团队交付。Block 文章提出的方向是：由客户现实产生信号，系统尝试组合已有能力；当组合失败时，失败本身暴露能力缺口，并形成未来 roadmap 输入。

这个模型将 roadmap 的来源从"人的预判"部分转向"客户现实反馈"。

### 3.4 Interfaces

Square、Cash App、Afterpay、TIDAL、bitkey、proto 等是交付界面。

文章并未否定界面价值，而是重新排序价值来源：界面是触达面，基础价值来自 capabilities、world model 和 intelligence layer 的组合。

## 4. 人的角色变化

文章将人的位置从层级内部的信息中继，调整到系统与现实接触的边界。

人的作用集中在：

- 专业建设与运营
- 跨域问题负责
- 判断、品味、伦理和高风险决策
- 现实反馈与新问题识别
- 人才培养和 craft 传承

对应角色包括：

- `IC`：建设和运营 capabilities、world model、intelligence layer 与 interfaces 的专家。
- `DRI`：对特定跨域问题或客户结果负责，可调动多个能力层资源。
- `player-coach`：同时承担实际建设和人才培养，不以信息转发作为主要职责。

因此，原文挑战的是"以信息路由为主要职责的永久中间层"，不是人的判断能力或组织责任本身。

## 5. 容易误读的点

### 5.1 不是所有组织都能立即替换层级

AI 能承担组织协调职能的前提是：

- 公司活动有高质量 artifact。
- 系统能持续更新对公司状态的理解。
- 客户信号足够真实、连续、可反馈。
- AI 协调边界清晰，不能替代人类最终责任。

如果这些条件不存在，AI 仍主要是个人或团队效率工具。

### 5.2 不应把组织设计直接迁移为治理规则

Block 的语境是公司组织设计和业务战略。它不能直接作为 agent governance 规范使用。

特别需要避免三类过度迁移：

- 将"不需要永久中层"理解为"不需要人工 review"。
- 将 Block 的 company world model 等同于本 repo 当前的 markdown/wiki 状态。
- 将一篇外部文章直接写入 `AGENTS.md`、`rules`、`skills` 或 OpenSpec requirement。

## 6. 对本 repo 的可用启发

### 6.1 从"规则分层"改为"信息路由栈"

当前 root/repo governance 讨论中，真正需要回答的问题不是某个文件应该多长，而是：

- 哪一层接收任务入口？
- 哪一层拥有安全硬停？
- 哪一层拥有 repo-specific policy？
- 哪一层拥有触发式能力？
- 哪一层拥有 change lifecycle？
- 哪一层只保留候选材料？
- 哪一层可以把候选提升为 accepted？

这与 Block 文章中的组织设计问题相似：层级存在不是目的，信息流和责任边界才是目的。

### 6.2 每层必须有明确职责

一个较稳的行为资产分工是：

- `root AGENTS`：跨 repo 安全地板、启动入口、硬停边界。
- `repo AGENTS`：repo-specific policy、OpenSpec 触发条件、wiki 路由、交付边界。
- `rules`：按工作类型加载的长期执行约束。
- `skills`：按意图触发的能力合同，保持短入口和渐进披露。
- `OpenSpec`：变更生命周期、任务进度、候选到接受的审查路径。
- `wiki / ADR / retro`：长期记忆、分歧材料、稳定决策。

每层都应明确：

- `owns`
- `must not own`
- `evidence`
- `promotion path`

没有这些字段，分层会变成重复和转述，而不是有效路由。

### 6.3 AI 可以辅助路由，但不能自动定案

迁移到本 repo 时，需要保留一条边界：

> AI 可以整理、比较、暴露冲突和建议落点；但 candidate 进入 accepted，必须通过 review artifact。

对应关系：

- intake 不是 method。
- design trace 不是 ADR。
- candidate routing table 不是 spec。
- OpenSpec proposal 不是 implementation approval。
- skill trigger draft 不是 runtime behavior。

如果这条边界不清，AI 不会减少治理层级，反而会制造新的责任不清。

## 7. 使用建议

### 7.1 可立即吸收

- 在当前 governance 设计中使用"信息路由栈"作为分析框架。
- 检查每一层是否具备 `owns / must not own / evidence / promotion path`。
- 对 candidate 内容明确当前层级和禁止升级位置。
- 将 Block 文章作为 benchmark signal，而不是规范来源。

### 7.2 当前不应执行

- 不把 Block 组织设计直接写进 repo `AGENTS.md`。
- 不把"不需要永久中层"改写成"不需要人工 review"。
- 不声称本 repo 已有 company world model 或自动上下文注入。
- 不把本 intake 直接升级为 ADR、method page 或 OpenSpec requirement。

### 7.3 后续条件

如果后续要正式吸收该框架，应满足至少一个条件：

- 它能解释两个以上 repo artifact 层之间的真实冲突。
- 它能帮助收敛当前 root/repo governance 的候选项。
- 它能生成可验证的职责字段或审查清单。

满足条件后，应通过新的 OpenSpec review，而不是从本页直接进入运行时规则。

## 8. 写法参考

用户提供的微信公众号文章在内容上与 Block 主题无关，但其结构值得参考：

- 开头直接提出被挑战的默认假设。
- 中段拆解证据链，而不是平铺资料。
- 主动处理常见误读。
- 结尾给出分层行动清单。
- 保留参考链接，便于读者回到原始资料。

本页吸收的是上述结构，不迁移其具体主题和表达风格。

## 9. 留下的问题

Block 原文最后提出的问题是：一家公司是否拥有真正难以理解、且每天都在加深的理解。如果没有，AI 只是成本优化工具；如果有，AI 会改变公司组织形态。

迁移到本 repo，可以改写为：

> 行为资产治理是否形成了一套可审计、可升级、可复用的信息路由栈？

这比"AGENTS.md 应该写多长"更关键。

长度是症状。更关键的是：每一层是否有明确的输入、输出、边界、升级路径和证据要求；这些理解是否随着每次 change、retro、ADR 持续加深。

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

## 11. H5 图文拆分

本主题适合做一页 H5 信息图，但不适合把全文都图形化。图的任务是帮助读者快速看懂"旧组织层级"与"intelligence-native organization"的结构差异；正文仍负责证据、边界和引用。

### 11.1 需要图文表达

| 模块 | 是否做图 | 理由 | H5 表达方式 |
|------|----------|------|-------------|
| 核心判断 | 是 | 需要在第一屏建立判断：问题不是 AI 提效，而是组织信息路由方式变化 | Hero 大标题 + 一句结论 |
| 旧组织结构 | 是 | 层级、汇报线、信息损耗适合视觉比较 | 左侧层级链路图 |
| 新组织结构 | 是 | capabilities / world model / intelligence layer / interfaces 是结构模型 | 右侧四层堆叠图 |
| 旧 vs 新对照 | 是 | 读者需要快速看到差异维度 | 对照表：路由主体、信息来源、roadmap 来源、人的位置 |
| 人的角色变化 | 是 | IC / DRI / player-coach 是可视化角色迁移 | 三角色卡片 |
| repo 迁移 | 是 | root AGENTS / repo AGENTS / rules / skills / OpenSpec / wiki 需要明确分工 | 信息路由栈卡片 |
| 行动建议 | 是 | 适合放在尾部形成操作清单 | 本周可用 / 本轮不做 / 后续条件 |

### 11.2 不需要图文表达

| 模块 | 不做图原因 | 保留位置 |
|------|------------|----------|
| 来源元信息 | 图上放过多链接会干扰阅读 | 本 md 的来源与参考链接 |
| 公众号写法参考 | 这是生产过程说明，不是主题内容 | 本 md 第 8 节 |
| 误读边界细节 | 适合文字精确说明，图上容易变成口号 | 本 md 第 5 节 |
| 正式吸收条件 | 属于治理边界，应该保留可审计文本 | 本 md 第 7.3 节 |
| 参考链接 | 链接需要可复制，不适合只做图片元素 | 本 md 第 10 节，H5 页脚只保留短链接说明 |

### 11.3 生成物

- H5 文件：`wiki/ops/intelligence-native-organization-h5.html`
- 手绘参考版：`wiki/ops/intelligence-native-organization-handdrawn-h5.html`
- 用途：用于一图流预览、截图或转成图文稿。
- 边界：H5 是视觉解释，不是 repo policy；正式吸收仍需 OpenSpec review。
