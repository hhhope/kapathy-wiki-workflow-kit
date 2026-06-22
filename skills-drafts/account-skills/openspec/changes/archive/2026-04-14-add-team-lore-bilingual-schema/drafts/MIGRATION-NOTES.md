# Migration Notes — first rollout slice drafts

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

## What these drafts demonstrate

These drafts demonstrate how the new agent-memory contract changes the first screen of a durable shared page.

Across all five pages, the migration pattern is the same:

- promote startup-relevant information into `Top Facts`
- add `Applies When` so an agent can justify loading the page
- add `Not For` so neighboring pages can be rejected quickly
- add `Load Next` so navigation becomes directional instead of link-only
- push long explanation into `Notes`

## What these drafts do not yet do

- they do not rewrite the entire historical `team-lore` corpus
- they do not provide full bilingual summaries; this slice only adds minimal routing aliases
- they do not yet update bootstrap scripts or weekly-review scripts

## Review questions

1. Is the first screen materially cheaper for an arbitrary agent to load?
2. Are page boundaries now sharp enough for startup and debugging tasks?
3. Does `Load Next` reduce unnecessary neighboring-page reads?
4. Which of these five pages most clearly still need bilingual routing support in the next pass?
