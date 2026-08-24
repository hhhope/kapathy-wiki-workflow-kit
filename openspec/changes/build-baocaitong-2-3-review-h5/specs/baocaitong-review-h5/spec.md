## ADDED Requirements

### Requirement: Source-traceable review content
The system SHALL persist both source screenshots and SHALL map every reader-visible business fact to a fact ID, source location, and confidence status.

#### Scenario: Source text is clear
- **WHEN** a fact can be read reliably from the source screenshot
- **THEN** the source summary and H5 SHALL preserve the fact and its source reference
- **AND** the fact SHALL be marked `confirmed` or `transcribed`.

#### Scenario: Source text is unclear or conflicting
- **WHEN** a field cannot be read reliably or conflicts with another source statement
- **THEN** the system SHALL mark it `待原文确认` or expose the conflict as an open question
- **AND** SHALL NOT invent or silently omit a business conclusion.

### Requirement: BaoCaiTong 2.0 and 3.0 decision flow
The H5 SHALL present the approved narrative from current state through target state, differences, change areas, rules, risks, and review decisions.

#### Scenario: Reader compares versions
- **WHEN** the reader opens the flow comparison
- **THEN** the H5 SHALL show both BaoCaiTong 2.0 and 3.0 account/fund-flow structures
- **AND** SHALL distinguish fund, relation, upgrade, and withdrawal edges with visible labels.

#### Scenario: Reader inspects implementation impact
- **WHEN** the reader opens the change and rule sections
- **THEN** the H5 SHALL show seven approved change areas and seven business-rule categories
- **AND** SHALL show product, engineering, and QA/compliance open questions separately.

### Requirement: Offline responsive and accessible H5
The H5 SHALL load from local files without remote resources and SHALL remain readable when JavaScript is unavailable.

#### Scenario: Desktop review
- **WHEN** the page is viewed at 1440 by 1000 CSS pixels
- **THEN** navigation, version comparison, matrices, labels, and detail controls SHALL be readable without clipping or uncontrolled page-level horizontal scrolling.

#### Scenario: Mobile review
- **WHEN** the page is viewed at 390 by 844 CSS pixels
- **THEN** flow panels SHALL stack into a readable linear layout
- **AND** control focus, labels, and section content SHALL remain usable.

#### Scenario: JavaScript is disabled
- **WHEN** client-side JavaScript does not run
- **THEN** both version flows, all change areas, business rules, open questions, and review fields SHALL remain available in document order.

### Requirement: Review-ready verification boundary
The repository SHALL provide automated contract checks and a reader-facing gate-review record before claiming the H5 review-ready.

#### Scenario: Candidate review draft is verified
- **WHEN** the candidate H5 is presented for review
- **THEN** source-to-screen tests, local-resource checks, interaction checks, desktop visual QA, and mobile visual QA SHALL have recorded outcomes
- **AND** unresolved business fields and unverified areas SHALL remain visible.

#### Scenario: External delivery is requested
- **WHEN** the local H5 passes review checks
- **THEN** the result SHALL still remain local
- **AND** Feishu sync, publication, or other external writes SHALL require a separate explicit approval.
