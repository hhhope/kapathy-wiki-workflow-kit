---
layer: sources
domain: unclassified
classification_needed: true
source_type: external-docs
artifact_type: source-learning-note
canonical_object: payment-domain-taxonomy-prior-art
title: payment-domain-taxonomy-prior-art / stripe-adyen-airwallex / 2026-06-03
status: candidate-observation
created_at: 2026-06-03
source_title: "Stripe、Adyen、Airwallex 公开文档"
source_author: "Stripe; Adyen; Airwallex"
source_date: unknown
source_url: "https://docs.stripe.com/; https://docs.adyen.com/api-explorer; https://www.airwallex.com/docs/"
---

# Stripe / Adyen / Airwallex 支付领域划分学习记录

## 来源参考

- Stripe API 与产品文档：<https://docs.stripe.com/>
- Stripe Connect: <https://docs.stripe.com/connect>
- Stripe Billing 与用量计费：<https://docs.stripe.com/billing>
- Stripe 报表与出款对账：<https://docs.stripe.com/reports/balance>, <https://docs.stripe.com/payouts/reconciliation>
- Adyen API Explorer: <https://docs.adyen.com/api-explorer>
- Airwallex 产品文档：<https://www.airwallex.com/docs/>
- Airwallex Connected Accounts：<https://www.airwallex.com/docs/connected-accounts__how-connected-accounts-work>
- Airwallex Payments for Platforms：<https://www.airwallex.com/docs/payments-for-platforms__understanding-payments-for-platforms>
- 访问日期：2026-06-03

## 来源分类

| 字段 | 判断 |
|---|---|
| 来源类型 | 一手来源 / 公开产品文档 |
| 主题 | 支付生态领域建模参考 |
| 本地相关性 | 对 requirements taxonomy 重构相关性高；但不能直接作为本地 taxonomy 值来源 |
| 回溯评分 | 78 / 100 |
| 深读结论 | 可作为 prior art；没有领域 owner 评审前，不足以定稿本地 taxonomy |

## 观察结论

三家公司公开文档都围绕支付受理、平台账户、计费、出款、发卡、风险、报表等能力组织产品和 API。它们的导航结构能证明能力簇存在，但本身不是干净的领域模型。

Stripe 更偏产品线组织：Payments、Billing、Connect、Tax、Revenue Recognition、Radar、Issuing、Treasury、Terminal、Financial Connections 和报表能力，都以产品或 API family 的形式出现。

Adyen 更偏收单与平台运营组织：Online Payments、In-person Payments、Payouts、recurring、Platforms、Balance Platform、card issuing、business accounts、risk、disputes、reports、reconciliation 等，以 API 或 guide family 的形式出现。

Airwallex 更偏账户与全球资金流组织：Connected Accounts、Accounts、Payments、Billing、Transactional FX、Payouts、Issuing、Spend、Global Treasury、Banking as a Service、Payments for Platforms 等，以产品或 use case family 的形式出现。

## 现场评审修正

第一次本地抽取错误地把公开产品功能直接变成了候选一级领域。以下候选都偏弱：

- `clearing_reconciliation`
- `subscription_payments`
- `marketplace_settlement`
- `agent_subscription_payments`

这些名字太接近功能、场景或 case slug。没有显式领域建模之前，不应成为 requirements taxonomy 的一级领域。

## 可复用认识

可复用的 prior art 信号：

- 成熟支付公司会区分面向客户的支付受理、平台赋能、计费/收入、账户或余额状态、资金流转、风险/合规、财务运营等能力。
- 公开文档通常混合了多个分类轴：产品包装、API 资源、运营流程、受监管实体模型、使用场景。
- 本地 requirements taxonomy 必须先选择一个主分类轴，再定义子域；否则会把功能、流程和场景混在一起。

## 本地化改造点

对本仓库来说，下一步不是复制任何一家厂商的产品导航，而是先定义：

- 一级领域的分类轴；
- 什么算领域，什么算子域，什么算能力；
- `account`、`clearing`、`settlement` 是并列领域，还是更大支付生态模型里的生命周期阶段；
- 平台/生态类工作如何关联账户、支付、结算、计费、风险、运营。

## 未正式化内容

- 未修改 `requirements/config/requirements-taxonomy.yaml`。
- 本学习记录没有创建 OpenSpec change。
- 没有把任何厂商产品导航提升为本地 `SHALL`。
- 不声称三家公司共享同一个一致领域模型。
- 不声称 `clearing_reconciliation` 或类似功能形态标签可以作为本地领域。

## 本仓库用途

这条记录作为后续 requirements taxonomy OpenSpec change 的输入证据。它的用途是：在处理新的支付生态需求前，先重建 requirements domain 骨架。

## 下一步

修改 requirements taxonomy 前，先创建或选择一个 OpenSpec change。设计阶段应先定义领域骨架，再分配子域和能力标签。厂商文档只能作为 prior art，不能直接照抄成领域模型。

证明边界：本记录只保留外部来源学习和现场评审修正。它不验证最终领域 taxonomy，也不授权修改 taxonomy 配置。
