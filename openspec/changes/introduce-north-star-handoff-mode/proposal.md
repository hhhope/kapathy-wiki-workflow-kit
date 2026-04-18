## Why

The repository already has strong governance layers:

- `OpenSpec` for scoped change lifecycle
- `wiki/ops` for operating-layer traces, reminders, and handoff preparation
- `ADR` for stable cross-change decisions
- `retro` pages for drift and failure review

But the live conversation still breaks before any of those layers can help. The agent does not reliably detect when the user has stopped asking isolated questions and has started repeatedly steering the discussion back to the same north-star goal.

That gap causes three recurring failures:

- important preferences remain buried in chat until someone manually extracts them
- process-level disagreements are rediscovered instead of being carried forward in-session
- repo-visible records are usually created after convergence is obvious, rather than during the conversation when the topic is actively being shaped

The user wants the first fix to happen inside the current conversation: when the same goal repeatedly pulls the discussion back, the system should recognize that shift and enter a structured handoff mode.

## What Changes

- Define a repository-default `north-star handoff mode` for conversations that repeatedly converge on the same goal.
- Add repo guidance for when ordinary Q&A becomes a handoff topic.
- Define the minimum slot structure for handoff mode:
  - north star
  - constraints
  - failure modes
  - preferences
  - disagreements
  - open questions
  - candidate practices
  - repo targets
- Define how handoff-mode outputs map into repo-visible layers such as `trace`, `retro`, `ADR`, `OpenSpec`, and `archive-review.md`.
- Explicitly defer automatic skill mutation, full archive-review gates, and full `wiki/ops` runtime automation to later changes.

## Capabilities

### New Capabilities

- `conversation-north-star-handoff`: the repository SHALL recognize repeated in-session convergence on the same goal and treat it as a structured handoff topic rather than as disconnected Q&A.

### Modified Capabilities

- `personal-ops`
- `archive-review-defaults`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/introduce-north-star-handoff-mode/`.
- Updates repo-visible workflow guidance for the operating layer.
- Defines the first explicit bridge between live conversation state and durable `wiki/ops` records.
- Creates a foundation for later changes that add closure checks, candidate-rule staging, or controlled skill evolution.
