# Design: Native Superpowers With OpenSpec Check/Archive

## Final Workflow

Use this sequence for Superpowers-native work that later needs OpenSpec
acceptance or archive:

```text
Superpowers brainstorming
-> Superpowers design spec with Acceptance Spec
-> user approves design
-> Superpowers writing-plans
-> plan-check during plan review
-> user approves plan
-> implement block by block from the Superpowers plan
-> if scope changes, stop and update/create OpenSpec
-> after all blocks complete, use OpenSpec for check, evidence, validation, and archive review
```

Superpowers plan is the implementation plan.
OpenSpec tasks are the check/archive ledger.
plan-check belongs to Superpowers plan review.
plan-check does not create a new plan.
Acceptance Spec lives inside the Superpowers design spec.
scope changes stop implementation.

## Responsibilities

Superpowers owns:

- design intent;
- Acceptance Spec;
- implementation block breakdown;
- TDD / RED / GREEN sequence;
- block-level verification;
- block-level recovery evidence.

OpenSpec owns:

- scope-change stops;
- formal acceptance scenarios;
- evidence summary;
- validation;
- archive review.

OpenSpec does not track Superpowers block progress during native execution.
`tasks.md` must not become a second implementation plan.

## Plan-Check Boundary

Plan-check happens before implementation, inside Superpowers plan review. It
checks that the Superpowers plan covers the Acceptance Spec and is resumable.

Allowed plan-check output:

- `PASS`;
- `FAIL: missing coverage for <acceptance item>`;
- `FAIL: block <n> is too large`;
- `FAIL: block <n> has no verify step`;
- `FAIL: behavior change lacks RED/GREEN or replay evidence`.

Forbidden plan-check output:

- new implementation tasks;
- replacement steps;
- a second task list;
- progress checkboxes.

## Resume Order

After interruption, resume from:

```text
Superpowers spec -> Superpowers plan -> git status -> git log -1 -> current unfinished block
```

Do not use OpenSpec `tasks.md` to decide how to implement a Superpowers plan
block.

## Conflict Handling

If implementation discovers work outside the approved plan or scope, stop and
use OpenSpec before continuing.

Conflict types:

- Superpowers plan requires work outside OpenSpec scope: scope change; stop and
  ask whether to expand scope.
- OpenSpec `tasks.md` contains implementation steps: reduce it back to
  check/archive lifecycle items.
- Superpowers TDD command is stale: update the Superpowers plan or evidence and
  record why.
- Implementation proves the design infeasible: stop, update design/evaluation,
  and ask for user confirmation when scope or acceptance changes.

## Completion Evidence

After Superpowers blocks complete, OpenSpec check/archive summarizes evidence.
It does not replace the Superpowers plan or retroactively track block progress.

OpenSpec evaluation should include:

- source Superpowers spec and plan paths;
- acceptance items checked;
- evidence from completed plan blocks;
- validation command results;
- residual risks.
