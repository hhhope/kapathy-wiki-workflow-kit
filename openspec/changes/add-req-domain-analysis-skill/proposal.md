# Proposal

## Why

The requirements flow now has a DDD-based domain standard and a first payment
domain skeleton, but `req-agent` still routes domain work directly into
`req-scope`. That keeps domain judgment mixed with scope clarification and makes
it easy to treat feature names, system names, or case slugs as domains.

The flow needs a dedicated domain-analysis step after intake and before scope so
humans and Agents can classify requirements against the domain standard before
roles, boundaries, stories, and acceptance functions are refined.

## What Changes

- Add a formal repo-local `.codex/skills/req-domain-analysis/SKILL.md`.
- Update `.codex/skills/req-agent/SKILL.md` to route through
  `req-domain-analysis` after `req-intake` and before `req-scope`.
- Preserve `req-scope` as the worker for roles, ownership, boundaries, and
  unknowns after domain analysis.
- Add behavior evaluation evidence for the semantic skill change.

## What Does Not Change

- Does not mutate requirements taxonomy.
- Does not change wiki frontmatter taxonomy.
- Does not create OpenSpec drafts before requirements readiness passes.
- Does not authorize implementation from a requirements case.
