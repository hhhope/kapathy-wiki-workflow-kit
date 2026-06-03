---
layer: sources
domain: unclassified
classification_needed: true
source_type: external-docs
artifact_type: source-learning-note
canonical_object: ddd-payment-domain-modeling-prior-art
title: ddd-payment-domain-modeling-prior-art / payment-taxonomy / 2026-06-03
status: candidate-observation
created_at: 2026-06-03
source_title: "DDD 参考资料与支付平台公开文档"
source_author: "Eric Evans; Martin Fowler; Microsoft Learn; Stripe; Adyen; Airwallex"
source_date: unknown
source_url: "https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf; https://martinfowler.com/bliki/BoundedContext.html; https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis"
---

# DDD 支付领域建模学习记录

## 来源参考

- Eric Evans, `Domain-Driven Design Reference`: <https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf>
- Martin Fowler, `Bounded Context`: <https://martinfowler.com/bliki/BoundedContext.html>
- Microsoft Learn, `Use Domain Analysis to Model Microservices`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis>
- Microsoft Learn, `Use Tactical DDD to Design Microservices`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design>
- Microsoft Learn, `Identify microservice boundaries`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries>
- Stripe docs: <https://docs.stripe.com/>
- Stripe Connect: <https://docs.stripe.com/connect>
- Stripe Billing: <https://docs.stripe.com/billing>
- Adyen API Explorer: <https://docs.adyen.com/api-explorer>
- Airwallex docs: <https://www.airwallex.com/docs/>
- Airwallex Connected Accounts: <https://www.airwallex.com/docs/connected-accounts__how-connected-accounts-work>
- 前置本地记录：`wiki/sources/payment-domain-taxonomy-prior-art-stripe-adyen-airwallex-2026-06-03.md`
- 访问日期：2026-06-03

## 来源分类

| 字段 | 判断 |
|---|---|
| 来源类型 | 一手 DDD 参考 + 厂商公开文档 |
| 主题 | DDD 风格的支付领域 taxonomy |
| 本地相关性 | 对 requirements taxonomy 重构相关性高 |
| 回溯评分 | 84 / 100 |
| 深读结论 | 可用于领域骨架 proposal；没有 OpenSpec 和 owner 评审前，不足以修改 taxonomy |

## 复用的 DDD 原则

本仓库不应默认把产品导航、API 分组或流程步骤当成一级领域。

可复用的 DDD 约束：

- 领域是软件所服务的业务问题空间。
- 模型是为了特定目的，对领域中的一部分进行选择和抽象。
- 限界上下文拥有自己的模型和语言边界。
- 大系统不应强行用一个统一模型覆盖所有区域。
- 同一个词在不同上下文里可能含义不同，例如 `account` 在客户入驻、支付余额、会计账本、平台身份里含义不同。
- 边界应跟随业务能力和领域关注点，而不是技术层或 API 导航。
- 聚合和领域服务是后续战术设计对象，不应拿来命名第一版领域骨架。
- DDD 是迭代式的。先有粗粒度领域骨架，再继续拆更细的上下文，是可以接受的。

## DDD 视角下的三家公司差异

### Stripe

Stripe 的公开模型更偏收入平台。`Payments`、`Billing`、`Connect` 作为独立产品界面出现；从 DDD 视角看，它们提示了不同的限界上下文：

- 支付受理和授权；
- 客户计费、订阅、价格、发票、用量生命周期；
- 平台和 marketplace 关系管理；
- 余额、transfer、payout、reconciliation 工作流；
- 风险、税务、身份、发卡、资金管理等相邻专门上下文。

本地启发：Stripe 是最强证据，说明订阅计费不是支付下面的小功能。它有自己的语言、生命周期、聚合候选和失败模式。

### Adyen

Adyen 的公开模型更偏收单与平台运营。它的文档强调 online/in-person payments、recurring、payouts、platforms、balance platform、issuing、business accounts、risk、reports、reconciliation。

DDD 解读：

- Adyen 把商户收单和支付方式受理放在中心。
- 平台工作接近 account holder 入驻、balance accounts、payout schedules、issuing、运营报表。
- reports 和 reconciliation 等财务运营能力，是支付流周边的运营上下文，不是 checkout 的同一个模型。

本地启发：Adyen 对商户、支付、收单、平台运营的参考价值更强；对订阅收入建模的参考价值弱于 Stripe。

### Airwallex

Airwallex 的公开模型更偏账户与资金流转。它呈现 Connected Accounts、Accounts、Payments、Billing、FX、Payouts、Issuing、Spend、Global Treasury、BaaS、Payments for Platforms。

DDD 解读：

- connected-account 关系是很强的限界上下文候选，因为它定义谁拥有资金、谁执行操作、适用什么合规要求，以及平台与客户责任如何拆分。
- wallet、多币种账户、FX、payout、issuing、spend 是不同的资金操作上下文；它们共享账户身份，但模型不同。
- Payments for Platforms 组合了支付受理、connected-account 归属、split/routing、payout、FX、合规。

本地启发：Airwallex 对账户归属、钱包、多币种资金流转、平台代客户操作、监管责任边界的参考价值最强。

## 本地领域骨架候选

这不是 taxonomy 变更，而是一个 DDD-informed 的 OpenSpec proposal 候选。

### 商户与平台关系

负责商户、平台、服务方身份，入驻，资质，能力开通，平台责任，以及平台与客户之间的关系规则。

为什么这是领域：同一个参与方可能是商户、平台客户、connected account holder、服务方或结算接收方。身份含义取决于关系和责任。

### 支付交易

负责支付订单、支付方式、授权、capture、扣款、退款、拒付、状态收敛、重试，以及支付侧失败语义。

为什么这是领域：它拥有一次支付尝试的生命周期，以及资金是否成功收取或冲正的规则。

### 计费与收入

负责客户订阅、价格、用量、席位、发票、出账、催缴、宽限期、收入恢复，以及收入确认的交接。

为什么这是领域：订阅和用量计费在支付执行前后都有自己的生命周期。业务问题不只是“能否扣款”，还包括“这个客户在什么计划下、什么时候、应该欠多少钱，以及失败收入如何恢复”。

### 账户与余额

负责支付账户、钱包、余额、可用/在途/冻结资金、账本视图、归属权和账户能力。

为什么这是领域：账户状态不同于支付状态或发票状态。它承载资金可用性和归属语义。

### 资金流转与结算

负责 transfer、payout、提现、split、结算批次、结算周期、平台费分配、接收方结算和外部银行资金移动。

为什么这是领域：支付收取之后，资金需要在归属和责任规则下进行移动、拆分、排期和结算。

### 财务运营

负责清分证据、对账、报表、费用核算、异常处理、财务关账支持和运营可审计性。

为什么这是领域：对账和报表不是结算执行本身。它们回答的是“发生了什么、为什么匹配或不匹配、财务能否关账”。

### 风险与合规

负责 KYC/KYB、AML、制裁、欺诈、交易监控、退款/拒付风险、自动扣款授权约束、税务/合规证据和消费者保护。

为什么这是领域：它横跨支付、平台、计费和结算，但有自己的规则、决策和问责边界。

### 嵌入式金融产品

当平台从支付和结算扩展到金融产品时，负责 issuing、treasury、cards、capital、spend 等受监管金融产品。

为什么这是领域：这些能力有独立的产品经济性、监管要求、账户状态和生命周期，不应强行塞进普通支付受理。

## Agent 订阅支付的本地映射

Agent 订阅支付需求不应成为独立一级领域。在这个骨架下：

- 主领域：`计费与收入`；
- 支撑领域：`支付交易`、`商户与平台关系`、`资金流转与结算`、`财务运营`、`风险与合规`；
- 条件领域：如果涉及钱包、余额或类托管行为，则进入 `账户与余额`；
- 默认不在范围内，除非明确要求：`嵌入式金融产品`。

## 未正式化内容

- 未修改 requirements taxonomy 文件。
- 本记录没有创建 OpenSpec proposal。
- 上述中文领域名只是候选标签，不是最终 YAML ID。
- 本记录不决定现有 `account`、`clearing`、`settlement` 应保留、重命名、嵌套还是迁移。
- 本记录不定义聚合、实体或领域服务。

## 下一步

OpenSpec proposal `reshape-requirements-domain-taxonomy` 应定义：

- 领域、子域、能力、case slug 的区别；
- 候选领域提升为 taxonomy 值的验收标准；
- 当前 `account`、`clearing`、`settlement` 的兼容策略；
- 支付生态的 DDD context map 草案；
- Agent 订阅支付材料在新骨架下的具体映射。

证明边界：本学习记录把 DDD 参考资料和厂商公开文档转化为本地候选推理。它不是已批准的 taxonomy，不是 requirements readiness gate 变更，也不是行为规则。
