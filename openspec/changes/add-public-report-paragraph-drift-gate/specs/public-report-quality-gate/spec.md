## ADDED Requirements

### Requirement: Public report gate SHALL anchor drafts with an article intent contract

The public report gate SHALL establish the reader-facing target before complex
drafting, scoring, Feishu sync, or review-ready claims.

#### Scenario: Complex reader-facing draft is prepared

- **WHEN** a reader-facing report, Feishu review draft, H5/share draft, or
  public material has reviewer-routing complexity signals, user-reported drift,
  or a required scorecard
- **THEN** the gate SHALL record an Article Intent Contract before drafting or
  scoring
- **AND** the contract SHALL identify the reader, reader decision or action,
  main line, non-goals, user-owned judgments, and agent-allowed operations

### Requirement: Public report gate SHALL provide section and paragraph drift diagnostics

The public report gate SHALL review sections and important paragraphs against
the article intent before review-ready claims.

#### Scenario: Draft sections are reviewed for drift

- **WHEN** a complex or drift-corrected reader-facing draft is reviewed
- **THEN** the gate SHALL record a Section And Paragraph Drift Review
- **AND** the review SHALL include section objective, paragraph claim, mainline
  role, target fit score, narrative drift score, evidence fit score, judgment
  source, and action
- **AND** the action SHALL be one of retain, compress, rewrite, delete, or ask
  the user

#### Scenario: Paragraph changes article judgment

- **WHEN** a paragraph changes the article's main line, conclusion,
  prioritization, or public stance without source support or user confirmation
- **THEN** the Paragraph Drift Gate SHALL fail
- **AND** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

### Requirement: Public report gate SHALL preserve user judgment ownership

The public report gate SHALL treat user-owned thought and judgment as separate
from delegable writing process.

#### Scenario: Agent makes an unsourced public judgment

- **WHEN** the agent turns source material, reference examples, or smooth prose
  into a local strategic conclusion, priority, proof-strength claim, or public
  stance that the user has not confirmed
- **THEN** the Judgment Ownership Gate SHALL fail
- **AND** the gate-review artifact SHALL identify the judgment source as user,
  source material, agent inference, or unknown

#### Scenario: Hard gate fails but diagnostics are useful

- **WHEN** Paragraph Drift Gate or Judgment Ownership Gate fails
- **THEN** the overall scorecard SHALL remain `INVALID`
- **AND** the gate MAY still record diagnostic 0-5 drift scores and required
  repair actions for sections or paragraphs
