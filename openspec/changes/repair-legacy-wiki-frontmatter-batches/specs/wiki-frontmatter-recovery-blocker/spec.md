# wiki-frontmatter-recovery-blocker Specification

## MODIFIED Requirements

### Requirement: Recovery blocker repair SHALL use explicit frontmatter batches

The system SHALL provide a bounded repair workflow for strict frontmatter gate
blockers that operates on explicit page batches rather than blind whole-repo
migration.

#### Scenario: Planner builds a repair batch

- **GIVEN** a full frontmatter precheck JSON report
- **WHEN** the repair planner is run with a batch limit
- **THEN** it SHALL group blockers by path
- **AND** include repair hints for each selected target
- **AND** mark pages without sufficient evidence as review-needed

#### Scenario: Apply modifies only approved frontmatter fields

- **GIVEN** an approved repair batch
- **WHEN** the apply command runs
- **THEN** it SHALL write only frontmatter fields in the approved batch
- **AND** SHALL NOT write relation fields
- **AND** SHALL NOT modify taxonomy config, MOC pages, ADR decisions, or
  OpenSpec lifecycle state

#### Scenario: Legacy batches preserve residual blocker accounting

- **GIVEN** repository-wide frontmatter blockers remain
- **WHEN** a legacy repair batch is applied
- **THEN** the batch evidence SHALL include the pre-batch blocker count
- **AND** the post-batch residual blocker count
- **AND** SHALL NOT claim recovery or archive readiness unless the recovery
  workflow reports a clean next route
