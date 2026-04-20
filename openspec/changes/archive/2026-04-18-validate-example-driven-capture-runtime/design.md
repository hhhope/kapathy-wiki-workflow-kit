## Context

The repository already states that extracted reusable learning from an external repo, README, article, or in-chat example should be written to wiki in the same turn without an extra reminder.

The missing piece is runtime proof.

This follow-up primarily validates the contract in a real replay after publication, and adds one narrow process-level requirement: replay validation for this behavior should leave repo-visible evidence.

## Goals / Non-Goals

**Goals**

- Run a concrete replay against the published example-driven capture behavior
- Preserve a repo-visible record of the replay
- Make the validation standard explicit for this specific workflow change

**Non-Goals**

- Do not redefine the existing `example-driven wiki capture` trigger or routing policy
- Do not add new routing layers
- Do not create a generic automation harness for all future workflow changes

## Replay Design

### RED baseline

The baseline comes from the documented state before the workflow was formalized:

- external example is discussed
- useful adaptation insight is extracted
- no extra reminder says `write this to wiki`
- the session may stop at chat summary

This baseline is already described in the archived `formalize-example-driven-wiki-capture` change and will be referenced rather than re-simulated in an older code state.

### GREEN replay

The green replay uses the already-discussed `gstack` and `larksuite/cli` examples as source material.

Success condition:

- the current session does not need a second prompt specifically asking for wiki capture
- the agent creates a dedicated runtime validation record in the same turn
- that record preserves:
  - source
  - what was reused
  - what was modified
  - what was still not formalized
  - next step

## Artifacts

This follow-up should create:

- a `wiki/ops` runtime-validation page
- `evaluation.md`
- `verification.md`

## Spec Delta

This change adds one narrow delta:

- when the repository validates `example-driven wiki capture` behavior, that validation should leave repo-visible replay evidence

The delta does not change the main trigger logic. It only closes the verification gap exposed by the user.
