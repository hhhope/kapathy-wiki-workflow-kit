## Context

Repo Phase 0 is already complete and archived. That means the repository now
has an accepted gate for repo `AGENTS.md` migration, but it does not yet have
the migration itself.

Current state:

- repo `AGENTS.md` still contains the long-form governance surface
- stable ADR/spec/wiki targets now exist for many of those sections
- the repository still needs a deliberate choice about what remains repo-local
  after compression

This change should be the implementation boundary for repo-local AGENTS
compression and proxy migration.

## Goals / Non-Goals

**Goals**

- Reduce the size and duplication of repo `AGENTS.md`.
- Replace repeated governance prose with bounded proxies to stable sources.
- Preserve repo-local delivery boundaries that still need to remain inline.
- Record before/after proof for the migration result.

**Non-Goals**

- Do not modify root `~/.codex/AGENTS.md`.
- Do not modify root `~/.claude/CLAUDE.md`.
- Do not add a repo-local commit hook implementation.
- Do not redesign the full governance model from scratch.

## Decisions To Resolve

### Decision: Compression target should be bounded, not aesthetic

The line-count target should be treated as a bounded verification target rather
than as an aesthetic number from a candidate playbook.

### Decision: Proxy coverage must be explicit

Every removed governance block must either:

- become a proxy to an accepted ADR/spec/page
- or remain inline because it is still a repo-only execution boundary

### Decision: Repo-local delivery sections stay until proven proxy-safe

Material-processing and meeting-note delivery boundaries should only be
proxied if the repository can still preserve runtime safety after migration.

## Pressure-Test Plan

- Verify each proxy target exists and is single-source.
- Verify the repo `AGENTS.md` still blocks forbidden Phase 1 shortcuts.
- Verify repo-only delivery boundaries remain visible after compression.
