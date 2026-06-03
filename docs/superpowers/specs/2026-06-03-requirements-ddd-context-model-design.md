# Requirements DDD Context Model Design

## Purpose

Upgrade the requirements taxonomy from a flat domain/role vocabulary into a
DDD-informed, multi-dimensional model. The goal is not DDD purity. The goal is
to reduce requirement drift when humans and Agents collaborate on payment and
Agent-service requirements.

The current taxonomy can name payment subdomains, but it cannot represent
bounded contexts, aggregate roots, lifecycle rules, context handoffs, fact
owners, or role obligations. That gap caused the Agent subscription payment
draft to miss `account_balance` and the funds/ledger owners after the user
confirmed real funds processing.

## Confirmed Direction

Use a three-change rollout:

1. `replace-requirements-taxonomy-with-ddd-context-model`
   - Upgrade the DDD standard.
   - Replace the flat taxonomy model with the first DDD context model.
   - Define payment and Agent-service ecosystem skeletons.
   - Define role obligations and context map model.
   - Include the Agent subscription payment case mapping example.
2. `rewrite-requirements-readiness-gate-for-ddd-model`
   - Replace the old single-layer `domain + roles + stories + acceptance`
     readiness logic with Domain Model Gate and Requirement Delivery Gate.
3. `upgrade-req-agent-domain-analysis-for-ddd-contexts`
   - Update `req-domain-analysis` and `req-scope` outputs to use the DDD model.

This design covers only the first change. It does not implement checker or
req-agent behavior changes.

## DDD Model

Use these concepts consistently:

- `business_ecosystem`: the broad business ecosystem, such as
  `payment_ecosystem` or `agent_service_ecosystem`.
- `subdomain`: a stable business problem space inside an ecosystem, such as
  `billing_revenue` or `account_balance`.
- `bounded_context`: a model boundary where language, aggregate lifecycle,
  rules, and fact ownership stay consistent.
- `aggregate_root`: the core object that owns lifecycle and consistency rules
  inside a context.
- `lifecycle`: meaningful aggregate state changes.
- `invariant`: a rule that cannot be violated inside the context.
- `policy`: a rule that reacts to state changes or external facts.
- `command`: a request for another context to do something.
- `domain_event`: a confirmed business fact produced by a context.
- `evidence`: audit, reporting, or reconciliation artifact consumed by another
  context or role.
- `fact_owner`: the owner of a business fact, not merely a team label.
- `role_obligation`: a role required because a context, aggregate, handoff, or
  trigger rule is present.
- `context_map`: explicit cross-context interaction through commands, events,
  policy decisions, queries, reports, or evidence.
- `case_mapping`: mapping from one requirement case to ecosystems, subdomains,
  contexts, aggregates, owners, handoffs, and open questions.

## Taxonomy Shape

The new `requirements/config/requirements-taxonomy.yaml` should move to a DDD
graph-like structure:

```yaml
version: 2
authority: requirements-ddd-model

business_ecosystems: {}
subdomains: {}
bounded_contexts: {}
role_archetypes: {}
context_map: []
case_classification: {}
readiness_gate_model: {}
```

This is a replacement model, not a compatibility-first projection. Historical
case migration is out of scope for the first change.

## Payment Ecosystem Skeleton

`payment_ecosystem` is the primary business ecosystem for payment requirements.

Stable subdomains:

- `merchant_platform_relationship`
- `billing_revenue`
- `payment_transaction`
- `account_balance`
- `funds_movement_settlement`
- `financial_operations`
- `risk_compliance`
- `embedded_financial_products`

### merchant_platform_relationship

Business problem: identify service providers, platforms, collection subjects,
capability users, and responsibility boundaries.

Contexts:

- `merchant_identity_context`
- `merchant_onboarding_context`
- `merchant_capability_context`
- `merchant_service_offering_context`
- `platform_responsibility_context`

Aggregate roots:

- `merchant`
- `platform_account`
- `onboarding_application`
- `capability_grant`
- `service_offering`
- `platform_relationship`

Fact owners:

- `merchant_profile_owner`
- `onboarding_owner`
- `capability_owner`
- `platform_relationship_owner`
- `service_offering_owner`

Disambiguation:

- `merchant_account` is not `payment_account`.
- `subscription_offering` is not `commercial_subscription`.
- `platform_account` is not `account_balance`.

### billing_revenue

Business problem: commercial charging relationships, pricing, invoices, billing
cycles, receivables, and revenue recovery.

Contexts:

- `commercial_subscription_context`
- `billing_invoice_context`
- `usage_rating_context`
- `revenue_recovery_context`

Aggregate roots:

- `commercial_subscription`
- `subscription_item`
- `subscription_status`
- `invoice`
- `price_plan`
- `billing_schedule`
- `usage_record`
- `rating_rule`
- `seat_assignment`
- `dunning_case`
- `grace_period`
- `retry_schedule`

Fact owners:

- `subscription_owner`
- `subscription_policy_owner`
- `revenue_owner`
- `billing_ops_owner`
- `usage_rating_owner`
- `dunning_owner`

Disambiguation:

- `commercial_subscription` is the paid commercial relationship.
- `merchant_subscription_offering` belongs to
  `merchant_platform_relationship`.
- `agent_entitlement` belongs to `agent_service_ecosystem`.

### payment_transaction

Business problem: one payment intent, attempt, authorization, charge, refund,
dispute, and payment status convergence.

Contexts:

- `payment_intent_context`
- `payment_attempt_authorization_context`
- `refund_context`
- `dispute_context`
- `payment_method_context`

Aggregate roots:

- `payment_intent`
- `payment_attempt`
- `payment_order`
- `payment_method_authorization`
- `charge`
- `refund`
- `dispute_case`
- `channel_transaction`

Fact owners:

- `payment_ops_owner`
- `payment_method_owner`
- `channel_owner`
- `refund_owner`
- `dispute_owner`

Disambiguation:

- `payment_intent` is not `invoice`.
- `payment_attempt` is not subscription renewal.
- Charge success is not funds availability.
- Refund is not settlement reversal.

### account_balance

Business problem: real fund ownership, account capability, balance state, ledger
posting, available/pending/reserved funds, and consistency between fund state
and ledger facts.

Contexts:

- `financial_account_context`
- `balance_ledger_context`
- `fund_state_context`
- `reserve_limit_context`

Aggregate roots:

- `payment_account`
- `wallet`
- `balance`
- `ledger_entry`
- `fund_state`
- `reserve`
- `account_limit`
- `fund_reservation`

Fact owners:

- `funds_account_owner`
- `ledger_owner`
- `balance_state_owner`
- `reserve_owner`
- `finance_owner`

Trigger rule:

```text
real_funds_processing=true
=> account_balance required
=> balance_ledger_context required
=> funds_account_owner, ledger_owner, balance_state_owner required
```

Disambiguation:

- `account_balance` is not a wallet page.
- `ledger_entry` is not a financial report.
- Available balance is not payment success.

### funds_movement_settlement

Business problem: moving funds to recipients through transfer, payout, split,
settlement batch, and settlement schedule.

Contexts:

- `internal_transfer_context`
- `split_allocation_context`
- `settlement_batch_context`
- `payout_context`
- `payout_schedule_context`

Aggregate roots:

- `transfer`
- `split_rule`
- `allocation_result`
- `platform_fee`
- `settlement_batch`
- `settlement_item`
- `settlement_schedule`
- `payout`
- `payout_instruction`
- `payout_recipient`

Fact owners:

- `transfer_owner`
- `split_rule_owner`
- `platform_fee_owner`
- `settlement_owner`
- `payout_owner`

Disambiguation:

- `transfer` means platform/account internal movement.
- `payout` means movement to an external bank or card.
- `settlement` means settlement batch, schedule, or settlement accounting fact.
- `split` means allocation rule/result.

### financial_operations

Business problem: auditable financial evidence, reconciliation, fee accounting,
exception handling, reporting, and close support.

Contexts:

- `reconciliation_context`
- `fee_accounting_context`
- `financial_reporting_context`
- `exception_resolution_context`
- `close_support_context`

Aggregate roots:

- `reconciliation_record`
- `reconciliation_match`
- `reconciliation_exception`
- `fee_record`
- `fee_rule`
- `cost_allocation`
- `financial_report`
- `close_report`
- `audit_evidence`

Fact owners:

- `reconciliation_owner`
- `fee_accounting_owner`
- `financial_report_owner`
- `exception_owner`
- `audit_evidence_owner`

Disambiguation:

- Reconciliation is not `payment_transaction`.
- Reporting is not settlement.
- `clearing_reconciliation` is a process/capability, not a subdomain.

### risk_compliance

Business problem: admission, KYC/KYB, AML, recurring payment consent,
transaction risk, consumer protection, and compliance evidence.

Contexts:

- `compliance_profile_context`
- `risk_decision_context`
- `mandate_authorization_context`
- `transaction_monitoring_context`
- `compliance_review_context`

Aggregate roots:

- `kyb_profile`
- `kyc_profile`
- `aml_case`
- `risk_decision`
- `risk_signal`
- `risk_rule`
- `payment_mandate`
- `authorization_consent`
- `consent_record`
- `compliance_review`

Fact owners:

- `compliance_owner`
- `kyb_owner`
- `risk_owner`
- `mandate_owner`
- `monitoring_owner`

Disambiguation:

- `mandate` and `consent` answer whether recurring payment is allowed.
- Payment authorization answers whether one payment attempt is authorized.
- Risk decision answers whether an action is allowed.

### embedded_financial_products

Business problem: regulated financial products adjacent to payments, including
issuing, treasury, spend, and capital.

Contexts:

- `issuing_context`
- `treasury_context`
- `spend_management_context`
- `capital_context`

Aggregate roots:

- `card_account`
- `card`
- `authorization_control`
- `treasury_account`
- `cash_position`
- `spend_policy`
- `expense_transaction`
- `credit_offer`
- `repayment_schedule`
- `credit_account`

Fact owners:

- `issuing_owner`
- `treasury_owner`
- `spend_owner`
- `capital_owner`
- `regulated_product_owner`

Trigger rules:

```text
issuing_in_scope=true => embedded_financial_products required
treasury_in_scope=true => embedded_financial_products required
capital_in_scope=true => embedded_financial_products required
```

## Agent Service Ecosystem Skeleton

`agent_service_ecosystem` is an adjacent ecosystem for AI/Agent service
delivery. It prevents Agent product entitlement, usage, seats, and service
delivery from being incorrectly absorbed into the payment ecosystem.

Stable first-pass subdomains:

- `agent_entitlement`
- `agent_usage_metering`
- `agent_workspace_seat`
- `agent_service_catalog`
- `agent_service_delivery`

### agent_entitlement

Business problem: whether a customer can use an Agent service after commercial
subscription, payment, suspension, cancellation, or quota change.

Contexts:

- `agent_entitlement_context`

Aggregate roots:

- `agent_entitlement`
- `access_state`
- `usage_quota`
- `seat_permission`

Fact owners:

- `agent_entitlement_owner`
- `access_policy_owner`

### agent_usage_metering

Business problem: Agent consumption measurement for usage-based billing or
service controls.

Contexts:

- `agent_usage_metering_context`

Aggregate roots:

- `agent_usage_record`
- `metering_dimension`
- `usage_counter`

Fact owners:

- `agent_usage_owner`
- `metering_owner`

### agent_workspace_seat

Business problem: workspace seats, user assignment, and seat-based access for
Agent services.

Contexts:

- `agent_workspace_seat_context`

Aggregate roots:

- `workspace`
- `seat_assignment`
- `workspace_member`

Fact owners:

- `workspace_owner`
- `seat_owner`

### agent_service_catalog

Business problem: which Agent services, plans, and capabilities can be offered
to customers.

Contexts:

- `agent_service_catalog_context`

Aggregate roots:

- `agent_service`
- `agent_plan`
- `agent_capability`

Fact owners:

- `agent_service_owner`
- `agent_catalog_owner`

### agent_service_delivery

Business problem: service availability and delivery state for Agent services.

Contexts:

- `agent_service_delivery_context`

Aggregate roots:

- `service_session`
- `delivery_state`
- `service_incident`

Fact owners:

- `agent_delivery_owner`
- `service_state_owner`

## Context Map

Minimum context map for Agent service subscription payment:

```text
merchant_service_offering_context
  -> commercial_subscription_context
  event: SubscriptionOfferingPublished

commercial_subscription_context
  -> billing_invoice_context
  command: GenerateInvoice

billing_invoice_context
  -> payment_intent_context
  command: ChargeInvoice

payment_intent_context
  -> payment_attempt_authorization_context
  command: AuthorizeAndCapture

payment_attempt_authorization_context
  -> balance_ledger_context
  event: PaymentSucceeded / RefundSucceeded / ChargebackCreated

balance_ledger_context
  -> reconciliation_context
  evidence: LedgerEntryPosted / BalanceSnapshotGenerated

payment_attempt_authorization_context
  -> revenue_recovery_context
  event: PaymentFailed

risk_decision_context
  -> payment_attempt_authorization_context
  policy_decision: PaymentAllowed / PaymentBlocked

commercial_subscription_context
  -> agent_entitlement_context
  event: CommercialSubscriptionActivated / CommercialSubscriptionSuspended / CommercialSubscriptionCancelled
```

## Case Mapping Example

Case slug:

```text
agent-service-subscription-payments
```

Mapping:

```yaml
business_ecosystem: payment_ecosystem
adjacent_ecosystems:
  - agent_service_ecosystem

primary_subdomain: billing_revenue
primary_contexts:
  - commercial_subscription_context
  - billing_invoice_context
  - revenue_recovery_context

required_payment_subdomains:
  - merchant_platform_relationship
  - payment_transaction
  - account_balance
  - financial_operations
  - risk_compliance

required_payment_contexts:
  - merchant_identity_context
  - merchant_capability_context
  - merchant_service_offering_context
  - payment_intent_context
  - payment_attempt_authorization_context
  - balance_ledger_context
  - fund_state_context
  - reconciliation_context
  - risk_decision_context
  - mandate_authorization_context

conditional_payment_subdomains:
  - funds_movement_settlement

conditional_payment_contexts:
  - split_allocation_context
  - settlement_batch_context
  - payout_context

required_agent_service_contexts:
  - agent_entitlement_context

conditional_agent_service_contexts:
  - agent_usage_metering_context
  - agent_workspace_seat_context
```

Key trigger rules:

```text
real_funds_processing=true
=> account_balance and balance_ledger_context required

paid_agent_service_access=true
=> agent_service_ecosystem.agent_entitlement_context required

usage_based_billing=true
=> billing_revenue.usage_rating_context required
=> agent_service_ecosystem.agent_usage_metering_context required

seat_based_billing=true
=> billing_revenue.usage_rating_context required
=> agent_service_ecosystem.agent_workspace_seat_context required

merchant_settlement_in_scope=true
=> funds_movement_settlement.settlement_batch_context and payout_context required

split_settlement_in_scope=true
=> funds_movement_settlement.split_allocation_context required

recurring_payment=true
=> risk_compliance.mandate_authorization_context required
```

## Readiness Model

The first change defines the model only. The gate implementation comes later.

Future Domain Model Gate should require:

- `business_ecosystem`
- `primary_subdomain`
- `primary_contexts`
- `required_contexts`
- `aggregate_roots`
- `fact_owners`
- `role_obligations`
- `context_handoffs`
- `non_domain_terms`
- `open_questions`

Future Requirement Delivery Gate should require:

- roles derived from role obligations;
- user stories bound to role and aggregate lifecycle;
- acceptance functions covering state changes, handoffs, failure paths, and
  evidence.

## Explicit Non-Goals

- Do not update `check_requirements_case.py` in the first change.
- Do not update `req-agent` or `req-domain-analysis` runtime behavior in the
  first change.
- Do not migrate historical requirement cases.
- Do not archive existing OpenSpec changes.
- Do not publish a final Feishu version before this design is accepted and
  copied into OpenSpec.

## Prior-Art Basis

The skeleton is informed by:

- Stripe API resources around Subscriptions, Invoices, PaymentIntents, Accounts,
  Transfers, Payouts, and Balance Transactions.
- Adyen API resources around Checkout, Balance Platform, Legal Entities, and
  Transfers.
- Airwallex API resources around Connected Accounts, PaymentIntents,
  Subscriptions, Settlements, and Account Capabilities.

These sources are prior art signals, not direct taxonomy templates. Public API
navigation mixes product packaging, technical resources, and operational
workflows, so the local model uses DDD boundaries to reduce term conflicts.

## Self-Review

- No implementation is included.
- The first change scope is limited to standards and taxonomy model.
- Checker and req-agent behavior are explicitly deferred.
- `subscription` is disambiguated into merchant offering, commercial
  subscription, and Agent entitlement.
- `account` is disambiguated across merchant/platform, payment account, and
  ledger/balance facts.
