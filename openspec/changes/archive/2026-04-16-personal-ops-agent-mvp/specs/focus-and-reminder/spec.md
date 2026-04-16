## ADDED Requirements

### Requirement: System SHALL maintain explicit active focus threads
The system SHALL provide a visible representation of current main threads so the user can understand what is actively driving work and attention.

#### Scenario: Main thread view is updated from linked activity
- **WHEN** new intake records and unresolved items accumulate around the same topic
- **THEN** the system SHALL allow that topic to appear as an active focus thread with linked evidence and pending actions

### Requirement: System SHALL track pending actions and reminders separately from raw intake
The system SHALL distinguish unresolved action items from general captured material so reminder views remain actionable.

#### Scenario: Reminder layer shows actionable work
- **WHEN** the user reviews current pending work
- **THEN** the system SHALL present reminder items that are linked to source context or focus threads instead of only raw notes

### Requirement: System SHALL surface stale unresolved work
The system SHALL make stale or unreviewed pending items visible so important work does not disappear into old notes.

#### Scenario: Pending item has not progressed
- **WHEN** an action item remains unresolved beyond its expected review window
- **THEN** the system SHALL allow it to be flagged as stale or still waiting
