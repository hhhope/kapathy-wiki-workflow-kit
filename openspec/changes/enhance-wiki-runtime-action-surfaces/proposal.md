# Change: Enhance Wiki Runtime Action Surfaces

## Why

The current `/wiki:*` command surface exposes the runtime layers, but graph,
scorecard, and apply-style execution output still read like raw capability
wrappers. The product need is more concrete: make LLM Wiki show what the wiki
can safely help with now, what evidence supports that guidance, and what is
blocked before change orchestration starts.

## What Changes

- Add an explainable `/wiki:graph` object view that summarizes structural object
  evidence without semantic inference.
- Add an actionable `/wiki:scorecard` diagnostic view that turns score and
  utilization output into bounded inspection guidance.
- Add `/wiki:queue` as a preview-only change queue surface built from existing
  self-directed execution output.
- Keep all three surfaces repo-local, read-only, and outside OpenSpec lifecycle
  mutation.

## Impact

- Affected specs: `wiki-runtime-slash-command-surface`
- Affected commands: `/wiki:graph`, `/wiki:scorecard`, `/wiki:queue`
- Affected scripts: new summary/preview helpers over existing runtime JSON
