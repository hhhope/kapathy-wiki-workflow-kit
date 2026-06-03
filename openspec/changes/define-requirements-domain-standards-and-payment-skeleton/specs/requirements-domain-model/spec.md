## ADDED Requirements

### Requirement: Requirements Domain Definition

The requirements workflow SHALL define a domain as a durable business problem
space with stable language, core objects, lifecycle, rules, factual ownership,
and collaboration boundaries.

#### Scenario: Feature name is not admitted as a domain

- **GIVEN** a candidate named `subscription_payments`
- **AND** the candidate describes a charging feature or case-specific payment
  mechanism
- **WHEN** the candidate is reviewed for top-level taxonomy admission
- **THEN** it SHALL NOT be admitted as a top-level domain until it can express
  its durable business problem, core objects, lifecycle, rules, owner, and
  neighboring boundaries.

### Requirement: Strategic DDD Basis

The requirements workflow SHALL use strategic DDD concepts as the basis for
domain admission: bounded context, ubiquitous language, core object lifecycle,
domain rules, and context-map relationships.

#### Scenario: Capability stays inside a domain

- **GIVEN** a candidate capability named `dunning`
- **WHEN** it is reviewed against the DDD domain standard
- **THEN** it SHALL be treated as a capability inside `billing_revenue` unless
  it independently owns a durable business problem, lifecycle, rules, and
  collaboration boundary.

### Requirement: Taxonomy Admission Classification

The requirements workflow SHALL classify each taxonomy candidate as one of:
top-level domain, subdomain, capability, case slug, system/process name, alias,
or rejected non-domain.

#### Scenario: System or process name is not admitted as top-level domain

- **GIVEN** a candidate named `clearing_reconciliation`
- **AND** the candidate describes an operational process spanning evidence,
  matching, exception handling, and reporting
- **WHEN** it is reviewed for top-level taxonomy admission
- **THEN** it SHALL NOT be admitted only because the function exists.
- **AND** it SHALL be mapped to the owning domain or domains that carry the
  business objects, lifecycle, rules, and fact ownership.

### Requirement: Payment Domain Skeleton

The requirements taxonomy SHALL include a first runnable payment-domain skeleton
covering merchant/platform relationship, payment transaction, billing/revenue,
account/balance, funds movement/settlement, financial operations, risk/compliance,
and embedded financial products.

#### Scenario: Skeleton values are available for requirements intake

- **GIVEN** a payment ecosystem requirement
- **WHEN** the requirements taxonomy is used to classify its domain
- **THEN** the taxonomy SHALL provide explicit domain IDs for
  `merchant_platform_relationship`, `payment_transaction`, `billing_revenue`,
  `account_balance`, `funds_movement_settlement`, `financial_operations`,
  `risk_compliance`, and `embedded_financial_products`.

### Requirement: Existing Taxonomy Compatibility

The requirements taxonomy SHALL preserve current `account`, `settlement`, and
`clearing` domain IDs while the first payment-domain skeleton is introduced.

#### Scenario: Existing domain values remain mappable

- **GIVEN** an existing requirement classified as `account`, `settlement`, or
  `clearing`
- **WHEN** the new payment-domain skeleton is reviewed
- **THEN** the existing classification SHALL remain valid for compatibility.
- **AND** the design SHALL document how those values map toward
  `account_balance`, `funds_movement_settlement`, and `financial_operations`.

### Requirement: Domain Collaboration Relationships

The requirements domain standard SHALL describe how accepted domains collaborate
through upstream/downstream boundaries, shared language, handoff artifacts, role
participation points, and factual ownership.

#### Scenario: Cross-domain subscription payment case is routed by primary domain

- **GIVEN** an Agent subscription payment requirement that includes subscription
  plan rules, payment retries, payment method charging, and platform settlement
- **WHEN** the requirement is mapped by domain
- **THEN** `billing_revenue` SHALL be the primary domain for pricing,
  subscription lifecycle, usage or seat billing, invoice, dunning, grace-period,
  retention, and revenue-recovery rules.
- **AND** related payment, merchant/platform, account/balance, funds
  movement/settlement, financial operations, and risk/compliance domains SHALL
  be represented as collaborating domains instead of being collapsed into the
  primary domain.

### Requirement: Compounding Domain Assets

The requirements domain standard SHALL treat domain outputs as compounding
assets for human-Agent collaboration rather than one-off classification labels.

#### Scenario: Domain review leaves reusable knowledge

- **GIVEN** a new requirements case introduces or challenges a domain boundary
- **WHEN** the boundary is reviewed
- **THEN** the review SHALL preserve reusable domain knowledge such as accepted
  language, rejected aliases, lifecycle rules, owner boundaries, collaboration
  points, and open questions for future cases.
