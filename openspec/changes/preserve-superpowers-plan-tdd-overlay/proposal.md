# Preserve Superpowers Plan TDD Overlay

## Why

The repository already has two adjacent safeguards:

- `openspec-router` prevents OpenSpec edits while `$superpowers:brainstorming`
  is still waiting on written-spec review.
- `openspec-apply-change` treats a detailed Superpowers plan as an execution
  overlay rather than a second progress ledger.

The remaining failure is different: after brainstorming and `writing-plans`
produce a detailed Superpowers plan, the follow-up OpenSpec artifacts can
rewrite the work at a higher level. Implementation then follows the narrower
OpenSpec wording and loses detailed acceptance structure, RED/GREEN sequence,
module strategy, or verification intent from the Superpowers plan.

The Stripe H5 repair recorded this exact class of drift: Superpowers design was
used as supporting context rather than an acceptance checklist, and later
OpenSpec changes verified keywords, screenshots, or adjacent visual work while
the intended reader path stayed unverified.

## What Changes

- Require OpenSpec changes that derive from an approved Superpowers design or
  plan to preserve it as an acceptance and TDD overlay.
- Require an explicit overlay mapping from Superpowers design/plan sections to
  OpenSpec tasks, spec scenarios, and verification evidence.
- Keep `tasks.md` as the only progress ledger, while making the overlay a
  required implementation input when it exists.
- Require completion evidence to include overlay conformance checks, not only
  OpenSpec checkbox completion.

## Out Of Scope

- Do not edit the upstream Superpowers plugin.
- Do not make Superpowers artifacts the lifecycle source of truth.
- Do not require every OpenSpec change to create a Superpowers plan.
- Do not reopen completed implementation changes.
- Do not archive this change in the proposal step.
