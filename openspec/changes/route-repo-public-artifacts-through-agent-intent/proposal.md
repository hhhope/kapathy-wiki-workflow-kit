# route-repo-public-artifacts-through-agent-intent

## Why

The repository has strong delivery gates, but an agent can still treat a
repo-public writing request as an ordinary Markdown edit.

The observed failure was `readMe写一下`: the README was rewritten before the
agent clearly routed the request through `public-report-quality-gate` and before
it scanned README-specific repository requirements. The missing step was an
entry-layer intent classification before acting.

## What Changes

- Add an `Agent Intent Routing` section to `AGENTS.md`.
- Route repo-public artifacts such as `README.md`, `docs/*`, `examples/*`, and
  published templates through `public-report-quality-gate` lightweight path.
- Add repo-public artifact trigger semantics and lightweight path rules to
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Add pressure scenarios for repo-public routing and non-interference with
  external learning, wiki frontmatter, and reader-facing publication gates.
- Add behavior replay evidence for the README incident.

## Out of Scope

- A large generic output routing framework.
- Making `public-report-quality-gate` the router for all tasks.
- Requiring `wiki/ops/*-report-gate-review.md` for every small README or docs
  edit.
- Replacing wiki frontmatter taxonomy, skill authoring, OpenSpec lifecycle, or
  learning-capture gates.
- Batch rewriting existing public materials.

## Source Design

- `docs/superpowers/specs/2026-05-13-agent-intent-routing-design.md`
