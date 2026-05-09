## ADDED Requirements

### Requirement: Public report gate SHALL separate local visual assets from Feishu image insertion

The public report gate SHALL treat local visual asset generation and Feishu
image insertion as separate delivery operations.

#### Scenario: User will add images manually

- **WHEN** a reader-facing report needs generated images or one-pagers
- **AND** the user says they will add images manually
- **THEN** the system SHALL generate or preserve local visual assets and asset
  paths
- **AND** SHALL NOT insert those images into Feishu
- **AND** MAY perform text-only Feishu sync when separately approved and gates
  pass

#### Scenario: Feishu sync is approved but image insertion is not explicit

- **WHEN** a reader-facing draft has local visual assets
- **AND** the user approves Feishu sync without explicitly approving image
  insertion
- **THEN** the system SHALL treat the Feishu operation as text-only
- **AND** SHALL record local asset paths or manual-image instructions instead
  of inserting image blocks

#### Scenario: User explicitly asks the agent to insert Feishu images

- **WHEN** the user explicitly asks the agent to insert generated images into a
  Feishu document
- **THEN** the system SHALL state the known client-freeze risk
- **AND** SHALL get explicit approval for the image-insertion operation
- **AND** SHALL record image tokens and read-back logs as audit evidence only,
  not as proof of client usability

#### Scenario: Image-bearing Feishu document freezes a client

- **WHEN** Codex, Feishu, or the user reports a freeze on an image-bearing
  Feishu document
- **THEN** the system SHALL stop further image-included Feishu writes for the
  current work
- **AND** SHALL switch to text-only sync, local asset paths, or a separately
  approved client-safe image workflow before any further delivery claim
