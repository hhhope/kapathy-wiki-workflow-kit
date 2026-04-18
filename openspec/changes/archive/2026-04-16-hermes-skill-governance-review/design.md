## Overview

This change is a review-and-trace change, not an implementation change. Its job is to record a grounded comparison between:

- the Weixin article `一文搞懂Hermes：新顶流Agent如何从经验中自我进化`
- the public GitHub project `NousResearch/hermes-agent`
- the current repository's agent-evolution model

The output should answer four questions:

1. What self-evolution mechanisms does Hermes make explicit?
2. Which of those mechanisms already exist here in a different form?
3. Which gaps are real enough to justify future OpenSpec changes?
4. Which decisions should be captured as ADRs versus retros?

## Sources

### External sources

- Weixin article:
  - `https://mp.weixin.qq.com/s/yHva-zLaRTxe8b4HSUr86Q`
- GitHub repository:
  - `https://github.com/NousResearch/hermes-agent`
- Hermes documentation:
  - `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
  - `https://hermes-agent.nousresearch.com/docs/guides/work-with-skills/`

### Internal baseline

- Global agent policy:
  - `AGENTS.md`
- Current project-management skill:
  - `.codex/skills/project-management-weekly-skill/SKILL.md`
- Skill migration pattern:
  - `.codex/skills/weixin-reader/SKILL.md`
  - `.codex/skills/weixin-reader/scripts/fetch_weixin.py`
- Existing review/pitfall trace:
  - `wiki/ops/scope-drift-retro.md`

## Comparison dimensions

The review compares Hermes and this repository across six dimensions.

### 1. Experience extraction trigger

Hermes is not centered on manually curated skills. It is centered on the agent noticing that a solved task produced reusable experience. The key governance question is not "should a human create a skill now?" but "under what conditions should the agent extract, stage, and later reuse that experience?"

This repository does not yet make those triggers explicit. Most reusable method capture still depends on the user noticing a need or on a visible incident after the fact.

### 2. Discovery and loading

Hermes makes skill discovery and loading explicit through:

- `skills_list()` as a compact inventory
- `skill_view(name)` for full content
- `skill_view(name, file_path)` for targeted reference loading
- explicit progressive disclosure to control token cost

This repository already follows a lighter version of progressive loading through the session-level skill list and selective file opening, but the policy is not yet codified as a repository governance pattern. It is mostly enforced by model instructions and manual discipline.

### 3. Candidate memory and lifecycle

Hermes treats skills as procedural memory that can be created, patched, edited, and deleted through a dedicated `skill_manage` workflow. Hermes docs also make stale-skill maintenance explicit.

This repository already has:

- local skill authoring
- migration from external skills
- incident-driven skill tightening
- explicit TDD expectations for semantic skill edits

The gap is broader than lifecycle state. We do not yet have an explicit candidate-memory layer between:

- raw experience from execution
- reusable but still untrusted method candidates
- stable reusable agent methods

Lifecycle labels like `draft / active / stale / deprecated` may still be useful, but they are secondary to the larger missing layer: where evolving experience lives before it becomes stable guidance.

### 4. Installation and trust

Hermes has a Skills Hub with trust levels, quarantine, audit, and security scanning for installed skills.

This repository already distinguishes local vs migrated skills and has migration discipline, but it does not yet have a formal trust model for imported skills. The current gap is not a full public hub; it is a minimal local trust-and-audit contract for adopted skills.

### 5. Verification, refresh, and incremental update

Hermes documentation frames skills as operational assets and supports explicit install/audit workflows. This repository has gone deeper in one narrow area by adding structural RED/GREEN checks for editable weekly visuals and requiring TDD when changing `skills/*`.

The gap is generalization and refresh semantics. Our strongest verification rules are currently concentrated in a few high-touch skills. We also do not yet clearly distinguish:

- not yet organized
- already organized
- changed and needs refresh
- stale and likely misleading

That means the repository still leans toward reprocessing from scratch instead of state-driven incremental refresh.

### 6. Human governance and incident traceability

This repository already has a better instinct for incident-driven governance than a generic skill folder, because we now:

- capture scope-drift retro pages
- tighten skills after concrete failures
- use OpenSpec to separate review from implementation

The remaining gap is consistency and role clarity. We need a stable contract for linking:

- incident
- affected skill
- baseline failure
- patch
- validation evidence

We also need a stable human-governance layer:

- the agent decides when to propose extraction or patching
- the human governs boundaries, approval level, and rollback
- the repository makes that governance visible through ADRs and retros

## ADR and retro split

This repository currently has retro capture but no stable ADR lane. To make self-evolution visible and reviewable, these two records need to be separated:

- `ADR`
  - what we decided
  - why we decided it
  - what boundary it sets
- `Retro`
  - what failed
  - why it failed
  - what changed afterward

For this review, the ADRs should live inside the change artifacts so they remain tied to the source comparison instead of being lost in chat history.

## Current strengths to preserve

- Strong OpenSpec boundary control after a completed change.
- Localized skill ownership inside the repository instead of hidden external dependencies.
- Explicit TDD expectations for semantic edits to `skills/*`.
- A concrete example of domain-specific structural verification in the project-management weekly skill.

## Candidate improvements

These are the likely follow-up changes, but they are out of scope for this review change:

1. Add explicit experience-extraction triggers for the agent.
2. Add a candidate-memory layer between raw execution and stable reusable method.
3. Add incremental refresh semantics for already-structured knowledge and weekly project-management material.
4. Add a repository skill index or compact inventory page for discovery and loading discipline.
5. Add a trust-and-audit contract for migrated external skills.
6. Add a generic verification matrix beyond the project-management weekly case.
7. Add a visible ADR template and a linked retro template for governance changes.

## Non-goals

- Do not rewrite the current skill architecture to match Hermes exactly.
- Do not auto-install Hermes patterns without a separate change.
- Do not edit unrelated skills as part of this review.
- Do not treat the Weixin article as a source of truth without checking the public Hermes repository/docs.
