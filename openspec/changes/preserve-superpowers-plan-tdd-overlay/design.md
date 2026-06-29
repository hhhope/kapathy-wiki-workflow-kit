# Design: Preserve Superpowers Plan TDD Overlay

## Model

OpenSpec remains the lifecycle authority:

- `proposal.md` defines why and scope.
- `design.md` defines the implementation model.
- delta specs define behavior requirements.
- `tasks.md` is the only progress and completion ledger.

Superpowers remains the method authority when it has been invoked:

- brainstorming design captures user intent, alternatives, and acceptance
  structure;
- writing-plans captures execution detail, TDD sequence, module strategy,
  verification commands, commit strategy, and handoff notes.

The bridge must not rewrite the Superpowers plan into a smaller OpenSpec shape.
Instead, OpenSpec should declare scope and lifecycle boundaries while preserving
the approved Superpowers artifact as an implementation overlay.

## Required Overlay Mapping

When an OpenSpec change is derived from a Superpowers design or plan, its
`design.md` or `tasks.md` must include an `Overlay Mapping` section with:

- source Superpowers spec and plan paths;
- key acceptance sections that must survive implementation;
- TDD / RED / GREEN strategy references;
- OpenSpec task or spec scenario that owns each mapped item;
- verification evidence required before completion.

The mapping may be compact, but it must be explicit enough that an implementer
cannot satisfy the OpenSpec change while ignoring the approved plan details.

## TDD Preservation

If the Superpowers plan contains TDD steps, OpenSpec must not collapse them into
generic wording such as "run tests" or "verify scoped files".

Acceptable preservation shapes:

- a task that explicitly says which RED evidence must be collected before
  implementation;
- a spec scenario that defines the missing behavior before implementation;
- an evaluation section with RED baseline and GREEN result;
- a verification checklist that cites the original TDD section.

## Conflict Handling

If OpenSpec wording and the Superpowers plan disagree:

1. Stop implementation.
2. State the conflict.
3. Re-anchor with the user or update the active OpenSpec change before coding.

Do not silently prefer the shorter OpenSpec wording when the Superpowers plan
contains more specific acceptance or TDD details.

## Completion Evidence

Before claiming completion for a derived change, the agent must report:

- OpenSpec task completion and validation evidence;
- overlay conformance evidence showing that mapped Superpowers acceptance and
  TDD details were implemented or explicitly deferred;
- residual risk for any mapped detail that could not be verified.

This keeps OpenSpec authoritative without letting the second write erase the
method-level detail.
