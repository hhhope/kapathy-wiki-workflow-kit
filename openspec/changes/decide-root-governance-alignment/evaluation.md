# Evaluation

## Baseline Scenarios

1. The user asks to implement the personal global AGENTS / skill / harness plan
   after a chat-level design.
2. The agent treats the chat plan as sufficient and prepares to edit behavior
   assets directly.
3. The agent treats wiki publication as the default landing zone before the SDD
   boundary is accepted.

## Before Results

- The implementation path was under-specified: the plan described the desired
  collaboration model but did not first bind it to the active OpenSpec change.
- The first follow-up needed re-anchoring because "implement the plan" could
  mean root dotfile edits, repo wiki publication, skill authoring, or design
  artifact updates.
- Wiki landing was still ambiguous: trace, retro, method page, and ADR were not
  separated before implementation.

## After Results

- The active change records a candidate hybrid ownership model for review
  instead of treating the model as accepted.
- The design records the SDD-first gate before any root dotfile, skill, or wiki
  method change.
- The AGENTS / SKILL / replay-harness collaboration split is recorded as a
  candidate design, not a final operating model.
- Wiki landing is explicitly gated: use the active change first, and only add a
  targeted `wiki/ops retro` if recovery needs outlive the change artifact.

## Residual Risks

- No root dotfile has been edited yet, so runtime behavior has not changed.
- No skill has been authored or modified, so skill trigger behavior remains
  untested.
- Replay-harness v1 is still a design contract; it has not been converted into
  executable validation for this topic.
- The final root/repo alignment model, ownership responsibility, and
  AGENTS/SKILL/harness split remain open pending review.
- The optional minimum sync tasks remain open and must not be treated as done
  until root-level edits, if any, are separately accepted and verified.
