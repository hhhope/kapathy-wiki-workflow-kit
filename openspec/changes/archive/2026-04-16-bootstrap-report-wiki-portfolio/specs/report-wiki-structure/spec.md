## ADDED Requirements

### Requirement: Repository SHALL expose a report wiki entry structure
The repository SHALL define a project identity file and a wiki entry structure that make the report knowledge base usable without external context.

#### Scenario: Repository opens with a clear knowledge entry point
- **WHEN** a contributor opens the repository for the first time
- **THEN** the repository SHALL provide a project definition and a wiki index that explain purpose, navigation, and expected content structure

### Requirement: Wiki SHALL support multidimensional navigation
The wiki SHALL provide stable top-level navigation for business topic, report output, timeline, and source evidence so the same knowledge can be reached from multiple views.

#### Scenario: User navigates the same knowledge from different views
- **WHEN** a source-backed report item is created
- **THEN** the wiki SHALL allow it to be referenced from domain, report, and timeline indexes without duplicating the underlying content body

### Requirement: Durable pages SHALL use a shared metadata contract
Durable wiki pages SHALL store a shared metadata contract that supports later machine indexing and human maintenance.

#### Scenario: Metadata is available for indexing
- **WHEN** a durable wiki page is created from a template
- **THEN** the page SHALL include fields for title, type, domain, audience, period, status, and update tracking
