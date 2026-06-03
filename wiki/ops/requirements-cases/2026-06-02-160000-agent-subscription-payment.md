---
layer: ops
domain: unclassified
classification_needed: true
ops_area: workflow-trace
canonical_object: requirements-case-file
artifact_type: requirements-case
status: requirements_ready
case_slug: agent-subscription-payment
created_at: 2026-06-03
---

# requirements-case

## Case Source
- Generated at: 2026-06-03T11:19:10.812029+00:00
- Scan root: `.`
- provenance: user invoked $report-wiki-portfolio:req-agent with Agent subscription payment pain-point material
- requirement_like: True
- source_type: chat_material
- title: 智能体服务订阅支付市场痛点

## Intent
- draft_requested: False
- intent: new_requirement_intake
- requested_action: process user-provided market pain-point material into requirements workflow state
- routed_worker: req-intake

## Domain
- Status: confirmed
- Confirmed: billing_revenue
### Candidates
- billing_revenue: derived from DDD domain_model primary subdomain

## Roles
- R-ai-service-provider: AI 服务商; confirmed_as=subscription_owner; status=confirmed; category=business_actor_owner
- R-billing-platform: 订阅支付平台; confirmed_as=billing_ops_owner; status=confirmed; category=system_owner
- R-revenue-recovery-owner: 续费与催缴运营责任方; confirmed_as=dunning_owner; status=confirmed; category=operation_owner
- R-usage-rating-owner: 混合计费规则责任方; confirmed_as=usage_rating_owner; status=confirmed; category=pricing_owner
- R-agent-entitlement-owner: Agent 服务权益责任方; confirmed_as=agent_entitlement_owner; status=confirmed; category=agent_service_owner
- R-seat-owner: 席位计费责任方; confirmed_as=seat_owner; status=confirmed; category=agent_service_owner
- R-metering-owner: 用量计量责任方; confirmed_as=metering_owner; status=confirmed; category=agent_service_owner
- R-mandate-owner: 支付授权责任方; confirmed_as=mandate_owner; status=confirmed; category=risk_compliance_owner
- R-split-settlement-owner: 分账结算责任方; confirmed_as=settlement_owner; status=confirmed; category=settlement_owner
- R-payout-owner: 出款责任方; confirmed_as=payout_owner; status=confirmed; category=settlement_owner

## User Stories
- US-001: role_ref=R-ai-service-provider; 作为 AI 服务商，我希望接入订阅支付能力，配置面向消费者的 Agent 服务订阅关系。; benefit=不用自建银行通道和订阅生命周期能力，就能商业化提供持续 Agent 服务。; acceptance=AF-001, AF-016
- US-002: role_ref=R-billing-platform; 作为订阅支付平台，我希望管理订阅创建、生效、续期、暂停和终止等生命周期状态。; benefit=AI 服务商可以获得完整订阅生命周期能力，而不是只完成一次性扣款。; acceptance=AF-002, AF-016
- US-003: role_ref=R-usage-rating-owner; 作为混合计费规则责任方，我希望支持固定订阅、按量计费和席位计费的组合计价。; benefit=Agent 服务可以按真实商业模型收费，而不是被限制在单一固定订阅。; acceptance=AF-003, AF-004
- US-004: role_ref=R-metering-owner; 作为用量计量责任方，我希望记录和汇总 Agent 服务使用量，供按量计费计算。; benefit=按量收费可以基于可追溯的用量事实，而不是人工估算或离线结算。; acceptance=AF-004, AF-005
- US-005: role_ref=R-seat-owner; 作为席位计费责任方，我希望管理服务席位数量和席位变更对账单的影响。; benefit=团队型或多用户 Agent 服务可以按席位扩缩容并形成正确应收。; acceptance=AF-004, AF-006
- US-006: role_ref=R-mandate-owner; 作为支付授权责任方，我希望在周期扣款前完成支付方式授权或委托扣款授权，并保留授权证据。; benefit=自动续费和重试扣款具备合规依据，降低扣款争议和失败风险。; acceptance=AF-007
- US-007: role_ref=R-billing-platform; 作为订阅支付平台，我希望在续期日自动生成账单并发起周期扣款和失败重试。; benefit=AI 服务商可以提高续费成功率，并减少人工催收和重复对接成本。; acceptance=AF-007, AF-008, AF-009, AF-016
- US-008: role_ref=R-revenue-recovery-owner; 作为续费与催缴运营责任方，我希望对续费失败用户触发催缴、宽限期和挽留策略。; benefit=在扣款失败后仍能恢复收入并提升月续费率。; acceptance=AF-009, AF-010, AF-011
- US-009: role_ref=R-agent-entitlement-owner; 作为 Agent 服务权益责任方，我希望根据订阅和付款状态开通、保持、降级或暂停 Agent 服务权益。; benefit=商业订阅状态可以准确驱动消费者可用的 Agent 服务访问权限。; acceptance=AF-010, AF-011, AF-012, AF-016
- US-010: role_ref=R-split-settlement-owner; 作为分账结算责任方，我希望按平台和服务方约定规则计算收入分账并形成结算批次。; benefit=平台型 Agent 服务可以把收入准确分配给多个服务方，降低结算链路复杂度。; acceptance=AF-013, AF-014, AF-016
- US-011: role_ref=R-payout-owner; 作为出款责任方，我希望将已结算金额按结算批次出款给对应服务方。; benefit=服务方可以按可追溯的结算结果收到资金，平台减少人工付款和对账负担。; acceptance=AF-014, AF-015, AF-016

## Acceptance Functions
- AF-001: AI 服务商完成订阅支付接入配置; stories=US-001; AI 服务商完成订阅支付能力接入后，系统可保存面向消费者的 Agent 服务订阅配置，并返回可用于后续订阅创建的配置标识。
- AF-002: 订阅生命周期状态可被创建和流转; stories=US-002; 创建订阅后，系统可记录并查询订阅创建、生效、续期、暂停和终止状态，且每次状态变化保留变更时间和原因。
- AF-003: 混合计费规则可配置; stories=US-003; 配置价格方案时，系统支持同一 Agent 服务同时包含固定订阅费、按量计费项和席位计费项。
- AF-004: 混合账单按规则汇总应收; stories=US-003, US-004, US-005; 生成账单时，系统将固定订阅费、用量费用和席位费用汇总为同一账单应收，并保留各计费项明细。
- AF-005: Agent 使用量可记录并参与计费; stories=US-004; 接收 Agent 使用量后，系统可按订阅周期汇总用量，并将汇总结果用于按量计费项计算。
- AF-006: 席位数量和变更影响账单; stories=US-005; 席位数量新增、减少或周期内变更后，系统可记录席位变更事实，并在账单中反映对应席位费用。
- AF-007: 周期扣款前存在有效授权证据; stories=US-006, US-007; 发起自动续费扣款前，系统能校验订阅关联的支付授权或委托扣款授权处于有效状态，并可查询授权证据。
- AF-008: 续期日自动生成账单并发起扣款; stories=US-007; 到达订阅续期日时，系统自动生成续期账单，并根据有效支付授权发起周期扣款。
- AF-009: 扣款失败后按策略重试; stories=US-007, US-008; 周期扣款失败后，系统按配置的重试策略重新发起扣款，并记录每次重试的时间、结果和失败原因。
- AF-010: 续费失败触发催缴和宽限期; stories=US-008, US-009; 续费扣款失败后，系统创建催缴事件并进入宽限期；宽限期内订阅状态和权益策略可被查询。
- AF-011: 挽留成功后订阅恢复正常; stories=US-008, US-009; 催缴或挽留期间补缴成功后，系统将订阅恢复为正常状态，并恢复或保持对应 Agent 服务权益。
- AF-012: 订阅和付款状态驱动 Agent 权益; stories=US-009; 订阅生效、付款成功、付款失败、暂停或终止后，系统可同步调整 Agent 服务权益为开通、保持、降级或暂停。
- AF-013: 按规则生成分账结果; stories=US-010; 账单收款成功后，系统可按平台和服务方约定规则生成收入分账结果，并保留平台、服务方、金额和规则版本。
- AF-014: 分账结果可汇入结算批次; stories=US-010, US-011; 满足结算条件后，系统可将待结算分账结果汇入结算批次，并记录批次状态、金额合计和明细。
- AF-015: 按结算批次完成出款; stories=US-011; 结算批次确认后，系统可根据批次明细向对应服务方发起出款，并记录出款状态和结果。
- AF-016: 支付、账单、权益、结算链路可追溯; stories=US-001, US-002, US-007, US-009, US-010, US-011; 针对同一订阅周期，系统可从订阅、账单、支付结果、权益状态、分账结果、结算批次和出款记录追溯完整链路。

## Soft Evidence
### Acceptance Extraction
- {"source": "req-acceptance", "summary": "Defined observable acceptance functions for subscription setup, lifecycle, mixed billing, metering, seats, mandate, renewal retry, dunning, entitlement, split settlement, payout, and traceability."}
### Domain Model
- {"aggregate_roots": ["commercial_subscription", "invoice", "dunning_case", "payment_intent", "payment_attempt", "ledger_entry", "fund_state", "reconciliation_record", "mandate", "agent_entitlement", "usage_event", "seat_assignment", "split_rule", "settlement_batch", "payout"], "bounded_contexts": ["commercial_subscription_context", "billing_invoice_context", "revenue_recovery_context", "payment_intent_context", "payment_attempt_authorization_context", "balance_ledger_context", "fund_state_context", "reconciliation_context", "mandate_authorization_context", "agent_entitlement_context", "agent_usage_metering_context", "agent_workspace_seat_context", "split_allocation_context", "settlement_batch_context", "payout_context"], "business_ecosystems": ["payment_ecosystem", "agent_service_ecosystem"], "candidates": [], "context_handoffs": [{"from_context": "commercial_subscription_context", "name": "GenerateInvoice", "to_context": "billing_invoice_context", "type": "command"}, {"from_context": "billing_invoice_context", "name": "ChargeInvoice", "to_context": "payment_intent_context", "type": "command"}, {"from_context": "payment_attempt_authorization_context", "name": "PaymentSucceeded", "to_context": "balance_ledger_context", "type": "domain_event"}, {"from_context": "commercial_subscription_context", "name": "CommercialSubscriptionActivated", "to_context": "agent_entitlement_context", "type": "domain_event"}], "fact_owners": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "non_domain_terms": ["subscription", "account", "settlement"], "open_questions": ["Confirm first-release payout/split settlement scope."], "role_obligations": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "status": "confirmed", "subdomains": ["billing_revenue", "merchant_platform_relationship", "payment_transaction", "account_balance", "funds_movement_settlement", "financial_operations", "risk_compliance", "agent_entitlement", "agent_usage_metering", "agent_workspace_seat"]}
### Intake Actors
- {"id": "ai_service_provider", "label": "AI service provider", "type": "organization"}
- {"id": "platform", "label": "platform", "type": "organization"}
- {"id": "consumer", "label": "consumer", "type": "person"}
- {"id": "recurring_billing_job", "label": "recurring billing automation", "type": "system"}
- {"id": "payment_channel", "label": "payment channel", "type": "external_system"}
### Open Questions
- {"question": "是否进入 req-handoff 生成 OpenSpec draft？"}
- {"question": "如不进入 handoff，是否需要先评审 US-001 至 US-011 和 AF-001 至 AF-016？"}
### Scope Decisions
- {"decision": "first_release_split_settlement", "evidence": "用户确认 1: 包含", "value": "in_scope"}
- {"decision": "target_customer", "evidence": "用户确认 2: AI 服务商", "value": "AI 服务商"}
- {"decision": "commercial_model", "evidence": "用户确认 3: 混合", "value": "混合计费"}
- {"decision": "mandate_and_recurring_retry", "evidence": "用户确认 4: 是", "value": "in_scope"}
### Source Material
- {"summary": "Agent service subscription payment market and pain points"}
- {"pain_point": "payment threshold is high; service providers lack subscription payment lifecycle capability"}
- {"pain_point": "renewal rate is low; dunning, grace period, and retention mechanisms are missing"}
- {"pain_point": "billing models are too simple; fixed subscription dominates while usage and seat billing are needed"}
- {"pain_point": "split settlement is complex for AI application marketplace and platform models"}
### Story Extraction
- {"source": "req-stories", "summary": "Normalized role/want/benefit stories from confirmed AI 服务商 scope, mixed billing, recurring mandate/retry, revenue recovery, entitlement, split settlement, and payout decisions."}
### Taxonomy Candidate Terms
- {"reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.", "term": "mandate"}
- {"reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.", "term": "usage_event"}
### User Confirmation
- {"answers": [{"answer": "包含", "question": "首版是否包含分账分配、结算批次和出款？"}, {"answer": "AI 服务商", "question": "目标客户和集成边界是什么？"}, {"answer": "混合计费", "question": "支持哪些商业计费模型？"}, {"answer": "是", "question": "支付方式授权/委托扣款与周期扣款重试是否进入首版？"}], "confirmed_at": "2026-06-03", "source": "chat_user_confirmation"}

## Readiness / Next Action
- Status: requirements_ready
- Next action: req-handoff
- Reason: Domain model, roles, user stories, acceptance functions, and bidirectional mappings are normalized; OpenSpec draft creation remains a separate handoff action.
### Blockers
- None

## Evidence Attachments
### Analysis
- `scripts/build_requirements_analysis_agent.py --material-file /tmp/agent-subscription-payment-material.md`
### Source
- `/tmp/agent-subscription-payment-material.md`
### Taxonomy
- `requirements/config/requirements-taxonomy.yaml`

## Proof Boundary
- This case now records intake, req-scope, req-stories, and req-acceptance evidence for user-provided market pain-point material.
- Acceptance functions are observable and bidirectionally mapped to user stories.
- Requirements checker must pass before OpenSpec handoff is claimed.
- No OpenSpec draft or implementation work has been created.

## Machine Case Data
<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [
    {
      "evidence_anchor": {
        "source_section": "US-001 / 原始材料: 订阅制持续服务"
      },
      "id": "AF-001",
      "name": "AI 服务商完成订阅支付接入配置",
      "source_acceptance": "US-001",
      "source_functions": [
        "原始痛点: 支付门槛高",
        "用户确认 2: AI 服务商"
      ],
      "then": "AI 服务商完成订阅支付能力接入后，系统可保存面向消费者的 Agent 服务订阅配置，并返回可用于后续订阅创建的配置标识。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-002 / 原始痛点: 支付门槛高"
      },
      "id": "AF-002",
      "name": "订阅生命周期状态可被创建和流转",
      "source_acceptance": "US-002",
      "source_functions": [
        "原始痛点: 管理订阅生命周期"
      ],
      "then": "创建订阅后，系统可记录并查询订阅创建、生效、续期、暂停和终止状态，且每次状态变化保留变更时间和原因。",
      "user_story_ids": [
        "US-002"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-003 / 用户确认 3: 混合"
      },
      "id": "AF-003",
      "name": "混合计费规则可配置",
      "source_acceptance": "US-003",
      "source_functions": [
        "原始痛点: 计费模式单一",
        "用户确认 3: 混合计费"
      ],
      "then": "配置价格方案时，系统支持同一 Agent 服务同时包含固定订阅费、按量计费项和席位计费项。",
      "user_story_ids": [
        "US-003"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-003 至 US-005 / 混合计费"
      },
      "id": "AF-004",
      "name": "混合账单按规则汇总应收",
      "source_acceptance": "US-003,US-004,US-005",
      "source_functions": [
        "用户确认 3: 混合计费"
      ],
      "then": "生成账单时，系统将固定订阅费、用量费用和席位费用汇总为同一账单应收，并保留各计费项明细。",
      "user_story_ids": [
        "US-003",
        "US-004",
        "US-005"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-004 / 用户确认 3: 混合"
      },
      "id": "AF-005",
      "name": "Agent 使用量可记录并参与计费",
      "source_acceptance": "US-004",
      "source_functions": [
        "原始痛点: 按量计费",
        "用户确认 3: 混合计费"
      ],
      "then": "接收 Agent 使用量后，系统可按订阅周期汇总用量，并将汇总结果用于按量计费项计算。",
      "user_story_ids": [
        "US-004"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-005 / 用户确认 3: 混合"
      },
      "id": "AF-006",
      "name": "席位数量和变更影响账单",
      "source_acceptance": "US-005",
      "source_functions": [
        "原始痛点: 席位计费",
        "用户确认 3: 混合计费"
      ],
      "then": "席位数量新增、减少或周期内变更后，系统可记录席位变更事实，并在账单中反映对应席位费用。",
      "user_story_ids": [
        "US-005"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-006 / 用户确认 4: 是"
      },
      "id": "AF-007",
      "name": "周期扣款前存在有效授权证据",
      "source_acceptance": "US-006,US-007",
      "source_functions": [
        "用户确认 4: 是",
        "领域模型: mandate_authorization_context"
      ],
      "then": "发起自动续费扣款前，系统能校验订阅关联的支付授权或委托扣款授权处于有效状态，并可查询授权证据。",
      "user_story_ids": [
        "US-006",
        "US-007"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-007 / 周期扣款"
      },
      "id": "AF-008",
      "name": "续期日自动生成账单并发起扣款",
      "source_acceptance": "US-007",
      "source_functions": [
        "原始痛点: 周期扣款",
        "用户确认 4: 是"
      ],
      "then": "到达订阅续期日时，系统自动生成续期账单，并根据有效支付授权发起周期扣款。",
      "user_story_ids": [
        "US-007"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-007 / US-008"
      },
      "id": "AF-009",
      "name": "扣款失败后按策略重试",
      "source_acceptance": "US-007,US-008",
      "source_functions": [
        "用户确认 4: 是",
        "原始痛点: 续费率低"
      ],
      "then": "周期扣款失败后，系统按配置的重试策略重新发起扣款，并记录每次重试的时间、结果和失败原因。",
      "user_story_ids": [
        "US-007",
        "US-008"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-008 / 原始痛点: 续费率低"
      },
      "id": "AF-010",
      "name": "续费失败触发催缴和宽限期",
      "source_acceptance": "US-008,US-009",
      "source_functions": [
        "原始痛点: 催缴、宽限期、挽留机制"
      ],
      "then": "续费扣款失败后，系统创建催缴事件并进入宽限期；宽限期内订阅状态和权益策略可被查询。",
      "user_story_ids": [
        "US-008",
        "US-009"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-008 / US-009"
      },
      "id": "AF-011",
      "name": "挽留成功后订阅恢复正常",
      "source_acceptance": "US-008,US-009",
      "source_functions": [
        "原始痛点: 挽留机制",
        "领域模型: agent_entitlement_context"
      ],
      "then": "催缴或挽留期间补缴成功后，系统将订阅恢复为正常状态，并恢复或保持对应 Agent 服务权益。",
      "user_story_ids": [
        "US-008",
        "US-009"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-009 / Agent 服务权益"
      },
      "id": "AF-012",
      "name": "订阅和付款状态驱动 Agent 权益",
      "source_acceptance": "US-009",
      "source_functions": [
        "领域模型: CommercialSubscriptionActivated",
        "原始材料: 持续服务"
      ],
      "then": "订阅生效、付款成功、付款失败、暂停或终止后，系统可同步调整 Agent 服务权益为开通、保持、降级或暂停。",
      "user_story_ids": [
        "US-009"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-010 / 用户确认 1: 包含"
      },
      "id": "AF-013",
      "name": "按规则生成分账结果",
      "source_acceptance": "US-010",
      "source_functions": [
        "原始痛点: 分账结算复杂",
        "用户确认 1: 包含"
      ],
      "then": "账单收款成功后，系统可按平台和服务方约定规则生成收入分账结果，并保留平台、服务方、金额和规则版本。",
      "user_story_ids": [
        "US-010"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-010 / US-011"
      },
      "id": "AF-014",
      "name": "分账结果可汇入结算批次",
      "source_acceptance": "US-010,US-011",
      "source_functions": [
        "用户确认 1: 包含",
        "领域模型: settlement_batch_context"
      ],
      "then": "满足结算条件后，系统可将待结算分账结果汇入结算批次，并记录批次状态、金额合计和明细。",
      "user_story_ids": [
        "US-010",
        "US-011"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "US-011 / 出款"
      },
      "id": "AF-015",
      "name": "按结算批次完成出款",
      "source_acceptance": "US-011",
      "source_functions": [
        "用户确认 1: 包含",
        "领域模型: payout_context"
      ],
      "then": "结算批次确认后，系统可根据批次明细向对应服务方发起出款，并记录出款状态和结果。",
      "user_story_ids": [
        "US-011"
      ]
    },
    {
      "evidence_anchor": {
        "source_section": "领域模型: context_handoffs"
      },
      "id": "AF-016",
      "name": "支付、账单、权益、结算链路可追溯",
      "source_acceptance": "cross-story-traceability",
      "source_functions": [
        "领域模型: context_handoffs",
        "用户确认: 首版包含完整支付与分账出款链路"
      ],
      "then": "针对同一订阅周期，系统可从订阅、账单、支付结果、权益状态、分账结果、结算批次和出款记录追溯完整链路。",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-007",
        "US-009",
        "US-010",
        "US-011"
      ]
    }
  ],
  "active": true,
  "blockers": [],
  "case_slug": "agent-subscription-payment",
  "case_source": {
    "provenance": "user invoked $report-wiki-portfolio:req-agent with Agent subscription payment pain-point material",
    "requirement_like": true,
    "source_type": "chat_material",
    "title": "智能体服务订阅支付市场痛点"
  },
  "current_intent": {
    "draft_requested": false,
    "intent": "new_requirement_intake",
    "requested_action": "process user-provided market pain-point material into requirements workflow state",
    "routed_worker": "req-intake"
  },
  "domain": {
    "candidates": [
      {
        "id": "billing_revenue",
        "reason": "derived from DDD domain_model primary subdomain"
      }
    ],
    "confirmed": "billing_revenue",
    "status": "confirmed"
  },
  "domain_model": {
    "aggregate_roots": [
      "commercial_subscription",
      "invoice",
      "dunning_case",
      "payment_intent",
      "payment_attempt",
      "ledger_entry",
      "fund_state",
      "reconciliation_record",
      "agent_entitlement",
      "seat_assignment",
      "split_rule",
      "settlement_batch",
      "payout"
    ],
    "bounded_contexts": [
      "commercial_subscription_context",
      "billing_invoice_context",
      "revenue_recovery_context",
      "payment_intent_context",
      "payment_attempt_authorization_context",
      "balance_ledger_context",
      "fund_state_context",
      "reconciliation_context",
      "mandate_authorization_context",
      "agent_entitlement_context",
      "agent_usage_metering_context",
      "agent_workspace_seat_context",
      "split_allocation_context",
      "settlement_batch_context",
      "payout_context"
    ],
    "business_ecosystems": [
      "payment_ecosystem",
      "agent_service_ecosystem"
    ],
    "candidates": [],
    "context_handoffs": [
      {
        "from_context": "commercial_subscription_context",
        "name": "GenerateInvoice",
        "to_context": "billing_invoice_context",
        "type": "command"
      },
      {
        "from_context": "billing_invoice_context",
        "name": "ChargeInvoice",
        "to_context": "payment_intent_context",
        "type": "command"
      },
      {
        "from_context": "payment_attempt_authorization_context",
        "name": "PaymentSucceeded",
        "to_context": "balance_ledger_context",
        "type": "domain_event"
      },
      {
        "from_context": "commercial_subscription_context",
        "name": "CommercialSubscriptionActivated",
        "to_context": "agent_entitlement_context",
        "type": "domain_event"
      }
    ],
    "fact_owners": [
      "subscription_owner",
      "subscription_policy_owner",
      "billing_ops_owner",
      "payment_ops_owner",
      "funds_account_owner",
      "ledger_owner",
      "balance_state_owner",
      "reconciliation_owner",
      "mandate_owner",
      "compliance_owner",
      "agent_entitlement_owner",
      "access_policy_owner",
      "usage_rating_owner",
      "agent_usage_owner",
      "metering_owner",
      "workspace_owner",
      "seat_owner",
      "split_rule_owner",
      "settlement_owner",
      "payout_owner"
    ],
    "non_domain_terms": [
      "subscription",
      "account",
      "settlement"
    ],
    "open_questions": [
      "Confirm first-release payout/split settlement scope.",
      "Confirm whether `mandate` is taxonomy-owned scope, candidate vocabulary, or only supporting evidence.",
      "Confirm whether `usage_event` is taxonomy-owned scope, candidate vocabulary, or only supporting evidence."
    ],
    "role_obligations": [
      "subscription_owner",
      "subscription_policy_owner",
      "billing_ops_owner",
      "payment_ops_owner",
      "funds_account_owner",
      "ledger_owner",
      "balance_state_owner",
      "reconciliation_owner",
      "mandate_owner",
      "compliance_owner",
      "agent_entitlement_owner",
      "access_policy_owner",
      "usage_rating_owner",
      "agent_usage_owner",
      "metering_owner",
      "workspace_owner",
      "seat_owner",
      "split_rule_owner",
      "settlement_owner",
      "payout_owner"
    ],
    "status": "confirmed",
    "subdomains": [
      "billing_revenue",
      "merchant_platform_relationship",
      "payment_transaction",
      "account_balance",
      "funds_movement_settlement",
      "financial_operations",
      "risk_compliance",
      "agent_entitlement",
      "agent_usage_metering",
      "agent_workspace_seat"
    ]
  },
  "evidence_attachments": {
    "analysis": [
      "scripts/build_requirements_analysis_agent.py --material-file /tmp/agent-subscription-payment-material.md"
    ],
    "source": [
      "/tmp/agent-subscription-payment-material.md"
    ],
    "taxonomy": [
      "requirements/config/requirements-taxonomy.yaml"
    ]
  },
  "generated_at": "2026-06-03T11:19:10.812029+00:00",
  "mode": "requirements_case",
  "proof_boundary_notes": [
    "This case now records intake, req-scope, req-stories, and req-acceptance evidence for user-provided market pain-point material.",
    "Acceptance functions are observable and bidirectionally mapped to user stories.",
    "Requirements checker must pass before OpenSpec handoff is claimed.",
    "No OpenSpec draft or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "req-handoff",
    "reason": "Domain model, roles, user stories, acceptance functions, and bidirectional mappings are normalized; OpenSpec draft creation remains a separate handoff action.",
    "status": "requirements_ready"
  },
  "roles": [
    {
      "category": "business_actor_owner",
      "confirmed_as": "subscription_owner",
      "evidence_anchor": {
        "source_section": "用户确认 2: AI 服务商"
      },
      "id": "R-ai-service-provider",
      "mention": "AI 服务商",
      "normalization_note": "目标客户已由用户确认为 AI 服务商；在订阅商业关系中作为 subscription_owner 的业务角色代表。",
      "source_actors": [
        "智能体服务方",
        "AI 服务商",
        "技术型团队"
      ],
      "status": "confirmed"
    },
    {
      "category": "system_owner",
      "confirmed_as": "billing_ops_owner",
      "evidence_anchor": {
        "source_section": "原始痛点: 支付门槛高 / 周期扣款 / 订阅生命周期"
      },
      "id": "R-billing-platform",
      "mention": "订阅支付平台",
      "normalization_note": "平台承载账单生成、订阅状态和计费运营责任，映射到 billing_ops_owner。",
      "source_actors": [
        "订阅支付能力",
        "周期扣款",
        "订阅生命周期"
      ],
      "status": "confirmed"
    },
    {
      "category": "operation_owner",
      "confirmed_as": "dunning_owner",
      "evidence_anchor": {
        "source_section": "原始痛点: 续费率低"
      },
      "id": "R-revenue-recovery-owner",
      "mention": "续费与催缴运营责任方",
      "normalization_note": "续费率、催缴、宽限期和挽留机制属于 revenue_recovery_context，映射到 dunning_owner。",
      "source_actors": [
        "催缴",
        "宽限期",
        "挽留机制"
      ],
      "status": "confirmed"
    },
    {
      "category": "pricing_owner",
      "confirmed_as": "usage_rating_owner",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合计费"
      },
      "id": "R-usage-rating-owner",
      "mention": "混合计费规则责任方",
      "normalization_note": "用户确认首版支持混合计费，按量和席位价格计算责任映射到 usage_rating_owner。",
      "source_actors": [
        "固定订阅",
        "按量计费",
        "席位计费",
        "混合计费"
      ],
      "status": "confirmed"
    },
    {
      "category": "agent_service_owner",
      "confirmed_as": "agent_entitlement_owner",
      "evidence_anchor": {
        "source_section": "原始材料: 智能体服务订阅"
      },
      "id": "R-agent-entitlement-owner",
      "mention": "Agent 服务权益责任方",
      "normalization_note": "商业订阅激活后需要开通或保持 Agent 服务权益，映射到 agent_entitlement_owner。",
      "source_actors": [
        "智能体服务",
        "持续服务",
        "订阅服务"
      ],
      "status": "confirmed"
    },
    {
      "category": "agent_service_owner",
      "confirmed_as": "seat_owner",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合计费"
      },
      "id": "R-seat-owner",
      "mention": "席位计费责任方",
      "normalization_note": "用户确认混合计费包含席位模型，席位分配责任映射到 seat_owner。",
      "source_actors": [
        "席位计费",
        "混合计费"
      ],
      "status": "confirmed"
    },
    {
      "category": "agent_service_owner",
      "confirmed_as": "metering_owner",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合计费"
      },
      "id": "R-metering-owner",
      "mention": "用量计量责任方",
      "normalization_note": "用户确认混合计费包含按量模型，计量事实责任映射到 metering_owner。",
      "source_actors": [
        "按量计费",
        "混合计费"
      ],
      "status": "confirmed"
    },
    {
      "category": "risk_compliance_owner",
      "confirmed_as": "mandate_owner",
      "evidence_anchor": {
        "source_section": "用户确认 4: 是"
      },
      "id": "R-mandate-owner",
      "mention": "支付授权责任方",
      "normalization_note": "用户确认支付授权/委托扣款进入首版，映射到 mandate_owner。",
      "source_actors": [
        "支付方式授权",
        "委托扣款",
        "周期扣款"
      ],
      "status": "confirmed"
    },
    {
      "category": "settlement_owner",
      "confirmed_as": "settlement_owner",
      "evidence_anchor": {
        "source_section": "用户确认 1: 包含"
      },
      "id": "R-split-settlement-owner",
      "mention": "分账结算责任方",
      "normalization_note": "用户确认首版包含分账、结算和出款，结算批次责任映射到 settlement_owner。",
      "source_actors": [
        "分账结算",
        "结算批次",
        "出款"
      ],
      "status": "confirmed"
    },
    {
      "category": "settlement_owner",
      "confirmed_as": "payout_owner",
      "evidence_anchor": {
        "source_section": "用户确认 1: 包含"
      },
      "id": "R-payout-owner",
      "mention": "出款责任方",
      "normalization_note": "用户确认出款进入首版，外部出款责任映射到 payout_owner。",
      "source_actors": [
        "出款",
        "分账结算"
      ],
      "status": "confirmed"
    }
  ],
  "soft_evidence": {
    "acceptance_extraction": [
      {
        "source": "req-acceptance",
        "summary": "Defined observable acceptance functions for subscription setup, lifecycle, mixed billing, metering, seats, mandate, renewal retry, dunning, entitlement, split settlement, payout, and traceability."
      }
    ],
    "domain_model": [
      {
        "aggregate_roots": [
          "commercial_subscription",
          "invoice",
          "dunning_case",
          "payment_intent",
          "payment_attempt",
          "ledger_entry",
          "fund_state",
          "reconciliation_record",
          "mandate",
          "agent_entitlement",
          "usage_event",
          "seat_assignment",
          "split_rule",
          "settlement_batch",
          "payout"
        ],
        "bounded_contexts": [
          "commercial_subscription_context",
          "billing_invoice_context",
          "revenue_recovery_context",
          "payment_intent_context",
          "payment_attempt_authorization_context",
          "balance_ledger_context",
          "fund_state_context",
          "reconciliation_context",
          "mandate_authorization_context",
          "agent_entitlement_context",
          "agent_usage_metering_context",
          "agent_workspace_seat_context",
          "split_allocation_context",
          "settlement_batch_context",
          "payout_context"
        ],
        "business_ecosystems": [
          "payment_ecosystem",
          "agent_service_ecosystem"
        ],
        "candidates": [],
        "context_handoffs": [
          {
            "from_context": "commercial_subscription_context",
            "name": "GenerateInvoice",
            "to_context": "billing_invoice_context",
            "type": "command"
          },
          {
            "from_context": "billing_invoice_context",
            "name": "ChargeInvoice",
            "to_context": "payment_intent_context",
            "type": "command"
          },
          {
            "from_context": "payment_attempt_authorization_context",
            "name": "PaymentSucceeded",
            "to_context": "balance_ledger_context",
            "type": "domain_event"
          },
          {
            "from_context": "commercial_subscription_context",
            "name": "CommercialSubscriptionActivated",
            "to_context": "agent_entitlement_context",
            "type": "domain_event"
          }
        ],
        "fact_owners": [
          "subscription_owner",
          "subscription_policy_owner",
          "billing_ops_owner",
          "payment_ops_owner",
          "funds_account_owner",
          "ledger_owner",
          "balance_state_owner",
          "reconciliation_owner",
          "mandate_owner",
          "compliance_owner",
          "agent_entitlement_owner",
          "access_policy_owner",
          "usage_rating_owner",
          "agent_usage_owner",
          "metering_owner",
          "workspace_owner",
          "seat_owner",
          "split_rule_owner",
          "settlement_owner",
          "payout_owner"
        ],
        "non_domain_terms": [
          "subscription",
          "account",
          "settlement"
        ],
        "open_questions": [
          "Confirm first-release payout/split settlement scope."
        ],
        "role_obligations": [
          "subscription_owner",
          "subscription_policy_owner",
          "billing_ops_owner",
          "payment_ops_owner",
          "funds_account_owner",
          "ledger_owner",
          "balance_state_owner",
          "reconciliation_owner",
          "mandate_owner",
          "compliance_owner",
          "agent_entitlement_owner",
          "access_policy_owner",
          "usage_rating_owner",
          "agent_usage_owner",
          "metering_owner",
          "workspace_owner",
          "seat_owner",
          "split_rule_owner",
          "settlement_owner",
          "payout_owner"
        ],
        "status": "confirmed",
        "subdomains": [
          "billing_revenue",
          "merchant_platform_relationship",
          "payment_transaction",
          "account_balance",
          "funds_movement_settlement",
          "financial_operations",
          "risk_compliance",
          "agent_entitlement",
          "agent_usage_metering",
          "agent_workspace_seat"
        ]
      }
    ],
    "intake_actors": [
      {
        "id": "ai_service_provider",
        "label": "AI service provider",
        "type": "organization"
      },
      {
        "id": "platform",
        "label": "platform",
        "type": "organization"
      },
      {
        "id": "consumer",
        "label": "consumer",
        "type": "person"
      },
      {
        "id": "recurring_billing_job",
        "label": "recurring billing automation",
        "type": "system"
      },
      {
        "id": "payment_channel",
        "label": "payment channel",
        "type": "external_system"
      }
    ],
    "open_questions": [
      {
        "question": "是否进入 req-handoff 生成 OpenSpec draft？"
      },
      {
        "question": "如不进入 handoff，是否需要先评审 US-001 至 US-011 和 AF-001 至 AF-016？"
      }
    ],
    "scope_decisions": [
      {
        "decision": "first_release_split_settlement",
        "evidence": "用户确认 1: 包含",
        "value": "in_scope"
      },
      {
        "decision": "target_customer",
        "evidence": "用户确认 2: AI 服务商",
        "value": "AI 服务商"
      },
      {
        "decision": "commercial_model",
        "evidence": "用户确认 3: 混合",
        "value": "混合计费"
      },
      {
        "decision": "mandate_and_recurring_retry",
        "evidence": "用户确认 4: 是",
        "value": "in_scope"
      }
    ],
    "source_material": [
      {
        "summary": "Agent service subscription payment market and pain points"
      },
      {
        "pain_point": "payment threshold is high; service providers lack subscription payment lifecycle capability"
      },
      {
        "pain_point": "renewal rate is low; dunning, grace period, and retention mechanisms are missing"
      },
      {
        "pain_point": "billing models are too simple; fixed subscription dominates while usage and seat billing are needed"
      },
      {
        "pain_point": "split settlement is complex for AI application marketplace and platform models"
      }
    ],
    "story_extraction": [
      {
        "source": "req-stories",
        "summary": "Normalized role/want/benefit stories from confirmed AI 服务商 scope, mixed billing, recurring mandate/retry, revenue recovery, entitlement, split settlement, and payout decisions."
      }
    ],
    "taxonomy_candidate_terms": [
      {
        "reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.",
        "term": "mandate"
      },
      {
        "reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.",
        "term": "usage_event"
      }
    ],
    "user_confirmation": [
      {
        "answers": [
          {
            "answer": "包含",
            "question": "首版是否包含分账分配、结算批次和出款？"
          },
          {
            "answer": "AI 服务商",
            "question": "目标客户和集成边界是什么？"
          },
          {
            "answer": "混合计费",
            "question": "支持哪些商业计费模型？"
          },
          {
            "answer": "是",
            "question": "支付方式授权/委托扣款与周期扣款重试是否进入首版？"
          }
        ],
        "confirmed_at": "2026-06-03",
        "source": "chat_user_confirmation"
      }
    ]
  },
  "status": "requirements_ready",
  "user_stories": [
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-016"
      ],
      "benefit": "不用自建银行通道和订阅生命周期能力，就能商业化提供持续 Agent 服务。",
      "evidence_anchor": {
        "source_section": "原始材料: AI 产品采用订阅制收费模式向消费者提供持续服务"
      },
      "id": "US-001",
      "role_ref": "R-ai-service-provider",
      "source_functions": [
        "原始痛点: 支付门槛高",
        "用户确认 2: AI 服务商"
      ],
      "want": "作为 AI 服务商，我希望接入订阅支付能力，配置面向消费者的 Agent 服务订阅关系。"
    },
    {
      "acceptance_function_ids": [
        "AF-002",
        "AF-016"
      ],
      "benefit": "AI 服务商可以获得完整订阅生命周期能力，而不是只完成一次性扣款。",
      "evidence_anchor": {
        "source_section": "原始痛点: 支付门槛高"
      },
      "id": "US-002",
      "role_ref": "R-billing-platform",
      "source_functions": [
        "原始痛点: 实现周期扣款、管理订阅生命周期"
      ],
      "want": "作为订阅支付平台，我希望管理订阅创建、生效、续期、暂停和终止等生命周期状态。"
    },
    {
      "acceptance_function_ids": [
        "AF-003",
        "AF-004"
      ],
      "benefit": "Agent 服务可以按真实商业模型收费，而不是被限制在单一固定订阅。",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合"
      },
      "id": "US-003",
      "role_ref": "R-usage-rating-owner",
      "source_functions": [
        "原始痛点: 计费模式单一",
        "用户确认 3: 混合计费"
      ],
      "want": "作为混合计费规则责任方，我希望支持固定订阅、按量计费和席位计费的组合计价。"
    },
    {
      "acceptance_function_ids": [
        "AF-004",
        "AF-005"
      ],
      "benefit": "按量收费可以基于可追溯的用量事实，而不是人工估算或离线结算。",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合"
      },
      "id": "US-004",
      "role_ref": "R-metering-owner",
      "source_functions": [
        "原始痛点: 按量计费",
        "用户确认 3: 混合计费"
      ],
      "want": "作为用量计量责任方，我希望记录和汇总 Agent 服务使用量，供按量计费计算。"
    },
    {
      "acceptance_function_ids": [
        "AF-004",
        "AF-006"
      ],
      "benefit": "团队型或多用户 Agent 服务可以按席位扩缩容并形成正确应收。",
      "evidence_anchor": {
        "source_section": "用户确认 3: 混合"
      },
      "id": "US-005",
      "role_ref": "R-seat-owner",
      "source_functions": [
        "原始痛点: 席位计费",
        "用户确认 3: 混合计费"
      ],
      "want": "作为席位计费责任方，我希望管理服务席位数量和席位变更对账单的影响。"
    },
    {
      "acceptance_function_ids": [
        "AF-007"
      ],
      "benefit": "自动续费和重试扣款具备合规依据，降低扣款争议和失败风险。",
      "evidence_anchor": {
        "source_section": "用户确认 4: 是"
      },
      "id": "US-006",
      "role_ref": "R-mandate-owner",
      "source_functions": [
        "用户确认 4: 是",
        "领域模型: mandate_authorization_context"
      ],
      "want": "作为支付授权责任方，我希望在周期扣款前完成支付方式授权或委托扣款授权，并保留授权证据。"
    },
    {
      "acceptance_function_ids": [
        "AF-007",
        "AF-008",
        "AF-009",
        "AF-016"
      ],
      "benefit": "AI 服务商可以提高续费成功率，并减少人工催收和重复对接成本。",
      "evidence_anchor": {
        "source_section": "原始痛点: 支付门槛高 / 续费率低"
      },
      "id": "US-007",
      "role_ref": "R-billing-platform",
      "source_functions": [
        "原始痛点: 周期扣款",
        "用户确认 4: 是"
      ],
      "want": "作为订阅支付平台，我希望在续期日自动生成账单并发起周期扣款和失败重试。"
    },
    {
      "acceptance_function_ids": [
        "AF-009",
        "AF-010",
        "AF-011"
      ],
      "benefit": "在扣款失败后仍能恢复收入并提升月续费率。",
      "evidence_anchor": {
        "source_section": "原始痛点: 续费率低"
      },
      "id": "US-008",
      "role_ref": "R-revenue-recovery-owner",
      "source_functions": [
        "原始痛点: 续费率低",
        "催缴、宽限期、挽留机制"
      ],
      "want": "作为续费与催缴运营责任方，我希望对续费失败用户触发催缴、宽限期和挽留策略。"
    },
    {
      "acceptance_function_ids": [
        "AF-010",
        "AF-011",
        "AF-012",
        "AF-016"
      ],
      "benefit": "商业订阅状态可以准确驱动消费者可用的 Agent 服务访问权限。",
      "evidence_anchor": {
        "source_section": "原始材料: 智能体服务订阅"
      },
      "id": "US-009",
      "role_ref": "R-agent-entitlement-owner",
      "source_functions": [
        "原始材料: 向消费者提供持续服务",
        "领域模型: CommercialSubscriptionActivated"
      ],
      "want": "作为 Agent 服务权益责任方，我希望根据订阅和付款状态开通、保持、降级或暂停 Agent 服务权益。"
    },
    {
      "acceptance_function_ids": [
        "AF-013",
        "AF-014",
        "AF-016"
      ],
      "benefit": "平台型 Agent 服务可以把收入准确分配给多个服务方，降低结算链路复杂度。",
      "evidence_anchor": {
        "source_section": "用户确认 1: 包含"
      },
      "id": "US-010",
      "role_ref": "R-split-settlement-owner",
      "source_functions": [
        "原始痛点: 分账结算复杂",
        "用户确认 1: 包含"
      ],
      "want": "作为分账结算责任方，我希望按平台和服务方约定规则计算收入分账并形成结算批次。"
    },
    {
      "acceptance_function_ids": [
        "AF-014",
        "AF-015",
        "AF-016"
      ],
      "benefit": "服务方可以按可追溯的结算结果收到资金，平台减少人工付款和对账负担。",
      "evidence_anchor": {
        "source_section": "用户确认 1: 包含"
      },
      "id": "US-011",
      "role_ref": "R-payout-owner",
      "source_functions": [
        "用户确认 1: 包含",
        "领域模型: payout_context"
      ],
      "want": "作为出款责任方，我希望将已结算金额按结算批次出款给对应服务方。"
    }
  ]
}
```
<!-- requirements-case-data:end -->
