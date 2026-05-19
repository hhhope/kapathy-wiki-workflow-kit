# wiki-medical-agent status prediagnosis design

## Problem

`wiki-medical-agent` currently makes the agent classify intent, validate the
active case, and report fixed fields such as Intent, Case, State, Allowed
action, Blocked action, and Next Action.

That is necessary but incomplete. When the medical-agent script returns
`report_status`, `blocked`, or `archive_ready`, the agent can mechanically
repeat the state even when the user's live intent is to continue, modify, or
understand what to do next. The result is a gate report without a useful
preadiagnosis.

## Scope

This change is intentionally small. It only changes the repo-local
`wiki-medical-agent` behavior contract. It does not create a global agent rule,
does not change the medical-agent script, and does not loosen existing write
boundaries.

## Proposed behavior

Add a compact `Status / Blocked Response` section to
`.codex/skills/wiki-medical-agent/SKILL.md`.

The section should require this behavior:

1. If the user is only asking for status, report the existing fixed fields.
2. If the user is trying to continue, modify, apply, repair, or decide next
   steps, and the medical-agent result is non-executing status such as
   `report_status`, `blocked`, `awaiting_confirmation`, or `archive_ready`, the
   agent must not stop at the fixed fields.
3. Before asking the user for missing details, the agent must provide a
   read-only prediagnosis based on already available state or at most one local
   read-only check.
4. The response should include:
   - script result
   - interpreted live user intent
   - read-only prediagnosis
   - recommended next action
   - the specific point, if any, that still requires user confirmation

Existing boundaries remain unchanged: the skill still must not auto-execute
newly discovered candidates, write relation fields, or mutate taxonomy config,
MOC pages, ADRs, AGENTS, skills, or OpenSpec lifecycle state unless a separate
approved workflow explicitly scopes it.

## Replay scenarios

The implementation should be checked against these lightweight cases:

- User says `那我继续做什么` while the case is `archive_ready`: response should
  translate archive readiness into a recommended next route, not only report
  status fields.
- User says `改 wiki/moc` and the script returns status: response should explain
  that direct generated-page mutation is not the immediate route, then provide
  a read-only prediagnosis and recommended safe next step.
- User replies only `1` after options were presented: response should preserve
  the live thread context and continue the selected option instead of asking the
  user to restate the full target.
- User asks why no prediagnosis was given: response should identify whether the
  skill result was treated too mechanically and what prediagnosis should have
  happened.

## Success criteria

- The skill remains compact and English-first.
- The added rule is specific to `wiki-medical-agent`.
- The rule does not expand write authority.
- Future responses cannot treat `report_status` as a complete answer when the
  live user intent is clearly to continue or modify.

