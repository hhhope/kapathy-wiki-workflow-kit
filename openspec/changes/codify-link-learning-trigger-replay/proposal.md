## Why

Recent live replay showed the repository already has enough rules for bare
links in an active learning/governance thread to trigger `learning-capture`.
However, the useful behavior still depends on the current agent remembering the
route from chat:

- bare link inside learning/governance context -> learning material
- source-specific reader first when needed
- admission gate and score before deep read
- durable wiki notes only when the score and topic anchor justify them
- no promotion into `AGENTS.md`, skill hard rules, spec `SHALL`, or archive
  claims without evidence-backed gates

That replay should become a governance anchor, not remain an ad hoc answer.

## What Changes

- Treat the "next link replay" matrix as a required runtime strategy for
  learning-source inputs.
- Add explicit replay scenarios to `learning-capture-routing` so future agents
  can verify the route without relying on memory.
- Define completion evidence for this change as behavior replay, not prose
  preference.

## Scope

In scope:

- `learning-capture-routing` OpenSpec delta
- repo-visible implementation artifacts that make the replay discoverable
- evaluation evidence for the replay matrix

Out of scope:

- changing root `~/.codex/AGENTS.md`
- changing root/global skills
- promoting any article takeaway into a hard rule
- implementing automated link crawlers or weekly-review automation
- archiving `decide-root-capability-extraction-boundary`

## Success Criteria

- A future agent can answer "what happens if the user drops a link next time?"
  from repo artifacts, not chat memory.
- The replay distinguishes learning links from raw fetch/news/fact lookup links.
- The replay states when to write wiki, when to keep a weekly-review candidate,
  and when to refuse promotion.
- The change includes RED/GREEN-style evidence for at least five input shapes:
  bare article link, WeChat link, GitHub repo/README link, raw fetch request,
  and unclear bare link outside learning context.
