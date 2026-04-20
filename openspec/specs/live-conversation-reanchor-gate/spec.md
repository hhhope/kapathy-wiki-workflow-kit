# live-conversation-reanchor-gate Specification

## Purpose
TBD - created by archiving change add-live-conversation-reanchor-gate. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL stop continuation and re-anchor when live conversation signals drift

When live conversation signals that the current work may have drifted away from the last confirmed requirement, the repository SHALL stop implementation continuation and re-anchor before more work proceeds.

#### Scenario: User signals return to the earlier requirement
- **WHEN** the user repeatedly says the work has drifted, is off-target, or should return to an earlier requirement
- **THEN** the repository SHALL stop continuation
- **AND** it SHALL restate the last confirmed requirement before more implementation proceeds

#### Scenario: `continue` has materially different meanings
- **WHEN** the same `continue` could now mean materially different next steps
- **THEN** the repository SHALL NOT silently inherit the current technical chain
- **AND** it SHALL re-anchor to the last confirmed mainline first

### Requirement: Repository SHALL use concrete trigger signals for live conversation re-anchor

The repository SHALL use concrete trigger signals rather than generic disagreement language to determine when re-anchor is required.

#### Scenario: Work crosses into a heavier layer
- **WHEN** the current work is crossing from analysis, documentation, or modeling into runtime, automation, or execution
- **AND** the mainline for that heavier layer has not been explicitly confirmed
- **THEN** the repository SHALL trigger re-anchor

#### Scenario: Agent is following the technical chain instead of the confirmed goal
- **WHEN** the agent is continuing from the current technical chain instead of the last confirmed product goal
- **THEN** the repository SHALL trigger re-anchor

### Requirement: Repository SHALL produce a repo-visible re-anchor artifact before continuation

When the live conversation re-anchor gate fires, the repository SHALL produce a repo-visible re-anchor artifact before further implementation continuation.

#### Scenario: Drift is unresolved in live conversation
- **WHEN** drift has been signaled and is not yet fully resolved inside the active change artifacts
- **THEN** the repository SHALL create or update a `wiki/ops retro`
- **AND** the retro SHALL record:
  - original requirement
  - current drift chain
  - keep
  - freeze
  - next action

### Requirement: Repository SHALL require explicit unblock conditions after re-anchor

After the live conversation re-anchor gate fires, the repository SHALL require explicit unblock conditions before implementation continuation resumes.

#### Scenario: Re-anchor remains unresolved
- **WHEN** the gate has fired
- **THEN** the repository SHALL keep implementation blocked until at least one of the following is true:
  - the user explicitly confirms the next mainline
  - a new OpenSpec change is created for the new direction
  - the retro or archive-review artifact records `keep`, `freeze`, and `next action`

### Requirement: Repository SHALL keep the re-anchor gate narrow

The repository SHALL keep the live conversation re-anchor gate narrow enough to avoid over-firing on ordinary correction.

#### Scenario: Ordinary factual correction
- **WHEN** the user provides a single factual correction or a weak objection that does not indicate drift
- **THEN** the repository SHALL NOT trigger the re-anchor gate automatically

