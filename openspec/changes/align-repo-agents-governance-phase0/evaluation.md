# Evaluation

## Baseline Scenarios

### Scenario 1: Candidate governance text is treated as if it were already accepted

- The repository has a candidate playbook and distill for `agents-governance-drift`
- A contributor wants to start migrating the repo `AGENTS.md`
- No accepted repo-level Phase 0 gate is written in stable surfaces yet

### Scenario 2: Repo work silently expands into root dotfiles

- The current user direction is repo-level `AGENTS.md` first
- Root dotfiles are related but not part of the confirmed repo mainline
- Without a repo-visible deferral rule, a later contributor can silently widen
  scope

### Scenario 3: Phase 1 starts while the repo still implies unresolved governance identity

- The repo governance surface still contains duplicate ADR numbering
- The repository has not made the repo-local commit-gate status explicit
- A contributor still tries to treat Phase 1 migration as ready

## RED Baseline

Before this change:

- the repository had no accepted repo-level Phase 0 gate for repo `AGENTS.md`
  migration
- the candidate playbook could be read as the nearest available mainline even
  though it explicitly stayed `candidate`
- root dotfiles had no stable repo-visible default deferral for this topic
- the ADR surface still contained duplicate `ADR-0007` numbering
- the repo-local commit-gate question was present in exploration, but not yet
  settled in stable repo guidance

So the failure was not lack of material. The failure was lack of a narrow,
accepted repo-level gate.

## GREEN Result

After this change:

- `openspec/specs/repo-agents-governance-phase0/spec.md` defines the repo-level
  Phase 0 contract
- `wiki/adr/0027-repo-phase0-before-repo-agents-migration.md` accepts the narrow
  repo-level Phase 0 mainline
- `AGENTS.md` explicitly blocks repo `AGENTS.md` migration until Phase 0 is
  accepted and keeps root dotfiles out of automatic scope
- the duplicate `ADR-0007` conflict is removed by renumbering the draft-surface
  ADR to `ADR-0026`
- the repository now states that commit-gate status must be explicit before
  Phase 1, while not pretending a hook implementation already exists

## Residual Risks

- This change does not implement a repo-local commit hook.
- This change does not perform Phase 1 `AGENTS.md` compression.
- Candidate governance pages still exist and may need later archive or further
  calibration, but they are no longer the nearest implied accepted mainline.
