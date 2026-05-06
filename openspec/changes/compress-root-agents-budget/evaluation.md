# Evaluation

## Baseline Scenarios

1. Archived `compress-codex-agents-md` ended with Pattern Catalog compliance
   but did not prove reduced drift from root context.
2. The first successor framing overfit to line count: extract `Global Rule
   Routing` into `~/.codex/rule-routing.md`, then load that file for
   non-trivial work.
3. That shape is fake progressive disclosure: file size drops, but default
   practical context for non-trivial work does not.
4. `~/.codex/AGENTS.md` is personal root guidance outside this repository's git
   tracking, so repo evidence must preserve before/after counts and scope.

## Before Results

- File: `~/.codex/AGENTS.md`
- Baseline count at change start: 283 lines, 1865 words, 12459 bytes.
- `Global Rule Routing`: 30 lines, 313 words, 2733 bytes.
- `Global Rule Routing` share of root AGENTS: about 10.6% of lines, 16.8% of
  words, and 21.9% of bytes.
- Baseline support file: not present at change start.
- Baseline section mapping: pending implementation.

## Harness Engineering Gate

### RED Scenario

Move `Global Rule Routing` out of `~/.codex/AGENTS.md` into
`~/.codex/rule-routing.md`, then instruct root `AGENTS.md` to load that file
before non-trivial implementation or verification.

Expected result: **FAIL**.

Reason: `AGENTS.md` line count drops, but the dominant non-trivial path still
loads the moved text. The plan optimizes file appearance rather than loaded
context or drift prevention.

### GREEN Behavior

Root `AGENTS.md` retains always-on hard stops and routing principles. Task
details load only after a concrete trigger such as git boundary, skill
authoring, frontend work, migration work, or security-sensitive code.

Moving text to another file counts as reduction only when the moved text is no
longer loaded on the default path.

## After Results

Pending implementation.

## Self-Check

| Column | Result | Evidence |
|---|---|---|
| Structural | pass | `openspec validate compress-root-agents-budget --strict` returned valid on 2026-05-06 |
| Semantic | pass | Target remains Root AGENTS; support files are allowed only as trigger-gated references |
| Evidence | partial | Baseline counts and RED/GREEN gate recorded; after loaded-context metrics wait for root implementation |
| Boundary | pass | No new Pattern Catalog pattern, checklist item, skill, wiki method page, or repo policy introduced |

## Residual Risks

- `~/.codex/` is outside this repository's git tracking.
- A support file can become hidden default context if root `AGENTS.md` points to
  it too broadly.
- Line count can still be useful supporting evidence, but it can no longer be
  treated as the primary success metric.
