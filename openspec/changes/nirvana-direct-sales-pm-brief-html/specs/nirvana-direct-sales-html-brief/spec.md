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

