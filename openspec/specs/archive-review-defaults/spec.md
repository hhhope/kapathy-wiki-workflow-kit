# archive-review-defaults Specification

## Purpose
TBD - created by archiving change archive-review-defaults. Update Purpose after archive.
## Requirements
### Requirement: Completed changes enter archive review before archival
When an OpenSpec change becomes `complete`, the workflow SHALL treat archive review as the default next action before moving the change into `openspec/changes/archive/`.

#### Scenario: Change reaches completion
- **WHEN** the active OpenSpec change reaches `all_done` or all `tasks.md` checkboxes are completed
- **THEN** implementation SHALL stop immediately
- **AND** the default next action SHALL be archive review rather than further implementation, ad hoc exploration, or immediate archival

#### Scenario: Archive review passes
- **WHEN** archive review confirms that closure checks are satisfied
- **THEN** the change MAY be archived under `openspec/changes/archive/`

### Requirement: Ordinary archive blockers stay lightweight
The workflow SHALL keep ordinary archive blockers lightweight when they are routine execution tails rather than governance judgments.

#### Scenario: Routine sync or verification tail remains
- **WHEN** archive review finds a missing external sync, final verification, or similarly routine closing step
- **THEN** the current change SHALL remain under `openspec/changes/`
- **AND** the blocker SHALL remain visible in `tasks.md`
- **AND** the reason and next action SHALL be captured in the related git history rather than requiring a separate review note

### Requirement: Governance-heavy archive blockers retain change-local reasoning
The workflow SHALL preserve repository-visible reasoning when the archive decision depends on governance judgment rather than on a simple missing action.

#### Scenario: Scope or governance judgment blocks archival
- **WHEN** archive review depends on scope ambiguity, reusable governance reasoning, or context that would be hard to recover later from `tasks.md` and git history alone
- **THEN** the change SHALL include an `archive-review.md` note in its own directory
- **AND** that note SHALL summarize the current conclusion, reasons, and next action

#### Scenario: Change is archived after a complex blocker
- **WHEN** a change with `archive-review.md` is later archived
- **THEN** the review note SHALL stay with the change history by moving together with the archived directory

