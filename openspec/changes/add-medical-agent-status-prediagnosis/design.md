# Design: medical-agent status prediagnosis

## Scope

This is a skill-contract patch. It changes how the agent responds after the
medical-agent script returns a non-executing status result.

## Behavior

When the user only asks for status, the existing fixed-field response remains
sufficient.

When the user is trying to continue, modify, apply, repair, or decide next
steps, and the script result is `report_status`, `blocked`,
`awaiting_confirmation`, or `archive_ready`, the agent must add a read-only
prediagnosis before asking for missing details.

The prediagnosis may use already known state or at most one local read-only
check. It must not write files or expand authority.

## Response Shape

The response should include:

- script result
- interpreted live user intent
- read-only prediagnosis
- recommended next action
- remaining user decision, if any

## Proof Boundary

This change improves agent response behavior. It does not prove that future
clients will always route correctly without loading the skill.
