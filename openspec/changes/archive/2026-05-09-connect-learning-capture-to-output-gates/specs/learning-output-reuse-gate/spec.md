## ADDED Requirements

### Requirement: Repository SHALL connect learning artifacts to reader-facing outputs

Reader-facing outputs that use external-source learning SHALL preserve a visible
handoff from learned artifact to output constraint.

#### Scenario: Reader-facing output uses learned references

- **WHEN** the user asks to write, rewrite, polish, sync, or prepare a
  reader-facing report, Feishu review draft, H5/share draft, or public material
  using previously learned articles, repositories, examples, or reference pages
- **THEN** the system SHALL identify applicable learning artifacts before
  drafting or claiming review-ready status
- **AND** it SHALL create or update a repo-visible output-use map

#### Scenario: Learning artifact is applied to output

- **WHEN** a learning point is used in the output process
- **THEN** the output-use map SHALL record the source artifact, source
  domain/topic, reusable capability type, learning point, and intended output
  use
- **AND** the intended output use SHALL point to a concrete section, visual,
  metric, evidence block, boundary statement, or other named output element

#### Scenario: Relevant learning artifact is not used

- **WHEN** an applicable learning point is considered but not used
- **THEN** the output-use map SHALL record a skip reason
- **AND** the system SHALL NOT silently discard the learning point while still
  claiming the output uses the learned reference

### Requirement: Learning capture SHALL distinguish source domain from reusable capability type

Learning capture SHALL avoid treating the source's topic as the same thing as
the reusable output capability learned from it.

#### Scenario: External source is captured as learning

- **WHEN** a learning artifact records a source takeaway for future reuse
- **THEN** it SHALL identify the source domain/topic when known
- **AND** it SHALL identify the reusable capability type when the takeaway is
  expected to affect future output

#### Scenario: Reusable capability type is recorded

- **WHEN** the system classifies what was learned for future output
- **THEN** it SHALL use explicit categories such as content, structure, visual,
  evidence, or boundary
- **AND** it SHALL NOT describe those categories as business domains

### Requirement: Learning-output reuse SHALL preserve promotion boundaries

Using a learning artifact in an output SHALL NOT by itself promote that learning
into a standing rule, spec, skill, or root instruction.

#### Scenario: Output use suggests a durable behavior rule

- **WHEN** an output-use map shows a learning point repeatedly shaping outputs
  and the user asks to turn it into a durable behavior asset
- **THEN** the promotion SHALL go through the repository evidence-backed
  promotion path or a scoped OpenSpec change
