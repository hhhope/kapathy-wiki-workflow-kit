## 1. Change Setup

- [x] 1.1 Create OpenSpec artifacts for the repo-level AGENTS governance
  Phase 0 change

## 2. Acceptance Boundary

- [x] 2.1 Confirm the repo-level Phase 0 scope and non-goals in change
  artifacts
- [x] 2.2 Record whether the accepted repo-level mainline is:
  - a narrow Phase 0 gate only
  - or an explicitly defined repo-level subset of the candidate v3.1 model
- [x] 2.3 Record explicit deferrals for:
  - root-level `~/.codex/AGENTS.md`
  - root-level `~/.claude/CLAUDE.md`
  - Phase 1 `AGENTS.md` compression / proxy migration
  - broader `evaluation.md` harmonization

## 3. Repo Governance Cleanup

- [x] 3.1 Remove the duplicate `ADR-0007` numbering conflict
- [x] 3.2 Add or update the repo-visible stable decision that records the
  accepted repo-level Phase 0 mainline
- [x] 3.3 Decide whether a repo-local commit gate such as `.githooks/pre-commit`
  is required before Phase 1 can begin

## 4. Readiness Gate

- [x] 4.1 Verify the repository no longer treats `candidate` governance wording
  as `accepted` by implication
- [x] 4.2 Verify the duplicate-ADR conflict is gone before calling Phase 0
  complete
- [x] 4.3 Verify that Phase 1 remains blocked until the accepted repo-level
  gate set is explicit
