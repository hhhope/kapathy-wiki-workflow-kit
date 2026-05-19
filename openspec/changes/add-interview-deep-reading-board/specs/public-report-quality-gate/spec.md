# public-report-quality-gate Specification Delta

## ADDED Requirements

### Requirement: Public report gate SHALL delegate interview deep-reading H5 structure

The public report gate SHALL remain the outer gate for reader-facing interview
HTML, H5, share drafts, and report outputs while delegating interview-specific
reading-board structure to `interview-deep-reading-board`.

#### Scenario: Reader-facing interview H5 is requested

- **WHEN** the user asks to produce a reader-facing H5, HTML, share draft, or
  report from interview-like material
- **AND** the requested output includes deep reading, word cloud, timeline,
  temperature axis, draggable evidence, or no-compression/full-text-coverage
  language
- **THEN** the public report gate SHALL preserve its reader-facing blockers
- **AND** the workflow SHALL route interview-specific structure through
  `interview-deep-reading-board` before ordinary HTML or report production

#### Scenario: Interview module is used under the public gate

- **WHEN** `interview-deep-reading-board` is delegated from the public report
  gate
- **THEN** the interview module SHALL NOT replace Article Intent Contract,
  Reference Output Shape Gate, Learning Use Map, Judgment Ownership Gate,
  Visual Gate, Publish Gate, Feishu sync approval, or review-ready evidence
  requirements
