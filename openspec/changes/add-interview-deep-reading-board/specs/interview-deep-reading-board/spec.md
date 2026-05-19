# interview-deep-reading-board Specification

## ADDED Requirements

### Requirement: Repository SHALL provide an interview deep-reading board skill

The repository SHALL provide a repo-local skill for interview, podcast
transcript, dialogue, and Q&A deep-reading workflows that are at risk of being
compressed into ordinary summaries or decorative word clouds.

#### Scenario: User asks for compression-sensitive interview reading output

- **WHEN** the source is interview-like
- **AND** the user asks for deep reading, word cloud, timeline, temperature
  axis, draggable evidence, H5 exploration, or full-text coverage without
  compression
- **THEN** the system SHALL route through `interview-deep-reading-board`
- **AND** the system SHALL ask whether to create a full-window interview
  reading board before building the output

#### Scenario: User reports an interview output dropped a passage

- **WHEN** the user identifies a missing or compressed interview passage
- **THEN** the system SHALL preserve that passage as an explicit reading window
  or window group in the repaired output plan
- **AND** the system SHALL NOT hide the passage under generic keywords

### Requirement: Interview reading board SHALL preserve source-order evidence

The interview reading-board workflow SHALL treat source-order windows as the
primary content unit.

#### Scenario: Word cloud is included

- **WHEN** an interview reading-board output includes a word cloud
- **THEN** the word cloud SHALL act as an index into ordered windows and
  evidence
- **AND** the word cloud SHALL NOT replace the reading-window structure

#### Scenario: Temperature axis is included

- **WHEN** an interview reading-board output includes a temperature axis
- **THEN** the temperature axis SHALL function as a horizontal reading control
  connected to windows, timeline position, keywords, and evidence
- **AND** the temperature axis SHALL NOT be decorative filtering alone

#### Scenario: Copyrighted source material is used

- **WHEN** the source interview is copyrighted or otherwise not owned by the
  repository
- **THEN** the workflow SHALL preserve coverage through source position,
  paraphrase, and short evidence snippets
- **AND** it SHALL NOT store the full interview transcript verbatim as the
  reference or example body

### Requirement: Interview H5 output shape SHALL be available as reference

The repository SHALL preserve the Li Xiang interview H5 shape as a reusable
reference/example for future interview reading-board work.

#### Scenario: Future agent needs output-shape guidance

- **WHEN** a future agent needs to build or review an interview reading-board
  H5
- **THEN** the system SHALL expose an H5 output-shape reference under
  `.codex/skills/interview-deep-reading-board/references/`
- **AND** it SHALL expose a validated wiki example linking the Li Xiang H5,
  data file, source note, and old word-cloud counterexample

#### Scenario: Old word-cloud artifact is referenced

- **WHEN** the old word-cloud artifact is used as evidence
- **THEN** the system SHALL treat it as a counterexample for compression risk
- **AND** it SHALL NOT treat it as the recommended interview deep-reading
  output shape
