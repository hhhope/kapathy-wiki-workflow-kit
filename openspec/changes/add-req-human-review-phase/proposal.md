# add-req-human-review-phase

## Why

The Baofu legal SMS requirements case exposed a repeatable failure in the
requirements workflow: the agent produced a readable Human Review document and
later added scenario matrices, but initially failed to update the user stories
and acceptance coverage in the authoritative requirements case. The result was a
split between a human-facing review view and the machine case state.

`req-agent` is already the normal user-facing controller and should remain the
entry point. Human Review should not become a separate normal entry skill, but it
also must not be a loose paragraph inside `req-agent`. It needs a bounded worker
phase with a fixed template and synchronization gate.

## What Changes

- Add `req-human-review` as a bounded worker under `req-agent`.
- Insert the phase between `req-acceptance` and `req-handoff`.
- Add a Human Review template that preserves required review elements.
- Add a synchronization gate: Human Review demand facts that change stories,
  acceptance, scope, domain, or readiness must be synchronized back to the
  machine requirements case before handoff.
- Update `req-handoff` to treat unsynchronized Human Review facts as a block.

## Out of Scope

- Making Human Review a normal user-facing entry point.
- Replacing the machine requirements case as the source of truth.
- Adding complex automatic consistency checking in the first release.
- Changing requirements taxonomy vocabulary.
- Creating OpenSpec drafts from Human Review alone.

## Prior Art

- `openspec/changes/req-agent`
- `openspec/changes/add-req-domain-analysis-skill`
- `openspec/changes/enforce-req-agent-design-hard-gates`
- `.codex/skills/req-agent/SKILL.md`
- `.codex/skills/req-handoff/SKILL.md`
- `wiki/ops/requirements-cases/2026-06-09-baofu-legal-sms-human-review.md`
