# Proposal: document README capability map boundary

## Summary

Clarify that the repository README may describe the project capability map and
layered wiki/runtime model, but it is not the runtime entrypoint, behavior
source of truth, or replacement for OpenSpec/ADR governance.

## Motivation

During the Obsidian graph and MOC projection design discussion, the user asked
to explain the whole project's layered capability map in the README before
continuing runtime work. The agent drifted twice:

- It first moved the request toward a separate capability-map runtime artifact.
- It then treated README as a possible runtime first-read contract.

The corrected requirement is narrower and more concrete: README is the project
description. It should explain the repository's layers, capabilities, runtime
surfaces, and boundaries clearly enough that future contributors and agents do
not mistake status, graph, apply, react, eval, MOC projection, or OpenSpec for
each other.

## Scope

- Update README with a project capability map and explicit boundary language.
- Add an ops drift trace for the README/capability-map misunderstanding.
- Add an ADR for the stable README capability-map boundary.
- Add an OpenSpec delta that captures the requirement.

## Non-Goals

- Do not implement Obsidian MOC projection.
- Do not add or change runtime scripts.
- Do not change `.codex/skills/*`, `AGENTS.md`, or command behavior.
- Do not make README the runtime source of truth.
- Do not reopen completed wiki runtime changes.
