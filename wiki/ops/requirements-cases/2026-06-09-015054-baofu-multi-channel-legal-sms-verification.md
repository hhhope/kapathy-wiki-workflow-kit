---
layer: ops
domain: unclassified
classification_needed: true
ops_area: workflow-trace
canonical_object: requirements-case-file
artifact_type: requirements-case
status: blocked
case_slug: baofu-multi-channel-legal-sms-verification
created_at: 2026-06-09
---

# requirements-case

## Case Source
- Generated at: 2026-06-09T01:50:54.065976+00:00
- Scan root: `.`
- provenance: user provided requirement text in chat on 2026-06-09 and requested `$report-wiki-portfolio:req-agent`
- requirement_like: True
- source_path: /tmp/baofu-legal-sms-verification-requirement.txt
- source_type: chat_requirement
- title: 多渠道收款商户法人短信认证

## Intent
- draft_requested: False
- intent: new_requirement_intake
- requested_action: 走我们的需求
- routed_worker: req-intake

## Domain
- Status: confirmed
- Confirmed: risk_compliance
### Candidates
- risk_compliance: primary requirement is legal representative intent verification for compliance evidence before product opening continues
- merchant_platform_relationship: product opening progress, onboarding gate, and merchant capability lifecycle are in scope
- account_balance: rejected as primary domain; electronic account complaint is risk background, not the requested account/balance lifecycle design

## Domain Coverage
- merchant_platform_relationship: coverage_type=primary; contexts=merchant_onboarding_context, merchant_capability_context; aggregates=onboarding_application, capability_grant, merchant; stories=US-001, US-002, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-012; acceptance=AF-001, AF-002, AF-006, AF-007, AF-008, AF-009, AF-010, AF-011, AF-013, AF-014, AF-015, AF-016, AF-017, AF-019; note=merchant opening gate, capability progress, stock merchant targeting, resend operations, and H5 identity-facing merchant context are first-release surfaces.
- risk_compliance: coverage_type=primary; contexts=mandate_authorization_context, compliance_review_context, risk_decision_context; aggregates=authorization_consent, consent_record, compliance_review, risk_rule, risk_decision; stories=US-001, US-002, US-003, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-011, US-012; acceptance=AF-001, AF-002, AF-003, AF-004, AF-005, AF-006, AF-007, AF-008, AF-009, AF-010, AF-011, AF-012, AF-013, AF-014, AF-015, AF-016, AF-017, AF-018, AF-019, AF-020; note=legal representative consent verification, retry/failure behavior, compliance evidence, URL/token safety, identity binding, and skip-policy decisions are primary compliance coverage.

## Roles
- R-onboarding-owner: 新会员/老前置进件开通流程 owner; confirmed_as=onboarding_owner; status=confirmed; category=fact_owner
- R-capability-owner: 多渠道收款产品开通进度 owner; confirmed_as=capability_owner; status=confirmed; category=fact_owner
- R-legal-representative: 商户法人; confirmed_as=mandate_owner; status=confirmed; category=business_actor
- R-compliance-owner: 合规; confirmed_as=compliance_owner; status=confirmed; category=fact_owner
- R-risk-owner: 短验跳过规则 owner; confirmed_as=risk_owner; status=confirmed; category=fact_owner

## User Stories
- US-001: role_ref=R-onboarding-owner; 在新会员 BM/API 入口开通多渠道收款且命中范围时，提交 118 流程前进入等待法人短验，并向法人发送含 H5 链接的短验通知短信; benefit=法人完成真实意愿核验后才继续产品开通，降低电子户开通不知情风险。; acceptance=AF-001, AF-008, AF-009, AF-013
- US-002: role_ref=R-onboarding-owner; 在老前置进件机审完成后、发起 83 流程前进入等待法人短验，并向法人发送含 H5 链接的短验通知短信; benefit=老前置链路也能在产品开通前取得法人短信认证。; acceptance=AF-002, AF-008, AF-010, AF-013
- US-003: role_ref=R-legal-representative; 通过短信链接进入 H5 页面，手动触发验证码短信并回填验证码; benefit=法人可以完成特约商户开立意愿核验，验证成功后页面进入完成状态且流程可继续。; acceptance=AF-003, AF-004, AF-005, AF-012, AF-013
- US-004: role_ref=R-compliance-owner; 按合规提供的存量商户列表一次性批量发送法人短验通知短信，并由研发配合查看短验进展; benefit=存量多渠道收款商户的法人意愿核验可以被核查和追踪，不新增存量进度功能。; acceptance=AF-011, AF-013
- US-005: role_ref=R-onboarding-owner; 对等待验证状态的商户在宝付 AD 或融证通 OMS 重新触发法人短验通知短信并重置验证码次数; benefit=验证码过期或法人未完成时，业务侧可以重新发起核验而不是让流程永久卡死。; acceptance=AF-006, AF-007, AF-013
- US-006: role_ref=R-capability-owner; 在新会员、宝付 AD、新 BM 和老前置 OMS 中展示法人短验等待、已短验、未短验或无需短验进展; benefit=产品开通进度能解释当前卡点并支持运营核查。; acceptance=AF-009, AF-010
- US-007: role_ref=R-risk-owner; 按代理商 Apollo 配置跳过法人短验，同时保证直客必须短验、代理商本身无需短验; benefit=短验范围可以按业务风险策略落地，并避免误阻断代理商自身或配置允许的代客。; acceptance=AF-008
- US-008: role_ref=R-risk-owner; 不命中首版范围的商户不进入法人短验，也不阻断 118 / 83; benefit=避免把合规短验扩大到范围外商户，造成误阻断。; acceptance=AF-014
- US-009: role_ref=R-onboarding-owner; 非等待法人短验状态不能触发宝付 AD / 融证通 OMS 法人短验重发; benefit=避免已完成、无需短验或范围外商户被重复发送短信。; acceptance=AF-015
- US-010: role_ref=R-capability-owner; 短验状态在 H5、AD、新 BM 和 OMS 的展示与阻断口径保持一致; benefit=评审和运营可以判断当前到底是等待、已短验、无需短验还是 H5 超限待宝付重发。; acceptance=AF-009, AF-010, AF-016
- US-011: role_ref=R-compliance-owner; 确认法人短信链接、验证码、H5 访问和证据记录满足监管、个人信息保护和安全要求; benefit=短验结果能作为合规证据，而不是产生新的钓鱼、冒用或个人信息泄露风险。; acceptance=AF-017, AF-018, AF-019, AF-020
- US-012: role_ref=R-legal-representative; 通过简短可信短信链接进入 H5，识别被核验商户和业务，并通过足够核身步骤确认意愿; benefit=法人能识别宝付真实核验流程，且不会因链接过长、信息不清或核身不足造成误操作。; acceptance=AF-017, AF-018, AF-019, AF-020

## Acceptance Functions
- AF-001: new_member_waits_for_legal_sms_before_118; stories=US-001; coverage=state_change, handoff, evidence; 系统发送含 H5 链接的短验通知短信给法人，产品开通停留在等待法人短验，法人验证成功前不提交后续 118 流程。
- AF-002: legacy_front_waits_for_legal_sms_before_83; stories=US-002; coverage=state_change, handoff, evidence; 系统发送含 H5 链接的短验通知短信给法人，流程停留在等待法人短验，法人验证成功前不发起后续 83 流程。
- AF-003: legal_representative_triggers_and_submits_code; stories=US-003; coverage=state_change, evidence; 验证码正确时系统记录法人短验成功，页面展示已完成法人信息核验，并允许对应产品开通流程继续。
- AF-004: invalid_or_expired_code_prompts_retry; stories=US-003; coverage=failure_path, state_change; H5 页面提醒“验证码有误或验证码超时，请重新触发”，并允许在未超过次数上限时重新触发验证码。
- AF-005: h5_retry_limit_requires_baofoo_resend; stories=US-003; coverage=failure_path, state_change; H5 页面提示“请联系宝付重新发送短信”，不再允许页面内重发验证码。
- AF-006: baofoo_ad_resends_legal_sms_for_new_member; stories=US-005; coverage=state_change, handoff; 系统重发含链接的短验通知短信，并重置验证码次数。
- AF-007: oms_resends_legal_sms_for_legacy_front; stories=US-005; coverage=state_change, handoff; 系统重发含链接的短验通知短信，并重置验证码次数。
- AF-008: agent_skip_policy_applies_only_to_configured_agent_chain; stories=US-001, US-002, US-007; coverage=state_change, handoff, evidence; 代理商本身无需法人短验；配置权限代理商直接或间接拓展的代客可跳过法人短验；直客必须进行法人短验。
- AF-009: new_member_progress_shows_waiting_legal_sms; stories=US-001, US-006; coverage=evidence, state_change; 审批步骤展示“等待法人短验”阶段。
- AF-010: legacy_front_progress_shows_legal_sms_status; stories=US-002, US-006; coverage=evidence, state_change; 页面展示“是否法人短验”字段，枚举为“已短验、未短验、无需短验”。
- AF-011: stock_merchant_batch_sms_requires_compliance_list; stories=US-004; coverage=state_change, handoff, evidence; 按合规提供的存量商户列表一次性发送短验通知短信；不新增存量进度功能，由研发配合查看短验进展。
- AF-012: completed_link_is_read_only; stories=US-003; coverage=state_change, evidence; 页面不能填写验证码或触发短信，并展示“已完成法人信息核验”。
- AF-013: sms_templates_match_required_content; stories=US-001, US-002, US-003, US-004, US-005; coverage=evidence; 短验通知短信包含监管身份识别、特约商户真实意愿确认、H5 链接、客服热线和非本人说明；验证码短信包含特约商户开立意愿核验、验证码和 5 分钟有效期。
- AF-014: out_of_scope_merchants_do_not_trigger_legal_sms; stories=US-008; coverage=state_change, handoff; 不属于首版范围的商户不发送法人短验通知、不展示等待法人短验、不阻断 118 / 83。
- AF-015: non_waiting_merchants_cannot_resend_legal_sms; stories=US-009; coverage=failure_path, state_change; 商户不处于等待法人短验状态时，AD / OMS 不允许触发法人短验重发，且不重置验证码次数。
- AF-016: legal_sms_status_mapping_is_consistent; stories=US-006, US-010; coverage=evidence, state_change; H5、AD、新 BM 和 OMS 对等待、已短验、无需短验、H5 超限待宝付重发的展示和阻断口径一致。
- AF-017: sms_url_length_and_payload_are_bounded; stories=US-011, US-012; coverage=evidence, failure_path; 短验通知短信有明确模板长度预算；H5 链接使用可信域名下短路径/短 token；不得把明文商户、法人或业务敏感参数放进 URL；链接超长时有降级或拒发处理。
- AF-018: h5_link_token_is_secure; stories=US-011, US-012; coverage=evidence, failure_path; H5 链接使用 HTTPS、可信域名和不可枚举 token；token 有有效期、状态、失效机制和访问频控；服务端不依赖客户端隐藏字段；日志、Referer 和页面跳转不泄露 token 或敏感信息。
- AF-019: legal_representative_identity_binding_is_verified; stories=US-011, US-012; coverage=state_change, evidence; 系统不能仅凭短信链接点击和验证码回填判断点击者就是法人；必须按合规确认的手机号来源、法人身份绑定、二次核身或人工兜底规则完成核身。
- AF-020: compliance_evidence_and_personal_information_controls_exist; stories=US-011, US-012; coverage=evidence; 系统记录核验对象、页面文案版本、短信模板版本、发送/重发记录、核身方式、验证码结果、意愿确认动作、时间、IP/设备、操作人和失败原因，并明确个人信息最小必要采集、脱敏展示、访问权限、留存期限和导出边界。

## Soft Evidence
### Api
- "Design evidence only: SMS sending channels, H5 verification endpoint, AD resend action, OMS resend action, and progress-query surfaces are implied but contracts are not provided."
### Business Rules
- "Scope: multi-channel collection business with business attribute 抖音平台-商品购销、本地生活-商品购销、掌财狸."
- "New member path waits before 118; legacy front path waits before 83."
- "H5 code is triggered manually from the link; code SMS is valid for 5 minutes."
- "Waiting for legal representative SMS verification is an onboarding process stage with no expiry; only the SMS verification code expires."
- "H5 trigger attempts over 3 without success require Baofoo-side resend."
- "Baofoo AD and OMS resend reset verification-code attempts only for waiting-verification merchants."
- "Agent itself needs no verification; configured first-level agent direct clients and second-level agent clients may skip; direct clients must verify."
- "SMS notification links must be short enough for the message template budget and must not carry plaintext merchant, legal representative, phone, certificate, or business-sensitive parameters."
- "SMS OTP proves phone possession or reachability only; legal representative identity binding and intent confirmation require compliance-confirmed identity evidence or compensating controls."
- "Consent and verification evidence must be retained with least-necessary personal information and controlled access."
### Detailed Design Hard Gates
- {"blocks_until_passed": "Detailed design, API contracts, state machines, and engineering breakdown.", "gate": "current_state_material_package", "hard_gate": true, "material_status": "missing", "pass_condition": "Product provides referenceable current-state flows/screens/contracts or explicitly waives each current-state dependency.", "required_from": "product_owner_or_requirement_proposer", "required_material": "For detailed design: current 118/83 entry points, existing new-member and old-front progress/status fields, current AD/OMS operation locations, SMS channel template/sending constraints, and the H5 page sample or confirmed no-sample boundary."}
- {"blocks_until_passed": "Rule model, status machine, retry/reset behavior, skip-policy implementation, and acceptance finalization.", "gate": "business_rule_position_table", "hard_gate": true, "material_status": "missing", "pass_condition": "Product confirms first-release rules, deferred rules, owners, and exact rule parameters or explicitly waives them.", "required_from": "product_owner_with_compliance_owner_and_onboarding_owner", "required_material": "For detailed design: exact scope predicates, skip-policy matching order, waiting status enum, code validity, H5 trigger limit, Baofoo-side resend reset semantics, stock one-time handling, and progress enum mapping."}
- {"blocks_until_passed": "API design, event/callback design, table/schema design, and integration breakdown.", "gate": "system_boundary_contract_table", "hard_gate": true, "material_status": "missing", "pass_condition": "Product identifies initiator, fact owner, API/event/callback boundary, idempotency/retry behavior, and failure recovery for each handoff.", "required_from": "product_owner_with_member_group_account_group_compliance_and_sms_channel_owner", "required_material": "For detailed design: owner and handoff table for new member, old front, AD, OMS, H5, SMS channel, Apollo config, 118/83 workflow continuation, and one-time stock batch progress lookup."}
### Exception Scenarios
- "验证码有误或验证码超时 prompts retry."
- "超过 3 次仍未验证成功 blocks H5 resend and asks legal representative to contact Baofoo."
- "Stock merchant handling is one-time: no new progress-view function; engineering only cooperates with progress lookup."
### Test Plan
- "AF-001 through AF-016 provide observable acceptance functions and story mappings."

## Readiness / Next Action
- Status: blocked
- Next action: supplement_sms_url_security_identity_and_compliance_facts
- Reason: Human review found demand-fact gaps around regulation, SMS URL length, link/token security, H5 identity binding, and compliance evidence. Re-run requirements checker and human review after synchronization.
### Blockers
- flowchart-missing: 流程图待补充，当前只能按文字触发点记录流程阻断与继续条件。
- h5-attachment-missing: 页面样例附件未随本次聊天提供，H5 细节只能按文字规则记录。
- legal-compliance-position-missing: 法规依据、监管口径、个人信息处理依据、证据留存期限和合规 owner 确认缺失。
- sms-url-constraint-missing: 短信模板长度预算、可信域名、短 token/短链方案、超长 URL 降级策略缺失。
- link-token-security-missing: token 有效期、单次/多次访问语义、重发后旧 token 处理、频控、日志脱敏和 Referer 防泄露规则缺失。
- identity-binding-missing: 法人手机号来源、身份绑定依据、二次核身字段和人工兜底规则缺失。

## Evidence Attachments
### Analysis
- `scripts/build_requirements_analysis_agent.py output rejected account_balance as primary-domain false positive`
### Human_Review
- `wiki/ops/requirements-cases/2026-06-09-baofu-legal-sms-human-review.md`
### Source
- `/tmp/baofu-legal-sms-verification-requirement.txt`
### Taxonomy
- `requirements/config/requirements-taxonomy.yaml`

## Proof Boundary
- This case records requirements intake and readiness evidence only.
- Analyzer output misclassified the case as account_balance because of the electronic account complaint; this case keeps account_balance as rejected primary-domain evidence.
- Electronic account is background risk evidence; first-pass requirement scope is legal representative SMS verification before multi-channel collection product opening continues.
- Human review on 2026-06-10 found that regulation, SMS URL length, H5 link security, identity binding, and compliance evidence are demand facts, not optional design polish.
- Detailed design, API contracts, DDL/schema, state machine, and engineering breakdown remain blocked until the detailed_design_hard_gates are provided or explicitly waived.
- No OpenSpec draft or implementation work has been created.

## Machine Case Data
<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [
    {
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record",
        "capability_grant"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context",
        "merchant_capability_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff",
        "evidence"
      ],
      "given": "商户通过新会员 BM/API 入口开通多渠道收款，业务属性属于抖音平台-商品购销、本地生活-商品购销或掌财狸，且未命中跳过规则",
      "id": "AF-001",
      "name": "new_member_waits_for_legal_sms_before_118",
      "source_acceptance": "场景一",
      "then": "系统发送含 H5 链接的短验通知短信给法人，产品开通停留在等待法人短验，法人验证成功前不提交后续 118 流程。",
      "user_story_ids": [
        "US-001"
      ],
      "when": "系统准备提交 118 流程"
    },
    {
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record",
        "capability_grant"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context",
        "merchant_capability_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff",
        "evidence"
      ],
      "given": "商户通过老前置进件且多渠道收款业务命中范围，未命中跳过规则",
      "id": "AF-002",
      "name": "legacy_front_waits_for_legal_sms_before_83",
      "source_acceptance": "场景二",
      "then": "系统发送含 H5 链接的短验通知短信给法人，流程停留在等待法人短验，法人验证成功前不发起后续 83 流程。",
      "user_story_ids": [
        "US-002"
      ],
      "when": "前置进件机审完成且系统准备发起 83 流程"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "state_change",
        "evidence"
      ],
      "given": "商户未完成法人短验且法人打开短信链接",
      "id": "AF-003",
      "name": "legal_representative_triggers_and_submits_code",
      "source_acceptance": "短验回填链接、验证码短信内容",
      "then": "验证码正确时系统记录法人短验成功，页面展示已完成法人信息核验，并允许对应产品开通流程继续。",
      "user_story_ids": [
        "US-003"
      ],
      "when": "法人在 H5 页面点击触发验证码并回填 5 分钟内有效的验证码"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
      "given": "法人已触发验证码短信",
      "id": "AF-004",
      "name": "invalid_or_expired_code_prompts_retry",
      "source_acceptance": "短验回填链接",
      "then": "H5 页面提醒“验证码有误或验证码超时，请重新触发”，并允许在未超过次数上限时重新触发验证码。",
      "user_story_ids": [
        "US-003"
      ],
      "when": "法人提交的验证码有误或超过有效期"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
      "given": "商户法人在同一短验链接中触发验证码超过 3 次仍未验证成功",
      "id": "AF-005",
      "name": "h5_retry_limit_requires_baofoo_resend",
      "source_acceptance": "短验回填链接",
      "then": "H5 页面提示“请联系宝付重新发送短信”，不再允许页面内重发验证码。",
      "user_story_ids": [
        "US-003"
      ],
      "when": "法人再次尝试触发验证码"
    },
    {
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff"
      ],
      "given": "新会员商户处于等待法人短验状态",
      "id": "AF-006",
      "name": "baofoo_ad_resends_legal_sms_for_new_member",
      "source_acceptance": "验证码重发-新会员",
      "then": "系统重发含链接的短验通知短信，并重置验证码次数。",
      "user_story_ids": [
        "US-005"
      ],
      "when": "宝付 AD 的会员产品开通进度操作中点击“法人短验重发”"
    },
    {
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff"
      ],
      "given": "老前置商户处于等待法人短验状态",
      "id": "AF-007",
      "name": "oms_resends_legal_sms_for_legacy_front",
      "source_acceptance": "验证码重发-老前置",
      "then": "系统重发含链接的短验通知短信，并重置验证码次数。",
      "user_story_ids": [
        "US-005"
      ],
      "when": "融证通 OMS 同城机构管理中选中记录并点击“法人短验重发”"
    },
    {
      "aggregate_refs": [
        "risk_rule",
        "risk_decision",
        "authorization_consent",
        "onboarding_application"
      ],
      "context_refs": [
        "risk_decision_context",
        "mandate_authorization_context",
        "merchant_onboarding_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff",
        "evidence"
      ],
      "given": "场景一或场景二进入产品开通流程",
      "id": "AF-008",
      "name": "agent_skip_policy_applies_only_to_configured_agent_chain",
      "source_acceptance": "短验跳过功能配置",
      "then": "代理商本身无需法人短验；配置权限代理商直接或间接拓展的代客可跳过法人短验；直客必须进行法人短验。",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-007"
      ],
      "when": "系统按 Apollo 配置判断商户为代理商本身、配置权限一代或其二代拓展的代客，或直客"
    },
    {
      "aggregate_refs": [
        "capability_grant",
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "merchant_capability_context",
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "evidence",
        "state_change"
      ],
      "given": "新会员商户产品开通处于法人短验等待阶段",
      "id": "AF-009",
      "name": "new_member_progress_shows_waiting_legal_sms",
      "source_acceptance": "进度展示-新会员",
      "then": "审批步骤展示“等待法人短验”阶段。",
      "user_story_ids": [
        "US-001",
        "US-006"
      ],
      "when": "用户查看宝付 AD 会员产品开通进度或新 BM 产品开通进度列表"
    },
    {
      "aggregate_refs": [
        "capability_grant",
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "context_refs": [
        "merchant_capability_context",
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "coverage_types": [
        "evidence",
        "state_change"
      ],
      "given": "老前置机构记录涉及多渠道收款法人短验",
      "id": "AF-010",
      "name": "legacy_front_progress_shows_legal_sms_status",
      "source_acceptance": "进度展示-老前置",
      "then": "页面展示“是否法人短验”字段，枚举为“已短验、未短验、无需短验”。",
      "user_story_ids": [
        "US-002",
        "US-006"
      ],
      "when": "用户查看融证通 OMS 同城机构管理列表"
    },
    {
      "aggregate_refs": [
        "compliance_review",
        "authorization_consent",
        "consent_record",
        "merchant"
      ],
      "context_refs": [
        "compliance_review_context",
        "mandate_authorization_context",
        "merchant_onboarding_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff",
        "evidence"
      ],
      "given": "合规提供存量需发送短信的商户列表",
      "id": "AF-011",
      "name": "stock_merchant_batch_sms_requires_compliance_list",
      "source_acceptance": "场景三、2026-06-08 会议确认存量为一次性事项不新增功能",
      "then": "按合规提供的存量商户列表一次性发送短验通知短信；不新增存量进度功能，由研发配合查看短验进展。",
      "user_story_ids": [
        "US-004"
      ],
      "when": "研发按列表批量给法人发送含 H5 链接的短验通知短信"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "state_change",
        "evidence"
      ],
      "given": "法人短信核验已经成功",
      "id": "AF-012",
      "name": "completed_link_is_read_only",
      "source_acceptance": "短验回填链接-完成状态",
      "then": "页面不能填写验证码或触发短信，并展示“已完成法人信息核验”。",
      "user_story_ids": [
        "US-003"
      ],
      "when": "法人再次打开短验链接页面"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "onboarding_application"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "merchant_onboarding_context"
      ],
      "coverage_types": [
        "evidence"
      ],
      "given": "系统发送法人短验通知短信或验证码短信",
      "id": "AF-013",
      "name": "sms_templates_match_required_content",
      "source_acceptance": "短信内容",
      "then": "短验通知短信包含监管身份识别、特约商户真实意愿确认、H5 链接、客服热线和非本人说明；验证码短信包含特约商户开立意愿核验、验证码和 5 分钟有效期。",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-003",
        "US-004",
        "US-005"
      ],
      "when": "法人收到短信并进入验证流程"
    },
    {
      "aggregate_refs": [
        "onboarding_application",
        "capability_grant",
        "risk_rule"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "merchant_capability_context",
        "risk_decision_context"
      ],
      "coverage_types": [
        "state_change",
        "handoff"
      ],
      "given": "商户不属于首版业务范围，或不是多渠道收款业务",
      "id": "AF-014",
      "name": "out_of_scope_merchants_do_not_trigger_legal_sms",
      "source_acceptance": "首版范围、场景覆盖矩阵",
      "then": "不发送法人短验通知，不展示等待法人短验，不阻断 118 / 83。",
      "user_story_ids": [
        "US-008"
      ],
      "when": "系统进行法人短验范围判定"
    },
    {
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record"
      ],
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context"
      ],
      "coverage_types": [
        "failure_path",
        "state_change"
      ],
      "given": "商户不处于等待法人短验状态",
      "id": "AF-015",
      "name": "non_waiting_merchants_cannot_resend_legal_sms",
      "source_acceptance": "验证码重发、场景覆盖矩阵",
      "then": "AD / OMS 不允许触发法人短验重发，且不重置验证码次数。",
      "user_story_ids": [
        "US-009"
      ],
      "when": "业务处理方尝试触发法人短验重发"
    },
    {
      "aggregate_refs": [
        "capability_grant",
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "context_refs": [
        "merchant_capability_context",
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "coverage_types": [
        "evidence",
        "state_change"
      ],
      "given": "商户存在法人短验判定或验证进展",
      "id": "AF-016",
      "name": "legal_sms_status_mapping_is_consistent",
      "source_acceptance": "进度展示、规则/状态矩阵",
      "then": "H5、AD、新 BM 和 OMS 对等待、已短验、无需短验、H5 超限待宝付重发的展示和阻断口径一致。",
      "user_story_ids": [
        "US-006",
        "US-010"
      ],
      "when": "页面或后台展示短验状态、判断是否阻断流程或是否允许后台重发"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "coverage_types": [
        "evidence",
        "failure_path"
      ],
      "given": "系统准备发送法人短验通知短信",
      "id": "AF-017",
      "name": "sms_url_length_and_payload_are_bounded",
      "source_acceptance": "人工评审补充-短信 URL 长度与承载",
      "then": "短验通知短信有明确模板长度预算；H5 链接使用可信域名下短路径/短 token；不得把明文商户、法人或业务敏感参数放进 URL；链接超长时有降级或拒发处理。",
      "user_story_ids": [
        "US-011",
        "US-012"
      ],
      "when": "短信模板渲染并生成 H5 链接"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "coverage_types": [
        "evidence",
        "failure_path"
      ],
      "given": "法人或持有短信链接的人访问 H5",
      "id": "AF-018",
      "name": "h5_link_token_is_secure",
      "source_acceptance": "人工评审补充-链接与 token 安全",
      "then": "H5 链接使用 HTTPS、可信域名和不可枚举 token；token 有有效期、状态、失效机制和访问频控；服务端不依赖客户端隐藏字段；日志、Referer 和页面跳转不泄露 token 或敏感信息。",
      "user_story_ids": [
        "US-011",
        "US-012"
      ],
      "when": "系统校验 H5 链接和 token"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review",
        "merchant"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context",
        "merchant_onboarding_context"
      ],
      "coverage_types": [
        "state_change",
        "evidence"
      ],
      "given": "点击者可以打开短信链接并回填验证码",
      "id": "AF-019",
      "name": "legal_representative_identity_binding_is_verified",
      "source_acceptance": "人工评审补充-法人身份核验",
      "then": "系统不能仅凭短信链接点击和验证码回填判断点击者就是法人；必须按合规确认的手机号来源、法人身份绑定、二次核身或人工兜底规则完成核身。",
      "user_story_ids": [
        "US-011",
        "US-012"
      ],
      "when": "系统准备记录法人短验成功"
    },
    {
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "coverage_types": [
        "evidence"
      ],
      "given": "系统完成或拒绝法人短验",
      "id": "AF-020",
      "name": "compliance_evidence_and_personal_information_controls_exist",
      "source_acceptance": "人工评审补充-合规证据链和个人信息保护",
      "then": "系统记录核验对象、页面文案版本、短信模板版本、发送/重发记录、核身方式、验证码结果、意愿确认动作、时间、IP/设备、操作人和失败原因，并明确个人信息最小必要采集、脱敏展示、访问权限、留存期限和导出边界。",
      "user_story_ids": [
        "US-011",
        "US-012"
      ],
      "when": "合规或运营查询核验结果和证据"
    }
  ],
  "active": true,
  "blockers": [
    {
      "id": "flowchart-missing",
      "reason": "流程图待补充，当前只能按文字触发点记录流程阻断与继续条件。"
    },
    {
      "id": "h5-attachment-missing",
      "reason": "页面样例附件未随本次聊天提供，H5 细节只能按文字规则记录。"
    },
    {
      "id": "legal-compliance-position-missing",
      "reason": "法规依据、监管口径、个人信息处理依据、证据留存期限和合规 owner 确认缺失。"
    },
    {
      "id": "sms-url-constraint-missing",
      "reason": "短信模板长度预算、可信域名、短 token/短链方案、超长 URL 降级策略缺失。"
    },
    {
      "id": "link-token-security-missing",
      "reason": "token 有效期、单次/多次访问语义、重发后旧 token 处理、频控、日志脱敏和 Referer 防泄露规则缺失。"
    },
    {
      "id": "identity-binding-missing",
      "reason": "法人手机号来源、身份绑定依据、二次核身字段和人工兜底规则缺失。"
    }
  ],
  "case_slug": "baofu-multi-channel-legal-sms-verification",
  "case_source": {
    "provenance": "user provided requirement text in chat on 2026-06-09 and requested `$report-wiki-portfolio:req-agent`",
    "requirement_like": true,
    "source_path": "/tmp/baofu-legal-sms-verification-requirement.txt",
    "source_type": "chat_requirement",
    "title": "多渠道收款商户法人短信认证"
  },
  "current_intent": {
    "draft_requested": false,
    "intent": "new_requirement_intake",
    "requested_action": "走我们的需求",
    "routed_worker": "req-intake"
  },
  "domain": {
    "candidates": [
      {
        "id": "risk_compliance",
        "reason": "primary requirement is legal representative intent verification for compliance evidence before product opening continues"
      },
      {
        "id": "merchant_platform_relationship",
        "reason": "product opening progress, onboarding gate, and merchant capability lifecycle are in scope"
      },
      {
        "id": "account_balance",
        "reason": "rejected as primary domain; electronic account complaint is risk background, not the requested account/balance lifecycle design"
      }
    ],
    "confirmed": "risk_compliance",
    "status": "confirmed"
  },
  "domain_coverage": [
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-002",
        "AF-006",
        "AF-007",
        "AF-008",
        "AF-009",
        "AF-010",
        "AF-011",
        "AF-013",
        "AF-014",
        "AF-015",
        "AF-016",
        "AF-017",
        "AF-019"
      ],
      "aggregate_roots": [
        "onboarding_application",
        "capability_grant",
        "merchant"
      ],
      "contexts": [
        "merchant_onboarding_context",
        "merchant_capability_context"
      ],
      "coverage_type": "primary",
      "review_note": "merchant opening gate, capability progress, stock merchant targeting, resend operations, and H5 identity-facing merchant context are first-release surfaces.",
      "subdomain": "merchant_platform_relationship",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-004",
        "US-005",
        "US-006",
        "US-007",
        "US-008",
        "US-009",
        "US-010",
        "US-012"
      ]
    },
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-002",
        "AF-003",
        "AF-004",
        "AF-005",
        "AF-006",
        "AF-007",
        "AF-008",
        "AF-009",
        "AF-010",
        "AF-011",
        "AF-012",
        "AF-013",
        "AF-014",
        "AF-015",
        "AF-016",
        "AF-017",
        "AF-018",
        "AF-019",
        "AF-020"
      ],
      "aggregate_roots": [
        "authorization_consent",
        "consent_record",
        "compliance_review",
        "risk_rule",
        "risk_decision"
      ],
      "contexts": [
        "mandate_authorization_context",
        "compliance_review_context",
        "risk_decision_context"
      ],
      "coverage_type": "primary",
      "review_note": "legal representative consent verification, retry/failure behavior, compliance evidence, URL/token safety, identity binding, and skip-policy decisions are primary compliance coverage.",
      "subdomain": "risk_compliance",
      "user_story_ids": [
        "US-001",
        "US-002",
        "US-003",
        "US-004",
        "US-005",
        "US-006",
        "US-007",
        "US-008",
        "US-009",
        "US-010",
        "US-011",
        "US-012"
      ]
    }
  ],
  "domain_model": {
    "aggregate_roots": [
      "onboarding_application",
      "capability_grant",
      "merchant",
      "authorization_consent",
      "consent_record",
      "compliance_review",
      "risk_rule",
      "risk_decision"
    ],
    "bounded_contexts": [
      "merchant_onboarding_context",
      "merchant_capability_context",
      "mandate_authorization_context",
      "compliance_review_context",
      "risk_decision_context"
    ],
    "business_ecosystems": [
      "payment_ecosystem"
    ],
    "context_handoffs": [
      {
        "from_context": "merchant_onboarding_context",
        "name": "StartLegalRepresentativeSmsVerification",
        "to_context": "mandate_authorization_context",
        "type": "compliance_gate"
      },
      {
        "from_context": "mandate_authorization_context",
        "name": "LegalRepresentativeVerifiedOrSkipped",
        "to_context": "merchant_capability_context",
        "type": "policy_decision"
      },
      {
        "from_context": "risk_decision_context",
        "name": "SmsVerificationSkipPolicyEvaluated",
        "to_context": "mandate_authorization_context",
        "type": "policy_rule"
      }
    ],
    "fact_owners": [
      "onboarding_owner",
      "capability_owner",
      "mandate_owner",
      "compliance_owner",
      "risk_owner"
    ],
    "non_domain_terms": [
      "118流程",
      "83流程",
      "宝付AD",
      "新BM",
      "融证通OMS",
      "Apollo"
    ],
    "open_questions": [
      "验证码次数重置是重置 H5 触发次数、验证码校验次数，还是两者都重置？",
      "短验通知短信中的链接 token、有效期、幂等和访问安全规则是什么？",
      "适用法规、监管口径、个人信息处理依据、证据留存期限和合规 owner 确认是什么？",
      "短信模板长度预算、可信域名、短 token/短链方案、超长 URL 降级策略是什么？",
      "法人手机号来源、身份绑定依据、二次核身字段和人工兜底规则是什么？",
      "token 访问频控、重发后旧 token 处理、日志脱敏、Referer 防泄露和异常告警规则是什么？"
    ],
    "role_obligations": [
      "onboarding_owner",
      "capability_owner",
      "mandate_owner",
      "compliance_owner",
      "risk_owner"
    ],
    "status": "confirmed",
    "subdomains": [
      "merchant_platform_relationship",
      "risk_compliance"
    ]
  },
  "evidence_attachments": {
    "analysis": [
      "scripts/build_requirements_analysis_agent.py output rejected account_balance as primary-domain false positive"
    ],
    "human_review": [
      "wiki/ops/requirements-cases/2026-06-09-baofu-legal-sms-human-review.md"
    ],
    "source": [
      "/tmp/baofu-legal-sms-verification-requirement.txt"
    ],
    "taxonomy": [
      "requirements/config/requirements-taxonomy.yaml"
    ]
  },
  "generated_at": "2026-06-09T01:50:54.065976+00:00",
  "mode": "requirements_case",
  "proof_boundary_notes": [
    "This case records requirements intake and readiness evidence only.",
    "Analyzer output misclassified the case as account_balance because of the electronic account complaint; this case keeps account_balance as rejected primary-domain evidence.",
    "Electronic account is background risk evidence; first-pass requirement scope is legal representative SMS verification before multi-channel collection product opening continues.",
    "Human review on 2026-06-10 found that regulation, SMS URL length, H5 link security, identity binding, and compliance evidence are demand facts, not optional design polish.",
    "Detailed design, API contracts, DDL/schema, state machine, and engineering breakdown remain blocked until the detailed_design_hard_gates are provided or explicitly waived.",
    "No OpenSpec draft or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "supplement_sms_url_security_identity_and_compliance_facts",
    "reason": "Human review found demand-fact gaps around regulation, SMS URL length, link/token security, H5 identity binding, and compliance evidence. Re-run requirements checker and human review after synchronization.",
    "status": "blocked"
  },
  "roles": [
    {
      "category": "fact_owner",
      "confirmed_as": "onboarding_owner",
      "evidence_anchor": {
        "source_quote": "提交 118 流程前 / 发起 83 流程之前，给法人发送短信，直到法人回填验证码后继续产品开通流程。",
        "source_section": "场景一、场景二"
      },
      "id": "R-onboarding-owner",
      "mention": "新会员/老前置进件开通流程 owner",
      "status": "confirmed"
    },
    {
      "category": "fact_owner",
      "confirmed_as": "capability_owner",
      "evidence_anchor": {
        "source_quote": "商户产品开通进度需体现等待法人短验阶段；老前置机构管理表展示是否法人短验。",
        "source_section": "进度展示"
      },
      "id": "R-capability-owner",
      "mention": "多渠道收款产品开通进度 owner",
      "status": "confirmed"
    },
    {
      "category": "business_actor",
      "confirmed_as": "mandate_owner",
      "evidence_anchor": {
        "source_quote": "法人点击链接手动触发验证码，宝付发送验证码短信，法人回填短信验证码。",
        "source_section": "短信回填链接"
      },
      "id": "R-legal-representative",
      "mention": "商户法人",
      "normalization_note": "Case-local external actor mapped to mandate_owner because the requirement records legal representative authorization/consent facts.",
      "status": "confirmed"
    },
    {
      "category": "fact_owner",
      "confirmed_as": "compliance_owner",
      "evidence_anchor": {
        "source_quote": "为保证业务合规开展，需要对存量及后续新增的多渠道收款商户增加法人短信认证。",
        "source_section": "背景、场景三"
      },
      "id": "R-compliance-owner",
      "mention": "合规",
      "status": "confirmed"
    },
    {
      "category": "fact_owner",
      "confirmed_as": "risk_owner",
      "evidence_anchor": {
        "source_quote": "场景一和场景二的产品开通流程，需要支持按代理商配置跳过短验环节，一期通过 Apollo 配置实现。",
        "source_section": "短验跳过功能配置"
      },
      "id": "R-risk-owner",
      "mention": "短验跳过规则 owner",
      "status": "confirmed"
    }
  ],
  "soft_evidence": {
    "api": [
      "Design evidence only: SMS sending channels, H5 verification endpoint, AD resend action, OMS resend action, and progress-query surfaces are implied but contracts are not provided."
    ],
    "business_rules": [
      "Scope: multi-channel collection business with business attribute 抖音平台-商品购销、本地生活-商品购销、掌财狸.",
      "New member path waits before 118; legacy front path waits before 83.",
      "H5 code is triggered manually from the link; code SMS is valid for 5 minutes.",
      "Waiting for legal representative SMS verification is an onboarding process stage with no expiry; only the SMS verification code expires.",
      "H5 trigger attempts over 3 without success require Baofoo-side resend.",
      "Baofoo AD and OMS resend reset verification-code attempts only for waiting-verification merchants.",
      "Agent itself needs no verification; configured first-level agent direct clients and second-level agent clients may skip; direct clients must verify.",
      "SMS notification links must be short enough for the message template budget and must not carry plaintext merchant, legal representative, phone, certificate, or business-sensitive parameters.",
      "SMS OTP proves phone possession or reachability only; legal representative identity binding and intent confirmation require compliance-confirmed identity evidence or compensating controls.",
      "Consent and verification evidence must be retained with least-necessary personal information and controlled access."
    ],
    "detailed_design_hard_gates": [
      {
        "blocks_until_passed": "Detailed design, API contracts, state machines, and engineering breakdown.",
        "gate": "current_state_material_package",
        "hard_gate": true,
        "material_status": "missing",
        "pass_condition": "Product provides referenceable current-state flows/screens/contracts or explicitly waives each current-state dependency.",
        "required_from": "product_owner_or_requirement_proposer",
        "required_material": "For detailed design: current 118/83 entry points, existing new-member and old-front progress/status fields, current AD/OMS operation locations, SMS channel template/sending constraints, and the H5 page sample or confirmed no-sample boundary."
      },
      {
        "blocks_until_passed": "Rule model, status machine, retry/reset behavior, skip-policy implementation, and acceptance finalization.",
        "gate": "business_rule_position_table",
        "hard_gate": true,
        "material_status": "missing",
        "pass_condition": "Product confirms first-release rules, deferred rules, owners, and exact rule parameters or explicitly waives them.",
        "required_from": "product_owner_with_compliance_owner_and_onboarding_owner",
        "required_material": "For detailed design: exact scope predicates, skip-policy matching order, waiting status enum, code validity, H5 trigger limit, Baofoo-side resend reset semantics, stock one-time handling, and progress enum mapping."
      },
      {
        "blocks_until_passed": "API design, event/callback design, table/schema design, and integration breakdown.",
        "gate": "system_boundary_contract_table",
        "hard_gate": true,
        "material_status": "missing",
        "pass_condition": "Product identifies initiator, fact owner, API/event/callback boundary, idempotency/retry behavior, and failure recovery for each handoff.",
        "required_from": "product_owner_with_member_group_account_group_compliance_and_sms_channel_owner",
        "required_material": "For detailed design: owner and handoff table for new member, old front, AD, OMS, H5, SMS channel, Apollo config, 118/83 workflow continuation, and one-time stock batch progress lookup."
      }
    ],
    "exception_scenarios": [
      "验证码有误或验证码超时 prompts retry.",
      "超过 3 次仍未验证成功 blocks H5 resend and asks legal representative to contact Baofoo.",
      "Stock merchant handling is one-time: no new progress-view function; engineering only cooperates with progress lookup."
    ],
    "test_plan": [
      "AF-001 through AF-020 provide observable acceptance functions and story mappings after 2026-06-10 human-review supplementation."
    ]
  },
  "status": "blocked",
  "user_stories": [
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-008",
        "AF-009",
        "AF-013"
      ],
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record",
        "capability_grant",
        "risk_rule"
      ],
      "benefit": "法人完成真实意愿核验后才继续产品开通，降低电子户开通不知情风险。",
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context",
        "merchant_capability_context",
        "risk_decision_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "场景一",
          "短验跳过功能配置",
          "进度展示"
        ]
      },
      "id": "US-001",
      "role_ref": "R-onboarding-owner",
      "want": "在新会员 BM/API 入口开通多渠道收款且命中范围时，提交 118 流程前进入等待法人短验，并向法人发送含 H5 链接的短验通知短信"
    },
    {
      "acceptance_function_ids": [
        "AF-002",
        "AF-008",
        "AF-010",
        "AF-013"
      ],
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record",
        "capability_grant",
        "risk_rule"
      ],
      "benefit": "老前置链路也能在产品开通前取得法人短信认证。",
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context",
        "merchant_capability_context",
        "risk_decision_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "场景二",
          "短验跳过功能配置",
          "进度展示"
        ]
      },
      "id": "US-002",
      "role_ref": "R-onboarding-owner",
      "want": "在老前置进件机审完成后、发起 83 流程前进入等待法人短验，并向法人发送含 H5 链接的短验通知短信"
    },
    {
      "acceptance_function_ids": [
        "AF-003",
        "AF-004",
        "AF-005",
        "AF-012",
        "AF-013"
      ],
      "aggregate_refs": [
        "authorization_consent",
        "consent_record"
      ],
      "benefit": "法人可以完成特约商户开立意愿核验，验证成功后页面进入完成状态且流程可继续。",
      "context_refs": [
        "mandate_authorization_context"
      ],
      "domain_refs": [
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "短验回填链接",
          "短信内容"
        ]
      },
      "id": "US-003",
      "role_ref": "R-legal-representative",
      "want": "通过短信链接进入 H5 页面，手动触发验证码短信并回填验证码"
    },
    {
      "acceptance_function_ids": [
        "AF-011",
        "AF-013"
      ],
      "aggregate_refs": [
        "compliance_review",
        "authorization_consent",
        "consent_record",
        "merchant"
      ],
      "benefit": "存量多渠道收款商户的法人意愿核验可以被核查和追踪，不新增存量进度功能。",
      "context_refs": [
        "compliance_review_context",
        "mandate_authorization_context",
        "merchant_onboarding_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "场景三",
          "短验进度查询"
        ]
      },
      "id": "US-004",
      "role_ref": "R-compliance-owner",
      "want": "按合规提供的存量商户列表一次性批量发送法人短验通知短信，并由研发配合查看短验进展"
    },
    {
      "acceptance_function_ids": [
        "AF-006",
        "AF-007",
        "AF-013"
      ],
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record"
      ],
      "benefit": "验证码过期或法人未完成时，业务侧可以重新发起核验而不是让流程永久卡死。",
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "验证码重发"
        ]
      },
      "id": "US-005",
      "role_ref": "R-onboarding-owner",
      "want": "对等待验证状态的商户在宝付 AD 或融证通 OMS 重新触发法人短验通知短信并重置验证码次数"
    },
    {
      "acceptance_function_ids": [
        "AF-009",
        "AF-010"
      ],
      "aggregate_refs": [
        "capability_grant",
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "benefit": "产品开通进度能解释当前卡点并支持运营核查。",
      "context_refs": [
        "merchant_capability_context",
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "进度展示"
        ]
      },
      "id": "US-006",
      "role_ref": "R-capability-owner",
      "want": "在新会员、宝付 AD、新 BM 和老前置 OMS 中展示法人短验等待、已短验、未短验或无需短验进展"
    },
    {
      "acceptance_function_ids": [
        "AF-008"
      ],
      "aggregate_refs": [
        "risk_rule",
        "risk_decision",
        "authorization_consent",
        "onboarding_application"
      ],
      "benefit": "短验范围可以按业务风险策略落地，并避免误阻断代理商自身或配置允许的代客。",
      "context_refs": [
        "risk_decision_context",
        "mandate_authorization_context",
        "merchant_onboarding_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "短验跳过功能配置"
        ]
      },
      "id": "US-007",
      "role_ref": "R-risk-owner",
      "want": "按代理商 Apollo 配置跳过法人短验，同时保证直客必须短验、代理商本身无需短验"
    },
    {
      "acceptance_function_ids": [
        "AF-014"
      ],
      "aggregate_refs": [
        "onboarding_application",
        "capability_grant",
        "risk_rule"
      ],
      "benefit": "避免把合规短验扩大到范围外商户，造成误阻断。",
      "context_refs": [
        "merchant_onboarding_context",
        "merchant_capability_context",
        "risk_decision_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "首版范围",
          "场景覆盖矩阵"
        ]
      },
      "id": "US-008",
      "role_ref": "R-risk-owner",
      "want": "不命中首版范围的商户不进入法人短验，也不阻断 118 / 83"
    },
    {
      "acceptance_function_ids": [
        "AF-015"
      ],
      "aggregate_refs": [
        "onboarding_application",
        "authorization_consent",
        "consent_record"
      ],
      "benefit": "避免已完成、无需短验或范围外商户被重复发送短信。",
      "context_refs": [
        "merchant_onboarding_context",
        "mandate_authorization_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "验证码重发",
          "场景覆盖矩阵"
        ]
      },
      "id": "US-009",
      "role_ref": "R-onboarding-owner",
      "want": "非等待法人短验状态不能触发宝付 AD / 融证通 OMS 法人短验重发"
    },
    {
      "acceptance_function_ids": [
        "AF-009",
        "AF-010",
        "AF-016"
      ],
      "aggregate_refs": [
        "capability_grant",
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "benefit": "评审和运营可以判断当前到底是等待、已短验、无需短验还是 H5 超限待宝付重发。",
      "context_refs": [
        "merchant_capability_context",
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "进度展示",
          "规则/状态矩阵"
        ]
      },
      "id": "US-010",
      "role_ref": "R-capability-owner",
      "want": "短验状态在 H5、AD、新 BM 和 OMS 的展示与阻断口径保持一致"
    },
    {
      "acceptance_function_ids": [
        "AF-017",
        "AF-018",
        "AF-019",
        "AF-020"
      ],
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review"
      ],
      "benefit": "短验结果能作为合规证据，而不是产生新的钓鱼、冒用或个人信息泄露风险。",
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context"
      ],
      "domain_refs": [
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "人工评审补充-法规与安全缺口",
          "人工评审补充-短信 URL 与核身"
        ]
      },
      "id": "US-011",
      "role_ref": "R-compliance-owner",
      "want": "确认法人短信链接、验证码、H5 访问和证据记录满足监管、个人信息保护和安全要求"
    },
    {
      "acceptance_function_ids": [
        "AF-017",
        "AF-018",
        "AF-019",
        "AF-020"
      ],
      "aggregate_refs": [
        "authorization_consent",
        "consent_record",
        "compliance_review",
        "merchant"
      ],
      "benefit": "法人能识别宝付真实核验流程，且不会因链接过长、信息不清或核身不足造成误操作。",
      "context_refs": [
        "mandate_authorization_context",
        "compliance_review_context",
        "merchant_onboarding_context"
      ],
      "domain_refs": [
        "merchant_platform_relationship",
        "risk_compliance"
      ],
      "evidence_anchor": {
        "source_functions": [
          "人工评审补充-短信链接体验",
          "人工评审补充-H5 法人核身"
        ]
      },
      "id": "US-012",
      "role_ref": "R-legal-representative",
      "want": "通过简短可信短信链接进入 H5，识别被核验商户和业务，并通过足够核身步骤确认意愿"
    }
  ]
}
```
<!-- requirements-case-data:end -->
