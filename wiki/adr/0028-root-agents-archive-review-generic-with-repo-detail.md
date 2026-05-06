# ADR-0028 Root AGENTS Archive-Review Semantics Stay as Generic Top-Level Rules With Repo-Owned Detail

## Status

Accepted

## Context

During `compress-codex-agents-md`, intake finding C2 flagged that `~/.codex/AGENTS.md` L110-122 (13 lines of `## OpenSpec boundary`) was "self-violating the repo-semantics-stay-in-repo line." The question the compression change had to settle: what portion of OpenSpec lifecycle guidance belongs in the cross-repo root card, and what belongs in each repo's `AGENTS.md`?

Three options were weighed:

1. Root keeps a compact tool-generic shape (8 lines: "complete is a stop condition, default next action is archive review, repo-local detail lives in each repo's AGENTS.md"). Each repo's AGENTS.md carries its own archive-review detail (disagreement material checks, wiki promotion gates, retro rules).
2. Root keeps all 13 lines unchanged and retracts the intake C2 finding. Justification: OpenSpec is a cross-repo tool, so its lifecycle semantics are cross-repo.
3. Move OpenSpec archive-review into a triggered `~/.codex/skills/openspec-archive-review/SKILL.md`. Root keeps only 3 lines pointing to the skill.

Option 3 looked purest but hit a real constraint: skill triggering in Anthropic Agent Skills is a natural-language similarity match with ~85% hit rate, not 100%. For short, stable, high-criticality rules ("complete is a stop condition" must be known every time an OpenSpec change closes), 85% is not enough — a miss means the agent silently keeps working past the stop boundary. Skills are the right container for long, intermittent capabilities (e.g., visual-governor workflows), not for short always-applicable rules.

Option 2 conflicted directly with the Pattern Catalog adopted in `2026-05-06-decide-root-governance-alignment`, whose Root AGENTS entry explicitly lists `archive-review detail` under `Must Not Own`. Keeping all 13 lines would require a retraction of the just-signed Pattern Catalog.

## Decision

- Root `~/.codex/AGENTS.md` keeps only OpenSpec tool-generic semantics: what "complete" means, what the default next action is, that out-of-scope requires a new change. Roughly 8 lines.
- Root ends the section with an explicit pointer: `Repo-local archive-review detail (wiki promotion, retro gates, etc.) lives in each repo's AGENTS.md.`
- Each repo's `AGENTS.md` carries the repo-specific archive-review rules. New repos that adopt OpenSpec inherit the 8 root lines automatically; they then author their own repo-specific detail when they need it.
- No `openspec-archive-review` skill is created at this time.

## Consequences

- When a new repo adopts OpenSpec, `codex` immediately knows the stop boundary and archive-review default. No initialization template step is required.
- Repo-specific archive-review detail (disagreement material checks, `archive-review.md` content convention, retro rules) must be written in each repo's `AGENTS.md`. There is no shared template file for this; the discipline is repo-by-repo authorship.
- Cross-repo divergence is possible: two repos may disagree on what counts as a routine closing tail versus a scope-ambiguity blocker. That divergence is accepted as repo-specific latitude, not drift.
- If at some future point three or more repos use OpenSpec deeply and their archive-review detail converges, a follow-up ADR should revisit whether extracting the shared detail into `~/.codex/skills/openspec-archive-review/` (option 3 revisited) becomes worthwhile. The current 85% skill trigger rate is the accepting threshold that would need to rise, or the volume of use would need to grow enough that missed triggers are acceptable against the centralization gain.
- The 283-line root file is not the final compression target. Line-count compression is deferred to a successor change (see `compress-codex-agents-md` evaluation §Budget Status).
