---
name: openspec-explore
description: Use when the user wants to think through repository-level workflow or design changes before implementation, or when an active OpenSpec change needs exploration rather than coding.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.2.0"
---

Explore an OpenSpec topic without implementing code.

## Hard Rules

- Explore, inspect, compare, and clarify. Do not implement production changes under this skill.
- Use `openspec list --json` to see current change context when relevant.
- If a change already exists, read its local artifacts before proposing new direction.
- Offer to capture conclusions into proposal, design, specs, or tasks only after the reasoning is clear.

## Default Flow

1. Inspect repository context and current changes.
2. Clarify the problem, constraints, and trade-offs.
3. Read any relevant OpenSpec artifacts if a matching change exists.
4. Summarize findings, risks, and next recommended action.

## Output Contract

- State whether the discussion is pre-change or tied to an existing change.
- Summarize the main options or discoveries.
- State the next step: keep exploring, create a change, or update existing artifacts.

## Anti-Patterns

- Acting as if a special slash command is a required entrypoint
- Writing application code while still in explore mode
- Creating artifact churn before the problem framing is stable
