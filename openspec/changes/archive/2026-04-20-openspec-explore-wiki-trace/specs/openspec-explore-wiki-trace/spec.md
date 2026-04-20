## ADDED Requirements

### Requirement: Repository SHALL create an ops trace before continuing `openspec-explore`
When a user triggers `openspec-explore` in this repository, the system SHALL first ensure there is a repo-visible trace under `wiki/ops/` before continuing the exploration.

#### Scenario: New exploration topic starts
- **WHEN** the user starts `openspec-explore` on a topic that does not yet have a corresponding `wiki/ops/` trace
- **THEN** the repository SHALL create a lightweight explore trace under `wiki/ops/`
- **AND** the exploration SHALL continue only after that trace exists

#### Scenario: Same exploration topic continues
- **WHEN** the user continues exploring the same topic
- **THEN** the repository SHALL update the existing `wiki/ops/` explore trace instead of creating a duplicate page

### Requirement: Explore traces SHALL reuse the intake container
The repository SHALL model explore traces using the existing `intake` container rather than inventing a separate page type.

#### Scenario: Explore trace is created
- **WHEN** a repo-visible explore trace is created
- **THEN** it SHALL use the `type: intake` structure
- **AND** it SHALL include an explicit explore marker and lightweight fields for trigger, focus, hypotheses, open questions, and next step

### Requirement: Explore traces SHALL stay distinct from formal OpenSpec artifacts
The repository SHALL distinguish opening exploration traces from formal implementation artifacts.

#### Scenario: Exploration later becomes a formal change
- **WHEN** an explored topic later turns into a formal OpenSpec change
- **THEN** the `wiki/ops/` explore trace SHALL remain the opening context
- **AND** `proposal.md`, `design.md`, and `tasks.md` SHALL remain the formal scope and progress source of truth
