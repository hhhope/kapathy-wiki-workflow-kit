## Context

Repo Phase 0 is complete, ADR-0030 has decided that repo-local commit hooks are
not part of the default governance path, and root `~/.codex/AGENTS.md`
loaded-context work has completed and archived.

The remaining repo-level issue is that repo `AGENTS.md` is still a large manual
instead of a compact entrypoint. It contains many sections that now have stable
source records elsewhere.

## Goals / Non-Goals

**Goals**

- Treat repo `AGENTS.md` as a map plus repo-only hard stops.
- Reduce default loaded context without hiding required behavior in another
  default-loaded file.
- Proxy stable governance blocks to ADRs, OpenSpec specs, wiki ops pages, or
  published skills.
- Preserve material-processing and meeting-note delivery boundaries unless a
  proxy can prove runtime safety.
- Record before/after evidence and residual risks.

**Non-Goals**

- Do not modify root `~/.codex/AGENTS.md`.
- Do not modify `~/.claude/CLAUDE.md`.
- Do not introduce a repo-local commit hook.
- Do not create new wiki runtime concepts.
- Do not compress by deleting source-of-record pointers or stop conditions.

## Decisions To Resolve During Implementation

### Decision: Hard stops stay inline

Repo-only execution blockers must remain visible in repo `AGENTS.md` unless an
accepted source proves a proxy is safer.

### Decision: Stable chains become proxies

Long wiki runtime sections should become bounded pointers to their existing
OpenSpec specs and wiki ops pages when those sources are accepted and
repo-visible.

### Decision: Delivery-sensitive workflows are proxy-cautious

Material processing and meeting-note output are runtime delivery boundaries.
They should stay inline until implementation proves a compact proxy still
preserves the required user-facing behavior.

## Evidence Plan

`evaluation.md` will record:

- before/after line, word, and byte counts
- proxy coverage by section
- retained hard stops and why they remain inline
- removed or shortened blocks and their source-of-record paths
- agent-legibility check: where to read, how to verify, when to stop
- residual risks
