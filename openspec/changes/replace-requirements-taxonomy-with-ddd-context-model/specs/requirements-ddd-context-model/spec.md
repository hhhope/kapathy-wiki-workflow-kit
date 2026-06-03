## ADDED Requirements

### Requirement: Requirements Taxonomy Uses DDD Context Model

The requirements taxonomy SHALL use a DDD context model instead of a flat
domain/role vocabulary as the authoritative model for new requirement domain
analysis.

#### Scenario: Taxonomy exposes DDD model roots

- **GIVEN** `requirements/config/requirements-taxonomy.yaml`
- **WHEN** the taxonomy is loaded
- **THEN** it SHALL include `business_ecosystems`, `subdomains`,
  `bounded_contexts`, `role_archetypes`, `context_map`,
  `case_classification`, `candidate_evolution`, and `readiness_gate_model`.

### Requirement: Payment Ecosystem Skeleton

The requirements taxonomy SHALL define the first `payment_ecosystem` skeleton
with stable subdomains for merchant/platform relationship, billing/revenue,
payment transaction, account/balance, funds movement/settlement, financial
operations, risk/compliance, and embedded financial products.

#### Scenario: Payment subdomains are explicit

- **GIVEN** the DDD taxonomy model
- **WHEN** `payment_ecosystem` is inspected
- **THEN** it SHALL include `merchant_platform_relationship`,
  `billing_revenue`, `payment_transaction`, `account_balance`,
  `funds_movement_settlement`, `financial_operations`, `risk_compliance`, and
  `embedded_financial_products`.

### Requirement: Agent Service Ecosystem Is Adjacent

The requirements taxonomy SHALL define `agent_service_ecosystem` as an adjacent
ecosystem for Agent entitlement, usage metering, workspace seats, service
catalog, and service delivery.

#### Scenario: Agent entitlement is not absorbed by payment

- **GIVEN** a paid Agent service requirement
- **WHEN** service access is controlled by payment or subscription state
- **THEN** the model SHALL map access control to
  `agent_service_ecosystem.agent_entitlement_context`.
- **AND** it SHALL NOT treat service access entitlement as a payment subdomain.

### Requirement: High-Conflict Terms Are Context-Specific

The requirements taxonomy SHALL treat high-conflict business terms as
context-specific language instead of globally shared objects.

#### Scenario: Subscription is disambiguated

- **GIVEN** a requirement mentions subscription
- **WHEN** the model maps the term
- **THEN** merchant subscription offering, commercial subscription, and Agent
  entitlement SHALL be represented in separate contexts.

### Requirement: Real Funds Processing Requires Account Balance

The requirements taxonomy SHALL encode a trigger rule that real funds processing
requires account/balance contexts and funds/ledger ownership.

#### Scenario: Real funds processing is in scope

- **GIVEN** `real_funds_processing=true`
- **WHEN** the case is mapped
- **THEN** `account_balance` and `balance_ledger_context` SHALL be required.
- **AND** `funds_account_owner`, `ledger_owner`, and `balance_state_owner` SHALL
  be required role obligations.

### Requirement: Candidate Evolution Is Explicit

The requirements taxonomy SHALL allow requirements to propose candidate
subdomains or bounded contexts only when existing skeletons cannot explain the
case.

#### Scenario: New term does not immediately become taxonomy

- **GIVEN** a requirement introduces a new business term
- **WHEN** existing subdomains or contexts cannot explain it
- **THEN** the model SHALL keep the item as `candidate_subdomain` or
  `candidate_context`.
- **AND** promotion SHALL require business problem, ubiquitous language,
  aggregate roots, lifecycle, invariants, fact owners, context map, and why
  existing contexts do not fit.
