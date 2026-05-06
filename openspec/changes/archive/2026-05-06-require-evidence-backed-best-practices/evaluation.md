# Evaluation

## Baseline Scenarios

1. External article learnings were captured, but the implementation gate was
   weak enough that a vague "best practice" could still be treated as an
   adopted rule.
2. The repo already has `Example-Driven Capture Default`, but it focuses on
   capturing reusable learning, not on preventing unsupported promotion into
   behavior assets.
3. A skill would be the wrong landing layer because this constraint must apply
   before skill selection; it is a repository-default promotion gate.

## Before Results

- Repo `AGENTS.md` had example-driven capture rules for wiki landing.
- Repo `AGENTS.md` had skill evaluation evidence rules for semantic skill
  changes.
- Repo `AGENTS.md` did not have a general evidence gate for promoting
  article-derived or example-derived learning into behavior assets.

## After Results

- Repo `AGENTS.md` now has an `Evidence-Backed Best Practice Gate` after
  `Example-Driven Capture Default`.
- The gate states that reusable learning can be captured, but promotion into a
  behavior asset requires evidence.
- The accepted evidence shapes are exactly:
  external-document excerpt, local demo/fixture, and git-like project
  comparison.
- The gate explicitly says this is a repo-default promotion constraint, not a
  skill.

## Self-Check

| Column | Result | Evidence |
|---|---|---|
| Structural | pass | `openspec validate require-evidence-backed-best-practices --strict` returned valid on 2026-05-06 |
| Semantic | pass | Landing layer is repo `AGENTS.md`; this is not hidden behind a skill trigger |
| Evidence | pass | `AGENTS.md` and spec delta both require evidence before promotion |
| Boundary | pass | No root dotfile, skill, or wiki method page changed |

## Residual Risks

- This gate is still prose-level. It will not mechanically block a future
  unsupported promotion unless an agent follows repo `AGENTS.md`.
- If repeated failures occur, a later change can add a replay harness or
  structural checker. That is intentionally out of scope here.
