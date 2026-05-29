---
layer: ops
domain: unclassified
classification_needed: true
ops_area: workflow-trace
canonical_object: requirements-case-file
artifact_type: requirements-case
status: requirements_ready
case_slug: embedded-account-phase1
created_at: 2026-05-29
---

# requirements-case

## Case Source

- Generated at: 2026-05-29T11:18:57+00:00
- Scan root: `.`
- source_path: inbox/prd-embedded-account-phase1(2).md
- source_type: prd
- title: 嵌入式账户一期 PRD
- requirement_like: true
- provenance: user requested `$report-wiki-portfolio:req-agent 处理inbox/prd-embedded-account-phase1(2)`

## Intent

- intent: new_requirement_intake
- requested_action: process inbox PRD into requirements workflow state
- routed_worker: req-intake
- draft_requested: false

## Domain

- Status: confirmed
- Confirmed: account

### Candidates

- account: confirmed by user on 2026-05-29; PRD title and main scope repeatedly use `账户`, and `account` is a known requirements taxonomy domain
- embedded_wallet: retained as rejected analyzer ambiguity; not a requirements taxonomy domain
- wallet_payment: retained as rejected analyzer ambiguity; not a requirements taxonomy domain

## Roles

- financial_customer: financial customer (business_actors); source actors: 商户、目标客户、权益类商户
- retail_customer: retail customer (business_actors); source actors: 商户终端用户、终端用户
- system_actor: system actor (system_actors); source actors: 商户系统、统一网关、通知中心、产品中心、嵌入式账户前置、账户核心、订阅支付产品、宝付通道
- product: product (delivery_owners); source actors: 产品中心、订阅支付产品、嵌入式账户产品需求 owner
- engineering: engineering (delivery_owners); source actors: 嵌入式账户前置、账户核心、统一网关、通知中心、订阅支付产品相关研发团队
- qa: QA (delivery_owners); source actors: 联调、测试、验收责任方

## User Stories

- US-001: role=financial_customer; 商户希望通过 API 为终端用户开立嵌入式账户，并在开户流程内完成首卡绑定；benefit=为订阅支付场景建立可用的账户与首张可支付银行卡基础。
- US-002: role=retail_customer; 终端用户希望在商户引导下完成首卡绑定或追加绑卡；benefit=后续账户支付可以使用已绑定银行卡完成扣款。
- US-003: role=financial_customer; 商户希望在账户开户成功后为终端用户追加绑定银行卡；benefit=提高账户支付成功率并支持多卡支付准备。
- US-004: role=financial_customer; 商户希望解除账户与银行卡之间的绑定关系；benefit=已解绑卡不再参与账户支付或订阅自动扣款。
- US-005: role=financial_customer; 商户希望在订阅支付中显式选择账户支付；benefit=订阅支付可以接入嵌入式账户能力且不发生自动支付方式路由。
- US-006: role=system_actor; 嵌入式账户前置希望按已绑卡优先级轮询发起快捷支付；benefit=在高优先级卡明确失败后可以继续尝试低优先级卡。
- US-007: role=system_actor; 嵌入式账户前置希望在支付异常或结果未明时通过查单与补偿收敛结果；benefit=保证单笔支付只有一个唯一最终状态且不重复扣款。

## Acceptance Functions

- AF-001: stories=US-001, US-002; source=AC-001; then=首卡绑定成功后，系统返回开户成功。
- AF-002: stories=US-001; source=AC-002; then=首卡绑定失败时，系统返回开户失败，不生成成功账户状态。
- AF-003: stories=US-001; source=AC-003; then=同一商户用户已开户成功后再次开户，系统返回已存在账户成功，不重复创建账户。
- AF-004: stories=US-001; source=AC-004; then=历史开户处理中再次开户，系统返回处理中。
- AF-005: stories=US-001; source=AC-005; then=历史开户失败后，系统允许重新走开户流程。
- AF-006: stories=US-002, US-003; source=AC-006; then=开户后追加绑卡成功，系统返回绑卡成功，新卡可用于支付。
- AF-007: stories=US-002, US-003; source=AC-007; then=通道识别多张卡后，系统按用户选择结果完成绑卡。
- AF-008: stories=US-004; source=AC-008; then=账户已绑定银行卡时调用解绑接口，系统成功解除账户与银行卡关系。
- AF-009: stories=US-004; source=AC-009; then=某张卡已解绑后再次发起账户支付，系统不再使用该卡支付。
- AF-010: stories=US-005; source=AC-010; then=商户显式传入账户支付时，订阅支付正确调用账户支付接口。
- AF-011: stories=US-005; source=AC-011; then=支付前置条件满足时调用账户支付接口，支付成功且订阅支付结果同步成功。
- AF-012: stories=US-006; source=AC-012; then=用户绑定多张卡后发起账户支付，系统优先使用高优先级卡支付。
- AF-013: stories=US-006; source=AC-013; then=高优先级卡明确失败后，系统切换低优先级卡继续支付。
- AF-014: stories=US-006, US-007; source=AC-014; then=当前卡支付结果未明时，系统先查单，不直接切下一张卡。
- AF-015: stories=US-006; source=AC-015; then=银行卡查询超过配置上限时，系统按配置上限最多处理 5 张卡。
- AF-016: stories=US-004, US-006; source=AC-016; then=自动扣款命中已解绑高优先级卡时，系统自动跳过并继续处理下一张可用卡。
- AF-017: stories=US-004, US-006; source=AC-017; then=所有卡均已解绑或不可用时，系统返回支付失败。
- AF-018: stories=US-007; source=AC-018; then=通道未返回明确支付结果后，系统调用查询接口并收敛出唯一最终支付结果。
- AF-019: stories=US-007; source=AC-019; then=补偿流程执行查询、补偿、重试时，不发生重复扣款，仅保留唯一有效支付结果。
- AF-020: stories=US-001; source=AC-020; then=开户受理后用户完成绑卡且系统收敛最终结果，商户收到最终开户结果通知。
- AF-021: stories=US-002, US-003; source=AC-021; then=绑卡受理后用户完成绑卡且系统收敛最终结果，商户收到最终绑卡结果通知。
- AF-022: stories=US-007; source=AC-022; then=支付处理中或异常后异步处理完成，订阅支付产品收到最终支付结果通知。
- AF-023: stories=US-001, US-003, US-007; source=AC-023; then=通知未送达时，调用方主动查询可获得唯一最终状态。
- AF-024: stories=US-001; source=AC-024; then=开户命中同商户同证件正常账户时，系统直接返回已存在账户成功，不重复开户。
- AF-025: stories=US-003, US-004; source=AC-025; then=商户未开通一键绑卡权限时，调用绑卡或解绑接口被拒绝并返回权限不足。
- AF-026: stories=US-005, US-007; source=AC-026; then=商户未开通协议支付权限时，调用账户支付接口被拒绝并返回权限不足。

## Soft Evidence

### Business Rules

- Source includes BR-001 through BR-035 covering开户、绑卡、解绑、账户支付、多卡轮询、支付结果收敛、权限校验、版本边界。
- Hard constraints include one account per merchant terminal user, real-name account opening with first-card binding, explicit account-payment selection, no balance payment in phase 1, no direct card switch while payment result is unknown, and a single converged final payment status.

### Api

- Source identifies API-001 through API-008, NTF-001 through NTF-003, INT-001 through INT-005, and CH-001 through CH-005 as phase-1 interface scope evidence.

### Test Plan

- Source includes AC-001 through AC-026; each has been normalized into AF-001 through AF-026 and mapped to user stories.

## Readiness / Next Action

- Status: requirements_ready
- Next action: req-handoff
- Reason: domain, roles, user stories, acceptance functions, and bidirectional story mappings are normalized; OpenSpec draft creation remains a separate handoff action.

### Blockers

- None

## Evidence Attachments

### Source

- `inbox/prd-embedded-account-phase1(2).md`

### Taxonomy

- `requirements/config/requirements-taxonomy.yaml`

### Lore

- `wiki/index.md`
- `wiki/inbox-intake.md`
- `wiki/domains/account-clearing.md`
- `wiki/moc/domain-account-clearing.md`
- `wiki/ops/requirements-agent-skill-isolation-explore-2026-05-29.md`

## Proof Boundary

- This case file records requirement intake evidence only.
- Hard-gate validation belongs to the requirements checker.
- Domain `account` is confirmed by user approval on 2026-05-29.
- Roles are normalized to existing requirements taxonomy IDs; exact PRD actor names are preserved as source notes.
- User stories are extracted from F-001 through F-007 and preserve role, want, and benefit.
- Acceptance functions are extracted from AC-001 through AC-026 and mapped back to user stories.
- API, business-rule, and acceptance-table evidence are supporting evidence, not an OpenSpec draft.
- No OpenSpec draft or implementation work has been created.

## Machine Case Data

<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [
    {
      "id": "AF-001",
      "name": "终端用户正常开户",
      "source_acceptance": "AC-001",
      "source_functions": [
        "F-001",
        "F-002"
      ],
      "then": "首卡绑定成功后，系统返回开户成功。",
      "user_story_ids": [
        "US-001",
        "US-002"
      ]
    },
    {
      "id": "AF-002",
      "name": "首卡绑定失败导致开户失败",
      "source_acceptance": "AC-002",
      "source_functions": [
        "F-001",
        "F-002"
      ],
      "then": "首卡绑定失败时，系统返回开户失败，不生成成功账户状态。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-003",
      "name": "同一商户用户重复开户",
      "source_acceptance": "AC-003",
      "source_functions": [
        "F-001"
      ],
      "then": "同一商户用户已开户成功后再次开户，系统返回已存在账户成功，不重复创建账户。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-004",
      "name": "历史开户处理中再次开户",
      "source_acceptance": "AC-004",
      "source_functions": [
        "F-001"
      ],
      "then": "历史开户处理中再次开户，系统返回处理中。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-005",
      "name": "历史开户失败重新开户",
      "source_acceptance": "AC-005",
      "source_functions": [
        "F-001"
      ],
      "then": "历史开户失败后，系统允许重新走开户流程。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-006",
      "name": "开户后追加绑卡成功",
      "source_acceptance": "AC-006",
      "source_functions": [
        "F-003"
      ],
      "then": "开户后追加绑卡成功，系统返回绑卡成功，新卡可用于支付。",
      "user_story_ids": [
        "US-002",
        "US-003"
      ]
    },
    {
      "id": "AF-007",
      "name": "多卡识别后用户选择绑卡",
      "source_acceptance": "AC-007",
      "source_functions": [
        "F-003"
      ],
      "then": "通道识别多张卡后，系统按用户选择结果完成绑卡。",
      "user_story_ids": [
        "US-002",
        "US-003"
      ]
    },
    {
      "id": "AF-008",
      "name": "解绑银行卡关系成功",
      "source_acceptance": "AC-008",
      "source_functions": [
        "F-004"
      ],
      "then": "账户已绑定银行卡时调用解绑接口，系统成功解除账户与银行卡关系。",
      "user_story_ids": [
        "US-004"
      ]
    },
    {
      "id": "AF-009",
      "name": "解绑后卡不可继续支付",
      "source_acceptance": "AC-009",
      "source_functions": [
        "F-004"
      ],
      "then": "某张卡已解绑后再次发起账户支付，系统不再使用该卡支付。",
      "user_story_ids": [
        "US-004"
      ]
    },
    {
      "id": "AF-010",
      "name": "订阅支付选择账户支付",
      "source_acceptance": "AC-010",
      "source_functions": [
        "F-005"
      ],
      "then": "商户显式传入账户支付时，订阅支付正确调用账户支付接口。",
      "user_story_ids": [
        "US-005"
      ]
    },
    {
      "id": "AF-011",
      "name": "账户支付成功",
      "source_acceptance": "AC-011",
      "source_functions": [
        "F-005"
      ],
      "then": "支付前置条件满足时调用账户支付接口，支付成功且订阅支付结果同步成功。",
      "user_story_ids": [
        "US-005"
      ]
    },
    {
      "id": "AF-012",
      "name": "按优先级先扣高优先级卡",
      "source_acceptance": "AC-012",
      "source_functions": [
        "F-006"
      ],
      "then": "用户绑定多张卡后发起账户支付，系统优先使用高优先级卡支付。",
      "user_story_ids": [
        "US-006"
      ]
    },
    {
      "id": "AF-013",
      "name": "高优先级卡失败切换低优先级卡",
      "source_acceptance": "AC-013",
      "source_functions": [
        "F-006"
      ],
      "then": "高优先级卡明确失败后，系统切换低优先级卡继续支付。",
      "user_story_ids": [
        "US-006"
      ]
    },
    {
      "id": "AF-014",
      "name": "支付结果未明禁止直接切卡",
      "source_acceptance": "AC-014",
      "source_functions": [
        "F-006"
      ],
      "then": "当前卡支付结果未明时，系统先查单，不直接切下一张卡。",
      "user_story_ids": [
        "US-006",
        "US-007"
      ]
    },
    {
      "id": "AF-015",
      "name": "银行卡查询超过上限",
      "source_acceptance": "AC-015",
      "source_functions": [
        "F-006"
      ],
      "then": "银行卡查询超过配置上限时，系统按配置上限最多处理 5 张卡。",
      "user_story_ids": [
        "US-006"
      ]
    },
    {
      "id": "AF-016",
      "name": "已解绑卡在自动扣款中被跳过",
      "source_acceptance": "AC-016",
      "source_functions": [
        "F-004",
        "F-006"
      ],
      "then": "自动扣款命中已解绑高优先级卡时，系统自动跳过并继续处理下一张可用卡。",
      "user_story_ids": [
        "US-004",
        "US-006"
      ]
    },
    {
      "id": "AF-017",
      "name": "所有卡不可用时支付失败",
      "source_acceptance": "AC-017",
      "source_functions": [
        "F-004",
        "F-006"
      ],
      "then": "所有卡均已解绑或不可用时，系统返回支付失败。",
      "user_story_ids": [
        "US-004",
        "US-006"
      ]
    },
    {
      "id": "AF-018",
      "name": "支付异常后查询收敛结果",
      "source_acceptance": "AC-018",
      "source_functions": [
        "F-007"
      ],
      "then": "通道未返回明确支付结果后，系统调用查询接口并收敛出唯一最终支付结果。",
      "user_story_ids": [
        "US-007"
      ]
    },
    {
      "id": "AF-019",
      "name": "异常补偿不重复支付",
      "source_acceptance": "AC-019",
      "source_functions": [
        "F-007"
      ],
      "then": "补偿流程执行查询、补偿、重试时，不发生重复扣款，仅保留唯一有效支付结果。",
      "user_story_ids": [
        "US-007"
      ]
    },
    {
      "id": "AF-020",
      "name": "开户受理后异步通知商户",
      "source_acceptance": "AC-020",
      "source_functions": [
        "F-001"
      ],
      "then": "开户受理后用户完成绑卡且系统收敛最终结果，商户收到最终开户结果通知。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-021",
      "name": "绑卡受理后异步通知商户",
      "source_acceptance": "AC-021",
      "source_functions": [
        "F-003"
      ],
      "then": "绑卡受理后用户完成绑卡且系统收敛最终结果，商户收到最终绑卡结果通知。",
      "user_story_ids": [
        "US-002",
        "US-003"
      ]
    },
    {
      "id": "AF-022",
      "name": "支付处理中异步通知订阅产品",
      "source_acceptance": "AC-022",
      "source_functions": [
        "F-007"
      ],
      "then": "支付处理中或异常后异步处理完成，订阅支付产品收到最终支付结果通知。",
      "user_story_ids": [
        "US-007"
      ]
    },
    {
      "id": "AF-023",
      "name": "异步通知失败后主动查询",
      "source_acceptance": "AC-023",
      "source_functions": [
        "F-001",
        "F-003",
        "F-007"
      ],
      "then": "通知未送达时，调用方主动查询可获得唯一最终状态。",
      "user_story_ids": [
        "US-001",
        "US-003",
        "US-007"
      ]
    },
    {
      "id": "AF-024",
      "name": "开户命中正常账户",
      "source_acceptance": "AC-024",
      "source_functions": [
        "F-001"
      ],
      "then": "开户命中同商户同证件正常账户时，系统直接返回已存在账户成功，不重复开户。",
      "user_story_ids": [
        "US-001"
      ]
    },
    {
      "id": "AF-025",
      "name": "商户未开通一键绑卡权限",
      "source_acceptance": "AC-025",
      "source_functions": [
        "F-003",
        "F-004"
      ],
      "then": "商户未开通一键绑卡权限时，调用绑卡或解绑接口被拒绝并返回权限不足。",
      "user_story_ids": [
        "US-003",
        "US-004"
      ]
    },
    {
      "id": "AF-026",
      "name": "商户未开通协议支付权限",
      "source_acceptance": "AC-026",
      "source_functions": [
        "F-005",
        "F-007"
      ],
      "then": "商户未开通协议支付权限时，调用账户支付接口被拒绝并返回权限不足。",
      "user_story_ids": [
        "US-005",
        "US-007"
      ]
    }
  ],
  "active": true,
  "blockers": [],
  "case_slug": "embedded-account-phase1",
  "case_source": {
    "provenance": "user requested `$report-wiki-portfolio:req-agent 处理inbox/prd-embedded-account-phase1(2)`",
    "requirement_like": true,
    "source_path": "inbox/prd-embedded-account-phase1(2).md",
    "source_type": "prd",
    "title": "嵌入式账户一期 PRD"
  },
  "current_intent": {
    "draft_requested": false,
    "intent": "new_requirement_intake",
    "requested_action": "process inbox PRD into requirements workflow state",
    "routed_worker": "req-intake"
  },
  "domain": {
    "candidates": [
      {
        "confidence": "high",
        "id": "account",
        "reason": "confirmed by user on 2026-05-29; PRD title and main scope repeatedly use `账户`, and `account` is a known requirements taxonomy domain"
      },
      {
        "confidence": "medium",
        "id": "embedded_wallet",
        "reason": "rejected analyzer ambiguity; not a requirements taxonomy domain"
      },
      {
        "confidence": "medium",
        "id": "wallet_payment",
        "reason": "rejected analyzer ambiguity; not a requirements taxonomy domain"
      }
    ],
    "confirmed": "account",
    "status": "confirmed"
  },
  "evidence_attachments": {
    "lore": [
      "wiki/index.md",
      "wiki/inbox-intake.md",
      "wiki/domains/account-clearing.md",
      "wiki/moc/domain-account-clearing.md",
      "wiki/ops/requirements-agent-skill-isolation-explore-2026-05-29.md"
    ],
    "source": [
      "inbox/prd-embedded-account-phase1(2).md"
    ],
    "taxonomy": [
      "requirements/config/requirements-taxonomy.yaml"
    ]
  },
  "generated_at": "2026-05-29T11:18:57+00:00",
  "mode": "requirements_case",
  "proof_boundary_notes": [
    "This case file records requirement intake evidence only.",
    "Hard-gate validation belongs to the requirements checker.",
    "Domain `account` is confirmed by user approval on 2026-05-29.",
    "Roles are normalized to existing requirements taxonomy IDs; exact PRD actor names are preserved as source notes.",
    "User stories are extracted from F-001 through F-007 and preserve role, want, and benefit.",
    "Acceptance functions are extracted from AC-001 through AC-026 and mapped back to user stories.",
    "API, business-rule, and acceptance-table evidence are supporting evidence, not an OpenSpec draft.",
    "No OpenSpec draft or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "req-handoff",
    "reason": "domain, roles, user stories, acceptance functions, and bidirectional story mappings are normalized; OpenSpec draft creation remains a separate handoff action.",
    "status": "requirements_ready"
  },
  "roles": [
    {
      "category": "business_actors",
      "id": "financial_customer",
      "label": "financial customer",
      "normalization_note": "Used for merchant/customer-side business actor vocabulary without mutating the taxonomy.",
      "source_actors": [
        "商户",
        "目标客户",
        "权益类商户"
      ]
    },
    {
      "category": "business_actors",
      "id": "retail_customer",
      "label": "retail customer",
      "normalization_note": "Used for merchant terminal users whose account opening and card binding outcome is represented by the requirement.",
      "source_actors": [
        "商户终端用户",
        "终端用户"
      ]
    },
    {
      "category": "system_actors",
      "id": "system_actor",
      "label": "system actor",
      "source_actors": [
        "商户系统",
        "统一网关",
        "通知中心",
        "产品中心",
        "嵌入式账户前置",
        "账户核心",
        "订阅支付产品",
        "宝付通道"
      ]
    },
    {
      "category": "delivery_owners",
      "id": "product",
      "label": "product",
      "source_actors": [
        "产品中心",
        "订阅支付产品",
        "嵌入式账户产品需求 owner"
      ]
    },
    {
      "category": "delivery_owners",
      "id": "engineering",
      "label": "engineering",
      "source_actors": [
        "嵌入式账户前置",
        "账户核心",
        "统一网关",
        "通知中心",
        "订阅支付产品相关研发团队"
      ]
    },
    {
      "category": "delivery_owners",
      "id": "qa",
      "label": "QA",
      "source_actors": [
        "联调",
        "测试",
        "验收责任方"
      ]
    }
  ],
  "soft_evidence": {
    "api": [
      {
        "summary": "Source identifies API-001 through API-008, NTF-001 through NTF-003, INT-001 through INT-005, and CH-001 through CH-005 as phase-1 interface scope evidence."
      }
    ],
    "business_rules": [
      {
        "summary": "Source includes BR-001 through BR-035 covering开户、绑卡、解绑、账户支付、多卡轮询、支付结果收敛、权限校验、版本边界。"
      },
      {
        "summary": "Hard constraints include one account per merchant terminal user, real-name account opening with first-card binding, explicit account-payment selection, no balance payment in phase 1, no direct card switch while payment result is unknown, and a single converged final payment status."
      }
    ],
    "test_plan": [
      {
        "summary": "Source includes AC-001 through AC-026; each has been normalized into AF-001 through AF-026 and mapped to user stories."
      }
    ]
  },
  "status": "requirements_ready",
  "user_stories": [
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-002",
        "AF-003",
        "AF-004",
        "AF-005",
        "AF-020",
        "AF-023",
        "AF-024"
      ],
      "benefit": "为订阅支付场景建立可用的账户与首张可支付银行卡基础。",
      "id": "US-001",
      "role": "financial_customer",
      "source_functions": [
        "F-001",
        "F-002"
      ],
      "want": "商户希望通过 API 为终端用户开立嵌入式账户，并在开户流程内完成首卡绑定。"
    },
    {
      "acceptance_function_ids": [
        "AF-001",
        "AF-006",
        "AF-007",
        "AF-021"
      ],
      "benefit": "后续账户支付可以使用已绑定银行卡完成扣款。",
      "id": "US-002",
      "role": "retail_customer",
      "source_functions": [
        "F-002",
        "F-003"
      ],
      "want": "终端用户希望在商户引导下完成首卡绑定或追加绑卡。"
    },
    {
      "acceptance_function_ids": [
        "AF-006",
        "AF-007",
        "AF-021",
        "AF-023",
        "AF-025"
      ],
      "benefit": "提高账户支付成功率并支持多卡支付准备。",
      "id": "US-003",
      "role": "financial_customer",
      "source_functions": [
        "F-003"
      ],
      "want": "商户希望在账户开户成功后为终端用户追加绑定银行卡。"
    },
    {
      "acceptance_function_ids": [
        "AF-008",
        "AF-009",
        "AF-016",
        "AF-017",
        "AF-025"
      ],
      "benefit": "已解绑卡不再参与账户支付或订阅自动扣款。",
      "id": "US-004",
      "role": "financial_customer",
      "source_functions": [
        "F-004"
      ],
      "want": "商户希望解除账户与银行卡之间的绑定关系。"
    },
    {
      "acceptance_function_ids": [
        "AF-010",
        "AF-011",
        "AF-026"
      ],
      "benefit": "订阅支付可以接入嵌入式账户能力且不发生自动支付方式路由。",
      "id": "US-005",
      "role": "financial_customer",
      "source_functions": [
        "F-005"
      ],
      "want": "商户希望在订阅支付中显式选择账户支付。"
    },
    {
      "acceptance_function_ids": [
        "AF-012",
        "AF-013",
        "AF-014",
        "AF-015",
        "AF-016",
        "AF-017"
      ],
      "benefit": "在高优先级卡明确失败后可以继续尝试低优先级卡。",
      "id": "US-006",
      "role": "system_actor",
      "source_functions": [
        "F-006"
      ],
      "want": "嵌入式账户前置希望按已绑卡优先级轮询发起快捷支付。"
    },
    {
      "acceptance_function_ids": [
        "AF-014",
        "AF-018",
        "AF-019",
        "AF-022",
        "AF-023",
        "AF-026"
      ],
      "benefit": "保证单笔支付只有一个唯一最终状态且不重复扣款。",
      "id": "US-007",
      "role": "system_actor",
      "source_functions": [
        "F-007"
      ],
      "want": "嵌入式账户前置希望在支付异常或结果未明时通过查单与补偿收敛结果。"
    }
  ]
}
```
<!-- requirements-case-data:end -->
