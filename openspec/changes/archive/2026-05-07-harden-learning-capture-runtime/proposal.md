## Why

External-source learning is now a frequent input path: the user may provide
dozens of articles, GitHub repositories, README files, or concrete examples in a
single working cycle.

The current repository has a useful learning-capture router and article
scorecard, but the runtime gate is incomplete:

- repo `AGENTS.md` does not list `learning-capture` as a runtime trigger
- repo/README learning has no admission gate or 75-point deep-read threshold
- article learning can be backfilled with retrospective scores that look like
  score-first evidence
- explicit topics such as agent / harness learning are not routed to existing
  wiki topic anchors before creating new notes
- unclear topics do not have a clear candidate path for weekly review

The result is repeated drift: sources are summarized or treated as support for
governance conclusions before they pass source grounding, scoring, topic
anchoring, and promotion gates.

## What Changes

- Harden `learning-capture` as the runtime trigger for external-source learning,
  reference, or adaptation material.
- Require topic anchoring before durable learning notes when the user provides a
  clear topic or the source strongly matches an existing wiki topic.
- Require unclear or weak topic matches to remain candidate material for weekly
  review instead of forced semantic linking.
- Extend repo/README learning with admission gate, scorecard, and the same
  75-point deep-read threshold used by article learning.
- Clarify that retrospective article scores are not score-first admission
  evidence.
- Add `learning-capture` to repo `AGENTS.md` runtime skill routing while keeping
  output routing separate.
- Record RED/GREEN pressure evidence in `evaluation.md`.

## Impact

- Updates repo `AGENTS.md`.
- Updates repo-local skills under `.codex/skills/learning-capture/`,
  `.codex/skills/article-learning-capture/`, and
  `.codex/skills/readme-learning-capture/`.
- Updates `wiki/ops/learning-capture-routing.md` as the durable explanation.
- Does not edit root `~/.codex/AGENTS.md`.
- Does not edit `~/.claude/CLAUDE.md`.
- Does not migrate wiki directory structure.
- Does not implement weekly-review automation.
