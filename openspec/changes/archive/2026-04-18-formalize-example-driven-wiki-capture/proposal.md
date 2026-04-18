## Why

The repository now defines `handoff mode`, but there is still a practical gap in day-to-day use.

When the user drops an external repo, a README, or concrete examples in chat, the agent can often extract a reusable method, workflow pattern, or adaptation insight. But unless the user explicitly reminds the agent to "write this to wiki," that learning can still remain trapped in the conversation.

That creates three recurring failures:

- useful external examples get discussed but not turned into repo-visible learning
- the user still has to remind the agent to create a wiki record for obvious reusable takeaways
- adaptation decisions such as "what we reused", "what we changed", and "what is still missing" are easy to lose

The user wants a stronger default: when an external example or in-chat example has already produced a reusable learning, the agent should write the wiki record in the same turn without waiting for an extra reminder.

## What Changes

- Define a repository-default `example-driven wiki capture` rule.
- Require repo-visible capture when external repos, READMEs, or concrete in-chat examples yield reusable workflow or operating insights.
- Define the minimum fields for those records:
  - source
  - what was reused
  - what was modified or rejected
  - what is still not formalized
  - next step
- Define routing boundaries between `wiki/ops`, `wiki/examples`, and `team-lore-candidates`.
- Add a real retro page for the current `gstack` and `larksuite/cli` learning session.

## Capabilities

### New Capabilities

- `example-driven-wiki-capture`: the repository SHALL capture reusable learnings from external examples or concrete in-chat examples without requiring an extra user reminder.

### Modified Capabilities

- `conversation-north-star-handoff`
- `personal-ops`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/formalize-example-driven-wiki-capture/`.
- Updates repository guidance for when example-based learning must become a wiki record.
- Adds an operating-layer page and a concrete retro page for the current `gstack` and `larksuite/cli` discussion.
