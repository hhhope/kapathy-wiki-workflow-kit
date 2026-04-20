## ADDED Requirements

### Requirement: System SHALL produce a takeover-oriented Nirvana handover document
The system SHALL create a handover document for the incoming account engineering owner that prioritizes unfinished work, risks, drift, acceptance status, and follow-up reminders.

#### Scenario: Incoming account owner reads the document
- **WHEN** the incoming account engineering owner opens the handover document
- **THEN** the document SHALL clearly show takeover-critical risks, unfinished items, and required follow-up actions

### Requirement: Document SHALL use dual baselines
The handover document SHALL compare current status against both the M3.1 full target and recent weekly-report commitments.

#### Scenario: Reader checks drift
- **WHEN** the reader looks for scope or delivery drift
- **THEN** the document SHALL distinguish M3.1 scope drift from recent weekly commitment drift

### Requirement: Document SHALL include item-level acceptance status
The handover document SHALL provide item-level acceptance status for relevant modules and functions within the handover scope.

#### Scenario: Reader checks whether an item is actually done
- **WHEN** the reader reviews a module or function item
- **THEN** the document SHALL show whether it is accepted, pending acceptance, blocked, in testing, or still needing confirmation

### Requirement: System SHALL preserve a local markdown draft and a Feishu publication target
The system SHALL keep a local markdown version of the handover document and publish the same content to Feishu when write access is available.

#### Scenario: Feishu publication succeeds or fails
- **WHEN** the handover document is prepared
- **THEN** the local markdown draft SHALL remain the durable source and the Feishu document SHALL be created or updated as the primary sharing surface
