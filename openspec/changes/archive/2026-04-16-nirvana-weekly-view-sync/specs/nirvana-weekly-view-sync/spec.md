## ADDED Requirements

### Requirement: System SHALL preserve a week-specific HTML view source
When a weekly Nirvana HTML preview view is provided, the system SHALL preserve it as a separate weekly source record instead of treating it as an untracked side file.

#### Scenario: Weekly HTML preview exists
- **WHEN** the repository receives `preview .html` for a weekly Nirvana update
- **THEN** it SHALL create a week-specific source page that records the HTML file lineage and summarizes its visual content

### Requirement: Weekly ops records SHALL absorb clarified alignment facts
If the user provides clarified weekly execution facts after the initial intake, the weekly source, intake, and reminder pages SHALL be updated to reflect those facts.

#### Scenario: User refines the weekly judgment
- **WHEN** the user provides clarified timing, ownership, or scope facts for the same weekly record
- **THEN** the weekly pages SHALL be updated so the archive reflects the latest confirmed judgment for that week
