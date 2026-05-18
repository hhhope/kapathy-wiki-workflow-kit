## ADDED Requirements

### Requirement: Public report gate SHALL prevent tool executor bypass

The public report gate SHALL prevent delivery-sensitive reader-facing report
work from routing directly to low-level executors when a parent workflow owns
the output shape, review boundary, or evidence boundary.

#### Scenario: H5 visual request mentions image model

- **WHEN** a reader-facing H5 or report needs new visual assets
- **AND** the user mentions image-model output or another low-level image tool
- **THEN** the public report gate SHALL remain the parent route
- **AND** the workflow SHALL inspect existing visuals when they exist
- **AND** the workflow SHALL produce or reference an article-level visual plan
  and per-image scripts before bitmap generation
- **AND** bitmap generation SHALL be treated as the final executor, not the
  route owner

#### Scenario: Feishu write request follows report drafting

- **WHEN** a reader-facing report or review draft needs Feishu writing
- **THEN** Feishu writing SHALL be treated as an executor after the workflow
  has established draft readiness, judgment ownership, publish/sync approval,
  and the required post-write read-back boundary
- **AND** the Feishu tool SHALL NOT replace the workflow that owns readiness
  and evidence

#### Scenario: Research lookup follows source-learning work

- **WHEN** a source-learning or public-report task needs search or browser tools
- **THEN** search and browser tools SHALL be treated as executors under the
  workflow that owns source selection, citation boundary, and evidence
  classification
