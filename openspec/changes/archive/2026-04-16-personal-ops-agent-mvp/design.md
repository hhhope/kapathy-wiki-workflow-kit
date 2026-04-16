## Context

The repository already defines a wiki-first structure for report knowledge, source ingestion, and AI-assisted summarization. What is missing is the layer that turns the repository into a personal operating system: a place where raw behaviors, notes, files, and tasks can be captured, interpreted by an agent, related to ongoing themes, and turned into reminders or executable engineering handoffs.

The user goal is not only archival. The user wants agent support for:
- landing all personal operational behavior into the system
- extracting and maintaining a visible main thread
- surfacing pending actions and reminder signals
- dispatching development-oriented todo items into Codex-ready tasks for collaboration

The MVP should prioritize a usable loop over completeness. It must support mixed material types, imperfect classification, and manual review without requiring a fully autonomous agent runtime on day one.

## Goals / Non-Goals

**Goals:**
- Define an intake shape for personal behaviors, files, notes, and events that can be stored in the wiki.
- Define how agents link new inputs to topics, todos, focus areas, and source pages.
- Define a simple “main thread + reminders + pending actions” layer that helps the user maintain focus.
- Define a Codex handoff record that translates selected engineering todos into executable development tasks with context.
- Keep the MVP markdown-first and compatible with later automation.

**Non-Goals:**
- Build a complete autonomous planner that manages the user’s life end-to-end.
- Replace existing issue trackers, calendars, or task systems.
- Solve every kind of workflow intake in the first version.
- Auto-execute Codex tasks without explicit user confirmation.

## Decisions

### Decision: Introduce a personal operations graph on top of wiki pages
The MVP will treat captured items as linked operational records rather than only static source pages. The minimum durable record types are:
- intake record
- focus thread
- todo/reminder item
- Codex handoff item

This allows the agent to relate “what happened”, “what matters now”, and “what should be done next” without needing a separate database in the first version.

Alternatives considered:
- Keep using only source pages and report pages: rejected because behavior capture and task routing become implicit and hard to track.
- Introduce a database immediately: rejected because the markdown model is still evolving and should be validated first.

### Decision: Make main-thread awareness explicit
The system will maintain a visible focus layer rather than assuming it can be inferred ad hoc from all captured material. The MVP should expose a small set of active threads with supporting evidence and unresolved actions.

Alternatives considered:
- Infer focus each time from raw material only: rejected because focus drift becomes invisible.
- Let the user maintain focus manually without agent help: rejected because the user explicitly wants agent-driven awareness.

### Decision: Separate working tasks from executable Codex handoffs
Not every todo becomes a Codex task. The MVP will distinguish:
- ordinary reminders and follow-ups
- engineering tasks that are mature enough for Codex dispatch

This prevents the handoff layer from being polluted by vague notes.

Alternatives considered:
- Treat every todo as a Codex task: rejected because most personal actions are not engineering work.
- Only maintain plain todo text without task records: rejected because Codex needs structured context.

### Decision: Use confidence-aware intake and linking
The agent will be allowed to classify and relate items with `high / medium / low` confidence. Low-confidence items should still land as records, but with review markers rather than silent assumptions.

Alternatives considered:
- Block all low-confidence intake: rejected because it creates too much friction.
- Auto-promote low-confidence guesses: rejected because trust would degrade quickly.

### Decision: Keep the first Codex handoff contract minimal
A Codex-ready handoff in the MVP will include:
- task title
- objective
- related source/intake links
- acceptance hint
- collaboration note
- status

This is enough to create a development task and evolve later into a richer workflow.

Alternatives considered:
- Require full PRD-level detail before handoff: rejected because it slows down fast task dispatch.
- Use only free-form markdown notes: rejected because agents need a predictable handoff structure.

## Risks / Trade-offs

- [Risk] Capturing “all behaviors” can produce noise and weak focus. → Mitigation: route everything through intake, but elevate only linked items into main-thread views.
- [Risk] The agent may over-link unrelated material. → Mitigation: require confidence labels and review flags for uncertain associations.
- [Risk] Reminder pages can become another stale dashboard. → Mitigation: anchor reminders to explicit focus threads and unresolved items.
- [Risk] Codex handoffs may be too vague to execute well. → Mitigation: require a minimal structured handoff template with objective, context, and acceptance hints.
- [Risk] The MVP can drift into a general personal knowledge system without finishing a usable loop. → Mitigation: scope the first version to capture, focus, reminders, and development-task dispatch only.

## Migration Plan

1. Extend wiki conventions with operational record types and templates.
2. Add pages for intake, focus threads, reminders, and Codex handoff records.
3. Define agent intake and linking rules for new raw inputs.
4. Add a main-thread view that highlights current focus and pending actions.
5. Add a Codex handoff workflow that turns selected todo items into executable task records.
6. Validate the loop with a small set of realistic sample records.

Rollback strategy:
- The MVP is documentation and workflow structure first. If the model is wrong, files can be revised or removed without data migration complexity.

## Open Questions

- Which personal behaviors should be excluded from intake to avoid low-signal noise.
- Whether reminders should be maintained in a single page or split by focus thread after the MVP.
- How the eventual Codex handoff action should be triggered once the markdown contract is validated.
