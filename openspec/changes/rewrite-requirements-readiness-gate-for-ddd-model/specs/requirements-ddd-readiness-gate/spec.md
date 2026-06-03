## ADDED Requirements

### Requirement: Requirements Checker Supports DDD Taxonomy V2

The requirements checker SHALL read taxonomy v2 DDD roots when
`requirements/config/requirements-taxonomy.yaml` declares `version: 2`.

#### Scenario: V2 taxonomy is not treated as an unknown flat domain vocabulary

- **GIVEN** taxonomy v2 with `business_ecosystems`, `subdomains`,
  `bounded_contexts`, and `role_archetypes`
- **WHEN** the requirements checker evaluates a DDD-shaped case
- **THEN** it SHALL use the v2 roots for known ecosystem, context, and role
  validation.
- **AND** it SHALL NOT require legacy `domains` or `roles.vocabulary` roots.

### Requirement: Domain Model Gate Is Separate From Delivery Gate

The requirements checker SHALL expose separate domain model and requirement
delivery gate results before computing the final hard gate.

#### Scenario: Delivery evidence is present but domain model is incomplete

- **GIVEN** a case has confirmed role instances, user stories, and acceptance
  functions
- **WHEN** the case has no confirmed bounded contexts
- **THEN** the checker SHALL block with a domain-model blocker.
- **AND** the final hard gate SHALL fail even if delivery checks pass.

### Requirement: Strict DDD Cases Require Domain Model Evidence

Strict DDD cases SHALL require confirmed ecosystems, subdomains, bounded
contexts, aggregate roots, fact owners, role obligations, and context handoffs.

#### Scenario: DDD case is complete

- **GIVEN** a strict case declares confirmed `domain_model` evidence
- **WHEN** all referenced ecosystems, subdomains, contexts, and role
  obligations exist in taxonomy v2
- **THEN** `domain_model_gate.passed` SHALL be true.
- **AND** the final hard gate SHALL pass when requirement delivery evidence also
  passes.

### Requirement: Role Obligations Use Role Archetypes

Role obligations in a strict DDD case SHALL be validated against taxonomy v2
`role_archetypes`.

#### Scenario: Unknown role obligation is declared

- **GIVEN** a DDD case declares `role_obligations`
- **WHEN** one obligation is not in `role_archetypes`
- **THEN** the checker SHALL block with a role-obligation taxonomy blocker.

### Requirement: Legacy Compatibility Remains Explicit

The requirements checker SHALL keep a compatibility path for legacy case files
when compatibility mode is requested.

#### Scenario: Legacy case is checked in compatibility mode

- **GIVEN** an old case with `domain.confirmed` and legacy role/story fields
- **WHEN** the checker is called with `strict=False`
- **THEN** it SHALL remain readable.
- **AND** the report SHALL identify legacy compatibility mode rather than DDD
  domain-model readiness.
