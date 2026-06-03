# Design

## Scope

This change replaces the requirements taxonomy data model with a DDD context
model. It is a standards and configuration change with a structural validator.
It does not change the current requirements readiness gate or req-agent runtime
behavior.

## Model Layers

- `business_ecosystem`: broad ecosystem such as `payment_ecosystem`.
- `subdomain`: stable business problem space inside an ecosystem.
- `bounded_context`: model boundary with consistent language, aggregate
  lifecycle, rules, and fact ownership.
- `aggregate_root`: object that owns lifecycle and consistency rules.
- `context_map`: command, event, policy decision, query, report, or evidence
  handoff between contexts.
- `role_obligation`: fact-owner role required because a context, aggregate,
  handoff, or trigger rule is present.
- `candidate_subdomain` and `candidate_context`: proposed model extensions when
  existing skeleton cannot explain a requirement.

## Ecosystem Skeleton

The first model includes `payment_ecosystem` and adjacent
`agent_service_ecosystem`.

`payment_ecosystem` subdomains:

- `merchant_platform_relationship`
- `billing_revenue`
- `payment_transaction`
- `account_balance`
- `funds_movement_settlement`
- `financial_operations`
- `risk_compliance`
- `embedded_financial_products`

`agent_service_ecosystem` subdomains:

- `agent_entitlement`
- `agent_usage_metering`
- `agent_workspace_seat`
- `agent_service_catalog`
- `agent_service_delivery`

## Disambiguation

High-conflict terms are context-specific language, not global objects. The model
must disambiguate terms such as `subscription`, `account`, `settlement`,
`payment`, `balance`, `merchant`, `entitlement`, `invoice`, and `refund`.

## Trigger Rules

`real_funds_processing=true` requires:

- `account_balance`
- `balance_ledger_context`
- `funds_account_owner`
- `ledger_owner`
- `balance_state_owner`

`paid_agent_service_access=true` requires:

- `agent_service_ecosystem`
- `agent_entitlement_context`

`recurring_payment=true` requires:

- `mandate_authorization_context`

## Proof Boundary

This change proves the DDD model exists in taxonomy and passes structural
validation. It does not prove old readiness checker compatibility and does not
prove runtime req-agent output changes.
