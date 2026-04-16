# Evaluation

## Baseline Scenarios

1. A repo-local skill is authored inside a Chinese-first repo and the authoring chain must decide whether the skill body should follow wiki language or stay English-first.
2. A repo-local workflow skill affects Feishu-facing delivery and the authoring chain must decide whether repo delivery constraints are mandatory input or optional context.
3. A repo-local skill starts accumulating repeated repo policy and long examples, and the authoring chain must decide whether to keep them inline or move them out of `SKILL.md`.

## Before Results

- Shared authoring guidance did not define a default language contract for behavior assets:
  - `writing-skills` had no English-first rule
  - `skill-creator` was itself Chinese-bodied
  - `development-workflow` required evaluation for skill changes but did not define language, repo-constraint scan, or compact-body defaults
- Repo-local skills showed the failure directly:
  - `meeting-note-output` body was Chinese and carried long inline workflow prose
  - `material-collaboration-defaults` repeated repo behavior that already lived in `AGENTS.md`
  - the four principle skills were Chinese-bodied even though they are high-frequency retrieval assets
- Repo-local Feishu constraints existed in `AGENTS.md`, but the shared authoring chain did not force authors to read repo delivery boundaries before writing skills.

## After Results

- Shared authoring guidance now carries the default contract:
  - `writing-skills` defines English-first behavior assets, repo-constraint scanning, and compact `SKILL.md` bodies
  - `skill-creator` now routes new skill work through that same contract
  - `development-workflow` now states the shared skill-authoring defaults at the rule layer
- Repo-local guidance now binds only the repo-specific boundary:
  - `AGENTS.md` defines the repo-local skill authoring contract and keeps Feishu-sensitive delivery rules in repo policy
- Current repo-local skills were refactored to match the contract:
  - principle skills are English-first
  - workflow skills are English-first and shorter
  - meeting-note output keeps Feishu and fixed-format constraints, but now references repo policy instead of re-explaining the whole workflow inline

## Residual Risks

- This is behavior evidence from file-level before/after inspection, not a fresh multi-session rollout test.
- Shared files under `/home/yan/.codex/` are outside this repo's git history, so the repo can document the contract but cannot version those shared edits here.
- There is still no mechanical lint that proves every future repo-local skill stays English-first and compact; current enforcement is rule-based plus review-based.
