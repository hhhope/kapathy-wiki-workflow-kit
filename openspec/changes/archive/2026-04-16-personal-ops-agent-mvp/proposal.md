## Why

Right now the repository can hold reporting knowledge, but it does not yet function as a personal operations system. The next step is to let the agent capture my raw behavior and materials, connect them into an evolving main thread, surface reminders and pending work, and hand off coding tasks into Codex when a todo becomes an engineering task.

This needs to be built as an MVP so the loop becomes usable early: capture -> analyze -> relate -> remind -> dispatch. Without that loop, the wiki remains a static archive instead of an active personal operating surface.

## What Changes

- Add an MVP intake model for capturing daily behavior, files, notes, and events into the project wiki.
- Add agent-driven analysis rules that connect new inputs to ongoing themes, open todos, and emerging main threads.
- Add a reminder-oriented view that highlights active priorities, pending items, and stale unresolved work.
- Add a handoff model for converting selected todo items into Codex-executable engineering tasks.
- Define clear separation between operational working memory, reusable knowledge, and task-dispatch records.

## Capabilities

### New Capabilities
- `behavior-capture-and-linking`: Capture personal inputs and events, classify them, and relate them to ongoing topics, todos, and source pages.
- `focus-and-reminder`: Maintain a visible main thread, pending actions, and reminder signals based on captured activity and unresolved items.
- `codex-task-handoff`: Convert development-oriented todo items into structured Codex task records with enough context for execution and collaboration.

### Modified Capabilities

None.

## Impact

- Adds new OpenSpec change artifacts under `openspec/changes/personal-ops-agent-mvp/`.
- Extends the wiki model beyond passive report archiving into active personal operations and task routing.
- Likely affects `wiki/` structure, intake conventions, reminder pages, and task handoff templates.
- Creates the contract for future automation that scans inbox-like sources and turns recognized work into linked knowledge and executable engineering tasks.
