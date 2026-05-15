# Design: Wiki Medical Loop Skills

## Scope

This change repairs the skill surface only. It does not change runtime package
builders or the existing generated record formats.

## User-Facing Names

The user-facing medical-loop skill sequence is:

```text
wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery
```

`wiki-review-decisions` remains as a compatibility alias for older references,
but it is no longer the preferred user-facing name.

## Skill Contracts

`wiki-confirm` owns the confirmation stage. It routes doctor output into draft
decision buckets and records. It does not approve repair.

`wiki-treatment` owns bounded low-risk frontmatter repair after explicit human
approval. It defaults to dry-run and writes only approved suggested frontmatter
when `--apply` and approval flags are both present.

`wiki-surgery` owns large structural and governance-sensitive planning. It is
plan-only and does not write frontmatter, relations, taxonomy, MOC, ADR, or
OpenSpec state.

`wiki-recovery` owns post-treatment or post-surgery proof. It runs bounded
non-mutating checks and records failures as findings.

`wiki-doctor` stays primarily diagnostic in this phase but must expose the
stage sequence and next-stage routing hints in natural language.

## Drift Fix

The previous implementation drifted because tests targeted Python executors and
only one skill marker. This change adds marker tests for the full stage surface
and for the legacy alias boundary.

## Boundaries

Skills are English-first behavior assets with Chinese stage labels where useful
for user-facing intent matching. Each skill references its implementation CLI,
but the skill body must describe the agent behavior first and CLI flags second.
