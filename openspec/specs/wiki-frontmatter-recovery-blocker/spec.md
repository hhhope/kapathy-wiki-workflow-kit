# wiki-frontmatter-recovery-blocker Specification

## Purpose
Define the bounded repair and recovery-reporting contract for wiki
frontmatter blockers, so medical-loop recovery can distinguish clean treatment
targets from remaining repository-wide frontmatter debt.

## Requirements
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

### Requirement: Recovery SHALL separate target cleanliness from repository debt

Medical-loop recovery SHALL report treatment-target frontmatter status
separately from whole-repository strict gate status.

#### Scenario: Treatment targets are clean but repository debt remains

- **GIVEN** all treatment target pages pass target-level frontmatter precheck
- **AND** the whole-wiki strict gate still has unrelated blockers
- **WHEN** recovery records the result
- **THEN** it SHALL preserve target-level pass evidence
- **AND** report repository-wide blockers as residual debt
- **AND** keep the next action blocked until the residual debt is resolved or
  explicitly routed to a separate change

### Requirement: Repair evidence SHALL include before and after target checks

Each applied batch SHALL include target-level precheck evidence before and after
the frontmatter update.

#### Scenario: Page is repaired

- **GIVEN** a target page selected for repair
- **WHEN** the repair is applied
- **THEN** the evidence SHALL include the pre-repair target precheck result
- **AND** the post-repair target precheck result
- **AND** a residual whole-wiki precheck summary
