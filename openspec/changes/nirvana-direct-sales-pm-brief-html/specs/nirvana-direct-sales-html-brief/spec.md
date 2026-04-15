## ADDED Requirements

### Requirement: Direct-sales HTML brief SHALL mirror the PM brief baseline
The system SHALL generate a single-page HTML brief for direct-sales phase1 that mirrors the management baseline defined in the PM brief and SHALL not introduce conclusions that do not exist in the markdown source.

#### Scenario: HTML is reviewed against the PM brief
- **WHEN** a user compares the HTML brief with the PM brief
- **THEN** the HTML SHALL preserve the same core dates, coverage judgments, constraints, and resource asks
- **AND** the HTML SHALL not add unsupported claims

### Requirement: Direct-sales HTML brief SHALL emphasize contrast
The system SHALL present information using strong visual contrast so that committed scope, current delivery scope, unresolved closure items, and resource actions can be distinguished at a glance.

#### Scenario: User needs to present the page in a meeting
- **WHEN** a user opens the HTML brief for leadership review
- **THEN** the page SHALL visually separate at least the following comparisons:
- **AND** committed scope versus current delivery scope
- **AND** minimum customer path versus unresolved closure items
- **AND** time nodes versus current delivery constraints
- **AND** resource constraints versus requested support

### Requirement: Direct-sales HTML brief SHALL be high-density but readable
The system SHALL use a compact single-page layout that supports high information density while remaining readable on desktop presentation screens.

#### Scenario: User needs dense information without scrolling through long prose
- **WHEN** a user scans the HTML brief
- **THEN** the page SHALL prioritize cards, tables, and grouped sections over long narrative paragraphs
- **AND** the page SHALL keep the most important management conclusions above the fold or in the first major sections

### Requirement: Direct-sales HTML brief SHALL use management language
The system SHALL use management-oriented labels and section titles instead of analysis-heavy labels such as generic `gap` headings.

#### Scenario: User wants to speak directly from the page
- **WHEN** a user uses the HTML brief as a presentation aid
- **THEN** section titles and labels SHALL align with management language such as committed scope, current delivery, delivery constraints, resource configuration constraints, and management decisions

### Requirement: Direct-sales HTML brief SHALL show direct-sales versus resale distance
The system SHALL include a management-facing comparison that shows how far direct-sales capabilities are from resale target capabilities for each major domain, rather than only showing abstract mode descriptions.

#### Scenario: Reader wants to understand distance between direct-sales and resale
- **WHEN** a user reviews the comparison section
- **THEN** the HTML SHALL show per domain the current direct-sales capability, the resale target capability, the current difference, customer-facing impact, and whether phase1 handles that difference

### Requirement: Direct-sales HTML brief SHALL separate mode comparison from customer-facing map
The system SHALL separate the “direct-sales versus resale distance” view from the “current customer-facing capability” view so that the reader can independently understand strategic distance and current external commitment.

#### Scenario: Reader wants to know both strategic distance and customer commitment
- **WHEN** a user scans the HTML brief
- **THEN** the page SHALL provide one section for direct-sales versus resale capability distance
- **AND** another section for current customer-facing capability coverage
- **AND** the two sections SHALL not collapse into a single ambiguous table

### Requirement: Direct-sales HTML brief SHALL use source workstream names in the gantt
The system SHALL use business-object or module names from the source schedules as the primary gantt workstream names instead of replacing them with reporter-invented abstract stage labels.

#### Scenario: Gantt rows are checked against source schedules
- **WHEN** a user compares the gantt rows with source schedules such as `协议支付交易`, `统一网关`, `涅槃账户`, or `分账分库`
- **THEN** the page SHALL prioritize workstream names that map directly to those business objects or modules
- **AND** the page SHALL not rename them into abstract labels like generic preparation, closure, or coupling stages unless the source itself uses that label

### Requirement: Direct-sales HTML brief SHALL preserve source status semantics
The system SHALL preserve the source status semantics for each workstream item and SHALL not render a source `未开始` item as an in-progress item merely because it has planned dates.

#### Scenario: Source item has planned dates but status is not started
- **WHEN** a source schedule item has planned dates and its source status is `未开始`
- **THEN** the page SHALL render it using the not-started visual class
- **AND** the page MAY add risk emphasis without changing the underlying not-started status

### Requirement: Direct-sales HTML brief SHALL distinguish original business milestones from current functional baselines
The system SHALL distinguish original business milestones from the current functional schedule baseline whenever a business milestone is already known to be materially off-track.

#### Scenario: Original business milestone has drifted
- **WHEN** the source materials show that a business milestone such as `直销模式业务支持完成时间 2026-06-30` has already drifted
- **THEN** the page SHALL label it as an original business milestone or original plan
- **AND** the page SHALL base current delivery judgment on the current functional schedules and states instead of presenting that original milestone as the live baseline

### Requirement: Direct-sales HTML brief SHALL include account as a first-class gantt workstream when account carries delivery scope
The system SHALL include account as a top-level gantt workstream when the source schedules show that account carries settlement, freeze, query, balance-movement, or account-compatibility scope for the current phase.

#### Scenario: Account appears in current-phase schedules
- **WHEN** the source schedules include account items such as `待分账户`, `分账接收户`, `统一动账`, `结算`, `冻结`, `结算出款`, or `账户查询兼容`
- **THEN** the gantt SHALL include an account workstream in the primary timeline
- **AND** that workstream SHALL not be relegated only to the technical-construction section

### Requirement: Direct-sales HTML brief SHALL avoid pseudo-precise coverage percentages
The system SHALL avoid pseudo-precise capability coverage percentages when no interface-level completion model exists in the source materials.

#### Scenario: User wants current capability coverage on the page
- **WHEN** the source materials do not provide a rigorous interface-level completion model
- **THEN** the page SHALL describe capability coverage using scope language such as committed, currently customer-facing, or not included in phase1
- **AND** the page SHALL not invent percentage figures such as `40%` as if they were measured facts
