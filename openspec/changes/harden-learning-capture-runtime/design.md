## Context

The repository now treats `AGENTS.md` as a compact loaded-context entrypoint.
That compression exposed a missing runtime edge: `learning-capture-routing` was
listed as an output/source reference, but `.codex/skills/learning-capture` was
not listed as the runtime trigger for learning inputs.

Two external repo references sharpen the model:

- `larksuite/cli`: agent runtime entrypoints should stay thin, with domain
  skills routing to module references.
- `gatelynch/llm-knowledge-base`: source intake, compiled knowledge,
  brainstorming, artifacts, and health checks should be distinct layers.

The repository will map those ideas onto existing directories instead of
creating new structure.

## Decisions

### Decision: Runtime stays light

Runtime learning capture decides whether to trigger learning, which module
applies, whether the source passes admission and scoring, and where the result
should go. It does not perform weekly knowledge compilation.

### Decision: Score gates cost

For both article and repo/README learning, sources below 75 are not deep-read by
default. They may remain brief candidates or skip records.

### Decision: Topic anchoring is explicit

When the user names a topic or the source strongly matches an existing wiki
topic by filename/title/index entry, learning capture should update or reference
that topic. If no strong anchor exists, the source remains a weekly-review
candidate; the agent must not invent a semantic link.

### Decision: Weekly review is an outlet, not runtime compilation

Weekly review may be used by repo health checks and task self-checks to clear
candidate learning, raw sources, retrospective scores, and complete changes. It
is not part of every source intake path.

## Evidence Plan

`evaluation.md` records:

- RED baseline against current repo state
- pressure scenarios for batch articles, repo learning, topic anchoring,
  unclear topics, promotion gates, and runtime trigger presence
- GREEN result after skill and repo entrypoint edits
- residual risks
