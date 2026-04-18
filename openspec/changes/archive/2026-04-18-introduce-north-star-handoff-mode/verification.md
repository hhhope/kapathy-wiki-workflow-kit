## Verification

### Before / after scenario

- Before:
  - repeated discussion could produce a good chat outcome
  - but the repo had no named handoff mode between loose Q&A and later durable artifacts
  - `openspec-explore` only covered explicit explore traces, not the broader pattern of repeated north-star pull during ordinary conversation
- After:
  - repo guidance now defines `handoff mode`
  - `wiki/ops/conversation-handoff-mode.md` explains when the mode starts and what it preserves
  - `wiki/ops/sample-handoff-topic.md` shows a durable record with time, original wording, north star, failure modes, and next step

### Non-promotion boundary

- The change guidance explicitly says first-version handoff mode is capture-and-structure only.
- It does not auto-edit `.codex/skills/*`, `AGENTS.md`, or other repository-default rules directly from conversation state.

### Validation commands

- `openspec validate introduce-north-star-handoff-mode`
  - `Change 'introduce-north-star-handoff-mode' is valid`
