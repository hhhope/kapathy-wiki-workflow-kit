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

## Domain Coverage
- billing_revenue: coverage_type=primary; contexts=commercial_subscription_context, billing_invoice_context, usage_rating_context, revenue_recovery_context; aggregates=commercial_subscription, invoice, price_plan, billing_schedule, usage_record, rating_rule, seat_assignment, dunning_case, grace_period, retry_schedule; stories=US-001, US-002, US-003, US-004, US-005, US-007, US-008; acceptance=AF-001, AF-002, AF-003, AF-004, AF-005, AF-006, AF-008, AF-009, AF-010, AF-011; note=主域覆盖订阅关系、账单、混合计费、续期、重试和催缴。
- merchant_platform_relationship: coverage_type=full_coverage; contexts=merchant_identity_context, merchant_capability_context, merchant_service_offering_context, platform_responsibility_context; aggregates=merchant, platform_account, capability_grant, service_offering, platform_relationship; stories=US-001, US-017, US-018, US-019, US-020; acceptance=AF-001, AF-021, AF-022, AF-023, AF-024; note=用户审核确认 4：商户身份、能力开通、服务供给和平台责任边界进入首版完整故事。
- payment_transaction: coverage_type=required_payment; contexts=payment_intent_context, payment_attempt_authorization_context, payment_method_context; aggregates=payment_intent, payment_attempt, charge, payment_method_authorization; stories=US-006, US-007, US-012; acceptance=AF-007, AF-008, AF-009, AF-017; note=补强后覆盖授权校验、续期扣款、失败重试、支付意图和支付尝试结果收敛。
- account_balance: coverage_type=required_payment; contexts=balance_ledger_context, fund_state_context; aggregates=ledger_entry, fund_state; stories=US-013; acceptance=AF-018, AF-016; note=补强后覆盖支付成功后的账本分录和资金状态；余额、reserve、limit 暂不展开。
- financial_operations: coverage_type=required_payment; contexts=reconciliation_context; aggregates=reconciliation_record, reconciliation_exception; stories=US-014; acceptance=AF-019, AF-016; note=补强后覆盖账单、支付、账本、分账、结算和出款链路对账；财务报表和关账暂不展开。
- risk_compliance: coverage_type=required_payment; contexts=mandate_authorization_context; aggregates=payment_mandate, authorization_consent, consent_record; stories=US-006; acceptance=AF-007; note=覆盖周期扣款授权证据；KYB、AML、交易风控不在当前首版故事中展开。
- funds_movement_settlement: coverage_type=conditional_payment_in_scope; contexts=split_allocation_context, settlement_batch_context, payout_context; aggregates=split_rule, allocation_result, platform_fee, settlement_batch, payout; stories=US-010, US-011, US-015, US-016; acceptance=AF-013, AF-014, AF-015, AF-020, AF-016; note=用户确认首版包含分账、结算和出款；补强后覆盖分账规则、平台费用、结算批次和出款。
- agent_entitlement: coverage_type=adjacent_agent_service; contexts=agent_entitlement_context; aggregates=agent_entitlement; stories=US-009; acceptance=AF-010, AF-011, AF-012, AF-016; note=覆盖订阅和付款状态驱动 Agent 权益开通、保持、降级或暂停。
- agent_usage_metering: coverage_type=adjacent_agent_service_conditional; contexts=agent_usage_metering_context; aggregates=candidate:usage_event; stories=US-004; acceptance=AF-004, AF-005; note=覆盖按量计费用量汇总；usage_event 仍是 taxonomy 候选术语，当前作为邻接证据保留。
- agent_workspace_seat: coverage_type=adjacent_agent_service_conditional; contexts=agent_workspace_seat_context; aggregates=seat_assignment; stories=US-005; acceptance=AF-004, AF-006; note=覆盖席位数量和席位变更对账单影响。

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
- R-payment-ops-owner: 支付交易处理责任方; confirmed_as=payment_ops_owner; status=confirmed; category=payment_owner
- R-ledger-owner: 账本入账责任方; confirmed_as=ledger_owner; status=confirmed; category=funds_owner
- R-balance-state-owner: 资金状态责任方; confirmed_as=balance_state_owner; status=confirmed; category=funds_owner
- R-reconciliation-owner: 对账责任方; confirmed_as=reconciliation_owner; status=confirmed; category=financial_ops_owner
- R-split-rule-owner: 分账规则责任方; confirmed_as=split_rule_owner; status=confirmed; category=settlement_owner
- R-platform-fee-owner: 平台手续费责任方; confirmed_as=platform_fee_owner; status=confirmed; category=settlement_owner
- R-merchant-profile-owner: AI 服务商身份责任方; confirmed_as=merchant_profile_owner; status=confirmed; category=merchant_platform_owner
- R-capability-owner: 订阅支付能力开通责任方; confirmed_as=capability_owner; status=confirmed; category=merchant_platform_owner
- R-service-offering-owner: Agent 服务供给责任方; confirmed_as=service_offering_owner; status=confirmed; category=merchant_platform_owner
- R-platform-relationship-owner: 平台责任边界责任方; confirmed_as=platform_relationship_owner; status=confirmed; category=merchant_platform_owner

## User Stories
- US-001: role_ref=R-ai-service-provider; 作为 AI 服务商，我希望接入订阅支付能力，配置面向消费者的 Agent 服务订阅关系。; benefit=不用自建银行通道和订阅生命周期能力，就能商业化提供持续 Agent 服务。; acceptance=AF-001, AF-016
- US-002: role_ref=R-billing-platform; 作为订阅支付平台，我希望管理订阅创建、生效、续期、暂停和终止等生命周期状态。; benefit=AI 服务商可以获得完整订阅生命周期能力，而不是只完成一次性扣款。; acceptance=AF-002, AF-016
- US-003: role_ref=R-usage-rating-owner; 作为混合计费规则责任方，我希望支持固定订阅、按量计费和席位计费的组合计价。; benefit=Agent 服务可以按真实商业模型收费，而不是被限制在单一固定订阅。; acceptance=AF-003, AF-004
- US-004: role_ref=R-metering-owner; 作为用量计量责任方，我希望记录和汇总 Agent 服务使用量，供按量计费计算。; benefit=按量收费可以基于可追溯的用量事实，而不是人工估算或离线结算。; acceptance=AF-004, AF-005
- US-005: role_ref=R-seat-owner; 作为席位计费责任方，我希望管理服务席位数量和席位变更对账单的影响。; benefit=团队型或多用户 Agent 服务可以按席位扩缩容并形成正确应收。; acceptance=AF-004, AF-006
- US-006: role_ref=R-mandate-owner; 作为支付授权责任方，我希望在周期扣款前完成支付方式授权或委托扣款授权，并保留授权证据。; benefit=自动续费和重试扣款具备合规依据，降低扣款争议和失败风险。; acceptance=AF-007
- US-007: role_ref=R-billing-platform; 作为订阅支付平台，我希望在续期日自动生成账单并发起周期扣款和失败重试。; benefit=AI 服务商可以提高续费成功率，并减少人工催收和重复对接成本。; acceptance=AF-007, AF-008, AF-009, AF-016, AF-017
- US-008: role_ref=R-revenue-recovery-owner; 作为续费与催缴运营责任方，我希望对续费失败用户触发催缴、宽限期和挽留策略。; benefit=在扣款失败后仍能恢复收入并提升月续费率。; acceptance=AF-009, AF-010, AF-011
- US-009: role_ref=R-agent-entitlement-owner; 作为 Agent 服务权益责任方，我希望根据订阅和付款状态开通、保持、降级或暂停 Agent 服务权益。; benefit=商业订阅状态可以准确驱动消费者可用的 Agent 服务访问权限。; acceptance=AF-010, AF-011, AF-012, AF-016
- US-010: role_ref=R-split-settlement-owner; 作为分账结算责任方，我希望在账单收款成功后，使用当前生效的分账规则版本和平台手续费规则版本计算收入分账并形成结算批次。; benefit=分账结果可以追溯到明确的规则版本、费用基数和计算顺序，降低多服务方结算争议。; acceptance=AF-013, AF-014, AF-016, AF-019, AF-020
- US-011: role_ref=R-payout-owner; 作为出款责任方，我希望将已结算金额按结算批次出款给对应服务方。; benefit=服务方可以按可追溯的结算结果收到资金，平台减少人工付款和对账负担。; acceptance=AF-014, AF-015, AF-016, AF-019
- US-012: role_ref=R-payment-ops-owner; 作为支付交易处理责任方，我希望订阅账单扣款能够生成支付意图和支付尝试，并收敛出唯一支付结果。; benefit=订阅续费不会停留在账单视角，支付交易状态可以明确驱动后续权益、入账和催缴。; acceptance=AF-016, AF-017, AF-018
- US-013: role_ref=R-ledger-owner; 作为账本入账责任方，我希望支付成功后生成账本分录并更新资金状态。; benefit=后续分账、结算、出款和对账可以基于真实资金事实，而不是只依赖支付成功事件。; acceptance=AF-016, AF-018, AF-019
- US-014: role_ref=R-reconciliation-owner; 作为对账责任方，我希望账单、支付、账本、分账、结算和出款记录可以被核对并标记异常。; benefit=财务运营可以发现链路不一致，保障收入、资金和结算证据一致。; acceptance=AF-016, AF-019
- US-015: role_ref=R-split-rule-owner; 作为分账规则责任方，我希望配置服务方分账规则，包括适用服务供给、收款主体、参与分配的服务方、分配比例或固定金额、生效时间和规则版本。; benefit=平台型 Agent 服务的服务方收入分配可以按已约定且可版本化的规则执行，而不是在结算时临时人工拆分。; acceptance=AF-016, AF-020
- US-016: role_ref=R-platform-fee-owner; 作为平台手续费责任方，我希望配置平台手续费规则，包括计费基数、费率或固定金额、优先扣除顺序、生效时间和规则版本。; benefit=平台收入先按明确规则从服务收入中计算出来，再进入服务方分配和结算，避免平台费用与服务方分账口径混淆。; acceptance=AF-016, AF-020
- US-017: role_ref=R-merchant-profile-owner; 作为 AI 服务商身份责任方，我希望记录 AI 服务商的平台账户、商户身份和收款主体信息。; benefit=订阅支付接入前可以明确谁提供服务、谁收款、谁承担平台关系责任。; acceptance=AF-021, AF-024
- US-018: role_ref=R-capability-owner; 作为订阅支付能力开通责任方，我希望为 AI 服务商开通订阅创建、周期扣款、混合计费和分账结算所需能力。; benefit=服务方不需要自行对接银行通道或拆分实现订阅支付基础能力。; acceptance=AF-022, AF-024
- US-019: role_ref=R-service-offering-owner; 作为 Agent 服务供给责任方，我希望把 Agent 服务、订阅方案和可售能力发布为可配置的服务供给。; benefit=消费者订阅的是明确的 Agent 服务和方案，而不是孤立的支付配置。; acceptance=AF-023, AF-024
- US-020: role_ref=R-platform-relationship-owner; 作为平台责任边界责任方，我希望明确平台与 AI 服务商在订阅、收款、权益、分账和结算中的责任边界。; benefit=平台型 Agent 服务可以在多服务方分账结算时保留清晰责任和追溯依据。; acceptance=AF-024

## Acceptance Functions
- AF-001: AI 服务商完成订阅支付接入配置; stories=US-001; coverage=state_change; AI 服务商完成订阅支付能力接入后，系统可保存面向消费者的 Agent 服务订阅配置，并返回可用于后续订阅创建的配置标识。
- AF-002: 订阅生命周期状态可被创建和流转; stories=US-002; coverage=state_change; 创建订阅后，系统可记录并查询订阅创建、生效、续期、暂停和终止状态，且每次状态变化保留变更时间和原因。
- AF-003: 混合计费规则可配置; stories=US-003; coverage=state_change; 配置价格方案时，系统支持同一 Agent 服务同时包含固定订阅费、按量计费项和席位计费项。
- AF-004: 混合账单按规则汇总应收; stories=US-003, US-004, US-005; coverage=state_change; 生成账单时，系统将固定订阅费、用量费用和席位费用汇总为同一账单应收，并保留各计费项明细。
- AF-005: Agent 使用量可记录并参与计费; stories=US-004; coverage=state_change; 接收 Agent 使用量后，系统可按订阅周期汇总用量，并将汇总结果用于按量计费项计算。
- AF-006: 席位数量和变更影响账单; stories=US-005; coverage=state_change; 席位数量新增、减少或周期内变更后，系统可记录席位变更事实，并在账单中反映对应席位费用。
- AF-007: 周期扣款前存在有效授权证据; stories=US-006, US-007; coverage=evidence, state_change; 发起自动续费扣款前，系统能校验订阅关联的支付授权或委托扣款授权处于有效状态，并可查询授权证据。
- AF-008: 续期日自动生成账单并发起扣款; stories=US-007; coverage=handoff, state_change; 到达订阅续期日时，系统自动生成续期账单，并根据有效支付授权发起周期扣款。
- AF-009: 扣款失败后按策略重试; stories=US-007, US-008; coverage=failure_path, state_change; 周期扣款失败后，系统按配置的重试策略重新发起扣款，并记录每次重试的时间、结果和失败原因。
- AF-010: 续费失败触发催缴和宽限期; stories=US-008, US-009; coverage=failure_path, state_change; 续费扣款失败后，系统创建催缴事件并进入宽限期；宽限期内订阅状态和权益策略可被查询。
- AF-011: 挽留成功后订阅恢复正常; stories=US-008, US-009; coverage=failure_path, state_change; 催缴或挽留期间补缴成功后，系统将订阅恢复为正常状态，并恢复或保持对应 Agent 服务权益。
- AF-012: 订阅和付款状态驱动 Agent 权益; stories=US-009; coverage=handoff, state_change; 订阅生效、付款成功、付款失败、暂停或终止后，系统可同步调整 Agent 服务权益为开通、保持、降级或暂停。
- AF-013: 按规则生成分账结果; stories=US-010; coverage=state_change; 账单收款成功后，系统使用订阅周期内当前生效的分账规则版本和平台手续费规则版本生成收入分账结果；结果必须保留费用基数、平台费用、服务方分配金额、规则版本和计算顺序。
- AF-014: 分账结果可汇入结算批次; stories=US-010, US-011; coverage=state_change; 满足结算条件后，系统可将待结算分账结果汇入结算批次，并记录批次状态、金额合计和明细。
- AF-015: 按结算批次完成出款; stories=US-011; coverage=state_change; 结算批次确认后，系统可根据批次明细向对应服务方发起出款，并记录出款状态和结果。
- AF-016: 支付、账单、权益、结算链路可追溯; stories=US-001, US-002, US-007, US-009, US-010, US-011, US-012, US-013, US-014, US-015, US-016; coverage=evidence; 针对同一订阅周期，系统可从订阅、账单、支付结果、权益状态、分账结果、结算批次和出款记录追溯完整链路。
- AF-017: 支付意图和支付尝试收敛唯一结果; stories=US-007, US-012; coverage=state_change; 订阅账单发起扣款后，系统创建支付意图和支付尝试；支付完成、失败或处理中状态最终收敛为一个可查询的最终结果。
- AF-018: 支付成功后生成账本和资金状态; stories=US-012, US-013; coverage=evidence, handoff, state_change; 支付成功事件产生后，系统生成对应账本分录，并把资金状态标记为可用于后续分账或结算的状态。
- AF-019: 支付到账本到结算链路可对账; stories=US-013, US-014, US-010, US-011; coverage=evidence; 系统可对同一订阅周期的账单、支付结果、账本分录、分账结果、结算批次和出款记录生成对账记录；不一致时生成对账异常。
- AF-020: 分账规则、平台手续费和分账结果关系明确; stories=US-010, US-015, US-016; coverage=state_change; 生成分账结果时，系统先确定费用基数，再按平台手续费规则计算平台费用，随后按服务方分账规则分配剩余可分配金额；每条分账结果都引用对应的分账规则版本和平台手续费规则版本。
- AF-021: AI 服务商身份和平台账户可记录; stories=US-017; coverage=state_change, evidence; AI 服务商接入前，系统可记录并查询其平台账户、商户身份、收款主体和平台关系状态。
- AF-022: 订阅支付能力可按服务方开通; stories=US-018; coverage=state_change; 平台可为 AI 服务商开通订阅创建、周期扣款、混合计费和分账结算能力，并记录能力开通状态、范围和生效时间。
- AF-023: Agent 服务供给可绑定订阅方案; stories=US-019; coverage=state_change; AI 服务商可发布 Agent 服务供给，并将服务供给绑定到固定订阅、按量计费、席位计费或混合订阅方案。
- AF-024: 平台责任边界可追溯; stories=US-017, US-018, US-019, US-020; coverage=evidence; 系统可查询平台与 AI 服务商在订阅配置、收款、权益、分账、结算和出款中的责任边界，并保留版本和生效记录。

## Soft Evidence
### Acceptance Extraction
- {"source": "req-acceptance", "summary": "Defined observable acceptance functions for subscription setup, lifecycle, mixed billing, metering, seats, mandate, renewal retry, dunning, entitlement, split settlement, payout, and traceability."}
### Design Clarification Gate
- {"approval_status": "approved_by_user", "design_boundary": "没有材料时只能保留需求骨架和待确认项，不能由 AGI 推断现状。", "gate": "current_state_materials", "gate_strength": "hard_before_detailed_design", "hard_gate_ref": "current_state_material_package", "must_clarify": "现有订阅、扣款、账单、权益、分账、结算、出款和对账流程是否已有系统、人工流程、合同或数据样例。", "owner": "requirement_proposer"}
- {"approval_status": "approved_by_user", "design_boundary": "需求只确认规则归属、版本和计算顺序；具体表达式和异常规则进入详细设计门禁。", "gate": "rule_detail_materials", "gate_strength": "hard_before_detailed_design", "hard_gate_ref": "business_rule_position_table", "must_clarify": "平台手续费、服务方分账、尾差舍入、退款/拒付/补偿、税费或成本扣减等规则是否进入首版以及具体口径。", "owner": "rule_owner_and_settlement_owner"}
- {"design_boundary": "验收只要求状态可流转和可追溯；策略参数不能凭行业默认值生成。", "gate": "lifecycle_policy_materials", "gate_strength": "dependent_before_detailed_design", "must_clarify": "订阅状态、续期日、扣款重试次数和间隔、宽限期、催缴/挽留触发条件、权益降级或暂停策略。", "owner": "billing_ops_owner_and_revenue_recovery_owner"}
- {"approval_status": "approved_by_user", "design_boundary": "需求可确认上下文交接，详细接口契约必须等系统边界材料确认。", "gate": "integration_boundary_materials", "gate_strength": "hard_before_detailed_design", "hard_gate_ref": "system_boundary_contract_table", "must_clarify": "AI 服务、服务供给、席位、用量、权益系统与订阅支付平台之间的 API、事件、回调、幂等和失败补偿边界。", "owner": "platform_relationship_owner_and_agent_service_owner"}
- {"design_boundary": "验收只要求链路可追溯和可对账；账务分录、资金状态机和批次规则需要设计前材料。", "gate": "funds_accounting_materials", "gate_strength": "dependent_before_detailed_design", "must_clarify": "支付成功如何入账、资金何时可分账/可结算/可出款、结算批次条件、出款失败处理、对账异常口径。", "owner": "ledger_owner_reconciliation_owner_and_payout_owner"}
- {"design_boundary": "需求已把该域升为首版完整故事；详细设计不能假设平台主体、商户主体或责任划分。", "gate": "merchant_platform_responsibility_materials", "gate_strength": "dependent_before_detailed_design", "must_clarify": "AI 服务商身份、收款主体、平台账户、能力开通范围、平台与服务商责任边界及版本化协议材料。", "owner": "merchant_profile_owner_capability_owner_and_platform_relationship_owner"}
- {"design_boundary": "验收要求可追溯；字段级审计模型和证据保留周期需在设计门禁中确认。", "gate": "traceability_and_audit_materials", "gate_strength": "dependent_before_detailed_design", "must_clarify": "哪些对象必须保留版本、生效时间、操作者、来源证据、外部流水号和跨链路追溯 ID。", "owner": "requirement_proposer_with_domain_owners"}
### Detailed Design Hard Gates
- {"approval_status": "approved_by_user", "approved_at": "2026-06-04", "blocks_until_passed": "详细设计、API 契约、DDL/表结构、状态机和研发拆解。", "gate": "current_state_material_package", "hard_gate": true, "pass_condition": "产品明确提供可引用材料，或明确确认当前没有存量系统/人工流程并给出首版约束。", "reason": "没有现状材料时，AGI 只能生成需求骨架，不能判断迁移约束、兼容约束或现有职责边界。", "required_from": "product_owner_or_requirement_proposer", "required_material": "现状材料：现有订阅、扣款、账单、权益、分账、结算、出款、对账流程的流程图、系统截图、配置样例、合同口径、账单样例或明确的 greenfield 确认。"}
- {"approval_status": "approved_by_user", "approved_at": "2026-06-04", "blocks_until_passed": "详细设计中的规则模型、金额计算、批次生成、反向分账和异常处理。", "gate": "business_rule_position_table", "hard_gate": true, "pass_condition": "产品明确每类规则是否进入首版、由谁维护、使用什么业务口径；未进入首版的规则必须记录延期边界。", "reason": "验收只确认规则可配置、可追溯和计算顺序；具体金额口径不能用行业默认值补齐。", "required_from": "product_owner_with_rule_owner_and_settlement_owner", "required_material": "规则口径表：平台手续费、服务方分账、尾差舍入、退款、拒付、补偿、税费、结算条件、出款失败和对账异常的首版/非首版边界及计算口径。"}
- {"approval_status": "approved_by_user", "approved_at": "2026-06-04", "blocks_until_passed": "接口设计、事件设计、权限/权益联动、用量计费联动和端到端时序设计。", "gate": "system_boundary_contract_table", "hard_gate": true, "pass_condition": "产品明确每个上下文交接由哪个系统发起、哪个系统承接、失败如何恢复、哪些字段由谁负责。", "reason": "需求可以确认上下文关系，但系统集成契约必须由真实系统边界材料决定。", "required_from": "product_owner_with_platform_relationship_owner_and_agent_service_owner", "required_material": "系统边界表：Agent 服务供给、用量、席位、权益系统与订阅支付平台之间的 API、事件、回调、幂等键、失败补偿、责任归属和数据 owner。"}
### Domain Coverage Matrix
- {"acceptance_function_ids": ["AF-001", "AF-002", "AF-003", "AF-004", "AF-005", "AF-006", "AF-008", "AF-009", "AF-010", "AF-011"], "aggregate_roots": ["commercial_subscription", "invoice", "price_plan", "billing_schedule", "usage_record", "rating_rule", "seat_assignment", "dunning_case", "grace_period", "retry_schedule"], "contexts": ["commercial_subscription_context", "billing_invoice_context", "usage_rating_context", "revenue_recovery_context"], "coverage_type": "primary", "review_note": "主域覆盖订阅关系、账单、混合计费、续期、重试和催缴。", "subdomain": "billing_revenue", "user_story_ids": ["US-001", "US-002", "US-003", "US-004", "US-005", "US-007", "US-008"]}
- {"acceptance_function_ids": ["AF-001", "AF-021", "AF-022", "AF-023", "AF-024"], "aggregate_roots": ["merchant", "platform_account", "capability_grant", "service_offering", "platform_relationship"], "contexts": ["merchant_identity_context", "merchant_capability_context", "merchant_service_offering_context", "platform_responsibility_context"], "coverage_type": "full_coverage", "review_note": "用户审核确认 4：商户身份、能力开通、服务供给和平台责任边界进入首版完整故事。", "subdomain": "merchant_platform_relationship", "user_story_ids": ["US-001", "US-017", "US-018", "US-019", "US-020"]}
- {"acceptance_function_ids": ["AF-007", "AF-008", "AF-009", "AF-017"], "aggregate_roots": ["payment_intent", "payment_attempt", "charge", "payment_method_authorization"], "contexts": ["payment_intent_context", "payment_attempt_authorization_context", "payment_method_context"], "coverage_type": "required_payment", "review_note": "补强后覆盖授权校验、续期扣款、失败重试、支付意图和支付尝试结果收敛。", "subdomain": "payment_transaction", "user_story_ids": ["US-006", "US-007", "US-012"]}
- {"acceptance_function_ids": ["AF-018", "AF-016"], "aggregate_roots": ["ledger_entry", "fund_state"], "contexts": ["balance_ledger_context", "fund_state_context"], "coverage_type": "required_payment", "review_note": "补强后覆盖支付成功后的账本分录和资金状态；余额、reserve、limit 暂不展开。", "subdomain": "account_balance", "user_story_ids": ["US-013"]}
- {"acceptance_function_ids": ["AF-019", "AF-016"], "aggregate_roots": ["reconciliation_record", "reconciliation_exception"], "contexts": ["reconciliation_context"], "coverage_type": "required_payment", "review_note": "补强后覆盖账单、支付、账本、分账、结算和出款链路对账；财务报表和关账暂不展开。", "subdomain": "financial_operations", "user_story_ids": ["US-014"]}
- {"acceptance_function_ids": ["AF-007"], "aggregate_roots": ["payment_mandate", "authorization_consent", "consent_record"], "contexts": ["mandate_authorization_context"], "coverage_type": "required_payment", "review_note": "覆盖周期扣款授权证据；KYB、AML、交易风控不在当前首版故事中展开。", "subdomain": "risk_compliance", "user_story_ids": ["US-006"]}
- {"acceptance_function_ids": ["AF-013", "AF-014", "AF-015", "AF-020", "AF-016"], "aggregate_roots": ["split_rule", "allocation_result", "platform_fee", "settlement_batch", "payout"], "contexts": ["split_allocation_context", "settlement_batch_context", "payout_context"], "coverage_type": "conditional_payment_in_scope", "review_note": "用户确认首版包含分账、结算和出款；补强后覆盖分账规则、平台费用、结算批次和出款。", "subdomain": "funds_movement_settlement", "user_story_ids": ["US-010", "US-011", "US-015", "US-016"]}
- {"acceptance_function_ids": ["AF-010", "AF-011", "AF-012", "AF-016"], "aggregate_roots": ["agent_entitlement"], "contexts": ["agent_entitlement_context"], "coverage_type": "adjacent_agent_service", "review_note": "覆盖订阅和付款状态驱动 Agent 权益开通、保持、降级或暂停。", "subdomain": "agent_entitlement", "user_story_ids": ["US-009"]}
- {"acceptance_function_ids": ["AF-004", "AF-005"], "aggregate_roots": ["candidate:usage_event"], "contexts": ["agent_usage_metering_context"], "coverage_type": "adjacent_agent_service_conditional", "review_note": "覆盖按量计费用量汇总；usage_event 仍是 taxonomy 候选术语，当前作为邻接证据保留。", "subdomain": "agent_usage_metering", "user_story_ids": ["US-004"]}
- {"acceptance_function_ids": ["AF-004", "AF-006"], "aggregate_roots": ["seat_assignment"], "contexts": ["agent_workspace_seat_context"], "coverage_type": "adjacent_agent_service_conditional", "review_note": "覆盖席位数量和席位变更对账单影响。", "subdomain": "agent_workspace_seat", "user_story_ids": ["US-005"]}
### Domain Coverage Review
- {"review_focus": "merchant_platform_relationship first-release depth", "status": "confirmed", "summary": "User review confirmed merchant platform relationship full-story scope."}
- {"review_focus": "US-010 US-015 US-016 split rule relationship", "status": "clarified", "summary": "User review asked to clarify the agreed rules and relationship among split settlement, split rule, and platform fee stories."}
- {"review_focus": "detail-design-clarification-gate", "status": "accepted_as_gate", "summary": "User accepted the requirement skeleton and clarified that missing current-state materials must become proposer clarification gates before detailed design, not AGI-inferred design facts."}
- {"review_focus": "product-hard-design-gates", "status": "accepted_as_hard_gate", "summary": "User asked whether the three missing material packages can become hard gates; case now treats them as product clarification gates that block detailed design but not the already reviewable requirement skeleton."}
- {"review_focus": "product-hard-design-gates-final-review", "status": "approved", "summary": "User confirmed the three hard design gates are acceptable; case can move from user review to waiting for product-provided gate materials."}
### Domain Model
- {"aggregate_roots": ["commercial_subscription", "invoice", "dunning_case", "payment_intent", "payment_attempt", "ledger_entry", "fund_state", "reconciliation_record", "mandate", "agent_entitlement", "usage_event", "seat_assignment", "split_rule", "settlement_batch", "payout"], "bounded_contexts": ["commercial_subscription_context", "billing_invoice_context", "revenue_recovery_context", "payment_intent_context", "payment_attempt_authorization_context", "balance_ledger_context", "fund_state_context", "reconciliation_context", "mandate_authorization_context", "agent_entitlement_context", "agent_usage_metering_context", "agent_workspace_seat_context", "split_allocation_context", "settlement_batch_context", "payout_context"], "business_ecosystems": ["payment_ecosystem", "agent_service_ecosystem"], "candidates": [], "context_handoffs": [{"from_context": "commercial_subscription_context", "name": "GenerateInvoice", "to_context": "billing_invoice_context", "type": "command"}, {"from_context": "billing_invoice_context", "name": "ChargeInvoice", "to_context": "payment_intent_context", "type": "command"}, {"from_context": "payment_attempt_authorization_context", "name": "PaymentSucceeded", "to_context": "balance_ledger_context", "type": "domain_event"}, {"from_context": "commercial_subscription_context", "name": "CommercialSubscriptionActivated", "to_context": "agent_entitlement_context", "type": "domain_event"}], "fact_owners": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "non_domain_terms": ["subscription", "account", "settlement"], "open_questions": ["Confirm first-release payout/split settlement scope."], "role_obligations": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "status": "confirmed", "subdomains": ["billing_revenue", "merchant_platform_relationship", "payment_transaction", "account_balance", "funds_movement_settlement", "financial_operations", "risk_compliance", "agent_entitlement", "agent_usage_metering", "agent_workspace_seat"]}
### Intake Actors
- {"id": "ai_service_provider", "label": "AI service provider", "type": "organization"}
- {"id": "platform", "label": "platform", "type": "organization"}
- {"id": "consumer", "label": "consumer", "type": "person"}
- {"id": "recurring_billing_job", "label": "recurring billing automation", "type": "system"}
- {"id": "payment_channel", "label": "payment channel", "type": "external_system"}
### Open Questions
- {"question": "硬门禁 1：产品是否能提供现状材料包，或明确确认当前没有存量系统/人工流程并给出首版约束？"}
- {"question": "硬门禁 2：产品是否能提供规则口径表，明确平台手续费、分账、尾差、退款/拒付/补偿、税费、结算和异常口径的首版边界？"}
- {"question": "硬门禁 3：产品是否能提供系统边界表，明确 Agent 服务、用量、席位、权益系统和订阅支付平台之间的 API/事件/回调/责任边界？"}
- {"question": "首版平台手续费是否只支持按比例和固定金额，还是需要阶梯费率？"}
- {"question": "尾差和舍入金额默认归平台、归最大服务方，还是要求显式配置？"}
- {"question": "退款、拒付、补偿是否进入首版反向分账规则，还是作为后续规则扩展？"}
### Rule Clarification
- {"summary": "US-015 owns service-provider split rule configuration; US-016 owns platform fee rule configuration; US-010 consumes the effective versions of both rules to produce allocation results and settlement batches.", "topic": "rule_ownership"}
- {"summary": "首版规则集合包括适用服务供给、收款主体、参与分配服务方、费用基数、平台手续费、服务方分配比例或固定金额、生效时间、规则版本、结算条件和追溯引用。", "topic": "first_release_rule_set"}
- {"summary": "分账计算顺序为：确认已收款账单费用基数 -> 使用平台手续费规则计算平台费用 -> 使用服务方分账规则分配剩余可分配金额 -> 生成分账结果 -> 满足结算条件后汇入结算批次。", "topic": "calculation_order"}
- {"summary": "需求阶段只确认业务规则关系和追溯字段；具体费率表达式、舍入尾差策略、税费处理、退款/拒付后的反向分账属于后续设计或扩展规则。", "topic": "traceability_boundary"}
### Scope Decisions
- {"decision": "first_release_split_settlement", "evidence": "用户复审确认 2: 确认", "value": "in_scope"}
- {"decision": "target_customer", "evidence": "用户复审确认 1: 没错", "value": "AI 服务商"}
- {"decision": "commercial_model", "evidence": "用户确认 3: 混合", "value": "混合计费"}
- {"decision": "mandate_and_recurring_retry", "evidence": "用户复审确认 3: 确认", "value": "in_scope"}
- {"decision": "merchant_platform_relationship_full_stories", "evidence": "用户复审确认 4: 确认", "value": "in_scope"}
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
- {"answers": [{"answer": "没错", "question": "US-001 首版是否只做 AI 服务商接入并配置订阅支付关系？"}, {"answer": "确认", "question": "首版是否包含分账、结算批次、出款、平台手续费？"}, {"answer": "确认", "question": "周期扣款授权/委托扣款是否进入首版？"}, {"answer": "确认", "question": "商户身份、能力开通、服务供给、平台责任边界是否升级为完整故事？"}], "confirmed_at": "2026-06-04", "source": "chat_user_review"}
- {"answers": [{"answer": "可以", "question": "US-010/US-015/US-016 规则关系是否可接受？"}, {"answer": "确认，应泛化到规则以外的详细设计前澄清点。", "question": "缺少现状材料时是否应通过门禁要求需求提出方澄清，而不是由 AGI 推断设计？"}], "confirmed_at": "2026-06-04", "source": "chat_user_design_gate_confirmation_2026_06_04"}
- {"answers": [{"answer": "可以；作为详细设计前硬门禁，由产品/需求提出方澄清。", "question": "现状材料、规则口径表、系统边界表是否可以变成硬门禁要求产品澄清？"}], "confirmed_at": "2026-06-04", "source": "chat_user_hard_gate_confirmation_2026_06_04"}
- {"answers": [{"answer": "认可，没问题。", "question": "三项详细设计硬门禁是否认可，可以作为后续要求产品澄清的规则？"}], "confirmed_at": "2026-06-04", "source": "chat_user_hard_gate_final_approval_2026_06_04"}

## Readiness / Next Action
- Status: requirements_ready
- Next action: await_product_hard_gate_materials
- Reason: The user approved the three detailed-design hard gates; product/requirement proposer must now provide the current-state material package, business rule position table, and system boundary contract table before detailed design starts.
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
- This case records intake, scope, stories, acceptance functions, and domain coverage evidence.
- The requirements checker now enforces domain_model_gate, domain_coverage_gate, and requirement_delivery_gate for strict taxonomy v2 cases.
- Passing gates prove the requirement case is reviewable for OpenSpec handoff; they do not prove implementation design, API, DDL, or release correctness.
- The acceptance skeleton is ready for review, but detailed design must pass proposer clarification gates for missing current-state materials, policy parameters, integration boundaries, accounting rules, and audit evidence.
- AGI-generated analysis must not infer current implementation state, rule parameters, operating policies, or accounting treatment without proposer-provided material evidence.
- The current-state material package, business rule position table, and system boundary contract table are hard gates before detailed design; missing them blocks API, DDL, state-machine, and work-breakdown design.
- These hard gates are product clarification gates for design readiness; they do not invalidate the current requirements_ready skeleton or its acceptance coverage.

## Machine Case Data
<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [
    {
      "aggregate_refs": [
        "billing_schedule",
        "capability_grant",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "merchant",
        "platform_relationship",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "service_offering",
        "usage_record"
      ],
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "merchant_capability_context",
        "merchant_identity_context",
        "merchant_service_offering_context",
        "platform_responsibility_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "candidate:usage_event",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "agent_usage_metering_context",
        "agent_workspace_seat_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "candidate:usage_event",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "agent_usage_metering_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "agent_workspace_seat_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "authorization_consent",
        "charge",
        "consent_record",
        "payment_attempt",
        "payment_intent",
        "payment_mandate",
        "payment_method_authorization"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context"
      ],
      "coverage_types": [
        "evidence",
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "charge",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "payment_attempt",
        "payment_intent",
        "payment_method_authorization",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "handoff",
        "state_change"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "charge",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "payment_attempt",
        "payment_intent",
        "payment_method_authorization",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
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
      "aggregate_refs": [
        "agent_entitlement",
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "agent_entitlement_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
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
      "aggregate_refs": [
        "agent_entitlement",
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "context_refs": [
        "agent_entitlement_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
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
      "aggregate_refs": [
        "agent_entitlement",
        "commercial_subscription"
      ],
      "context_refs": [
        "agent_entitlement_context",
        "commercial_subscription_context"
      ],
      "coverage_types": [
        "handoff",
        "state_change"
      ],
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
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "then": "账单收款成功后，系统使用订阅周期内当前生效的分账规则版本和平台手续费规则版本生成收入分账结果；结果必须保留费用基数、平台费用、服务方分配金额、规则版本和计算顺序。",
      "user_story_ids": [
        "US-010"
      ]
    },
    {
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "coverage_types": [
        "state_change"
      ],
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
      "aggregate_refs": [
        "agent_entitlement",
        "allocation_result",
        "fund_state",
        "ledger_entry",
        "payout",
        "platform_fee",
        "reconciliation_exception",
        "reconciliation_record",
        "settlement_batch",
        "split_rule"
      ],
      "context_refs": [
        "agent_entitlement_context",
        "balance_ledger_context",
        "fund_state_context",
        "payout_context",
        "reconciliation_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "coverage_types": [
        "evidence"
      ],
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
        "US-011",
        "US-012",
        "US-013",
        "US-014",
        "US-015",
        "US-016"
      ]
    },
    {
      "aggregate_refs": [
        "charge",
        "payment_attempt",
        "payment_intent",
        "payment_method_authorization"
      ],
      "context_refs": [
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context"
      ],
      "coverage_types": [
        "state_change"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: payment_transaction"
      },
      "id": "AF-017",
      "name": "支付意图和支付尝试收敛唯一结果",
      "source_acceptance": "US-012",
      "source_functions": [
        "domain coverage: payment_transaction"
      ],
      "then": "订阅账单发起扣款后，系统创建支付意图和支付尝试；支付完成、失败或处理中状态最终收敛为一个可查询的最终结果。",
      "user_story_ids": [
        "US-007",
        "US-012"
      ]
    },
    {
      "aggregate_refs": [
        "fund_state",
        "ledger_entry",
        "payment_attempt"
      ],
      "context_refs": [
        "balance_ledger_context",
        "fund_state_context",
        "payment_attempt_authorization_context"
      ],
      "coverage_types": [
        "evidence",
        "handoff",
        "state_change"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: account_balance"
      },
      "id": "AF-018",
      "name": "支付成功后生成账本和资金状态",
      "source_acceptance": "US-013",
      "source_functions": [
        "domain coverage: account_balance"
      ],
      "then": "支付成功事件产生后，系统生成对应账本分录，并把资金状态标记为可用于后续分账或结算的状态。",
      "user_story_ids": [
        "US-012",
        "US-013"
      ]
    },
    {
      "aggregate_refs": [
        "reconciliation_exception",
        "reconciliation_record"
      ],
      "context_refs": [
        "reconciliation_context"
      ],
      "coverage_types": [
        "evidence"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: financial_operations"
      },
      "id": "AF-019",
      "name": "支付到账本到结算链路可对账",
      "source_acceptance": "US-014",
      "source_functions": [
        "domain coverage: financial_operations"
      ],
      "then": "系统可对同一订阅周期的账单、支付结果、账本分录、分账结果、结算批次和出款记录生成对账记录；不一致时生成对账异常。",
      "user_story_ids": [
        "US-013",
        "US-014",
        "US-010",
        "US-011"
      ]
    },
    {
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "coverage_types": [
        "state_change"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: split_allocation_context"
      },
      "id": "AF-020",
      "name": "分账规则、平台手续费和分账结果关系明确",
      "source_acceptance": "US-015,US-016",
      "source_functions": [
        "domain coverage: split_allocation_context"
      ],
      "then": "生成分账结果时，系统先确定费用基数，再按平台手续费规则计算平台费用，随后按服务方分账规则分配剩余可分配金额；每条分账结果都引用对应的分账规则版本和平台手续费规则版本。",
      "user_story_ids": [
        "US-010",
        "US-015",
        "US-016"
      ]
    },
    {
      "aggregate_refs": [
        "merchant",
        "platform_account",
        "platform_relationship"
      ],
      "context_refs": [
        "merchant_identity_context",
        "platform_responsibility_context"
      ],
      "coverage_types": [
        "state_change",
        "evidence"
      ],
      "id": "AF-021",
      "name": "AI 服务商身份和平台账户可记录",
      "source_acceptance": "用户审核确认 4 / 商户身份完整故事",
      "then": "AI 服务商接入前，系统可记录并查询其平台账户、商户身份、收款主体和平台关系状态。",
      "user_story_ids": [
        "US-017"
      ]
    },
    {
      "aggregate_refs": [
        "capability_grant",
        "platform_relationship"
      ],
      "context_refs": [
        "merchant_capability_context",
        "platform_responsibility_context"
      ],
      "coverage_types": [
        "state_change"
      ],
      "id": "AF-022",
      "name": "订阅支付能力可按服务方开通",
      "source_acceptance": "用户审核确认 4 / 能力开通完整故事",
      "then": "平台可为 AI 服务商开通订阅创建、周期扣款、混合计费和分账结算能力，并记录能力开通状态、范围和生效时间。",
      "user_story_ids": [
        "US-018"
      ]
    },
    {
      "aggregate_refs": [
        "service_offering",
        "platform_relationship"
      ],
      "context_refs": [
        "merchant_service_offering_context",
        "platform_responsibility_context"
      ],
      "coverage_types": [
        "state_change"
      ],
      "id": "AF-023",
      "name": "Agent 服务供给可绑定订阅方案",
      "source_acceptance": "用户审核确认 4 / 服务供给完整故事",
      "then": "AI 服务商可发布 Agent 服务供给，并将服务供给绑定到固定订阅、按量计费、席位计费或混合订阅方案。",
      "user_story_ids": [
        "US-019"
      ]
    },
    {
      "aggregate_refs": [
        "platform_relationship",
        "platform_account"
      ],
      "context_refs": [
        "platform_responsibility_context"
      ],
      "coverage_types": [
        "evidence"
      ],
      "id": "AF-024",
      "name": "平台责任边界可追溯",
      "source_acceptance": "用户审核确认 4 / 平台责任边界完整故事",
      "then": "系统可查询平台与 AI 服务商在订阅配置、收款、权益、分账、结算和出款中的责任边界，并保留版本和生效记录。",
      "user_story_ids": [
        "US-017",
        "US-018",
        "US-019",
        "US-020"
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
  "domain_coverage": [
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-002",
        "AF-003",
        "AF-004",
        "AF-005",
        "AF-006",
        "AF-008",
        "AF-009",
        "AF-010",
        "AF-011"
      ],
      "aggregate_roots": [
        "commercial_subscription",
        "invoice",
        "price_plan",
        "billing_schedule",
        "usage_record",
        "rating_rule",
        "seat_assignment",
        "dunning_case",
        "grace_period",
        "retry_schedule"
      ],
      "contexts": [
        "commercial_subscription_context",
        "billing_invoice_context",
        "usage_rating_context",
        "revenue_recovery_context"
      ],
      "coverage_type": "primary",
      "review_note": "主域覆盖订阅关系、账单、混合计费、续期、重试和催缴。",
      "subdomain": "billing_revenue",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-003",
        "US-004",
        "US-005",
        "US-007",
        "US-008"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-021",
        "AF-022",
        "AF-023",
        "AF-024"
      ],
      "aggregate_roots": [
        "merchant",
        "platform_account",
        "capability_grant",
        "service_offering",
        "platform_relationship"
      ],
      "contexts": [
        "merchant_identity_context",
        "merchant_capability_context",
        "merchant_service_offering_context",
        "platform_responsibility_context"
      ],
      "coverage_type": "full_coverage",
      "review_note": "用户审核确认 4：商户身份、能力开通、服务供给和平台责任边界进入首版完整故事。",
      "subdomain": "merchant_platform_relationship",
      "user_story_ids": [
        "US-001",
        "US-017",
        "US-018",
        "US-019",
        "US-020"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-007",
        "AF-008",
        "AF-009",
        "AF-017"
      ],
      "aggregate_roots": [
        "payment_intent",
        "payment_attempt",
        "charge",
        "payment_method_authorization"
      ],
      "contexts": [
        "payment_intent_context",
        "payment_attempt_authorization_context",
        "payment_method_context"
      ],
      "coverage_type": "required_payment",
      "review_note": "补强后覆盖授权校验、续期扣款、失败重试、支付意图和支付尝试结果收敛。",
      "subdomain": "payment_transaction",
      "user_story_ids": [
        "US-006",
        "US-007",
        "US-012"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-018",
        "AF-016"
      ],
      "aggregate_roots": [
        "ledger_entry",
        "fund_state"
      ],
      "contexts": [
        "balance_ledger_context",
        "fund_state_context"
      ],
      "coverage_type": "required_payment",
      "review_note": "补强后覆盖支付成功后的账本分录和资金状态；余额、reserve、limit 暂不展开。",
      "subdomain": "account_balance",
      "user_story_ids": [
        "US-013"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-019",
        "AF-016"
      ],
      "aggregate_roots": [
        "reconciliation_record",
        "reconciliation_exception"
      ],
      "contexts": [
        "reconciliation_context"
      ],
      "coverage_type": "required_payment",
      "review_note": "补强后覆盖账单、支付、账本、分账、结算和出款链路对账；财务报表和关账暂不展开。",
      "subdomain": "financial_operations",
      "user_story_ids": [
        "US-014"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-007"
      ],
      "aggregate_roots": [
        "payment_mandate",
        "authorization_consent",
        "consent_record"
      ],
      "contexts": [
        "mandate_authorization_context"
      ],
      "coverage_type": "required_payment",
      "review_note": "覆盖周期扣款授权证据；KYB、AML、交易风控不在当前首版故事中展开。",
      "subdomain": "risk_compliance",
      "user_story_ids": [
        "US-006"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-013",
        "AF-014",
        "AF-015",
        "AF-020",
        "AF-016"
      ],
      "aggregate_roots": [
        "split_rule",
        "allocation_result",
        "platform_fee",
        "settlement_batch",
        "payout"
      ],
      "contexts": [
        "split_allocation_context",
        "settlement_batch_context",
        "payout_context"
      ],
      "coverage_type": "conditional_payment_in_scope",
      "review_note": "用户确认首版包含分账、结算和出款；补强后覆盖分账规则、平台费用、结算批次和出款。",
      "subdomain": "funds_movement_settlement",
      "user_story_ids": [
        "US-010",
        "US-011",
        "US-015",
        "US-016"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-010",
        "AF-011",
        "AF-012",
        "AF-016"
      ],
      "aggregate_roots": [
        "agent_entitlement"
      ],
      "contexts": [
        "agent_entitlement_context"
      ],
      "coverage_type": "adjacent_agent_service",
      "review_note": "覆盖订阅和付款状态驱动 Agent 权益开通、保持、降级或暂停。",
      "subdomain": "agent_entitlement",
      "user_story_ids": [
        "US-009"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-004",
        "AF-005"
      ],
      "aggregate_roots": [
        "candidate:usage_event"
      ],
      "contexts": [
        "agent_usage_metering_context"
      ],
      "coverage_type": "adjacent_agent_service_conditional",
      "review_note": "覆盖按量计费用量汇总；usage_event 仍是 taxonomy 候选术语，当前作为邻接证据保留。",
      "subdomain": "agent_usage_metering",
      "user_story_ids": [
        "US-004"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-004",
        "AF-006"
      ],
      "aggregate_roots": [
        "seat_assignment"
      ],
      "contexts": [
        "agent_workspace_seat_context"
      ],
      "coverage_type": "adjacent_agent_service_conditional",
      "review_note": "覆盖席位数量和席位变更对账单影响。",
      "subdomain": "agent_workspace_seat",
      "user_story_ids": [
        "US-005"
      ]
    }
  ],
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
    "This case records intake, scope, stories, acceptance functions, and domain coverage evidence.",
    "The requirements checker now enforces domain_model_gate, domain_coverage_gate, and requirement_delivery_gate for strict taxonomy v2 cases.",
    "Passing gates prove the requirement case is reviewable for OpenSpec handoff; they do not prove implementation design, API, DDL, or release correctness.",
    "The acceptance skeleton is ready for review, but detailed design must pass proposer clarification gates for missing current-state materials, policy parameters, integration boundaries, accounting rules, and audit evidence.",
    "AGI-generated analysis must not infer current implementation state, rule parameters, operating policies, or accounting treatment without proposer-provided material evidence.",
    "The current-state material package, business rule position table, and system boundary contract table are hard gates before detailed design; missing them blocks API, DDL, state-machine, and work-breakdown design.",
    "These hard gates are product clarification gates for design readiness; they do not invalidate the current requirements_ready skeleton or its acceptance coverage."
  ],
  "readiness_next_action": {
    "next_action": "await_product_hard_gate_materials",
    "reason": "The user approved the three detailed-design hard gates; product/requirement proposer must now provide the current-state material package, business rule position table, and system boundary contract table before detailed design starts.",
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
    },
    {
      "category": "payment_owner",
      "confirmed_as": "payment_ops_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: payment_transaction"
      },
      "id": "R-payment-ops-owner",
      "mention": "支付交易处理责任方",
      "normalization_note": "订阅续期扣款需要 payment_intent 和 payment_attempt 状态收敛，映射到 payment_ops_owner。",
      "source_actors": [
        "周期扣款",
        "支付结果",
        "失败重试"
      ],
      "status": "confirmed"
    },
    {
      "category": "funds_owner",
      "confirmed_as": "ledger_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: account_balance"
      },
      "id": "R-ledger-owner",
      "mention": "账本入账责任方",
      "normalization_note": "订阅扣款成功后的账本分录和资金事实映射到 ledger_owner。",
      "source_actors": [
        "收款成功",
        "账本",
        "资金状态"
      ],
      "status": "confirmed"
    },
    {
      "category": "funds_owner",
      "confirmed_as": "balance_state_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: account_balance"
      },
      "id": "R-balance-state-owner",
      "mention": "资金状态责任方",
      "normalization_note": "收款后资金状态从支付成功到可结算/待结算的变化映射到 balance_state_owner。",
      "source_actors": [
        "资金状态",
        "可结算金额",
        "待结算金额"
      ],
      "status": "confirmed"
    },
    {
      "category": "financial_ops_owner",
      "confirmed_as": "reconciliation_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: financial_operations"
      },
      "id": "R-reconciliation-owner",
      "mention": "对账责任方",
      "normalization_note": "支付、账本、结算和出款之间的可核对证据映射到 reconciliation_owner。",
      "source_actors": [
        "账单",
        "支付结果",
        "账本",
        "结算批次"
      ],
      "status": "confirmed"
    },
    {
      "category": "settlement_owner",
      "confirmed_as": "split_rule_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: funds_movement_settlement"
      },
      "id": "R-split-rule-owner",
      "mention": "分账规则责任方",
      "normalization_note": "用户确认首版包含分账，分账规则和分配结果映射到 split_rule_owner。",
      "source_actors": [
        "分账规则",
        "服务方收入分配"
      ],
      "status": "confirmed"
    },
    {
      "category": "settlement_owner",
      "confirmed_as": "platform_fee_owner",
      "evidence_anchor": {
        "source_section": "领域覆盖补强: funds_movement_settlement"
      },
      "id": "R-platform-fee-owner",
      "mention": "平台手续费责任方",
      "normalization_note": "平台抽佣或服务费作为分账规则的一部分，映射到 platform_fee_owner。",
      "source_actors": [
        "平台型智能体服务",
        "收入分给多个服务方"
      ],
      "status": "confirmed"
    },
    {
      "category": "merchant_platform_owner",
      "confirmed_as": "merchant_profile_owner",
      "evidence_anchor": {
        "source_section": "用户审核确认: 商户身份升级为完整首版故事"
      },
      "id": "R-merchant-profile-owner",
      "mention": "AI 服务商身份责任方",
      "source_actors": [
        "AI 服务商"
      ],
      "status": "confirmed"
    },
    {
      "category": "merchant_platform_owner",
      "confirmed_as": "capability_owner",
      "evidence_anchor": {
        "source_section": "用户审核确认: 能力开通升级为完整首版故事"
      },
      "id": "R-capability-owner",
      "mention": "订阅支付能力开通责任方",
      "source_actors": [
        "订阅支付平台"
      ],
      "status": "confirmed"
    },
    {
      "category": "merchant_platform_owner",
      "confirmed_as": "service_offering_owner",
      "evidence_anchor": {
        "source_section": "用户审核确认: 服务供给升级为完整首版故事"
      },
      "id": "R-service-offering-owner",
      "mention": "Agent 服务供给责任方",
      "source_actors": [
        "AI 服务商",
        "平台型智能体服务"
      ],
      "status": "confirmed"
    },
    {
      "category": "merchant_platform_owner",
      "confirmed_as": "platform_relationship_owner",
      "evidence_anchor": {
        "source_section": "用户审核确认: 平台责任边界升级为完整首版故事"
      },
      "id": "R-platform-relationship-owner",
      "mention": "平台责任边界责任方",
      "source_actors": [
        "AI 服务商",
        "平台"
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
    "design_clarification_gate": [
      {
        "approval_status": "approved_by_user",
        "design_boundary": "没有材料时只能保留需求骨架和待确认项，不能由 AGI 推断现状。",
        "gate": "current_state_materials",
        "gate_strength": "hard_before_detailed_design",
        "hard_gate_ref": "current_state_material_package",
        "must_clarify": "现有订阅、扣款、账单、权益、分账、结算、出款和对账流程是否已有系统、人工流程、合同或数据样例。",
        "owner": "requirement_proposer"
      },
      {
        "approval_status": "approved_by_user",
        "design_boundary": "需求只确认规则归属、版本和计算顺序；具体表达式和异常规则进入详细设计门禁。",
        "gate": "rule_detail_materials",
        "gate_strength": "hard_before_detailed_design",
        "hard_gate_ref": "business_rule_position_table",
        "must_clarify": "平台手续费、服务方分账、尾差舍入、退款/拒付/补偿、税费或成本扣减等规则是否进入首版以及具体口径。",
        "owner": "rule_owner_and_settlement_owner"
      },
      {
        "design_boundary": "验收只要求状态可流转和可追溯；策略参数不能凭行业默认值生成。",
        "gate": "lifecycle_policy_materials",
        "gate_strength": "dependent_before_detailed_design",
        "must_clarify": "订阅状态、续期日、扣款重试次数和间隔、宽限期、催缴/挽留触发条件、权益降级或暂停策略。",
        "owner": "billing_ops_owner_and_revenue_recovery_owner"
      },
      {
        "approval_status": "approved_by_user",
        "design_boundary": "需求可确认上下文交接，详细接口契约必须等系统边界材料确认。",
        "gate": "integration_boundary_materials",
        "gate_strength": "hard_before_detailed_design",
        "hard_gate_ref": "system_boundary_contract_table",
        "must_clarify": "AI 服务、服务供给、席位、用量、权益系统与订阅支付平台之间的 API、事件、回调、幂等和失败补偿边界。",
        "owner": "platform_relationship_owner_and_agent_service_owner"
      },
      {
        "design_boundary": "验收只要求链路可追溯和可对账；账务分录、资金状态机和批次规则需要设计前材料。",
        "gate": "funds_accounting_materials",
        "gate_strength": "dependent_before_detailed_design",
        "must_clarify": "支付成功如何入账、资金何时可分账/可结算/可出款、结算批次条件、出款失败处理、对账异常口径。",
        "owner": "ledger_owner_reconciliation_owner_and_payout_owner"
      },
      {
        "design_boundary": "需求已把该域升为首版完整故事；详细设计不能假设平台主体、商户主体或责任划分。",
        "gate": "merchant_platform_responsibility_materials",
        "gate_strength": "dependent_before_detailed_design",
        "must_clarify": "AI 服务商身份、收款主体、平台账户、能力开通范围、平台与服务商责任边界及版本化协议材料。",
        "owner": "merchant_profile_owner_capability_owner_and_platform_relationship_owner"
      },
      {
        "design_boundary": "验收要求可追溯；字段级审计模型和证据保留周期需在设计门禁中确认。",
        "gate": "traceability_and_audit_materials",
        "gate_strength": "dependent_before_detailed_design",
        "must_clarify": "哪些对象必须保留版本、生效时间、操作者、来源证据、外部流水号和跨链路追溯 ID。",
        "owner": "requirement_proposer_with_domain_owners"
      }
    ],
    "detailed_design_hard_gates": [
      {
        "approval_status": "approved_by_user",
        "approved_at": "2026-06-04",
        "blocks_until_passed": "详细设计、API 契约、DDL/表结构、状态机和研发拆解。",
        "gate": "current_state_material_package",
        "hard_gate": true,
        "pass_condition": "产品明确提供可引用材料，或明确确认当前没有存量系统/人工流程并给出首版约束。",
        "reason": "没有现状材料时，AGI 只能生成需求骨架，不能判断迁移约束、兼容约束或现有职责边界。",
        "required_from": "product_owner_or_requirement_proposer",
        "required_material": "现状材料：现有订阅、扣款、账单、权益、分账、结算、出款、对账流程的流程图、系统截图、配置样例、合同口径、账单样例或明确的 greenfield 确认。"
      },
      {
        "approval_status": "approved_by_user",
        "approved_at": "2026-06-04",
        "blocks_until_passed": "详细设计中的规则模型、金额计算、批次生成、反向分账和异常处理。",
        "gate": "business_rule_position_table",
        "hard_gate": true,
        "pass_condition": "产品明确每类规则是否进入首版、由谁维护、使用什么业务口径；未进入首版的规则必须记录延期边界。",
        "reason": "验收只确认规则可配置、可追溯和计算顺序；具体金额口径不能用行业默认值补齐。",
        "required_from": "product_owner_with_rule_owner_and_settlement_owner",
        "required_material": "规则口径表：平台手续费、服务方分账、尾差舍入、退款、拒付、补偿、税费、结算条件、出款失败和对账异常的首版/非首版边界及计算口径。"
      },
      {
        "approval_status": "approved_by_user",
        "approved_at": "2026-06-04",
        "blocks_until_passed": "接口设计、事件设计、权限/权益联动、用量计费联动和端到端时序设计。",
        "gate": "system_boundary_contract_table",
        "hard_gate": true,
        "pass_condition": "产品明确每个上下文交接由哪个系统发起、哪个系统承接、失败如何恢复、哪些字段由谁负责。",
        "reason": "需求可以确认上下文关系，但系统集成契约必须由真实系统边界材料决定。",
        "required_from": "product_owner_with_platform_relationship_owner_and_agent_service_owner",
        "required_material": "系统边界表：Agent 服务供给、用量、席位、权益系统与订阅支付平台之间的 API、事件、回调、幂等键、失败补偿、责任归属和数据 owner。"
      }
    ],
    "domain_coverage_matrix": [
      {
        "acceptance_function_ids": [
          "AF-001",
          "AF-002",
          "AF-003",
          "AF-004",
          "AF-005",
          "AF-006",
          "AF-008",
          "AF-009",
          "AF-010",
          "AF-011"
        ],
        "aggregate_roots": [
          "commercial_subscription",
          "invoice",
          "price_plan",
          "billing_schedule",
          "usage_record",
          "rating_rule",
          "seat_assignment",
          "dunning_case",
          "grace_period",
          "retry_schedule"
        ],
        "contexts": [
          "commercial_subscription_context",
          "billing_invoice_context",
          "usage_rating_context",
          "revenue_recovery_context"
        ],
        "coverage_type": "primary",
        "review_note": "主域覆盖订阅关系、账单、混合计费、续期、重试和催缴。",
        "subdomain": "billing_revenue",
        "user_story_ids": [
          "US-001",
          "US-002",
          "US-003",
          "US-004",
          "US-005",
          "US-007",
          "US-008"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-001",
          "AF-021",
          "AF-022",
          "AF-023",
          "AF-024"
        ],
        "aggregate_roots": [
          "merchant",
          "platform_account",
          "capability_grant",
          "service_offering",
          "platform_relationship"
        ],
        "contexts": [
          "merchant_identity_context",
          "merchant_capability_context",
          "merchant_service_offering_context",
          "platform_responsibility_context"
        ],
        "coverage_type": "full_coverage",
        "review_note": "用户审核确认 4：商户身份、能力开通、服务供给和平台责任边界进入首版完整故事。",
        "subdomain": "merchant_platform_relationship",
        "user_story_ids": [
          "US-001",
          "US-017",
          "US-018",
          "US-019",
          "US-020"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-007",
          "AF-008",
          "AF-009",
          "AF-017"
        ],
        "aggregate_roots": [
          "payment_intent",
          "payment_attempt",
          "charge",
          "payment_method_authorization"
        ],
        "contexts": [
          "payment_intent_context",
          "payment_attempt_authorization_context",
          "payment_method_context"
        ],
        "coverage_type": "required_payment",
        "review_note": "补强后覆盖授权校验、续期扣款、失败重试、支付意图和支付尝试结果收敛。",
        "subdomain": "payment_transaction",
        "user_story_ids": [
          "US-006",
          "US-007",
          "US-012"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-018",
          "AF-016"
        ],
        "aggregate_roots": [
          "ledger_entry",
          "fund_state"
        ],
        "contexts": [
          "balance_ledger_context",
          "fund_state_context"
        ],
        "coverage_type": "required_payment",
        "review_note": "补强后覆盖支付成功后的账本分录和资金状态；余额、reserve、limit 暂不展开。",
        "subdomain": "account_balance",
        "user_story_ids": [
          "US-013"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-019",
          "AF-016"
        ],
        "aggregate_roots": [
          "reconciliation_record",
          "reconciliation_exception"
        ],
        "contexts": [
          "reconciliation_context"
        ],
        "coverage_type": "required_payment",
        "review_note": "补强后覆盖账单、支付、账本、分账、结算和出款链路对账；财务报表和关账暂不展开。",
        "subdomain": "financial_operations",
        "user_story_ids": [
          "US-014"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-007"
        ],
        "aggregate_roots": [
          "payment_mandate",
          "authorization_consent",
          "consent_record"
        ],
        "contexts": [
          "mandate_authorization_context"
        ],
        "coverage_type": "required_payment",
        "review_note": "覆盖周期扣款授权证据；KYB、AML、交易风控不在当前首版故事中展开。",
        "subdomain": "risk_compliance",
        "user_story_ids": [
          "US-006"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-013",
          "AF-014",
          "AF-015",
          "AF-020",
          "AF-016"
        ],
        "aggregate_roots": [
          "split_rule",
          "allocation_result",
          "platform_fee",
          "settlement_batch",
          "payout"
        ],
        "contexts": [
          "split_allocation_context",
          "settlement_batch_context",
          "payout_context"
        ],
        "coverage_type": "conditional_payment_in_scope",
        "review_note": "用户确认首版包含分账、结算和出款；补强后覆盖分账规则、平台费用、结算批次和出款。",
        "subdomain": "funds_movement_settlement",
        "user_story_ids": [
          "US-010",
          "US-011",
          "US-015",
          "US-016"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-010",
          "AF-011",
          "AF-012",
          "AF-016"
        ],
        "aggregate_roots": [
          "agent_entitlement"
        ],
        "contexts": [
          "agent_entitlement_context"
        ],
        "coverage_type": "adjacent_agent_service",
        "review_note": "覆盖订阅和付款状态驱动 Agent 权益开通、保持、降级或暂停。",
        "subdomain": "agent_entitlement",
        "user_story_ids": [
          "US-009"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-004",
          "AF-005"
        ],
        "aggregate_roots": [
          "candidate:usage_event"
        ],
        "contexts": [
          "agent_usage_metering_context"
        ],
        "coverage_type": "adjacent_agent_service_conditional",
        "review_note": "覆盖按量计费用量汇总；usage_event 仍是 taxonomy 候选术语，当前作为邻接证据保留。",
        "subdomain": "agent_usage_metering",
        "user_story_ids": [
          "US-004"
        ]
      },
      {
        "acceptance_function_ids": [
          "AF-004",
          "AF-006"
        ],
        "aggregate_roots": [
          "seat_assignment"
        ],
        "contexts": [
          "agent_workspace_seat_context"
        ],
        "coverage_type": "adjacent_agent_service_conditional",
        "review_note": "覆盖席位数量和席位变更对账单影响。",
        "subdomain": "agent_workspace_seat",
        "user_story_ids": [
          "US-005"
        ]
      }
    ],
    "domain_coverage_review": [
      {
        "review_focus": "merchant_platform_relationship first-release depth",
        "status": "confirmed",
        "summary": "User review confirmed merchant platform relationship full-story scope."
      },
      {
        "review_focus": "US-010 US-015 US-016 split rule relationship",
        "status": "clarified",
        "summary": "User review asked to clarify the agreed rules and relationship among split settlement, split rule, and platform fee stories."
      },
      {
        "review_focus": "detail-design-clarification-gate",
        "status": "accepted_as_gate",
        "summary": "User accepted the requirement skeleton and clarified that missing current-state materials must become proposer clarification gates before detailed design, not AGI-inferred design facts."
      },
      {
        "review_focus": "product-hard-design-gates",
        "status": "accepted_as_hard_gate",
        "summary": "User asked whether the three missing material packages can become hard gates; case now treats them as product clarification gates that block detailed design but not the already reviewable requirement skeleton."
      },
      {
        "review_focus": "product-hard-design-gates-final-review",
        "status": "approved",
        "summary": "User confirmed the three hard design gates are acceptable; case can move from user review to waiting for product-provided gate materials."
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
        "question": "硬门禁 1：产品是否能提供现状材料包，或明确确认当前没有存量系统/人工流程并给出首版约束？"
      },
      {
        "question": "硬门禁 2：产品是否能提供规则口径表，明确平台手续费、分账、尾差、退款/拒付/补偿、税费、结算和异常口径的首版边界？"
      },
      {
        "question": "硬门禁 3：产品是否能提供系统边界表，明确 Agent 服务、用量、席位、权益系统和订阅支付平台之间的 API/事件/回调/责任边界？"
      },
      {
        "question": "首版平台手续费是否只支持按比例和固定金额，还是需要阶梯费率？"
      },
      {
        "question": "尾差和舍入金额默认归平台、归最大服务方，还是要求显式配置？"
      },
      {
        "question": "退款、拒付、补偿是否进入首版反向分账规则，还是作为后续规则扩展？"
      }
    ],
    "rule_clarification": [
      {
        "summary": "US-015 owns service-provider split rule configuration; US-016 owns platform fee rule configuration; US-010 consumes the effective versions of both rules to produce allocation results and settlement batches.",
        "topic": "rule_ownership"
      },
      {
        "summary": "首版规则集合包括适用服务供给、收款主体、参与分配服务方、费用基数、平台手续费、服务方分配比例或固定金额、生效时间、规则版本、结算条件和追溯引用。",
        "topic": "first_release_rule_set"
      },
      {
        "summary": "分账计算顺序为：确认已收款账单费用基数 -> 使用平台手续费规则计算平台费用 -> 使用服务方分账规则分配剩余可分配金额 -> 生成分账结果 -> 满足结算条件后汇入结算批次。",
        "topic": "calculation_order"
      },
      {
        "summary": "需求阶段只确认业务规则关系和追溯字段；具体费率表达式、舍入尾差策略、税费处理、退款/拒付后的反向分账属于后续设计或扩展规则。",
        "topic": "traceability_boundary"
      }
    ],
    "scope_decisions": [
      {
        "decision": "first_release_split_settlement",
        "evidence": "用户复审确认 2: 确认",
        "value": "in_scope"
      },
      {
        "decision": "target_customer",
        "evidence": "用户复审确认 1: 没错",
        "value": "AI 服务商"
      },
      {
        "decision": "commercial_model",
        "evidence": "用户确认 3: 混合",
        "value": "混合计费"
      },
      {
        "decision": "mandate_and_recurring_retry",
        "evidence": "用户复审确认 3: 确认",
        "value": "in_scope"
      },
      {
        "decision": "merchant_platform_relationship_full_stories",
        "evidence": "用户复审确认 4: 确认",
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
      },
      {
        "answers": [
          {
            "answer": "没错",
            "question": "US-001 首版是否只做 AI 服务商接入并配置订阅支付关系？"
          },
          {
            "answer": "确认",
            "question": "首版是否包含分账、结算批次、出款、平台手续费？"
          },
          {
            "answer": "确认",
            "question": "周期扣款授权/委托扣款是否进入首版？"
          },
          {
            "answer": "确认",
            "question": "商户身份、能力开通、服务供给、平台责任边界是否升级为完整故事？"
          }
        ],
        "confirmed_at": "2026-06-04",
        "source": "chat_user_review"
      },
      {
        "answers": [
          {
            "answer": "可以",
            "question": "US-010/US-015/US-016 规则关系是否可接受？"
          },
          {
            "answer": "确认，应泛化到规则以外的详细设计前澄清点。",
            "question": "缺少现状材料时是否应通过门禁要求需求提出方澄清，而不是由 AGI 推断设计？"
          }
        ],
        "confirmed_at": "2026-06-04",
        "source": "chat_user_design_gate_confirmation_2026_06_04"
      },
      {
        "answers": [
          {
            "answer": "可以；作为详细设计前硬门禁，由产品/需求提出方澄清。",
            "question": "现状材料、规则口径表、系统边界表是否可以变成硬门禁要求产品澄清？"
          }
        ],
        "confirmed_at": "2026-06-04",
        "source": "chat_user_hard_gate_confirmation_2026_06_04"
      },
      {
        "answers": [
          {
            "answer": "认可，没问题。",
            "question": "三项详细设计硬门禁是否认可，可以作为后续要求产品澄清的规则？"
          }
        ],
        "confirmed_at": "2026-06-04",
        "source": "chat_user_hard_gate_final_approval_2026_06_04"
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
      "aggregate_refs": [
        "billing_schedule",
        "capability_grant",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "merchant",
        "platform_relationship",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "service_offering",
        "usage_record"
      ],
      "benefit": "不用自建银行通道和订阅生命周期能力，就能商业化提供持续 Agent 服务。",
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "merchant_capability_context",
        "merchant_identity_context",
        "merchant_service_offering_context",
        "platform_responsibility_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "billing_revenue",
        "merchant_platform_relationship"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "AI 服务商可以获得完整订阅生命周期能力，而不是只完成一次性扣款。",
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "billing_revenue"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "Agent 服务可以按真实商业模型收费，而不是被限制在单一固定订阅。",
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "billing_revenue"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "candidate:usage_event",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "按量收费可以基于可追溯的用量事实，而不是人工估算或离线结算。",
      "context_refs": [
        "agent_usage_metering_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "agent_usage_metering",
        "billing_revenue"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "团队型或多用户 Agent 服务可以按席位扩缩容并形成正确应收。",
      "context_refs": [
        "agent_workspace_seat_context",
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "agent_workspace_seat",
        "billing_revenue"
      ],
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
      "aggregate_refs": [
        "authorization_consent",
        "charge",
        "consent_record",
        "payment_attempt",
        "payment_intent",
        "payment_mandate",
        "payment_method_authorization"
      ],
      "benefit": "自动续费和重试扣款具备合规依据，降低扣款争议和失败风险。",
      "context_refs": [
        "mandate_authorization_context",
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context"
      ],
      "domain_refs": [
        "payment_transaction",
        "risk_compliance"
      ],
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
        "AF-016",
        "AF-017"
      ],
      "aggregate_refs": [
        "billing_schedule",
        "charge",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "payment_attempt",
        "payment_intent",
        "payment_method_authorization",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "AI 服务商可以提高续费成功率，并减少人工催收和重复对接成本。",
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "billing_revenue",
        "payment_transaction"
      ],
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
      "aggregate_refs": [
        "billing_schedule",
        "commercial_subscription",
        "dunning_case",
        "grace_period",
        "invoice",
        "price_plan",
        "rating_rule",
        "retry_schedule",
        "seat_assignment",
        "usage_record"
      ],
      "benefit": "在扣款失败后仍能恢复收入并提升月续费率。",
      "context_refs": [
        "billing_invoice_context",
        "commercial_subscription_context",
        "revenue_recovery_context",
        "usage_rating_context"
      ],
      "domain_refs": [
        "billing_revenue"
      ],
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
      "aggregate_refs": [
        "agent_entitlement"
      ],
      "benefit": "商业订阅状态可以准确驱动消费者可用的 Agent 服务访问权限。",
      "context_refs": [
        "agent_entitlement_context"
      ],
      "domain_refs": [
        "agent_entitlement"
      ],
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
        "AF-016",
        "AF-019",
        "AF-020"
      ],
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "benefit": "分账结果可以追溯到明确的规则版本、费用基数和计算顺序，降低多服务方结算争议。",
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "domain_refs": [
        "funds_movement_settlement"
      ],
      "evidence_anchor": {
        "source_section": "用户确认 1: 包含"
      },
      "id": "US-010",
      "role_ref": "R-split-settlement-owner",
      "source_functions": [
        "原始痛点: 分账结算复杂",
        "用户确认 1: 包含"
      ],
      "want": "作为分账结算责任方，我希望在账单收款成功后，使用当前生效的分账规则版本和平台手续费规则版本计算收入分账并形成结算批次。"
    },
    {
      "acceptance_function_ids": [
        "AF-014",
        "AF-015",
        "AF-016",
        "AF-019"
      ],
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "benefit": "服务方可以按可追溯的结算结果收到资金，平台减少人工付款和对账负担。",
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "domain_refs": [
        "funds_movement_settlement"
      ],
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
    },
    {
      "acceptance_function_ids": [
        "AF-016",
        "AF-017",
        "AF-018"
      ],
      "aggregate_refs": [
        "charge",
        "payment_attempt",
        "payment_intent",
        "payment_method_authorization"
      ],
      "benefit": "订阅续费不会停留在账单视角，支付交易状态可以明确驱动后续权益、入账和催缴。",
      "context_refs": [
        "payment_attempt_authorization_context",
        "payment_intent_context",
        "payment_method_context"
      ],
      "domain_refs": [
        "payment_transaction"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: payment_transaction"
      },
      "id": "US-012",
      "role_ref": "R-payment-ops-owner",
      "source_functions": [
        "领域覆盖补强: payment_transaction",
        "context: payment_intent_context / payment_attempt_authorization_context"
      ],
      "want": "作为支付交易处理责任方，我希望订阅账单扣款能够生成支付意图和支付尝试，并收敛出唯一支付结果。"
    },
    {
      "acceptance_function_ids": [
        "AF-016",
        "AF-018",
        "AF-019"
      ],
      "aggregate_refs": [
        "fund_state",
        "ledger_entry"
      ],
      "benefit": "后续分账、结算、出款和对账可以基于真实资金事实，而不是只依赖支付成功事件。",
      "context_refs": [
        "balance_ledger_context",
        "fund_state_context"
      ],
      "domain_refs": [
        "account_balance"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: account_balance"
      },
      "id": "US-013",
      "role_ref": "R-ledger-owner",
      "source_functions": [
        "领域覆盖补强: account_balance",
        "context: balance_ledger_context / fund_state_context"
      ],
      "want": "作为账本入账责任方，我希望支付成功后生成账本分录并更新资金状态。"
    },
    {
      "acceptance_function_ids": [
        "AF-016",
        "AF-019"
      ],
      "aggregate_refs": [
        "reconciliation_exception",
        "reconciliation_record"
      ],
      "benefit": "财务运营可以发现链路不一致，保障收入、资金和结算证据一致。",
      "context_refs": [
        "reconciliation_context"
      ],
      "domain_refs": [
        "financial_operations"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: financial_operations"
      },
      "id": "US-014",
      "role_ref": "R-reconciliation-owner",
      "source_functions": [
        "领域覆盖补强: financial_operations",
        "context: reconciliation_context"
      ],
      "want": "作为对账责任方，我希望账单、支付、账本、分账、结算和出款记录可以被核对并标记异常。"
    },
    {
      "acceptance_function_ids": [
        "AF-016",
        "AF-020"
      ],
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "benefit": "平台型 Agent 服务的服务方收入分配可以按已约定且可版本化的规则执行，而不是在结算时临时人工拆分。",
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "domain_refs": [
        "funds_movement_settlement"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: split_allocation_context"
      },
      "id": "US-015",
      "role_ref": "R-split-rule-owner",
      "source_functions": [
        "领域覆盖补强: funds_movement_settlement",
        "用户确认 1: 包含"
      ],
      "want": "作为分账规则责任方，我希望配置服务方分账规则，包括适用服务供给、收款主体、参与分配的服务方、分配比例或固定金额、生效时间和规则版本。"
    },
    {
      "acceptance_function_ids": [
        "AF-016",
        "AF-020"
      ],
      "aggregate_refs": [
        "allocation_result",
        "payout",
        "platform_fee",
        "settlement_batch",
        "split_rule"
      ],
      "benefit": "平台收入先按明确规则从服务收入中计算出来，再进入服务方分配和结算，避免平台费用与服务方分账口径混淆。",
      "context_refs": [
        "payout_context",
        "settlement_batch_context",
        "split_allocation_context"
      ],
      "domain_refs": [
        "funds_movement_settlement"
      ],
      "evidence_anchor": {
        "source_section": "domain coverage: platform_fee"
      },
      "id": "US-016",
      "role_ref": "R-platform-fee-owner",
      "source_functions": [
        "领域覆盖补强: funds_movement_settlement",
        "原始痛点: 分账结算复杂"
      ],
      "want": "作为平台手续费责任方，我希望配置平台手续费规则，包括计费基数、费率或固定金额、优先扣除顺序、生效时间和规则版本。"
    },
    {
      "acceptance_function_ids": [
        "AF-021",
        "AF-024"
      ],
      "aggregate_refs": [
        "merchant",
        "platform_account",
        "platform_relationship"
      ],
      "benefit": "订阅支付接入前可以明确谁提供服务、谁收款、谁承担平台关系责任。",
      "context_refs": [
        "merchant_identity_context",
        "platform_responsibility_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship"
      ],
      "evidence_anchor": {
        "source_section": "用户审核确认 4: 商户身份升级为完整首版故事"
      },
      "id": "US-017",
      "role_ref": "R-merchant-profile-owner",
      "want": "作为 AI 服务商身份责任方，我希望记录 AI 服务商的平台账户、商户身份和收款主体信息。"
    },
    {
      "acceptance_function_ids": [
        "AF-022",
        "AF-024"
      ],
      "aggregate_refs": [
        "capability_grant",
        "platform_relationship"
      ],
      "benefit": "服务方不需要自行对接银行通道或拆分实现订阅支付基础能力。",
      "context_refs": [
        "merchant_capability_context",
        "platform_responsibility_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship"
      ],
      "evidence_anchor": {
        "source_section": "用户审核确认 4: 能力开通升级为完整首版故事"
      },
      "id": "US-018",
      "role_ref": "R-capability-owner",
      "want": "作为订阅支付能力开通责任方，我希望为 AI 服务商开通订阅创建、周期扣款、混合计费和分账结算所需能力。"
    },
    {
      "acceptance_function_ids": [
        "AF-023",
        "AF-024"
      ],
      "aggregate_refs": [
        "service_offering",
        "platform_relationship"
      ],
      "benefit": "消费者订阅的是明确的 Agent 服务和方案，而不是孤立的支付配置。",
      "context_refs": [
        "merchant_service_offering_context",
        "platform_responsibility_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship"
      ],
      "evidence_anchor": {
        "source_section": "用户审核确认 4: 服务供给升级为完整首版故事"
      },
      "id": "US-019",
      "role_ref": "R-service-offering-owner",
      "want": "作为 Agent 服务供给责任方，我希望把 Agent 服务、订阅方案和可售能力发布为可配置的服务供给。"
    },
    {
      "acceptance_function_ids": [
        "AF-024"
      ],
      "aggregate_refs": [
        "platform_relationship",
        "platform_account"
      ],
      "benefit": "平台型 Agent 服务可以在多服务方分账结算时保留清晰责任和追溯依据。",
      "context_refs": [
        "platform_responsibility_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship"
      ],
      "evidence_anchor": {
        "source_section": "用户审核确认 4: 平台责任边界升级为完整首版故事"
      },
      "id": "US-020",
      "role_ref": "R-platform-relationship-owner",
      "want": "作为平台责任边界责任方，我希望明确平台与 AI 服务商在订阅、收款、权益、分账和结算中的责任边界。"
    }
  ]
}
```
<!-- requirements-case-data:end -->
