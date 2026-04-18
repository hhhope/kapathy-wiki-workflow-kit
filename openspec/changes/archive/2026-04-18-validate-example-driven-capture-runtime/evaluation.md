## Evaluation

### Behavior Expected To Validate

- Published `example-driven wiki capture` behavior should create a repo-visible record in the same turn once reusable learning is already extracted from an example.

### RED Baseline

Reference source:

- archived change:
  - `formalize-example-driven-wiki-capture`

Baseline behavior:

- an external repo or README can be discussed
- adaptation insight can be extracted
- without an explicit follow-up reminder, the result can stop at chat summary

### GREEN Replay

Replay inputs:

- `https://github.com/garrytan/gstack`
- `https://github.com/larksuite/cli`

Replay condition:

- no extra prompt specifically instructs the agent to `write this to wiki`
- the user only asks to continue and confirms the desired default behavior

Observed green result:

- the session created a repo-visible record:
  - `wiki/ops/gstack-lark-learning-retro-2026-04-18.md`
- the record preserved:
  - source
  - what was reused
  - what was modified
  - what was not formalized
  - next step

### Residual Risks

- This is manual replay evidence, not a reusable automated harness.
- The RED baseline is referenced from an archived change rather than executed against an old repository state.
