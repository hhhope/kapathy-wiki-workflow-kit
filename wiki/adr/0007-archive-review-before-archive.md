# ADR-0007 Archive Review Before Archive

- Status: accepted
- Date: 2026-04-16

## Context

The repository already treats OpenSpec completion as a hard stop on implementation, but it did not define a default closing action after that stop. This left completed changes mixed with still-active changes and made archive blockers inconsistent:

- some blockers are ordinary execution tails
- some blockers are governance or scope judgments

Without a visible closing rule, the reasoning for archive decisions can disappear into chat history or scattered git commits.

## Decision

For OpenSpec work in this repository:

- `complete` means stop implementation, not "archive immediately"
- the default next action after `complete` is `archive review`
- ordinary archive blockers stay lightweight through `tasks.md` plus git evidence
- governance-heavy archive blockers use change-local `archive-review.md`

`archive-review.md` belongs in the current change directory so the review evidence moves with the archived change history instead of becoming a separate global event page.

## Consequences

- The active change list keeps a clearer distinction between "still closing" and "archived"
- Routine tail blockers do not force unnecessary extra notes
- Complex archive judgments remain repository-visible and recoverable later
- Stable policy remains visible as an ADR while change-specific archive evidence stays with the change
