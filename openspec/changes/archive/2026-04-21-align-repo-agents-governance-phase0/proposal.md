## Why

The repository has accumulated enough governance evidence around
`agents-governance-drift` to show a real problem, but not yet enough accepted
decision material to justify directly rewriting the repo-level `AGENTS.md`.

The current situation is unstable in a specific way:

- the repository already has a candidate playbook for AGENTS-governance drift
- that playbook explicitly says it is `candidate`, not `accepted`
- the only current active/completed OpenSpec change in this area validates
  distill-calibration structure, not governance acceptance
- the repo still has at least one immediate contradiction inside the current
  governance surface: duplicate `ADR-0007` numbering

The next useful step is therefore not Phase 1 compression. It is a narrower
repo-level Phase 0 change that decides whether and how the repository should
accept a stable mainline for repo-level AGENTS governance work.

## What Changes

- Create a repo-scoped Phase 0 governance change for `agents-governance-drift`
  before any repo-level `AGENTS.md` compression or proxy migration begins.
- Define the acceptance boundary for repo-level AGENTS governance:
  what must be accepted now, what must be implemented before migration, and
  what stays deferred.
- Resolve the duplicate `ADR-0007` numbering conflict as part of the repo-local
  governance cleanup required by Phase 0.
- Decide whether a repo-local commit gate such as `.githooks/pre-commit` is
  part of the repo Phase 0 acceptance set.
- Record explicit deferrals for:
  - root-level `~/.codex/AGENTS.md`
  - root-level `~/.claude/CLAUDE.md`
  - Phase 1 `AGENTS.md` compression / proxy migration
  - broader `evaluation.md` field harmonization

## Capabilities

### New Capabilities

- `repo-agents-governance-phase0`: The repository SHALL establish an accepted
  repo-level Phase 0 mainline before executing AGENTS-governance migration on
  the repo `AGENTS.md`.

### Modified Capabilities

- `personal-ops`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/align-repo-agents-governance-phase0/`.
- Prepares a narrow repo-level decision path for AGENTS-governance work without
  yet compressing or proxy-migrating `AGENTS.md`.
- Creates the formal scope needed to decide the repo-local gate set and to fix
  the duplicate `ADR-0007` conflict.
- Keeps root dotfiles and later migration phases out of scope unless a later
  change explicitly brings them in.
