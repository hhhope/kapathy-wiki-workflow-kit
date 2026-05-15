## Purpose

Define a canonical case-file model for LLM-WIKI medical-loop records so stage
records remain evidence instead of competing sources of truth.

## ADDED Requirements

### Requirement: Medical loop SHALL preserve one canonical case file per case

The repository SHALL provide one canonical case file as the primary review
surface for a medical-loop run.

#### Scenario: A new medical-loop case is opened

- **WHEN** doctor and confirmation evidence exist for a medical-loop run
- **THEN** the repository SHALL be able to create or update one case file under
  `wiki/ops/wiki-medical-cases/`
- **AND** the case file SHALL include sections for diagnosis, confirmed
  decisions, treatment, surgery plan, recovery, archive or next action,
  evidence attachments, and proof boundary
- **AND** pending stages SHALL remain visible as pending sections.

### Requirement: Stage records SHALL be evidence attachments

Generated doctor, confirm, treatment, surgery, and recovery records SHALL be
linked as evidence attachments, not treated as replacement authority.

#### Scenario: A stage record is generated

- **WHEN** a stage writes a generated record
- **THEN** the case file SHALL link the generated record as evidence
- **AND** the generated record SHALL NOT silently override confirmed case
  decisions
- **AND** any new decision or changed routing SHALL be represented in the case
  file or a successor case.

### Requirement: Surgery planning SHALL derive from confirmed case decisions

Surgery planning SHALL use confirmed decisions as its source, not raw script
output alone.

#### Scenario: Surgery plan is prepared

- **WHEN** a surgery plan is generated for a medical-loop case
- **THEN** the plan SHALL cite the confirmed decision source it derives from
- **AND** it SHALL separate relation evidence review from governance,
  ADR, taxonomy, MOC, and OpenSpec-sensitive work
- **AND** it SHALL NOT write frontmatter, relation fields, taxonomy config,
  MOC files, ADRs, AGENTS, skills, or OpenSpec lifecycle state.

### Requirement: Human review SHALL target case decisions first

The repository SHALL make the human review target explicit.

#### Scenario: A human reviews a surgery-ready case

- **WHEN** the case contains surgery candidates
- **THEN** the human SHALL review the case file's confirmed decisions first
- **AND** the surgery plan SHALL be reviewed as a fidelity check against those
  confirmed decisions
- **AND** the repository SHALL NOT ask the human to treat a regenerated surgery
  record as an independent diagnosis.
