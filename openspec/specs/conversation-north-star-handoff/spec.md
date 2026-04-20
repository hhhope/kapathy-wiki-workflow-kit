# conversation-north-star-handoff Specification

## Purpose
TBD - created by archiving change introduce-north-star-handoff-mode. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL detect repeated in-session convergence on the same north-star goal

When a live discussion repeatedly returns to the same underlying goal, the repository SHALL treat that shift as a structured handoff topic rather than as disconnected Q&A.

#### Scenario: Same goal repeatedly pulls the discussion back

- **WHEN** the user repeatedly steers the conversation back to the same goal during the current session
- **THEN** the system SHALL recognize the topic as a handoff-mode conversation candidate
- **AND** the repository SHALL stop treating the exchange as isolated questions only

### Requirement: Handoff mode SHALL maintain a minimum slot structure

When the repository enters handoff mode for a conversation topic, it SHALL preserve a minimum structure that makes the topic resumable and promotable later.

#### Scenario: Handoff topic is active

- **WHEN** a conversation is being handled in handoff mode
- **THEN** the system SHALL preserve at least:
  - north star
  - constraints
  - failure modes
  - preferences
  - disagreements
  - open questions
  - candidate practices
  - repo targets

### Requirement: Same-topic discussion beyond two rounds SHALL count as a strong trigger

The repository SHALL treat repeated discussion of the same topic beyond two rounds as a strong signal that the conversation may need handoff-mode handling.

#### Scenario: Topic continues beyond two rounds

- **WHEN** the same topic continues across more than two discussion rounds
- **THEN** the system SHALL treat that recurrence as a strong trigger for handoff-mode evaluation
- **AND** it SHALL not require recurrence count to be the only trigger

### Requirement: Handoff topics SHALL route to the lowest durable repository layer that preserves recovery

The repository SHALL route handoff topics to the lowest correct durable layer rather than flattening all outputs into the same record type.

#### Scenario: Topic opens but has not become a stable repo-wide decision

- **WHEN** a handoff topic needs continuity but has not yet become a stable decision or scoped implementation change
- **THEN** the repository SHALL prefer an operating-layer record such as `trace`, `intake`, or `retro`

#### Scenario: Topic becomes a stable decision

- **WHEN** a handoff topic becomes a stable decision that should survive across changes
- **THEN** the repository SHALL promote that conclusion to `ADR`

#### Scenario: Topic becomes a scoped workflow or implementation change

- **WHEN** a handoff topic becomes a repository-default workflow change or scoped implementation track
- **THEN** the repository SHALL route it into an `OpenSpec change`

#### Scenario: Topic specifically concerns closure reasoning

- **WHEN** a handoff topic is specifically about whether a current change is archive-ready
- **THEN** the repository SHALL use change-local `archive-review.md` when the blocker is governance-heavy

### Requirement: First-version handoff mode SHALL not auto-mutate rules or skills

The first version of the handoff layer SHALL stop at capture, structure, and correct durable routing.

#### Scenario: Conversation surfaces a candidate workflow rule or best practice

- **WHEN** a handoff topic surfaces a candidate workflow rule, best practice, or behavior pattern
- **THEN** the system SHALL preserve it as a candidate artifact or structured note
- **AND** it SHALL not directly auto-edit `.codex/skills/*`, `AGENTS.md`, or other repository-default workflow rules in the same first-stage behavior

