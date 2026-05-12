# wiki-explore-command Specification

## Purpose
TBD - created by archiving change add-wiki-explore-depth-contract. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose a wiki explore depth skill

The repository SHALL provide a repo-local Codex skill named `wiki-explore` for
wiki-backed exploration threads that require evidence-depth judgment.

#### Scenario: User invokes wiki explore explicitly

- **WHEN** the user explicitly invokes `wiki:explore`
- **THEN** the system SHALL load the `wiki-explore` skill
- **AND** it SHALL identify the current wiki-backed object before answering
- **AND** it SHALL inspect repo-visible wiki/source/spec/skill evidence before
  making enoughness claims

#### Scenario: Ongoing wiki-backed exploration is rejected as not enough

- **WHEN** an ongoing wiki-backed exploration, source review, report repair, or
  governance replay is rejected as shallow, incomplete, off-target, or not
  enough
- **THEN** the system SHALL re-anchor through the `wiki-explore` output
  contract before continuing

### Requirement: Wiki explore SHALL produce an evidence-depth answer

The wiki explore skill SHALL report the evidence surface and enoughness
boundary instead of returning only a shallow summary.

#### Scenario: Wiki explore answer is produced

- **WHEN** the system answers under `wiki-explore`
- **THEN** the answer SHALL include the current object, opened evidence,
  evidence surface, enoughness judgment, and next boundary
- **AND** it SHALL identify missing source layers or proof boundaries when the
  topic is not deep enough for the requested use

#### Scenario: Public material is involved

- **WHEN** the explored topic depends on public or external material
- **THEN** the answer SHALL distinguish primary sources, secondary/media
  sources, candidate leads, transcript/upstream-capture gaps, and internal
  synthesis
- **AND** it SHALL NOT treat a source pool as public-ready proof by itself

### Requirement: Wiki explore SHALL preserve non-execution boundaries

Wiki explore SHALL be an exploration-depth surface, not an implementation or
OpenSpec lifecycle mutator.

#### Scenario: Wiki explore completes

- **WHEN** the wiki explore skill completes
- **THEN** it SHALL NOT create, modify, archive, or queue OpenSpec changes by
  itself
- **AND** it SHALL NOT mark tasks complete or execute queued work
- **AND** it MAY recommend a new OpenSpec change when behavior or default
  workflow needs to change

