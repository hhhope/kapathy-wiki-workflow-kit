## ADDED Requirements

### Requirement: Requirements Analysis Produces DDD Domain Model

The requirements analysis agent SHALL produce a DDD `domain_model` when
taxonomy v2 is active.

#### Scenario: Agent subscription payment material is analyzed

- **GIVEN** requirement material about Agent service subscription payments
- **WHEN** the analysis agent evaluates the material against taxonomy v2
- **THEN** the output SHALL include `domain_model.business_ecosystems` with
  `payment_ecosystem`.
- **AND** it SHALL include adjacent `agent_service_ecosystem` when service
  access is in scope.
- **AND** it SHALL include bounded contexts instead of only a flat domain id.

### Requirement: Real Actors Are Separate From Role Obligations

The requirements analysis agent SHALL keep real actors separate from DDD role
obligations.

#### Scenario: Subscription context creates obligations

- **GIVEN** material mentions paid subscriptions
- **WHEN** `commercial_subscription_context` is selected
- **THEN** `subscription_owner` MAY appear as a role obligation.
- **AND** it SHALL NOT be emitted as a first-line user-story actor unless the
  source explicitly names that actor.

### Requirement: Real Funds Processing Requires Account Balance

The requirements analysis agent SHALL derive account/balance obligations when
real funds processing is in scope.

#### Scenario: Real funds are processed

- **GIVEN** `real_funds_processing=true` or equivalent material evidence
- **WHEN** domain analysis is produced
- **THEN** `account_balance` and `balance_ledger_context` SHALL be included.
- **AND** `funds_account_owner`, `ledger_owner`, and `balance_state_owner` SHALL
  be included as role obligations.

### Requirement: Unknown Terms Remain Candidates

The requirements analysis agent SHALL not force unknown terms into existing DDD
taxonomy IDs.

#### Scenario: Material contains an unsupported domain term

- **GIVEN** requirement material contains a business term that cannot be mapped
  to existing ecosystems, subdomains, or bounded contexts
- **WHEN** the analysis agent runs
- **THEN** the term SHALL be preserved as a candidate or open question.
- **AND** it SHALL NOT become a formal taxonomy id.

### Requirement: Worker Guidance Uses Actor And Obligation Split

Req-agent worker guidance SHALL describe the split between actors and DDD role
obligations.

#### Scenario: Domain analysis hands off to scope

- **GIVEN** `req-domain-analysis` produces DDD contexts and role obligations
- **WHEN** handoff moves to `req-scope`
- **THEN** `req-scope` SHALL assign obligations to concrete owners or preserve
  open questions.
- **AND** it SHALL NOT treat role obligations as user-story actors by default.
