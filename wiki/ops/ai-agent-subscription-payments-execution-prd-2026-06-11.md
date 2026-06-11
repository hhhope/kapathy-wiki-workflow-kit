---
title: ai agent subscription payments execution prd
canonical_object: ai-agent-subscription-payments-execution-prd
artifact_type: ops-trace
layer: ops
domain: account-clearing
ops_area: workflow-trace
status: active
created_at: 2026-06-11
updated_at: 2026-06-11
ai_generated: true
language: zh-CN
source_path: "chat://pm-execution/ai-agent-subscription-payments/2026-06-11"
source_type: conversation
derived_from:
  - wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md
  - wiki/ops/ai-agent-subscription-payments-product-strategy-2026-06-11.md
---

# AI Agent 订阅支付 / Execution PRD

## Execution Route

- 使用路线：`pm-execution:create-prd` 为主，合并 `user-stories` 和 `sprint-plan`
  的执行拆解。
- 当前阶段：从 strategy 进入验证型 MVP 规划。
- 输出边界：本页是执行草案，不是已批准开发范围，不替代真实客户访谈、支付合规评审
  或工程技术设计。

## 1. Summary

本 PRD 草案定义一个 AI Agent 服务商的收入泄漏诊断与 concierge 计费 MVP。目标是在不
自建支付通道、不做真实资金分账的前提下，验证目标客户是否愿意为 `订阅 + 用量计费 +
续费恢复` 付费。

第一版重点不是做完整计费平台，而是帮助 3 家真实试点客户跑完一个完整账期，并证明
产品能减少未计费用量损失、恢复失败续费或提升套餐升级机会。

## 2. Contacts

| Role | Owner | Comment |
|---|---|---|
| Product | TBD | 负责客户访谈、范围取舍、PRD 维护 |
| Engineering | TBD | 评估用量事件采集、账单规则和报表实现 |
| Design | TBD | 设计诊断表、定价配置流和账单解释体验 |
| Legal / Compliance | TBD | 判断支付、分账、资金链路边界 |
| Pilot Customer Owner | TBD | 维护 3 家试点客户关系和反馈 |

## 3. Background

AI Agent 产品的收入模型正在从固定订阅走向混合计费。Agent 的真实成本会随 token、
调用、任务、模型选择和重试行为波动。很多技术团队可以接入支付网关，但缺少把用量、
成本、套餐、续费和账单解释连起来的能力。

为什么现在：

- AI Agent 使用量更不稳定，固定订阅更容易出现重度用户亏损；
- 客户开始接受额度、credit、用量包和超额计费；
- 通用订阅工具不理解 Agent 用量语义；
- 早期团队还没准备好自建账务系统。

## 4. Objective

目标：验证 AI Agent 服务商是否愿意为垂直收入基础设施付费。

客户收益：

- 看清每个客户的用量、成本和收入关系；
- 快速配置混合计费方案；
- 通过失败重试、宽限期和催缴恢复减少续费损失；
- 用账单解释和对账报表降低人工运营成本。

业务收益：

- 验证首个高痛点细分；
- 获得真实账期数据；
- 判断是否值得进入工程化 MVP。

### Key Results

| KR | Target |
|---|---|
| KR1 | 访谈 20 家 AI SaaS / Agent 团队，至少 8 家确认存在收入泄漏或账单不可解释问题 |
| KR2 | 完成 5 家收入泄漏诊断，至少 3 家愿意进入试点 |
| KR3 | 3 家试点客户跑完一个完整账期 |
| KR4 | 至少 1 家试点客户愿意付费进入第二账期 |
| KR5 | 每家试点客户至少识别 1 个可量化收入保护机会 |

## 5. Market Segments

第一段客户：

- 已有付费用户；
- 月收入约 1 万到 50 万美元；
- 正在从固定订阅转向 `订阅 + 用量包 / 额度 / 超额计费`；
- 团队有 AI SaaS、垂直 Agent、AI workflow 或 API 包装产品；
- 当前靠 Stripe / Paddle / Chargebee、表格、日志或人工对账处理计费。

客户约束：

- 不想迁移所有支付；
- 不愿把资金链路交给不清楚合规边界的新平台；
- 需要快速看到一个账期内的价值；
- 工程资源紧张，不能为计费系统排大项目。

## 6. Value Propositions

### VP1: 收入泄漏诊断

客户当前不知道哪些用户正在造成亏损、哪些用量没有被正确计费、哪些失败扣款没有恢复。
MVP 提供一个结构化诊断表，把 MRR、模型成本、套餐额度、失败续费和用量分布放在一起。

结果：客户能在 1 小时内看到主要收入泄漏点。

### VP2: 混合计费配置

客户想尝试订阅、额度包、超额计费、席位计费，但不想自研账务系统。
MVP 用配置原型帮助客户描述当前套餐和目标套餐，输出人工可执行的计费规则。

结果：客户能判断新套餐是否值得工程化。

### VP3: 一个账期 concierge

客户需要真实跑账期才能相信价值。MVP 用人工 + 半自动方式跑一次账期，完成用量导入、
账单计算、异常说明和续费恢复建议。

结果：客户获得一次可审查的账单和收入保护结果。

## 7. Solution

### 7.1 UX / Prototype

第一版只需要 4 个工作表或轻量界面：

1. 收入泄漏诊断表：输入 MRR、套餐、模型成本、客户用量、失败扣款。
2. 用量导入模板：按客户、时间、usage unit、成本、关联订阅记录用量。
3. 定价规则配置表：固定月费、额度、超额单价、席位、宽限期、重试策略。
4. 账期报告：客户级收入、成本、毛利风险、未计费用量、失败续费和建议动作。

### 7.2 Key Features

#### Feature A: Pilot Intake

- 收集客户当前套餐、支付工具、模型供应商、用量来源和账单周期。
- 标记是否存在失败扣款、超额用量、人工对账或分润需求。

#### Feature B: Usage Ledger MVP

- 接收 CSV 或手工导入的 token / 调用 / 任务 / 席位 / 额度消耗。
- 关联到客户、订阅计划和账期。
- 计算估算成本和可计费用量。

#### Feature C: Billing Rule Prototype

- 支持固定月费、额度包、超额计费和席位计费。
- 支持宽限期、失败重试次数、催缴动作记录。
- 输出账单计算明细，而不是直接扣款。

#### Feature D: Revenue Recovery Report

- 展示未计费用量损失；
- 展示失败扣款和可恢复金额；
- 展示高风险毛利客户；
- 输出升级、催缴或套餐调整建议。

#### Feature E: Concierge Playbook

- 记录每个试点客户的账期操作步骤；
- 记录异常、人工判断和客户反馈；
- 形成后续自动化需求。

### 7.3 Technology

第一版不要求完整后端。可用表格、脚本和轻量 dashboard 完成验证。

技术边界：

- 不接管真实扣款；
- 不做真实资金分账；
- 不存储敏感支付凭证；
- 用客户脱敏用量数据跑账期；
- 支付状态可从客户现有系统导出。

### 7.4 Assumptions

- 客户愿意提供脱敏用量和账单数据；
- CSV / 手工导入足以跑首批试点；
- 一个账期内能量化收入保护；
- 账单解释比自动扣款更适合作为第一版信任入口；
- 支付伙伴可在下一阶段解决资金链路。

## 8. Release

### V0: Discovery Pack

相对周期：1 周。

范围：

- 访谈脚本；
- 收入泄漏诊断表；
- 试点筛选标准；
- concierge 账期操作清单。

### V1: Concierge Billing MVP

相对周期：2-3 周。

范围：

- 用量导入模板；
- 计费规则配置表；
- 账期报告模板；
- 3 家试点客户跑账期；
- 收入保护结果复盘。

### V2: Semi-Automated MVP

相对周期：4-6 周，取决于 V1 结果。

范围：

- 基础用量 ledger；
- 规则配置 UI；
- 账单报告生成；
- 支付状态导入；
- 续费恢复 workflow。

不进入 V1：

- 真实扣款；
- 资金分账；
- 税务计算；
- 多支付通道聚合；
- 完整自助注册。

## User Stories

### Story 1: Revenue Leakage Diagnosis

As an AI Agent founder, I want to enter my revenue, model costs, plans, failed payments, and usage data, so that I can see where revenue is leaking.

Acceptance criteria:

1. The template captures MRR, plan name, included quota, overage price, model cost, and failed payment amount.
2. The template can mark customers with high usage but low revenue.
3. The output shows at least one suspected leakage type per flagged customer.
4. The output can be reviewed without connecting a payment account.

### Story 2: Usage Ledger Import

As an operator, I want to import customer usage by account and billing period, so that usage can be matched to a subscription plan.

Acceptance criteria:

1. The import format includes customer id, period, unit type, quantity, estimated cost, and source.
2. The system or spreadsheet flags missing customer id, period, or quantity.
3. The ledger can group usage by customer and billing period.
4. The ledger preserves raw imported rows for audit.

### Story 3: Hybrid Billing Rule Configuration

As a product owner, I want to configure fixed subscription, included quota, overage price, and seat rules, so that I can test a new pricing plan before engineering it.

Acceptance criteria:

1. The configuration supports fixed monthly fee.
2. The configuration supports included quota and overage unit price.
3. The configuration supports seat count when provided.
4. The output shows calculated invoice amount and usage assumptions.
5. The configuration marks unsupported rules clearly.

### Story 4: Failed Renewal Recovery Review

As a founder, I want to see failed renewals and suggested recovery actions, so that I can recover revenue before canceling accounts.

Acceptance criteria:

1. The report lists failed payment customers by billing period.
2. Each failed payment has amount, status, and suggested action.
3. The report separates failed payment recovery from product churn.
4. The report records whether action was taken and what happened.

### Story 5: Pilot Account Closeout

As the pilot owner, I want a final closeout report for each pilot customer, so that I can decide whether the customer should continue.

Acceptance criteria:

1. The report includes revenue protected, leakage found, manual effort, and customer feedback.
2. The report lists what was automated, manual, and unsupported.
3. The report includes a continue / stop / redesign recommendation.
4. The report states proof boundary and unresolved assumptions.

## Sprint Plan

Sprint goal：完成 V0 Discovery Pack，并让至少 3 家潜在客户可以进入 concierge 试点评估。

Duration：1 week。

Assumed capacity：10 story points，保留 20% buffer。

| Story | Points | Owner | Dependencies |
|---|---:|---|---|
| Revenue Leakage Diagnosis | 3 | Product + Design | Strategy page |
| Usage Ledger Import | 2 | Product + Engineering | Sample usage fields |
| Hybrid Billing Rule Configuration | 2 | Product + Engineering | ICP pricing assumptions |
| Failed Renewal Recovery Review | 1 | Product | Payment-status export assumptions |
| Pilot Account Closeout | 1 | Product | Pilot criteria |

Committed：9 points。Buffer：1 point。

Risks:

- 客户不愿提供数据 -> 允许脱敏样例，先跑结构化诊断。
- 用量字段不统一 -> 第一版只支持 CSV 模板，不做 API 集成。
- 支付合规边界不清 -> 第一版只输出账单建议，不执行扣款或分账。
- 范围膨胀到完整平台 -> V1 前不得做真实支付、税务或 marketplace 分账。

## Open Questions

- 试点客户优先选择 B2B AI SaaS 还是垂直 Agent 服务？
- 是否允许客户用假名或脱敏 customer id 参与诊断？
- 第一版收入保护金额按估算还是客户确认口径记录？
- 失败续费恢复是否只看支付失败，还是包括额度耗尽后的升级转化？

## Proof Boundary

本页把产品战略转成执行草案和首个 sprint 计划。它没有完成客户验证、合规评审、
工程估算或真实账期试点。任何工程实现前仍需要基于客户数据和技术约束重新确认范围。
