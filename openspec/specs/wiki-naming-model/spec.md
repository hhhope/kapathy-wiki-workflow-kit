## Purpose

Define a repository naming model for evolution-bearing pages so agents can read
stable object identity separately from artifact type across covered layers.

## Requirements

### Requirement: Repository SHALL define a canonical object naming model for evolution-bearing layers

The repository SHALL define a naming model for workflow-evolution pages that separates
object identity from artifact type.

#### Scenario: New covered-layer page is created

- **WHEN** a new page is created in `wiki/ops`, `wiki/adr`, `openspec/specs`, or `wiki/examples`
- **THEN** the page SHALL follow the repository's `canonical object / artifact type` naming model

### Requirement: Repository SHALL admit canonical objects only when they unify a real evolution chain

The repository SHALL only treat a topic as a canonical object when it is stable
enough to unify multiple related artifacts across layers.

#### Scenario: Temporary symptom is proposed as an object

- **WHEN** a candidate name mainly describes a temporary symptom, local gap, or one-time event
- **THEN** the repository SHALL reject it as a canonical object

#### Scenario: Stable object spans multiple layers

- **WHEN** a candidate name is non-event-like, appears across at least two artifact layers, and can unify a real evolution chain
- **THEN** the repository SHALL allow it as a canonical object

### Requirement: Repository SHALL keep canonical object names consistent across covered layers

The repository SHALL reuse the same canonical object name across `ops`, `ADR`,
`spec`, and `example` layers for the same object family.

#### Scenario: Object appears across layers

- **WHEN** the same object family appears in multiple covered layers
- **THEN** the repository SHALL preserve one canonical object name instead of renaming it per layer

### Requirement: Repository SHALL treat dates, statuses, and symptom phrasing as metadata rather than title core

The repository SHALL keep title cores focused on object identity and artifact type,
and SHALL push local state details out of the primary title model.

#### Scenario: Page title proposal includes local state details

- **WHEN** a page title proposal includes dates, validation-round wording, status words, or local symptom phrasing
- **THEN** the repository SHALL treat those details as metadata rather than title core

### Requirement: Repository SHALL roll out the naming model strongly for new pages and weakly for existing pages

The repository SHALL stop new naming drift without forcing immediate full-repository migration.

#### Scenario: Existing covered-layer page predates the model

- **WHEN** an existing page predates the naming model
- **THEN** the repository MAY keep it unchanged until that page is intentionally touched or migrated

#### Scenario: New covered-layer page is added after model adoption

- **WHEN** a new page is added after model adoption
- **THEN** the repository SHALL require the new page to follow the naming model
