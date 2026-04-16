## Context

OpenSpec already exposes a `complete` state, but that state is not rich enough for this repository's closing discipline. A change can be `complete` at the artifact level while still failing closure checks such as:

- external publication or sync not finished
- final verification not finished
- spec / ADR follow-up not yet landed
- boundary ambiguity about whether a remaining item belongs to the current change or a new one

The workflow therefore needs a repository-level rule that treats `complete` as a stop on implementation, not as automatic permission to archive.

## Goals / Non-Goals

**Goals**

- Make `archive review` the default next step after a change becomes `complete`.
- Keep the default lightweight for simple blockers.
- Preserve repository-visible reasoning when the archive decision depends on governance or scope judgment.
- Promote the pattern into global personal guidance only after it is first grounded in repo-visible artifacts.

**Non-Goals**

- Add a new OpenSpec CLI status such as `ready_to_archive`.
- Automatically archive completed changes without a human review step.
- Rewrite the local OpenSpec skills as part of this change.
- Turn every archive review into a long-form report.

## Decisions

### Decision: Completion leads to archive review, not to automatic archive

When a change becomes `complete`, the default next action is `archive review`. The review decides whether the change is actually archive-ready or whether it remains in `openspec/changes/` with explicit blockers.

Alternative considered:
- Treat `complete` as sufficient to archive.
  - Rejected because repository closure also depends on verification, external sync, and boundary cleanliness.

### Decision: Simple blockers use `tasks.md` plus git evidence

If archive review finds an ordinary tail blocker such as a missing sync step or missing final verification, the workflow should stay lightweight:

- keep the current status visible in `tasks.md`
- record the reasoning and next action in the related git commit message

Alternative considered:
- Require a dedicated note for every archive blocker.
  - Rejected because many blockers are routine execution tails, not governance decisions.

### Decision: Governance-heavy blockers require `archive-review.md`

If the archive decision involves scope ambiguity, reusable governance judgment, or reasoning that would be hard to reconstruct later from `tasks.md` and git history alone, the change directory must gain an `archive-review.md` note.

This keeps:

- task execution in `tasks.md`
- stable cross-change decisions in `wiki/adr/`
- event-level archive judgment in the current change directory

Alternative considered:
- Put archive-review notes under `wiki/ops/`.
  - Rejected because archive review belongs to the current change context and should archive with that change.

### Decision: Promote the repository rule into global personal guidance

This closing pattern is not specific to material-processing work. It generalizes to any repository that uses OpenSpec and needs a disciplined boundary between `complete` and `archived`. The personal global guidance should therefore carry the same rule after the repository version is published and checked.

Alternative considered:
- Leave the rule repository-local only.
  - Rejected because the failure mode is workflow-generic rather than domain-specific.

## Evaluation Plan

### Baseline scenario A: Completed change with no default archive action

- Before change: `complete` stops implementation, but no default next action tells the agent to run archive review.
- Expected failure: completed changes remain in the active list with no consistent closing behavior.

### Baseline scenario B: Routine archive blocker

- Before change: a missing sync or final verification step has no documented lightweight rule for closure evidence.
- Expected failure: the agent either over-documents a routine tail or leaves the reason only in chat.

### Baseline scenario C: Governance-heavy archive blocker

- Before change: a boundary-heavy archive decision has no explicit record location inside the change.
- Expected failure: reasoning gets lost in chat or buried in git history.

### After-change expectation

- Scenario A resolves by making archive review the default next step after `complete`.
- Scenario B resolves by routing simple blockers to `tasks.md` plus git evidence.
- Scenario C resolves by requiring `archive-review.md` inside the current change directory.

## Evaluation Results

### Baseline

- `git show HEAD:AGENTS.md | rg -n "Archive Review Default|archive review|archive-review.md"` returned no matches.
- Result: the prior repository guidance had no default archive-review handoff after `complete` and no named location for complex archive-review reasoning.

### After Change

- `rg -n "Archive Review Default|archive review|archive-review.md" AGENTS.md openspec/changes/archive-review-defaults wiki/adr/0007-archive-review-before-archive.md` now returns the new repository rule, the OpenSpec change artifacts, and the stable ADR.
- `openspec validate archive-review-defaults` returns `Change 'archive-review-defaults' is valid`.
- `openspec status --change "archive-review-defaults" --json` reports all spec-driven artifacts as `done`.
- `git diff --name-only -- .codex/skills` returns no changed skill files, confirming this change published policy without silently rewriting local skill behavior.
- `sed -n '112,136p' /home/yan/.codex/AGENTS.md` shows the same archive-review defaults in the global OpenSpec boundary section.
