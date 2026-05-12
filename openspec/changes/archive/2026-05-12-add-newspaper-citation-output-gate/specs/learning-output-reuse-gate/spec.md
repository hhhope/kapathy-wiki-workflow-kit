## MODIFIED Requirements

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

#### Scenario: Newspaper output needs reader-visible citations

- **WHEN** a learning artifact shapes a newspaper-style H5, share package, or
  public newspaper draft
- **THEN** the output-use map SHALL remain internal process evidence
- **AND** the system SHALL separately identify whether the learned source also
  needs a reader-visible citation route for load-bearing claims, figures, or
  visual panels
- **AND** review-ready, publish, sync, or share claims SHALL NOT rely on the
  internal output-use map as a substitute for reader-visible citation surface
