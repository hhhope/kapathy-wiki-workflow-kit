---
title: ai agent subscription payments product discovery
canonical_object: ai-agent-subscription-payments-product-discovery
artifact_type: ops-trace
layer: ops
domain: account-clearing
ops_area: workflow-trace
status: active
created_at: 2026-06-11
updated_at: 2026-06-11
ai_generated: true
language: zh-CN
source_path: "chat://pm-product-discovery/ai-agent-subscription-payments/2026-06-11"
source_type: conversation
---

# AI Agent 订阅支付 / Product Discovery

## 触发场景

用户用 `$pm-product-discovery` 提供了智能体服务订阅支付的市场背景和痛点：
支付门槛高、续费率低、计费模式单一、分账结算复杂。初次回答只停留在聊天
内，随后用户指出这类 skill 输出需要记录 wiki，并要求改造工作流。

## Product Discovery Route

- 使用路线：PM/product-discovery opportunity framing、assumption mapping、lean
  experiment planning。
- repo 路由：本记录作为产品发现工作记忆落入 `wiki/ops/`，不作为外部来源学习
  笔记，也不作为已验证市场结论。
- OpenSpec 改造：`openspec/changes/route-product-discovery-through-wiki-capture`。

## Target Segment / ICP

优先 ICP：

- 月收入约 1 万到 50 万美元；
- 已有付费用户；
- 正在从固定订阅转向 `订阅 + 用量包 / 额度 / 超额计费`；
- 团队有 AI Agent、AI SaaS、垂直 Agent 服务或 AI workflow 产品；
- 当前支付能力依赖通用支付网关、手写脚本或人工对账。

暂缓 ICP：

- 大型 AI 应用市场；
- 复杂多方真实资金分账平台；
- 强监管金融交易或资金清分场景。

原因：这些需求大，但合规、结算、销售周期会显著放大早期 MVP 范围。

## Opportunity Framing

核心机会不是普通支付网关，而是面向 AI Agent 产品的
`AI-native Revenue OS`：把成本、用量、订阅、续费、账单和分润报表连起来。

优先机会：

1. 服务商无法稳定把 AI token / API 成本转嫁给客户。
2. 服务商不会做完整订阅生命周期、失败重试、宽限期和催缴恢复。
3. 固定订阅无法支撑 Agent 的用量波动，需要混合计费。
4. 平台型 Agent 收入需要分给开发者或服务方，但早期不宜直接做真实资金清分。

## Assumptions And Risks

| Assumption | Risk | Suggested Test |
|---|---|---|
| AI Agent 服务商愿意为垂直计费工具付费 | 高 | 20 家目标客户访谈 + 预付费试点 |
| 通用 Stripe / Chargebee / Paddle 方案不能满足 Agent 场景 | 高 | 对比客户当前计费配置和缺口 |
| token / 调用量数据可以稳定、可信、低成本采集 | 中高 | 接 2-3 个主流模型或 API 做 PoC |
| 续费率低主要由支付和订阅运营导致 | 高 | 拆分失败支付、主动取消、沉默流失 |
| 分账是早期刚需 | 中 | 先验证报表分账是否足够 |
| 合规可通过支付伙伴解决 | 高 | 早期法律 / 支付伙伴评估 |

## Validation Experiments

1. 访谈 20 家 AI SaaS / Agent 团队，确认是否存在用户越活跃越亏损、账单不可
   预测、续费恢复薄弱等真实案例。成功阈值：至少 8 家有明确痛感，至少 3 家
   愿意接入试点。
2. Concierge MVP：用现成支付通道 + 手工账单配置，为 3 家团队跑一个月订阅与
   续费恢复。成功阈值：至少 1 家愿意付费继续使用。
3. 无代码定价配置原型：让客户现场配置固定月费、额度包、超额计费、席位计费
   和企业账单。成功阈值：80% 目标客户能在 10 分钟内配置当前或目标定价模型。
4. 分账先做报表，不做资金清分。成功阈值：2 家 marketplace 型客户愿意用报表
   做内部结算。

## What Was Not Formalized

- 本页不验证市场规模。
- 本页不形成 PRD 或 OpenSpec 产品需求。
- 本页不把任何外部报道或搜索结果晋升为 repo 规则。
- 本页不批准真实分账、资金归集或清结算能力建设。

## Next Step

围绕优先 ICP 做客户访谈脚本，重点问事实问题：

- 当前月 AI 成本占收入比例是多少；
- 是否有用户用量导致亏损；
- 最近 3 个月失败续费、主动取消、沉默流失分别占比多少；
- 当前是否已经尝试混合计费或用量包；
- 是否愿意为订阅 + 用量计费 + 续费恢复试点付费。

## Proof Boundary

这是一份产品发现工作记忆，只保留当前机会判断、假设和验证路线。它不是市场
事实报告、投资建议、合规建议或已批准产品方案。
