## ADDED Requirements

### Requirement: Repository SHALL expose user-facing medical-loop skills

The repository SHALL publish repo-local skills for the user-facing medical-loop
stages `wiki-confirm`, `wiki-treatment`, `wiki-surgery`, and `wiki-recovery`.

#### Scenario: User wants to operate after a doctor diagnosis

- **WHEN** the user asks how to proceed from `wiki-doctor` output
- **THEN** the skill surface SHALL expose the sequence
  `wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery`
- **AND** it SHALL use the Chinese stage labels `诊断`, `确诊`, `治疗`, `手术`,
  and `复查` in user-facing guidance.

### Requirement: wiki-confirm SHALL replace implementation-shaped review naming

The repository SHALL treat `wiki-confirm` as the preferred user-facing skill for
the medical-loop confirmation stage.

#### Scenario: User confirms doctor findings

- **WHEN** the user asks to confirm, triage, route, 确诊, or decide treatment
  or surgery routing for doctor output
- **THEN** `wiki-confirm` SHALL route to the existing review-decision package
- **AND** it SHALL preserve that confirmation records are draft routing, not
  approval to repair.

### Requirement: wiki-review-decisions SHALL remain a compatibility alias

The repository SHALL preserve `wiki-review-decisions` only as a legacy
compatibility alias for `wiki-confirm`.

#### Scenario: Older prompt invokes wiki-review-decisions

- **WHEN** the legacy skill is loaded
- **THEN** it SHALL direct the agent to prefer `wiki-confirm`
- **AND** it SHALL preserve the same non-writing boundaries.

### Requirement: Stage skills SHALL preserve write boundaries

Medical-loop stage skills SHALL not weaken the existing doctor, confirmation,
treatment, surgery, or recovery boundaries.

#### Scenario: User asks for broad repair

- **WHEN** the request involves large, structural, relation, MOC, ADR,
  taxonomy, governance, or OpenSpec-sensitive changes
- **THEN** the skill surface SHALL route to `wiki-surgery` planning rather than
  `wiki-treatment`.

#### Scenario: User asks whether the wiki is fixed

- **WHEN** treatment or surgery has run, or the user asks to复查
- **THEN** the skill surface SHALL route to `wiki-recovery`
- **AND** recovery SHALL record failed checks as findings rather than hiding
  them.
