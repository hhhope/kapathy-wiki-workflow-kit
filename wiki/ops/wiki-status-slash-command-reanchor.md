---
layer: ops
domain: wiki
ops_area: workflow-trace
canonical_object: wiki-status-slash-command
artifact_type: reanchor
title: Wiki Status Slash Command Reanchor
type: ops
status: draft
created: 2026-05-09
source: live-conversation
---

# Wiki Status Slash Command Reanchor

## Trigger

During live exploration, the user questioned whether the wiki status command
should be exposed as `/report-wiki-portfolio:wiki-status` or as the simpler
`/wiki:status`, and asked whether the prior implementation properly followed a
change.

## Current Question

- Should repo-published slash command naming preserve the shorter product
  namespace `/wiki:status`?
- Did the prior work follow an OpenSpec change, or did it drift outside the
  intended change boundary?

## Findings

- The prior work did use OpenSpec changes:
  - `add-wiki-status-slash-command`
  - `replace-claude-wiki-status-with-codex-plugin-command`
- The first change validated the wrong command surface: Claude command files,
  not Codex repo-published command files.
- The second change corrected the surface to Codex plugin shape, but overfit the
  user-facing command name to the plugin identity:
  `/report-wiki-portfolio:wiki-status`.
- Existing command history points to product or capability namespace names:
  `/opsx:apply`, `/opsx:archive`, `/opsx:explore`, `/opsx:propose`.
- For the wiki status surface, the clearer intended command name is
  `/wiki:status`.

## Next Candidate

If implementation resumes, create a new change that renames the repo-level wiki
status command contract from `/report-wiki-portfolio:wiki-status` to
`/wiki:status`, while preserving the repo-published Codex command packaging.

## Boundary

This page records exploration context only. It does not define the final command
contract and does not authorize implementation.
