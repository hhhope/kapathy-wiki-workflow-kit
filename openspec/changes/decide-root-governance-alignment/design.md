## Confirmed Boundaries

The last confirmed requirement is to repair
`decide-root-governance-alignment` into a reviewable design state. This step is
not root dotfile implementation, skill authoring, wiki method publication, or
runtime enforcement.

Current chain being followed:

1. Record the design boundary in this active OpenSpec change.
2. Make overclaiming visible where candidate wording was written as a decision.
3. Leave implementation and promotion decisions for review.

Drift judgment: the previous draft drifted by using decision language before
the alignment model was accepted. The repair must separate confirmed process
boundaries from candidate content.

Confirmed boundaries:

- SDD-first: root dotfile, skill, or wiki method changes must not happen from a
  chat-level plan alone. The active OpenSpec change must record the boundary,
  evaluation evidence, and open decisions first.
- Wiki-gated: wiki can be a trace or retro candidate when recovery needs outlive
  the change, but it is not the default landing place for a method page or ADR.
- Root files are out of scope for this step: do not edit `~/.codex/AGENTS.md`,
  `~/.claude/CLAUDE.md`, repo-local skills, or wiki method pages.
- Replay harness v1 is an evidence contract only. Here, "replay harness" means a
  small set of recorded scenarios, expected RED/GREEN outcomes, and proof
  boundaries that can be replayed to check whether a design overclaims. It is
  not a hook, CI gate, runtime gate, or automatic enforcement mechanism.

## Candidate Design

Candidate model: hybrid split with explicit ownership, pending review.

This candidate says the repository may record the relationship between repo
governance and personal root dotfiles, but it does not own the full content of
personal global dotfiles. Root files may align on shared safety boundaries while
keeping personal or agent-specific behavior separate.

Candidate required alignment:

- When operating inside this repository, root files should not contradict
  repo-owned boundaries.
- Repo `AGENTS.md`, `PROJECT.md`, and active OpenSpec changes should remain the
  source of repo-specific workflow semantics.
- Behavior-asset changes should have evaluation evidence before they are
  treated as complete.

Candidate allowed divergence:

- personal global startup preferences
- agent-specific capability differences
- cross-repo defaults that are not specific to this repository
- local machine paths, provided they are not mistaken for repo policy

Candidate collaboration split:

- `AGENTS.md` as an entry card: scope, hard stops, startup gates, git truth
  rules, and routing to deeper assets.
- `SKILL.md` as compact behavior contracts: trigger conditions, hard rules,
  anti-patterns, and short loading pointers.
- replay harness as evidence: RED/GREEN behavior records and proof boundaries.

Candidate update burden:

- This change records design evidence only.
- Any later root sync should be a minimum wording update, not a broad rewrite.
- If review rejects the candidate model, no root sync should proceed from this
  change.

## Open Questions

- Should the final root/repo relationship be hybrid split, intentional
  divergence, full alignment on selected clauses, or something else?
- Which exact clauses must align across repo `AGENTS.md`,
  `~/.codex/AGENTS.md`, and `~/.claude/CLAUDE.md`?
- Who owns future updates when root defaults and repo policy disagree?
- What is the final responsibility split among `AGENTS.md`, `SKILL.md`, and
  replay-harness evidence?
- Is a targeted `wiki/ops retro` needed for this correction, or is the active
  change sufficient durable recovery?
- What evidence is required before archive readiness?

## Review Criteria

The design is ready for review when:

- confirmed boundaries are written as decisions, and candidate content is
  labeled as candidate
- no root dotfile, repo skill, or wiki method page is edited
- `tasks.md` does not mark final alignment, ownership, or collaboration model
  decisions complete
- evaluation records the RED baseline, current after-state, and residual risks
  without claiming runtime behavior changed
- OpenSpec validation passes
