## Why

Recent product alignment work drifted between scorecards, graph gaps, Feishu
delivery rules, external repo learning, and OpenSpec task state. The underlying
issue is that the repository has not yet stated the core product contract for
its LLM Wiki.

The user corrected the framing: agent self-service learning and
learning-to-change orchestration are useful enhancements, but they are not the
core value. The core value is a durable compiled context layer that lets agents
and humans reuse scattered report material without repeatedly reconstructing
source, status, proof boundaries, or reading routes from chat history.

## What Changes

- Define the repository's LLM Wiki north star as durable compiled context for
  agents and humans.
- Define the core loop as:
  - Capture once
  - Compile once
  - Retrieve cheaply
  - Apply safely
- Separate core capabilities from enhancements such as agent self-service
  learning, scorecard calibration, graph/lint dashboards, and
  learning-to-change orchestration.
- Reframe the `Ar9av/obsidian-wiki` comparison under the core loop instead of
  treating it as a feature-copy list.
- Add a repo-visible product contract page in `wiki/ops/` so future agents can
  recover the north star and backlog ordering without chat memory.

## Impact

- Adds an OpenSpec capability contract for `llm-wiki-core-contract`.
- Adds `wiki/ops/llm-wiki-core-product-contract.md`.
- Updates `wiki/ops/index.md` to expose the product contract.
- Does not implement manifest generation, query tooling, graph UI, scorecard
  changes, or learning-to-change orchestration.
- Does not modify Feishu documents or external delivery behavior.
