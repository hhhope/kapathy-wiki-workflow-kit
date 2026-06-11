---
title: agentic loan repayment revenue platform execution prd
canonical_object: agentic-loan-repayment-revenue-platform-execution-prd
artifact_type: ops-trace
layer: ops
domain: account-clearing
ops_area: workflow-trace
status: active
created_at: 2026-06-11
updated_at: 2026-06-11
ai_generated: true
language: zh-CN
source_path: "chat://agentic-loan-repayment-revenue-platform/execution-prd/2026-06-11"
source_type: conversation
derived_from:
  - wiki/ops/ai-agent-subscription-payments-execution-prd-2026-06-11.md
  - wiki/ops/loan-repayment-order-data-execution-prd-2026-06-11.md
  - wiki/ops/agentic-loan-repayment-revenue-platform-product-discovery-2026-06-11.md
  - wiki/ops/agentic-loan-repayment-revenue-platform-product-strategy-2026-06-11.md
---

# 贷款还款 Agent 收入平台 / Execution PRD

## Trigger

用户要求把 Agent 支付与贷款还款订单数据增收结合，形成一套新的执行文档。

## Route

- `pm-execution:create-prd`
- repo-local `product-discovery-wiki-capture`
- repo-local `wiki-frontmatter-taxonomy`

## 1. Summary

本 PRD 定义一个面向贷款机构和贷款服务商的“贷款还款 Agent 收入平台”。产品用 Agent 辅助处理还款失败、账单解释、复贷候选和对账差错，并记录 Agent 任务、人工确认、业务结果和计费依据。

MVP 不做自动授信、自动定价、真实资金清分或无人审批触达。第一版做历史订单 Agent 回放、人机协同试点和模拟账单。

## 2. Contacts

| Role | Owner | Comment |
|---|---|---|
| Product | 待定 | 负责范围、指标、取舍 |
| Data / Analytics | 待定 | 负责订单事实层、回放、归因 |
| Agent Engineering | 待定 | 负责 Agent 任务、提示、评估、审计 |
| Billing / Payment Product | 待定 | 负责计费项、账单、分账报表 |
| Compliance / Legal | 待定 | 负责数据用途、触达、复贷、输出边界 |
| Customer Success | 待定 | 负责试点客户和运营复盘 |

## 3. Background

单独做 AI Agent 支付，会停在“Agent 服务商怎么收钱”。单独做贷款还款数据增收，会停在“订单数据怎么降本增收”。组合后，产品可以回答更具体的问题：

> 当 Agent 真正参与贷款还款运营后，它做了哪些任务、影响了哪些订单、带来了多少恢复金额或节省，并应该如何向客户收费？

这个组合适合从贷款还款生命周期切入，因为该场景具备：

- 高频订单；
- 明确结果；
- 可回放历史数据；
- 运营动作重复；
- 对账和客服成本可量化；
- B 端付费意愿更容易验证。

## 4. Objective

目标：

> 验证贷款客户是否愿意为可审计、可归因、可计费的还款 Agent 运营服务付费。

### Key Results

1. 完成 2 个客户的历史订单 Agent 回放。
2. 至少 1 个客户完成一个还款周期人机协同试点。
3. Agent 建议人工通过率达到客户可接受水平。
4. 至少证明 1 个增量价值：
   - 失败还款恢复；
   - 对账差错追回；
   - 客服工单下降；
   - 复贷候选转化。
5. 输出一份客户认可的模拟账单或试点账单。

## 5. Market Segment(s)

### Primary Segment: 消费金融 / 小贷 / 助贷平台

使用者：

- 贷后运营负责人；
- 客服负责人；
- 财务对账负责人；
- 产品运营负责人；
- 数据负责人。

核心约束：

- 数据敏感；
- 触达要受控；
- 复贷要合规；
- 账单和结果要可解释。

### Secondary Segment: 贷款科技 / 贷后服务商

使用者：

- 解决方案负责人；
- 交付负责人；
- 客户成功负责人；
- 商务负责人。

核心约束：

- 多租户；
- 白标；
- 客户之间数据隔离；
- 机构账单和分账报表。

### Partner Segment: 支付 / 清算服务商

使用者：

- 金融行业方案负责人；
- 通道产品负责人；
- 清算产品负责人。

核心约束：

- 不越界成为贷款决策方；
- 不直接处理未经授权的个人金融数据；
- 需要和贷款机构业务系统配合。

## 6. Value Proposition(s)

### Job 1: 我想让 Agent 预处理还款失败订单

收益：

- 更快分类；
- 更快生成下一步建议；
- 人工只处理高价值或高风险订单；
- 宽限期内恢复更多金额。

### Job 2: 我想知道 Agent 到底创造了多少价值

收益：

- 每个 Agent 动作都有任务记录；
- 每个动作关联订单、人工确认和结果；
- 可以生成账单和 ROI 报告；
- 方便内部立项和外部收费。

### Job 3: 我想用 Agent 降低账单解释和客服成本

收益：

- 自动生成账单解释草稿；
- 客服回答更一致；
- 减少重复咨询；
- 降低扣款误解和投诉。

### Job 4: 我想用 Agent 找对账差错

收益：

- 自动筛查还款成功未销账、冲正、退回、手续费异常；
- 每条差错有证据路径；
- 财务可以确认和追回。

## 7. Solution

### 7.1 User Flow

1. 客户提交脱敏历史订单样本。
2. 系统建立订单事实层。
3. 客户选择试点 Agent：
   - 还款失败挽回 Agent；
   - 账单解释 Agent；
   - 对账差错 Agent；
   - 复贷候选 Agent。
4. Agent 对历史订单回放，生成建议和证据。
5. 客户人工标注建议是否可用。
6. 系统生成 Agent 任务账本和模拟计费单。
7. 进入一个还款周期人机协同试点。
8. 试点结束后生成价值归因报告和正式报价。

### 7.2 Key Features

#### Feature A: Loan Order Fact Layer

功能：

- 导入放款订单；
- 导入还款计划；
- 导入还款订单；
- 导入渠道流水；
- 导入清算结果；
- 关联同一客户、同一贷款、同一期还款。

验收：

- 能输出字段质量报告；
- 能输出订单链路匹配率；
- 能标记缺失字段和不可用字段。

#### Feature B: Agent Task Ledger

功能：

- 记录 Agent 任务类型；
- 记录触发订单；
- 记录输入字段；
- 记录输出建议；
- 记录人工确认结果；
- 记录后续业务结果。

验收：

- 每个 Agent 输出都能回放；
- 每个收费项都能追到任务和订单；
- 敏感字段访问有审计记录。

#### Feature C: Repayment Recovery Agent

功能：

- 失败原因分类；
- 重试建议；
- 渠道建议；
- 提醒和解释草稿；
- 宽限期优先级队列；
- 结果归因。

验收：

- 能生成待处理队列；
- 人工可确认、修改或拒绝建议；
- 能统计 24/72 小时恢复结果。

#### Feature D: Bill Explanation Agent

功能：

- 解释应还、实还、罚息、手续费、提前还款、部分还款；
- 解释扣款失败原因；
- 生成客服回复草稿；
- 生成客户自助页内容草稿。

验收：

- 客服可一键采用或修改；
- 输出不得承诺不确定结果；
- 输出必须引用订单事实。

#### Feature E: Reconciliation Agent

功能：

- 识别还款成功未销账；
- 识别渠道退回、冲正、退款；
- 识别手续费异常；
- 生成证据包；
- 记录追回结果。

验收：

- 每条差错包含订单、渠道流水、规则命中原因；
- 财务可确认或驳回；
- 能统计追回金额和人工节省。

#### Feature F: Agent-native Billing

功能：

- 定义计费项：
  - Agent 任务；
  - 还款订单；
  - 客户租户；
  - 恢复金额；
  - 差错追回；
  - SaaS 模块。
- 生成模拟账单；
- 生成分账报表；
- 生成客户 ROI 报告。

验收：

- 账单可追溯到 Agent 任务；
- 支持试点期人工确认；
- 不做真实资金清分。

### 7.3 Technology Notes

MVP 技术原则：

- 批量导入优先，实时接口后置；
- 人机协同优先，自动执行后置；
- 规则 + LLM 草稿优先，复杂模型后置；
- 模拟账单优先，真实资金清分后置；
- 审计和权限前置。

### 7.4 Assumptions

- 客户愿意提供历史订单样本；
- 客户有人工团队可以确认 Agent 建议；
- 贷款还款场景里至少有一个高频、低风险、可量化任务适合 Agent；
- 客户愿意用模拟账单讨论正式收费；
- 合规团队接受 MVP 的人机协同边界。

## 8. Release

### V0: Offline Agent Replay

范围：

- 字段盘点；
- 订单事实层；
- Agent 回放；
- 人工标注；
- 模拟账单；
- 价值归因报告。

不做：

- 生产触达；
- 自动扣款；
- 自动授信；
- 真实分账。

### V1: Human-in-the-loop Pilot

范围：

- 还款失败 Agent 队列；
- 账单解释 Agent 草稿；
- 对账差错 Agent 证据包；
- 人工确认工作台；
- 试点账单。

不做：

- 无人审批触达；
- 跨机构数据共享；
- C 端贷款推荐；
- 外部信用评分。

### V2: Productized Agent Billing Workbench

范围：

- 多租户；
- 白标；
- 模块化 Agent；
- 标准计费项；
- 分账报表；
- 客户 ROI dashboard；
- API 接入。

## User Stories

| User | Story | Acceptance |
|---|---|---|
| 贷后运营负责人 | 我想让 Agent 先筛出失败订单处理优先级 | 队列包含原因、建议、金额、风险和人工确认 |
| 客服负责人 | 我想让 Agent 生成账单解释草稿 | 草稿引用订单事实，可人工修改 |
| 财务负责人 | 我想让 Agent 找出可疑对账差错 | 每条差错有证据包和确认状态 |
| 产品负责人 | 我想知道 Agent 是否值得付费 | 有任务账本、结果归因和模拟账单 |
| 服务商商务 | 我想把 Agent 能力卖给多家贷款机构 | 支持租户、模块和分账报表 |
| 合规负责人 | 我想限制 Agent 使用数据和输出内容 | 有用途记录、权限、审计和禁止动作 |

## Open Questions

1. 第一个试点应选择还款失败、账单解释还是对账差错？
2. 客户能接受哪种计费方式：任务、订单、恢复金额、订阅还是混合？
3. Agent 输出的人工通过率达到多少才可进入生产试点？
4. 哪些触达内容必须人工审批？
5. 分账报表是否足够，还是客户会要求真实资金清分？
