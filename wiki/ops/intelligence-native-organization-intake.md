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
related_objects:
  - behavior-asset-governance
  - agents-governance-drift
notes_scope: 记录 Jack Dorsey / Roelof Botha 关于 intelligence-native organization 的外部文章学习。这里只保留可复用信号和边界，不把文章主张直接转成 repo policy、AGENTS 规则、skill 或 OpenSpec requirement。
---

# intelligence-native-organization / intake

## 1. 触发

用户问："帮我搜索下block这个CEO最近写了什么文章"，随后要求"记录md文件"。

本页记录 2026-05-04 搜索结果中最相关的一篇署名文章：

- 标题：`From Hierarchy to Intelligence`
- 作者：Jack Dorsey and Roelof Botha
- 日期：2026-03-31
- 官方来源：Block 官网与 Sequoia 官网均有发布

Block 官方 leadership 页当前称 Jack Dorsey 为 `Block Head, Chairman, and cofounder of Block`。外部媒体仍常用 CEO 口径指代。

## 2. 来源摘要

### 2.1 文章主张

文章把传统层级组织解释为一种信息路由机制：当组织规模扩大，人类只能通过管理层级来聚合、传递、协调信息。作者认为 AI 现在可以持续维护公司的运行模型，并承担部分过去由中层管理完成的信息路由、对齐和协调工作。

文章区分了两种 AI 使用方式：

- 把 AI 当作 productivity enhancer：在原组织结构里给每个人加 copilot。
- 把公司重构为 intelligence-native organization：让 world model 和 intelligence layer 成为公司运转结构的一部分。

### 2.2 Block 模型

文章提出 Block 需要两类关键模型：

- company world model：从远程工作产生的决策、讨论、代码、设计、计划、问题和进展中持续理解公司自身运行状态。
- customer world model：基于 Cash App、Square 等交易与经营数据理解客户真实经济活动。

在这个模型下，人的角色被归纳为三类：

- IC：深度专家，围绕能力、模型、智能层和界面建设。
- DRI：对跨域问题或客户结果负责，按问题调动资源。
- player-coach：同时做事和培养人，替代主要负责信息路由的传统 manager。

### 2.3 背景事件

2026-02，Block 宣布裁掉 4000 多名员工。Dorsey 在公开 memo / shareholder letter 中把这次调整与 AI 工具、较小且更扁平的团队、以及 intelligence-native company 方向联系起来。PBS/AP 等报道记录了这个背景。

## 3. 可复用信号

1. **组织层级可以被视为信息流问题。**
   对本 repo 的启发不是"减少管理层"，而是把行为资产治理也看成信息路由问题：root AGENTS、repo AGENTS、rules、skills、OpenSpec、wiki、ADR 各自负责什么信息流。

2. **world model 需要真实 artifact。**
   Block 文章强调远程工作产生的可机器读取 artifact。对应到本 repo，可靠上下文应来自 `PROJECT.md`、OpenSpec artifacts、wiki/ops、ADR、tasks 和 evaluation，而不是聊天记忆。

3. **AI 不是简单加速器，可能改变工作结构。**
   对行为资产治理的可复用点是：不要只把 skill / rules 当作更多提示词，而要定义它们在治理栈里的责任边界。

4. **人的角色应更靠近判断、品味、伦理和高风险边界。**
   这支持当前 repo 中"候选、review、accepted、runtime"必须分层的做法：AI 可以整理和路由，但不能把未审定候选规则直接升级成运行时规则。

## 4. 需要修改后再用的部分

- Block 文章是公司组织设计与战略表达，不是 agent governance 规范。不能直接当作 root AGENTS、repo AGENTS 或 skill 的规则来源。
- "AI 替代中层管理"这个表述太强，放到本 repo 容易误导为自动化替代人工 review。这里更适合抽象成"减少信息路由层级，但保留决策边界"。
- 文章把 world model 设想为持续运行系统；本 repo 目前只有文档和人工检索，不应 overclaim 为自动上下文注入或 runtime autonomy。
- Block 的 customer world model 依赖交易数据和业务闭环；本 repo 没有类似高频闭环数据，不能照搬其 compounding signal 论证。

## 5. 尚未形式化

- 未把该文章加入当前 OpenSpec spec requirement。
- 未修改 repo `AGENTS.md`、root `AGENTS.md`、rules 或 skills。
- 未新增 replay harness。
- 未把 `intelligence-native-organization` 提升为 ADR、method page 或正式治理模型。

## 6. Repo target

当前最可能的落点是：

- `openspec/changes/decide-root-governance-alignment/design.md` 的 benchmark / design-review 输入。
- `wiki/ops/behavior-asset-governance-design-trace.md` 的外部参考候选。
- 后续如果要转成正式原则，应走 OpenSpec review，而不是从本 intake 直接落规则。

## 7. Next step

如果继续用于当前 root/repo governance 设计评审，建议只抽取两条低风险原则：

1. 层级与行为资产的核心问题都是信息路由和责任边界。
2. AI 可以辅助路由和整理，但候选规则升级为运行时规则必须经过 review artifact。

其余关于裁员、取消中层管理、company mini-AGI、world model 自动协调的表述，暂时只作为外部案例背景，不进入 repo policy。
