---
layer: ops
domain: unclassified
classification_needed: true
ops_area: workflow-trace
canonical_object: requirements-case-file
artifact_type: requirements-case
status: intake
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
- None

## User Stories
- None

## Acceptance Functions
- None

## Soft Evidence
### Domain Model
- {"aggregate_roots": ["commercial_subscription", "invoice", "dunning_case", "payment_intent", "payment_attempt", "ledger_entry", "fund_state", "reconciliation_record", "mandate", "agent_entitlement", "usage_event", "seat_assignment", "split_rule", "settlement_batch", "payout"], "bounded_contexts": ["commercial_subscription_context", "billing_invoice_context", "revenue_recovery_context", "payment_intent_context", "payment_attempt_authorization_context", "balance_ledger_context", "fund_state_context", "reconciliation_context", "mandate_authorization_context", "agent_entitlement_context", "agent_usage_metering_context", "agent_workspace_seat_context", "split_allocation_context", "settlement_batch_context", "payout_context"], "business_ecosystems": ["payment_ecosystem", "agent_service_ecosystem"], "candidates": [], "context_handoffs": [{"from_context": "commercial_subscription_context", "name": "GenerateInvoice", "to_context": "billing_invoice_context", "type": "command"}, {"from_context": "billing_invoice_context", "name": "ChargeInvoice", "to_context": "payment_intent_context", "type": "command"}, {"from_context": "payment_attempt_authorization_context", "name": "PaymentSucceeded", "to_context": "balance_ledger_context", "type": "domain_event"}, {"from_context": "commercial_subscription_context", "name": "CommercialSubscriptionActivated", "to_context": "agent_entitlement_context", "type": "domain_event"}], "fact_owners": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "non_domain_terms": ["subscription", "account", "settlement"], "open_questions": ["Confirm first-release payout/split settlement scope."], "role_obligations": ["subscription_owner", "subscription_policy_owner", "billing_ops_owner", "payment_ops_owner", "funds_account_owner", "ledger_owner", "balance_state_owner", "reconciliation_owner", "mandate_owner", "compliance_owner", "agent_entitlement_owner", "access_policy_owner", "usage_rating_owner", "agent_usage_owner", "metering_owner", "workspace_owner", "seat_owner", "split_rule_owner", "settlement_owner", "payout_owner"], "status": "confirmed", "subdomains": ["billing_revenue", "merchant_platform_relationship", "payment_transaction", "account_balance", "funds_movement_settlement", "financial_operations", "risk_compliance", "agent_entitlement", "agent_usage_metering", "agent_workspace_seat"]}
### Intake Actors
- {"id": "ai_service_provider", "label": "AI service provider", "type": "organization"}
- {"id": "platform", "label": "platform", "type": "organization"}
- {"id": "consumer", "label": "consumer", "type": "person"}
- {"id": "recurring_billing_job", "label": "recurring billing automation", "type": "system"}
- {"id": "payment_channel", "label": "payment channel", "type": "external_system"}
### Open Questions
- {"question": "Confirm whether first release includes split allocation, settlement batch, and payout, or records them as follow-up scope."}
- {"question": "Confirm target customers and integration boundary: standalone Agent provider, Agent marketplace/platform, or both."}
- {"question": "Confirm supported commercial models: fixed subscription, usage billing, seat billing, or mixed billing."}
- {"question": "Confirm whether payment method authorization/mandate and recurring deduction retry policy are in first-release scope."}
### Source Material
- {"summary": "Agent service subscription payment market and pain points"}
- {"pain_point": "payment threshold is high; service providers lack subscription payment lifecycle capability"}
- {"pain_point": "renewal rate is low; dunning, grace period, and retention mechanisms are missing"}
- {"pain_point": "billing models are too simple; fixed subscription dominates while usage and seat billing are needed"}
- {"pain_point": "split settlement is complex for AI application marketplace and platform models"}

## Readiness / Next Action
- Status: intake
- Next action: run_requirements_checker
- Reason: Hard-gate validation belongs to the requirements checker lifecycle.
### Blockers
- roles_missing: Source material names actor types, but case roles have not been confirmed or normalized.
- user_stories_missing: No role/want/benefit user stories have been normalized from the material yet.
- acceptance_functions_missing: No observable acceptance functions have been defined or mapped to user stories yet.
- scope_confirmation_needed: First-release split settlement, metering, seat billing, mandate, retry, and dunning scope need confirmation.

## Evidence Attachments
### Analysis
- `scripts/build_requirements_analysis_agent.py --material-file /tmp/agent-subscription-payment-material.md`
### Source
- `/tmp/agent-subscription-payment-material.md`
### Taxonomy
- `requirements/config/requirements-taxonomy.yaml`

## Proof Boundary
- This case records intake evidence for user-provided market pain-point material.
- Domain analysis is taxonomy-derived; first-release scope still requires product confirmation.
- Actors are detected source signals, not confirmed case roles.
- No user stories, acceptance functions, OpenSpec draft, or implementation work has been created.

## Machine Case Data
<!-- requirements-case-data:start -->
```json
{
  "acceptance_functions": [],
  "active": true,
  "blockers": [
    {
      "id": "roles_missing",
      "reason": "Source material names actor types, but case roles have not been confirmed or normalized."
    },
    {
      "id": "user_stories_missing",
      "reason": "No role/want/benefit user stories have been normalized from the material yet."
    },
    {
      "id": "acceptance_functions_missing",
      "reason": "No observable acceptance functions have been defined or mapped to user stories yet."
    },
    {
      "id": "scope_confirmation_needed",
      "reason": "First-release split settlement, metering, seat billing, mandate, retry, and dunning scope need confirmation."
    }
  ],
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
    "This case records intake evidence for user-provided market pain-point material.",
    "Domain analysis is taxonomy-derived; first-release scope still requires product confirmation.",
    "Actors are detected source signals, not confirmed case roles.",
    "No user stories, acceptance functions, OpenSpec draft, or implementation work has been created."
  ],
  "readiness_next_action": {
    "next_action": "run_requirements_checker",
    "reason": "Hard-gate validation belongs to the requirements checker lifecycle.",
    "status": "intake"
  },
  "roles": [],
  "soft_evidence": {
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
        "question": "Confirm whether first release includes split allocation, settlement batch, and payout, or records them as follow-up scope."
      },
      {
        "question": "Confirm target customers and integration boundary: standalone Agent provider, Agent marketplace/platform, or both."
      },
      {
        "question": "Confirm supported commercial models: fixed subscription, usage billing, seat billing, or mixed billing."
      },
      {
        "question": "Confirm whether payment method authorization/mandate and recurring deduction retry policy are in first-release scope."
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
    "taxonomy_candidate_terms": [
      {
        "reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.",
        "term": "mandate"
      },
      {
        "reason": "Analyzer surfaced term, but requirements taxonomy does not currently register it as an aggregate root.",
        "term": "usage_event"
      }
    ]
  },
  "status": "intake",
  "user_stories": []
}
```
<!-- requirements-case-data:end -->
