## ADDED Requirements

### Requirement: Req-Agent Domain Analysis Worker

The requirements workflow SHALL provide a repo-local `req-domain-analysis`
worker skill under `.codex/skills/req-domain-analysis/SKILL.md`.

#### Scenario: Domain analysis is available as a worker skill

- **GIVEN** a requirements case has been created or updated by intake
- **WHEN** the normal requirements flow needs domain classification
- **THEN** `req-agent` SHALL be able to route to `req-domain-analysis` as a
  bounded worker.

### Requirement: Domain Analysis Runs Before Scope

The normal `req-agent` worker route SHALL place `req-domain-analysis` after
`req-intake` and before `req-scope`.

#### Scenario: Intake output requires domain judgment

- **GIVEN** intake material mentions subscription payments, marketplace
  settlement, and channel behavior
- **WHEN** the next worker is selected
- **THEN** `req-agent` SHALL route to `req-domain-analysis` before `req-scope`
  handles roles, ownership, boundaries, and unknowns.

### Requirement: Domain Analysis Uses DDD Admission Standard

`req-domain-analysis` SHALL classify candidate terms using the repository's DDD
requirements-domain standard and active requirements taxonomy.

#### Scenario: Feature-like candidate is not forced into top-level taxonomy

- **GIVEN** a candidate term named `subscription_payments`
- **WHEN** `req-domain-analysis` evaluates the term
- **THEN** it SHALL classify the term as a capability, case slug, alias, or
  pending candidate unless it can form a durable top-level domain under the DDD
  admission standard.

### Requirement: Domain Analysis Preserves Parent Gate

`req-domain-analysis` SHALL remain a worker under `req-agent` and SHALL NOT
become an independent normal user-facing entry point.

#### Scenario: User asks for normal requirements intake

- **GIVEN** a user asks to analyze a new requirement
- **WHEN** the request is handled normally
- **THEN** the agent SHALL use `req-agent` as the entry point.
- **AND** direct `req-domain-analysis` use SHALL be limited to explicit debug or
  worker context.

### Requirement: Domain Analysis Does Not Mutate Taxonomy

`req-domain-analysis` SHALL NOT mutate requirements taxonomy, wiki taxonomy,
skills, AGENTS, or OpenSpec lifecycle state.

#### Scenario: Candidate domain is unknown

- **GIVEN** a requirement contains an unknown domain candidate
- **WHEN** `req-domain-analysis` cannot map it with sufficient confidence
- **THEN** the worker SHALL keep it as a pending candidate or open question.
- **AND** it SHALL NOT edit taxonomy or force the candidate into an existing
  domain ID.
