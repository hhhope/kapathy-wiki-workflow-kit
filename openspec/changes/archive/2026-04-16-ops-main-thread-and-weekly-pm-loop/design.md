## Context

The repository has already completed its initial bootstrap and MVP documentation loops:

- report wiki portfolio bootstrap
- personal ops MVP
- Nirvana handover local delivery

But the operational surfaces still say the next step is to add sample records and Codex handoff flow, which is no longer true. The next phase is to make the wiki usable as a real agent operating console for ongoing work, especially weekly project-management tracking.

The user also stated that more weekly project-management data will be provided later. The wiki therefore needs a stable place to receive that data without waiting for new design work each time.

## Goals / Non-Goals

**Goals:**

- Re-state the real active main thread in plain Chinese.
- Replace stale reminders with the next operational reminders.
- Create a dedicated weekly project-management loop page that explains:
  - what materials can be dropped in
  - how agent should classify them
  - what summary outputs should be produced weekly
  - when items should become reminders or Codex handoffs
- Update the inbox intake contract to mention project-management weekly materials explicitly.

**Non-Goals:**

- Build new executable automation in this change.
- Create a full project dashboard or gantt renderer.
- Normalize historical project-management materials already outside the current repo.

## Decisions

### Decision: Treat weekly PM materials as an ops input type, not as a report-only artifact

Weekly status sheets, project plans, milestone deltas, and risk lists are not just evidence for reports. They also drive reminders, focus threads, and possible engineering handoffs. They belong in the ops layer first, with optional downstream report use.

### Decision: Keep one active main thread

The main-thread page should describe the real current objective:

- turn the wiki into an agent-operable personal system
- stabilize the weekly PM loop
- keep Codex handoff reserved for engineering-ready items

This avoids splitting attention across multiple pseudo-main-lines.

### Decision: Add a dedicated weekly PM loop page instead of overloading reminders

The weekly PM page will define:

- inputs
- weekly cadence
- expected outputs
- escalation rules

This keeps reminder pages focused on actionable items rather than workflow policy.

## Risks / Trade-offs

- [Risk] Main thread wording may become stale again as the repo evolves. → Mitigation: state the page as an active control surface and keep its scope narrow.
- [Risk] Weekly PM intake could become too broad and swallow all project materials. → Mitigation: define concrete input types and keep downstream routing explicit.
- [Risk] Without automation, weekly PM upkeep could drift into manual overhead. → Mitigation: keep the page procedural and lightweight so it works before automation exists.

## Migration Plan

1. Create and validate the change artifacts.
2. Update the main-thread and reminder pages.
3. Add the weekly project-management loop page.
4. Link it from the ops index and inbox intake rules.
5. Verify the new pages describe the next real workflow clearly.
