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

- None

## User Stories

- None

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
- Next action: normalize_roles
- Reason: domain is confirmed as `account`; hard-gate readiness still requires normalized roles, user stories, and acceptance functions.

### Blockers

- roles_missing: requirement actors and owners have not been normalized to `requirements/config/requirements-taxonomy.yaml`.
- user_stories_missing: PRD functions have not been converted to role/want/benefit stories.
- acceptance_functions_missing: PRD acceptance criteria have not been converted to observable acceptance functions mapped to stories.

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
      "id": "roles_missing",
      "reason": "requirement actors and owners have not been normalized to `requirements/config/requirements-taxonomy.yaml`"
    },
    {
      "id": "user_stories_missing",
      "reason": "PRD functions have not been converted to role/want/benefit stories"
    },
    {
      "id": "acceptance_functions_missing",
      "reason": "PRD acceptance criteria have not been converted to observable acceptance functions mapped to stories"
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
    "API, business-rule, and acceptance-table evidence are supporting evidence, not an OpenSpec draft.",
    "No OpenSpec draft or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "normalize_roles",
    "reason": "domain is confirmed as `account`; hard-gate readiness still requires normalized roles, user stories, and acceptance functions.",
    "status": "diagnose"
  },
  "roles": [],
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
  "user_stories": []
}
```
<!-- requirements-case-data:end -->
