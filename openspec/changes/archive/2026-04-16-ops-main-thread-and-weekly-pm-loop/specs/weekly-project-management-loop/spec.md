## ADDED Requirements

### Requirement: System SHALL describe a weekly project-management loop in the ops layer
The wiki SHALL define how recurring project-management weekly materials are captured, linked, reviewed, and escalated inside the ops layer.

#### Scenario: User provides weekly progress material
- **WHEN** the user drops weekly project-management material into the repo workflow
- **THEN** the wiki SHALL state where it belongs, how it should be classified, and what outputs the agent should produce

### Requirement: Ops control surfaces SHALL reflect the true current workstream
The main-thread and reminder pages SHALL reflect the current operational phase rather than stale MVP bootstrap tasks.

#### Scenario: User checks the current main line
- **WHEN** the user opens the ops main thread or reminder pages
- **THEN** the pages SHALL show the real active workstream and the next concrete actions
