## Why

The current `ops` layer still reflects the earlier MVP bootstrap state. The main thread and reminder pages are out of date relative to the work already completed, and the repository has no explicit intake path for weekly project-management progress materials.

The user wants this wiki to become a durable agent workspace, not just a static report wiki. That requires:

- recalibrating the active main thread to reflect the true next phase
- refreshing reminders so they track real remaining work instead of stale bootstrap tasks
- adding a dedicated weekly project-management loop so recurring status materials can be captured, linked, and reviewed consistently

## What Changes

- Refresh the personal ops main-thread and reminder pages to reflect the current true workstream.
- Add a project-management weekly loop page under `wiki/ops/` that defines how weekly progress materials should be captured and reviewed.
- Extend inbox intake guidance so weekly project-management inputs can be routed consistently.

## Capabilities

### New Capabilities

- `weekly-project-management-loop`: The wiki can explicitly accept and organize recurring weekly project-management progress inputs for agent follow-up.

### Modified Capabilities

- `personal-ops-agent-mvp`: The main-thread and reminder layer are recalibrated from MVP bootstrap language to the next operational phase.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/ops-main-thread-and-weekly-pm-loop/`.
- Updates `wiki/ops/main-thread.md` and `wiki/ops/reminders.md`.
- Adds a new project-management operating page under `wiki/ops/`.
- Updates `wiki/ops/index.md` and `wiki/inbox-intake.md` so the new loop is discoverable and routable.
