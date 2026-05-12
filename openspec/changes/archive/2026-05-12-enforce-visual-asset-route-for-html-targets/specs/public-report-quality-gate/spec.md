## ADDED Requirements

### Requirement: Public report gate SHALL route HTML-target visual requests to visual assets first before HTML edits

The public report gate SHALL route reader-facing HTML report or H5 page requests
to visual asset work first when the request also asks for visual deliverables.
It SHALL NOT treat the HTML target path as permission to satisfy the request by
adding in-page H5 sections only.

#### Scenario: Existing HTML report asks for knowledge cards and a one-page infographic

- **WHEN** the user names an existing `.html` report or H5 page
- **AND** the request includes visual-deliverable wording such as `一图流`,
  `知识卡`, `章节配图`, `图片`, `生图`, `跑图`, or `图片模型`
- **THEN** the system SHALL stop before direct HTML body edits
- **AND** SHALL route first to visual package scripting, output-mode selection
  or inference, and standalone visual asset production or planning
- **AND** SHALL NOT claim the request is complete by adding only HTML sections

#### Scenario: HTML embedding is explicitly requested or follows accepted visual assets

- **WHEN** the user explicitly asks for an in-page H5/HTML module
- **OR** standalone visual assets have already been accepted and the next step
  is embedding or linking those assets in HTML
- **THEN** HTML editing MAY proceed within the public report gate boundary

#### Scenario: Ordinary HTML report edits do not ask for visual deliverables

- **WHEN** the user names an `.html` report and asks for ordinary text, evidence,
  layout, or citation edits without visual-deliverable wording
- **THEN** the gate MAY allow scoped HTML/report editing without requiring
  standalone visual asset production first
