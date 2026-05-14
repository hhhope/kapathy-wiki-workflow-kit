## Purpose

Define the repository's LLM-WIKI self-evolution lifecycle as a medical loop while
preserving review, write, verification, and archive boundaries.

## ADDED Requirements

### Requirement: Repository SHALL define the LLM-WIKI medical loop

The repository SHALL define LLM-WIKI self-evolution as a staged lifecycle:
`checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive`.

#### Scenario: Future agent explains self-evolution stages

- **WHEN** a future agent needs to describe the LLM-WIKI self-evolution process
- **THEN** it SHALL use the medical-loop lifecycle vocabulary
- **AND** it SHALL preserve each stage as a distinct responsibility.

### Requirement: Repository SHALL separate diagnosis, confirmation, write, proof, and archive

The repository SHALL preserve the boundary that doctor diagnoses, review
confirms, treatment or surgery writes, recovery proves, and archive preserves.

#### Scenario: Doctor output exists

- **WHEN** a doctor diagnosis record exists
- **THEN** the repository SHALL treat it as diagnosis evidence only
- **AND** it SHALL NOT treat diagnosis as approval for frontmatter, taxonomy,
  relation, MOC, ADR, AGENTS, skill, or OpenSpec mutation.

#### Scenario: Repair is requested from diagnosis output

- **WHEN** a repair request is based on doctor findings
- **THEN** the repository SHALL require a human review decision or a later
  scoped OpenSpec change before write-capable workflows execute.

### Requirement: Repository SHALL define artifact expectations for each stage

The repository SHALL expect repo-visible artifacts at each lifecycle stage so
important state does not live only in stdout or chat.

#### Scenario: Lifecycle stage is discussed

- **WHEN** checkup, doctor, review, treatment, surgery, recovery, or archive is
  discussed as a repository workflow stage
- **THEN** the repository SHALL identify the repo-visible artifact class for that
  stage
- **AND** it SHALL preserve proof and approval boundaries in that artifact.

### Requirement: Repository SHALL route broad or governance-sensitive repair to surgery planning

The repository SHALL classify large, structural, or governance-sensitive repair
as surgery planning rather than treatment.

#### Scenario: Doctor output includes structural or governance risk

- **WHEN** doctor output includes broad batch writes, relation rebuilding, MOC
  projection writes, ADR or governance pages, OpenSpec-required findings,
  high-volume weak relation evidence, drift traces, or repository behavior
  changes
- **THEN** the repository SHALL classify the case as a surgery candidate
- **AND** it SHALL NOT execute the repair as ordinary treatment.

### Requirement: Repository SHALL keep later workflow capabilities out of this change

This change SHALL NOT create write-capable treatment, surgery, recovery, or
review-decision workflows.

#### Scenario: The medical loop is formalized

- **WHEN** this change is complete
- **THEN** no new skill, command, script, frontmatter write, relation write, MOC
  write, ADR mutation, AGENTS mutation, or OpenSpec archive mutation SHALL be
  introduced by this change.
