# learning-capture Specification

## Requirements

### Requirement: Learning capture SHALL classify learning level before deep work

`learning-capture` SHALL classify reusable learning requests into L0, L1, L2, or L3 before deep analysis when the request is non-trivial.

#### Scenario: User asks for ordinary source learning
- **WHEN** the user asks to learn reusable points from a normal article, repo, README, or example
- **THEN** the agent SHALL default to L1 unless stronger signals apply
- **AND** the output SHALL include reusable point and non-transfer boundary

#### Scenario: User asks for local adaptation or value judgment
- **WHEN** the source may affect local reports, skills, OpenSpec, AGENTS guidance, H5, PPT, Feishu review, or public artifacts
- **THEN** the agent SHALL route as at least L2
- **AND** the agent SHALL state method, input inventory, value judgment, and transfer boundary

#### Scenario: User asks for company path or long-horizon reconstruction
- **WHEN** the task involves company evolution, industry trend, future judgment, long timeline, multi-source evidence pool, or source queue
- **THEN** the agent SHALL route as L3
- **AND** the agent SHALL use research reconstruction, evidence matrix, and proof-boundary concepts

### Requirement: Learning capture SHALL classify learning type

`learning-capture` SHALL classify non-trivial learning as technical, business, company case, industry trend, output expression, or governance/agent workflow before selecting methods.

#### Scenario: Technical repo learning
- **WHEN** the user provides a GitHub repo and asks whether its approach helps local CR-agent work
- **THEN** the agent SHALL route as technical learning
- **AND** the agent SHALL distinguish architecture/tooling learning from code-quality claims

#### Scenario: Stripe-style company learning
- **WHEN** the user asks for Stripe-style company path research
- **THEN** the agent SHALL route as company-case L3 learning
- **AND** the agent SHALL use case study, process tracing, triangulation, evidence sufficiency, and source layering

### Requirement: L2 and L3 learning records SHALL use structured output contracts

L2 and L3 learning records SHALL include machine-checkable YAML fields for level, type, methods, input inventory, evidence, value judgment, and proof boundary.

#### Scenario: L3 record lacks proof boundary
- **WHEN** a L3 learning record has no proof boundary
- **THEN** the checker SHALL fail the record

### Requirement: Public writing transformation SHALL be separate from learning capture

Reader-facing articles, H5/share drafts, PPTs, and public reports SHALL use a writing transformation layer after learning capture.

#### Scenario: Research note is intended for H5 output
- **WHEN** the learning result will feed a reader-facing H5 or report
- **THEN** the output SHALL include article intent, reader path, thesis, evidence placement, claim-strength control, citation surface, and section drift review
