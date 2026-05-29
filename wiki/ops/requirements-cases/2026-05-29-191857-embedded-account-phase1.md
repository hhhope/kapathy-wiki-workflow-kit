---
layer: ops
domain: unclassified
classification_needed: true
ops_area: workflow-trace
canonical_object: requirements-case-file
artifact_type: requirements-case
status: diagnose
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

- None

## Soft Evidence

### Business Rules

- Source includes BR-001 through BR-035 covering开户、绑卡、解绑、账户支付、多卡轮询、支付结果收敛、权限校验、版本边界。
- Hard constraints include one account per merchant terminal user, real-name account opening with first-card binding, explicit account-payment selection, no balance payment in phase 1, no direct card switch while payment result is unknown, and a single converged final payment status.

### Api

- Source identifies API-001 through API-008, NTF-001 through NTF-003, INT-001 through INT-005, and CH-001 through CH-005 as phase-1 interface scope evidence.

### Test Plan

- Source includes AC-001 through AC-026 as PRD acceptance evidence, but these have not yet been normalized into traceable requirements acceptance functions.

## Readiness / Next Action

- Status: diagnose
- Next action: write_acceptance_functions
- Reason: domain, roles, and user stories are normalized; hard-gate readiness still requires acceptance functions and story-to-acceptance mappings.

### Blockers

- acceptance_functions_missing: PRD acceptance criteria have not been converted to observable acceptance functions mapped to stories.
- story_acceptance_mapping_missing: user stories are intentionally not mapped until the req-acceptance worker writes acceptance functions.

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
- User stories are extracted from F-001 through F-007 and preserve role, want, and benefit; acceptance mapping remains pending.
- API, business-rule, and acceptance-table evidence are supporting evidence, not an OpenSpec draft.
- No OpenSpec draft or implementation work has been created.

## Machine Case Data

<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [],
  "active": true,
  "blockers": [
    {
      "id": "acceptance_functions_missing",
      "reason": "PRD acceptance criteria have not been converted to observable acceptance functions mapped to stories"
    },
    {
      "id": "story_acceptance_mapping_missing",
      "reason": "user stories are intentionally not mapped until the req-acceptance worker writes acceptance functions"
    }
  ],
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
    "User stories are extracted from F-001 through F-007 and preserve role, want, and benefit; acceptance mapping remains pending.",
    "API, business-rule, and acceptance-table evidence are supporting evidence, not an OpenSpec draft.",
    "No OpenSpec draft or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "write_acceptance_functions",
    "reason": "domain, roles, and user stories are normalized; hard-gate readiness still requires acceptance functions and story-to-acceptance mappings.",
    "status": "diagnose"
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
        "summary": "Source includes AC-001 through AC-026 as PRD acceptance evidence, but these have not yet been normalized into traceable requirements acceptance functions."
      }
    ]
  },
  "status": "diagnose",
  "user_stories": [
    {
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
      "benefit": "提高账户支付成功率并支持多卡支付准备。",
      "id": "US-003",
      "role": "financial_customer",
      "source_functions": [
        "F-003"
      ],
      "want": "商户希望在账户开户成功后为终端用户追加绑定银行卡。"
    },
    {
      "benefit": "已解绑卡不再参与账户支付或订阅自动扣款。",
      "id": "US-004",
      "role": "financial_customer",
      "source_functions": [
        "F-004"
      ],
      "want": "商户希望解除账户与银行卡之间的绑定关系。"
    },
    {
      "benefit": "订阅支付可以接入嵌入式账户能力且不发生自动支付方式路由。",
      "id": "US-005",
      "role": "financial_customer",
      "source_functions": [
        "F-005"
      ],
      "want": "商户希望在订阅支付中显式选择账户支付。"
    },
    {
      "benefit": "在高优先级卡明确失败后可以继续尝试低优先级卡。",
      "id": "US-006",
      "role": "system_actor",
      "source_functions": [
        "F-006"
      ],
      "want": "嵌入式账户前置希望按已绑卡优先级轮询发起快捷支付。"
    },
    {
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
