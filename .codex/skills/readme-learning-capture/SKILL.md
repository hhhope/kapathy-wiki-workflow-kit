---
name: readme-learning-capture
description: Use when the user provides a GitHub or GitLab repo or README and wants to learn what should be reused, adapted, rejected, or formalized in this repository.
---

# README Learning Capture

## Overview

Turn GitHub / GitLab README analysis into repository learning, not just source summary.

## When to Use

- The user provides a GitHub or GitLab repo link.
- The user asks to analyze a README, compare approaches, or extract what is worth copying.
- The user wants the result turned into wiki, a template, a skill candidate, or a workflow decision.

Do not use this skill for ordinary article summarization or for generic code review without README-driven learning intent.

## Rules

- Start from the README or repo-level operating docs, then extract repository learning.
- Preserve the adaptation boundary. Capture at least:
  - source
  - what was reused
  - what was modified
  - what was rejected or not yet formalized
  - repo target
- Do not stop at generic summary if the user is clearly asking what should change in this repository.
- Reuse existing routing:
  - `wiki/ops` for workflow and governance learning
  - `wiki/examples` for validated output-shape examples
  - `wiki/team-lore-candidates.md` only after a project-local page already exists
  - `OpenSpec change` when the learning becomes a scoped repository change
- Follow [AGENTS.md](../../../AGENTS.md) and [example-driven wiki capture](../../../wiki/ops/example-driven-wiki-capture.md) instead of inventing a separate storage model.

## Output Checklist

- Name the source repo or README
- State what is worth reusing
- State what should be adapted instead of copied
- State what is still not formalized
- Pick the repo target

## Common Mistakes

- Writing only a README summary with no repository adaptation
- Copying the source structure directly without checking repo boundaries
- Forgetting to create the wiki record when the reusable takeaway is already clear
- Treating every GitHub or GitLab link as worth a durable page
