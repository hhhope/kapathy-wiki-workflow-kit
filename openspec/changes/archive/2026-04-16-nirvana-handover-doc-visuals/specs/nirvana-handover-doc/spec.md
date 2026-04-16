## MODIFIED Requirements

### Requirement: System SHALL produce a takeover-oriented Nirvana handover document
The handover document SHALL include an at-a-glance milestone progress drift view and a project team member list for the incoming account engineering owner.

#### Scenario: Incoming account owner checks takeover readiness
- **WHEN** the incoming account engineering owner opens the handover document
- **THEN** the document SHALL show both milestone-level drift and the relevant project member roster needed for alignment

### Requirement: Document SHALL use dual baselines
The handover document SHALL compare current status against both the M3.1 full target and recent weekly-report commitments, and it SHALL include milestone baseline nodes where those dates are available.

#### Scenario: Reader checks milestone drift
- **WHEN** the reader reviews milestone progress
- **THEN** the document SHALL present milestone baseline dates together with current status and drift judgment in a Feishu-compatible visual format
