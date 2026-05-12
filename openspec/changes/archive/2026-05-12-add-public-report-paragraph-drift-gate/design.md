## Context

The existing public report gate is intentionally lightweight. It coordinates
reference mapping, learning use, split decisions, review routing, scoring, and
Feishu delivery boundaries. The reviewer template carries heavier review logic
for complex outputs.

The new behavior should follow that split:

- `SKILL.md` keeps the trigger and hard-rule surface compact.
- `references/scorecard.md` owns gate definitions and diagnostic scoring.
- `references/gate-review-artifact.md` owns persisted evidence shape.
- `.codex/agents/public-report-reviewer.md` owns the detailed manual review
  steps.
- `pressure-scenarios.md` owns regression replay language.

## Design

### Article Intent Contract

Before complex public drafting or review-ready claims, the process records:

- reader
- reader decision or action
- main line
- non-goals
- user-owned judgments
- agent-allowed operations

This establishes the baseline for drift. Without it, paragraph scoring has no
anchor.

### Section And Paragraph Drift Review

The gate-review artifact records a matrix for sections and important
paragraphs:

- section objective
- paragraph claim
- mainline role
- target fit score
- narrative drift score
- evidence fit score
- judgment source
- action

The drift scale is 0-5:

- 0: fully serves the main line
- 1: weak but acceptable support
- 2: related but should be compressed
- 3: drifting and should be rewritten
- 4: changes the article judgment and needs user review
- 5: violates the target or replaces user judgment

### Judgment Ownership Gate

The gate blocks review-ready claims when the agent silently decides:

- article main line
- strategic conclusion
- prioritization
- public-facing stance
- local proof strength

The agent may organize, summarize, rewrite, and propose alternatives, but
conclusions and stance must be sourced or user-confirmed.

### Diagnostic Scores With Invalid Overall Score

Existing behavior correctly blocks numeric overall scoring when any hard gate
is not fully passed. This change preserves that rule while allowing diagnostic
paragraph scores. The artifact can therefore say:

- overall score: `INVALID`
- section drift diagnostics: available
- required action: retain, compress, rewrite, delete, or ask the user

## Boundaries

- This change does not automate article scoring.
- This change does not make the agent the owner of public stance or local
  conclusions.
- This change does not make existing drafts review-ready retroactively.
- This change does not alter Feishu write behavior.
