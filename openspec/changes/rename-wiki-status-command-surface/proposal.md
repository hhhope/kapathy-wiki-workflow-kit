# Proposal: rename wiki status command surface

## Why

The medical-loop surgery review left `detail-0118` as an OpenSpec candidate:
`wiki/ops/wiki-status-slash-command-reanchor.md`.

That trace records a command-surface drift: the status entrypoint was shaped as
`/report-wiki-portfolio:wiki-status`, while the user-facing product namespace
was expected to stay closer to `/wiki:status`. Existing specs define the wiki
status surface and skill boundary, but they do not settle whether a shorter
product-oriented command alias should exist.

## What Changes

- Define a bounded command-surface contract for wiki status naming.
- Preserve the existing repo-local `wiki-status` skill and generated status
  artifacts.
- Investigate whether the runtime command system can expose `/wiki:status` as a
  supported alias without breaking package/plugin namespacing.
- If supported, implement the shortest compatible wiki status command surface.
- If unsupported, record the constraint and keep the existing prefixed command
  as the supported invocation.

## Scope

- Applies only to the wiki status command/name surface.
- May touch command packaging or docs only after implementation verifies the
  supported runtime shape.
- Does not change wiki status generation behavior, product status scoring,
  query behavior, graph behavior, or medical-loop routing.

## Non-Goals

- Do not rename the `.codex/skills/wiki-status/` skill directory unless runtime
  verification proves it is required.
- Do not change `scripts/build_wiki_status.py`.
- Do not add query, graph, scorecard, repair, apply, or archive behavior to
  wiki status.
- Do not claim `/wiki:status` works unless there is local replay or packaging
  evidence.

## Evidence

- Source trace:
  `wiki/ops/wiki-status-slash-command-reanchor.md`
- Current specs:
  `openspec/specs/wiki-status-surface/spec.md`,
  `openspec/specs/wiki-status-skill/spec.md`
- Medical case:
  `wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md`
