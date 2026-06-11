# product-discovery-wiki-capture Specification

## ADDED Requirements

### Requirement: Repository SHALL route durable product-discovery analysis to wiki capture

The repository SHALL provide a repo-local route for PM/product-discovery
analysis that the user expects to preserve as repository memory.

#### Scenario: Product-discovery analysis has explicit wiki intent

- **WHEN** the user invokes PM/product-discovery style work and asks to record,
  capture, or write the result to wiki
- **THEN** the system SHALL route through a repo-local product-discovery wiki
  capture skill
- **AND** the system SHALL create or update a wiki record instead of leaving the
  discovery output only in chat

#### Scenario: Prior product-discovery output is corrected as missing wiki capture

- **WHEN** a PM/product-discovery analysis has just been produced and the user
  says the skill should record wiki output or asks to remodel that behavior
- **THEN** the system SHALL treat the request as workflow repair
- **AND** the repair SHALL be scoped through OpenSpec before semantic skill or
  routing edits

### Requirement: Product-discovery wiki capture SHALL stay bounded

Product-discovery wiki capture SHALL preserve parent gates and avoid turning all
PM analysis into durable wiki records.

#### Scenario: Product-discovery answer is one-off

- **WHEN** the user asks a quick product-discovery, market framing, or PM
  analysis question without wiki, durable-memory, reuse, or follow-up intent
- **THEN** the system SHALL NOT create durable wiki output by default

#### Scenario: Product-discovery work uses external source learning

- **WHEN** the product-discovery work is grounded in external articles, repos,
  papers, READMEs, or examples
- **THEN** `learning-capture` SHALL remain the parent gate for source learning
- **AND** product-discovery wiki capture SHALL NOT replace source grounding or
  promotion evidence

#### Scenario: Product-discovery output becomes reader-facing

- **WHEN** the captured product-discovery output is prepared as a reader-facing
  report, Feishu draft, H5, share page, README, docs, examples, or published
  template
- **THEN** the applicable public or reader-facing output gate SHALL still apply
