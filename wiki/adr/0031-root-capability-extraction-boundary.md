---
layer: adr
domain: none
canonical_object: root-capability-extraction
artifact_type: adr
formalizes:
- root-capability-extraction
related_objects:
- root-governance-alignment
- repo-agents-loaded-context
- principle-skills-layer
derived_from:
- openspec/changes/archive/2026-05-07-decide-root-capability-extraction-boundary/
- wiki/ops/root-capability-extraction-retro.md
---

# root-capability-extraction / adr

- Status: accepted
- Date: 2026-05-07

## Context

Repo `AGENTS.md` now lists high-frequency repo-local skills so agents can load
the right behavior card at runtime. This made routing more legible, but it also
blurred ownership: a skill can be available in this repo without being
repo-owned.

The gap surfaced when `verify-before-claiming` was compared with root git
truth-source gates. The skill is a generic completion-claim capability, while
root `AGENTS.md` already owns much of the git truth-source behavior. The same
ownership pressure applies to `clarify-before-acting`, `simplicity-first`, and
`surgical-changes`.

## Decision

Repo High-Frequency Skills is a runtime trigger map, not an ownership map.

Any repo guidance that exposes reusable skill triggers must distinguish at
least these ownership statuses:

- `repo-owned`: the behavior is specific to this repository's workflows,
  outputs, or delivery boundaries.
- `root-candidate`: the behavior is generally useful across repositories but is
  currently incubated or referenced here.
- `root-owned-reference`: the behavior is already owned by root/global guidance
  and the repo only points to or tightens it.
- `shared`: the capability has a general core while this repo owns local
  details.

Publishing a skill under repo `.codex/skills/` does not by itself make the
behavior repo-owned.

Root candidates must not be promoted into root `AGENTS.md`, root skills, or
root rules without a root-focused OpenSpec change and before/after evaluation
evidence.

## Consequences

- Repo `AGENTS.md` can keep a High-Frequency Skills table, but it must not be
  read as an ownership table.
- Generic principle skills may remain available in this repo while they are
  marked as root candidates.
- Repo-owned workflows such as material processing and meeting-note output stay
  in repo governance.
- Future root migration is a successor change, not part of this ADR.
