---
title: agentic loan repayment revenue platform product discovery
canonical_object: agentic-loan-repayment-revenue-platform-product-discovery
artifact_type: ops-trace
layer: ops
domain: account-clearing
ops_area: workflow-trace
status: active
created_at: 2026-06-11
updated_at: 2026-06-11
ai_generated: true
language: zh-CN
source_path: "chat://agentic-loan-repayment-revenue-platform/product-discovery/2026-06-11"
source_type: conversation
derived_from:
  - wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md
  - wiki/ops/ai-agent-subscription-payments-product-strategy-2026-06-11.md
  - wiki/ops/loan-repayment-order-data-product-discovery-2026-06-11.md
  - wiki/ops/loan-repayment-order-data-product-strategy-2026-06-11.md
---

# 贷款还款 Agent 收入平台 / Product Discovery

## Trigger

用户确认前一套贷款还款分析后，要求：

> 再把 Agent 支付和这个结合起来再做一套。

本页把两条主线合并：

- AI Agent 支付：订阅、用量计费、续费恢复、分账报表、收入保护。
- 贷款还款订单：还款恢复、复贷生命周期、对账差错、渠道成本、账单解释。

## Route

- `pm-product-discovery:opportunity-solution-tree`
- repo-local `product-discovery-wiki-capture`
- repo-local `wiki-frontmatter-taxonomy`

## Product Concept

产品暂名：

> 贷款还款 Agent 收入与运营平台

一句话：

> 用 Agent 处理贷款还款生命周期中的提醒、解释、挽回、复贷候选、对账差错和运营复盘，并用 Agent-native billing 把 Agent 的任务量、订单量、恢复金额和分账关系转成可收费收入。

关键边界：

- Agent 服务对象是贷款机构、贷款科技服务商、支付/清算服务商，不是直接做 C 端贷款导流。
- 初期不让 Agent 自动授信、自动定价、自动放款或自动催收。
- 初期不做真实资金清分牌照能力，分账先做报表和结算依据。
- 还款订单数据只在客户授权、合同目的和合规评审范围内使用。

## Desired Outcome

在 8-12 周内验证：

> 贷款机构愿意为“可审计的还款 Agent 运营服务 + 可归因的计费/分账系统”付费。

首个 outcome：

- 至少 2 个贷款场景客户完成历史订单 Agent 回放；
- 至少 1 个客户完成一个还款周期 Agent 试点；
- 试点能证明至少一种可收费价值：
  - 失败还款恢复金额；
  - 复贷候选转化；
  - 对账差错追回；
  - 客服工单下降；
  - Agent 服务按任务/订单/效果出账。

## Opportunity Solution Tree

### Opportunity 1: 贷款机构想用 Agent 降低还款运营成本，但无法证明 Agent 值多少钱

客户视角：

> 我可以让 Agent 做提醒、解释、分类、对账和复盘，但我不知道每个 Agent 动作创造了多少收入或节省了多少成本，也不知道怎么向内部或客户收费。

可选方案：

1. Agent Activity Ledger：记录每次 Agent 任务、触发订单、输入数据、输出动作、人工确认和结果。
2. Outcome Attribution：把 Agent 动作和恢复金额、复贷转化、差错追回、客服减少做归因。
3. Agent Billing Meter：按任务、订单、用量、恢复金额、坐席、客户租户生成计费依据。

实验：

- 假设：客户愿意先为“Agent 任务账本 + 价值归因报表”付费，而不是先要求全自动 Agent。
- 方法：拿 3 个月历史订单做 Agent 回放，人工确认 Agent 建议，生成价值归因账单。
- 指标：可归因金额、人工确认通过率、客户愿付费意向。
- 成功阈值：至少 1 个客户愿意为下一周期试点付费。

### Opportunity 2: 还款失败挽回需要高频动作，人工团队做不过来

客户视角：

> 每天有大量还款失败订单，人工只能处理大额或逾期订单。很多失败其实可以通过解释、提醒、重试和渠道建议在宽限期内恢复。

可选方案：

1. Repayment Recovery Agent：识别失败原因，生成下一步动作建议。
2. Customer Explanation Agent：生成账单解释、失败原因解释和下一步说明。
3. Ops Copilot：给人工运营一个确认台，避免 Agent 直接触达高风险客户。

实验：

- 假设：Agent 预处理能提升运营团队处理效率和失败后 72 小时恢复率。
- 方法：历史订单回放 + 小流量人工确认试点。
- 指标：每人每日处理订单数、72 小时恢复率、投诉率、重复触达率。
- 成功阈值：处理效率提升 30%，恢复率提升 5%，投诉率不升高。

### Opportunity 3: 复贷运营需要既懂还款行为，又能控制过度借贷风险

客户视角：

> 我想经营结清和稳定还款客户，但不能简单让 Agent 自动推荐贷款。需要解释候选原因、授权边界、排除原因和后续风险表现。

可选方案：

1. Lifecycle Candidate Agent：生成结清、提前还款、稳定还款、恢复后客户候选池。
2. Compliance Guardrail：记录授权、退订、排除规则、触达原因和人工审批。
3. Campaign Billing：按候选池生成、触达任务、复贷转化或服务包收费。

实验：

- 假设：Agent 生成的复贷候选池能比粗放召回更高效，同时不恶化早期逾期。
- 方法：历史复贷样本回放，先不自动触达。
- 指标：候选命中率、复贷转化、早期逾期、退订/投诉。
- 成功阈值：转化提升 10%，早期逾期不恶化。

### Opportunity 4: 对账和渠道差错适合 Agent 先筛查，但需要可审计证据链

客户视角：

> Agent 可以帮我查还款成功未销账、渠道退回、冲正、手续费异常，但财务不能接受黑盒结论，必须有订单链路和证据。

可选方案：

1. Reconciliation Agent：自动生成差错清单和证据路径。
2. Evidence Packet：每条差错包含平台订单、渠道流水、清算记录、规则命中原因。
3. Recovery Fee Meter：按差错追回金额或处理订单量收费。

实验：

- 假设：Agent 筛查能减少财务人工排查时间，并发现可追回差错。
- 方法：选择一个渠道 3 个月订单做对账回放。
- 指标：差错金额、人工时长、确认准确率、追回金额。
- 成功阈值：人工时长下降 30%，确认准确率达到客户可接受水平。

### Opportunity 5: 贷款科技服务商想把 Agent 能力打包卖给多家贷款机构

客户视角：

> 我有贷款客户和交付团队，想把 Agent 能力做成增值服务，但不知道如何按租户、订单、任务和效果分账。

可选方案：

1. White-label Agent Ops：白标还款 Agent 工作台。
2. Multi-tenant Billing：按机构、产品、Agent 模块、订单量和恢复金额出账。
3. Partner Settlement Report：先给服务商、贷款机构、Agent 模块方生成分账报表，不先做真实清分。

实验：

- 假设：服务商愿意以白标方式采购 Agent + billing 能力。
- 方法：找 2 家贷款科技服务商做 solution walkthrough。
- 指标：愿意转介绍的贷款机构数、白标需求、可接受计费方式。
- 成功阈值：至少 1 家愿意联合试点。

## Prioritized Discovery Backlog

| Rank | Opportunity | Why First | First Evidence |
|---|---|---|---|
| 1 | Agent 任务账本 + 价值归因 | 连接 Agent 支付和贷款增收的核心 | 历史订单 Agent 回放 + 归因账单 |
| 2 | 还款失败 Agent 挽回 | 现金回收最直接，动作高频 | 失败原因、恢复率、人工确认通过率 |
| 3 | 对账差错 Agent | 证据链清晰，合规阻力相对低 | 差错金额、人工时长、确认准确率 |
| 4 | 复贷候选 Agent | 收入潜力高，但合规更敏感 | 授权、排除规则、转化与风险 |
| 5 | 白标多租户计费 | 复制潜力高，复杂度也高 | 服务商联合试点意愿 |

## Critical Assumptions

1. 贷款机构愿意让 Agent 读取脱敏或授权范围内的放款、还款、对账订单。
2. Agent 动作可以被记录、审计、回放，不是不可解释的黑盒。
3. 客户愿意按 Agent 任务、订单量、恢复金额、差错追回或模块订阅付费。
4. 绩效归因可以达成商业共识，即便不是严格因果实验。
5. 合规团队接受“Agent 建议 + 人工确认 + 审计记录”的早期模式。

## Risks

- 合规风险：Agent 触达借款人、生成复贷候选、解释还款义务时必须受控。
- 过度自动化风险：若直接让 Agent 执行扣款、催收、授信或定价，风险会快速放大。
- 归因争议：恢复金额和复贷收入可能与原有运营策略重叠。
- 数据质量风险：订单链路不完整会导致 Agent 判断不稳定。
- 商业复杂度风险：同时卖 Agent、数据、支付、分账，容易范围失控。

## Validation Plan

### Phase 1: Offline Replay

- 输入历史放款、还款计划、还款订单、渠道流水、清算结果；
- Agent 生成失败挽回、账单解释、差错识别、复贷候选；
- 人工标注 Agent 建议是否可用；
- 生成 Agent 任务账本和模拟计费单。

### Phase 2: Human-in-the-loop Pilot

- Agent 只生成建议和草稿；
- 人工确认后执行触达、对账处理或运营动作；
- 系统记录动作、结果、成本和收费依据；
- 结束后输出价值归因报告。

### Phase 3: Commercial Pilot

- 对客户收取试点费；
- 选择一种附加收费模式：
  - 按订单量；
  - 按 Agent 任务；
  - 按恢复金额分成；
  - 按差错追回分成；
  - SaaS 模块订阅。

## What Was Not Formalized

- 不把本产品定义为征信、催收外包或贷款撮合。
- 不批准 Agent 自动授信、自动定价或自动放款。
- 不批准未授权个人金融数据交易。
- 不在 MVP 阶段建设真实资金分账和持牌清分能力。
- 不把合规判断当作已完成结论。

## Next Step

先做一个组合验证包：

1. 选择一个有还款失败和对账痛点的贷款客户；
2. 用 3-6 个月历史订单做 Agent 回放；
3. 生成 Agent 任务账本、价值归因报表、模拟计费单；
4. 判断客户愿意为哪一种收费方式继续试点。
