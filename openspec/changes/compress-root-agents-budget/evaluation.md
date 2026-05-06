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
5. External harness-engineering sources converge on a stronger target:
   root guidance should act as an agent-legible map backed by source-of-record
   artifacts, feedback loops, and recoverable progress state.

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

## External Article Calibration

The 2026-05-06 article pass changes the target from "compress root context" to
"make root context an agent-legible governance harness."

Local target criteria:

- **Map, not manual**: `AGENTS.md` points to source-of-record artifacts instead
  of inlining detailed knowledge.
- **Legible environment**: the agent can inspect the right repo-visible files,
  validation commands, and recovery notes without relying on chat memory.
- **Stable interfaces over stale assumptions**: root instructions should be
  hard stops, stable source pointers, trigger-gated detail, or candidate
  assumptions marked for review.
- **Feedback loop**: gather context -> act -> verify -> leave artifact.
- **Evaluation by outcome**: grade whether the agent finds the right source,
  verifies the intended behavior, and leaves recoverable state; do not require
  one exact path when multiple valid paths exist.

## Evidence Standard for Best Practices

Best practices are adoptable only when backed by one of these evidence shapes:

| Evidence shape | Required proof | What it can support |
|---|---|---|
| External documentation | URL, publish/access date when available, exact section or line reference, narrow claim boundary | Candidate or adopted principle when the claim is directly supported |
| Local demo / fixture | RED/GREEN scenario, input/output, command or manual replay record | Behavior claim about this repository or this agent workflow |
| Git-like project comparison | Repository, commit/path, and observable structure or behavior difference | Structural analogy or implementation pattern, not universal proof |

Practices without one of these evidence shapes stay as candidate observations.
They must not enter root `AGENTS.md`, spec `SHALL`, skill hard rules, or
archive-ready claims.

## After Results

Pending implementation.

## Self-Check

| Column | Result | Evidence |
|---|---|---|
| Structural | pass | `openspec validate compress-root-agents-budget --strict` returned valid on 2026-05-06 |
| Semantic | pass | Target remains Root AGENTS; support files are allowed only as trigger-gated references |
| Evidence | partial | Baseline counts, RED/GREEN gate, article calibration, and evidence standard recorded; after loaded-context and agent-legibility metrics wait for root implementation |
| Boundary | pass | No new Pattern Catalog pattern, checklist item, skill, wiki method page, or repo policy introduced |

## Residual Risks

- `~/.codex/` is outside this repository's git tracking.
- A support file can become hidden default context if root `AGENTS.md` points to
  it too broadly.
- Line count can still be useful supporting evidence, but it can no longer be
  treated as the primary success metric.
