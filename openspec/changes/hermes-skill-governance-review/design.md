## Overview

This change is a review-and-trace change, not an implementation change. Its job is to record a grounded comparison between:

- the Weixin article `一文搞懂Hermes：新顶流Agent如何从经验中自我进化`
- the public GitHub project `NousResearch/hermes-agent`
- the current repository's skill-governance model

The output should answer three questions:

1. What governance mechanisms does Hermes make explicit?
2. Which of those mechanisms already exist here in a different form?
3. Which gaps are real enough to justify future OpenSpec changes?

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

The review compares Hermes and this repository across five dimensions.

### 1. Discovery and loading

Hermes makes skill discovery and loading explicit through:

- `skills_list()` as a compact inventory
- `skill_view(name)` for full content
- `skill_view(name, file_path)` for targeted reference loading
- explicit progressive disclosure to control token cost

This repository already follows a lighter version of progressive loading through the session-level skill list and selective file opening, but the policy is not yet codified as a repository governance pattern. It is mostly enforced by model instructions and manual discipline.

### 2. Lifecycle and maintenance

Hermes treats skills as procedural memory that can be created, patched, edited, and deleted through a dedicated `skill_manage` workflow. Hermes docs also make stale-skill maintenance explicit.

This repository already has:

- local skill authoring
- migration from external skills
- incident-driven skill tightening
- explicit TDD expectations for semantic skill edits

The gap is lifecycle state and maintenance policy. We do not yet track whether a skill is `draft`, `active`, `stale`, or `deprecated`, and we do not yet require a stale-skill review loop.

### 3. Installation and trust

Hermes has a Skills Hub with trust levels, quarantine, audit, and security scanning for installed skills.

This repository already distinguishes local vs migrated skills and has migration discipline, but it does not yet have a formal trust model for imported skills. The current gap is not a full public hub; it is a minimal local trust-and-audit contract for adopted skills.

### 4. Verification and rollback

Hermes documentation frames skills as operational assets and supports explicit install/audit workflows. This repository has gone deeper in one narrow area by adding structural RED/GREEN checks for editable weekly visuals and requiring TDD when changing `skills/*`.

The gap is generalization. Our strongest verification rules are currently concentrated in a few high-touch skills. We do not yet have a shared verification matrix for all skill categories.

### 5. Incident traceability

This repository already has a better instinct for incident-driven governance than a generic skill folder, because we now:

- capture scope-drift retro pages
- tighten skills after concrete failures
- use OpenSpec to separate review from implementation

The remaining gap is consistency. We need a stable contract for linking:

- incident
- affected skill
- baseline failure
- patch
- validation evidence

## Current strengths to preserve

- Strong OpenSpec boundary control after a completed change.
- Localized skill ownership inside the repository instead of hidden external dependencies.
- Explicit TDD expectations for semantic edits to `skills/*`.
- A concrete example of domain-specific structural verification in the project-management weekly skill.

## Candidate improvements

These are the likely follow-up changes, but they are out of scope for this review change:

1. Add skill lifecycle metadata and stale-review policy.
2. Add a repository skill index or compact inventory page for discovery and loading discipline.
3. Add a trust-and-audit contract for migrated external skills.
4. Add a generic skill verification matrix beyond the project-management weekly case.
5. Add a traceability template that links incidents, patches, and validation evidence.

## Non-goals

- Do not rewrite the current skill architecture to match Hermes exactly.
- Do not auto-install Hermes patterns without a separate change.
- Do not edit unrelated skills as part of this review.
- Do not treat the Weixin article as a source of truth without checking the public Hermes repository/docs.
