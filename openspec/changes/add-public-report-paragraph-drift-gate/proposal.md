## Why

The current `public-report-quality-gate` blocks obvious public-report failures:
missing reference mapping, missing split strategy, voice leakage, premature
Feishu sync, and invalid scoring after a hard gate fails.

It still leaves a writing-judgment gap. A draft can pass coarse article-level
checks while individual sections or paragraphs quietly drift away from the
article's main line. It can also let the agent convert reference material or
smooth prose into a local judgment the user never made.

The user clarified the governing principle: process can be delegated, but
thought and judgment cannot. Public-report review therefore needs a paragraph
drift review and a judgment-ownership gate, not only a final publish gate.

## What Changes

- Add an Article Intent Contract before complex reader-facing drafting or
  review-ready claims.
- Require section and paragraph drift diagnostics for complex or
  drift-corrected public materials.
- Add a Judgment Ownership Gate that separates source-backed facts, agent
  organization, and user-owned conclusions.
- Allow diagnostic drift scores even when the overall scorecard remains
  `INVALID`.
- Extend the public-report reviewer template with reverse outline and
  paragraph-level review before scoring.
- Add pressure scenarios and evaluation evidence for the new behavior.

## Impact

- Updates `.codex/skills/public-report-quality-gate/`.
- Updates `.codex/agents/public-report-reviewer.md`.
- Updates `openspec/specs/public-report-quality-gate/spec.md` via spec delta.
- Updates `openspec/specs/public-report-reviewer-routing/spec.md` via spec
  delta.
- Adds focused tests for public-report gate behavior.
- Does not rewrite any existing public report or sync Feishu.
