## ADDED Requirements

### Requirement: Public report reviewer SHALL inspect paragraph drift before scoring

The manual public report reviewer SHALL inspect the actual draft structure
before assigning score evidence.

#### Scenario: Reviewer handles complex reader-facing material

- **WHEN** reviewer routing is required for a public report, Feishu review
  draft, H5/share draft, or reference-shaped output
- **THEN** the reviewer SHALL run a reverse outline before score evidence
- **AND** the reviewer SHALL compare section objectives and paragraph claims
  against the Article Intent Contract

#### Scenario: Reviewer finds user-owned judgment drift

- **WHEN** a paragraph introduces a conclusion, priority, public stance, or
  proof-strength claim that is not sourced or user-confirmed
- **THEN** the reviewer SHALL mark judgment ownership as failed or needs-user
  confirmation
- **AND** the reviewer SHALL recommend retain, compress, rewrite, delete, or ask
  the user before scoring or sync-readiness decisions
