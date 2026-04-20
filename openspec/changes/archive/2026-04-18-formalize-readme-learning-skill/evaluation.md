## Evaluation

### Behavior Expected To Change

- Before this change, GitHub / GitLab README analysis relied on generic prompting and could stop at source summary.
- After this change, these requests should route through a dedicated skill that preserves adaptation boundaries and repo targets.

### RED Baseline

Baseline without dedicated skill:

- a repo README can be analyzed
- the result may identify useful points
- but the workflow is generic and may stop at summary or partial adaptation notes

Evidence:

- prior repository example guidance listed generic skills only:
  - `material-collaboration-defaults`
  - `openspec-explore`

### GREEN Result

After change:

- a dedicated repo-local skill exists:
  - `.codex/skills/readme-learning-capture/SKILL.md`
- GitHub README analysis example guidance now points to this skill
- the skill explicitly requires:
  - source
  - reused
  - modified
  - rejected or not formalized
  - repo target

### Residual Risks

- This change defines workflow and trigger shape, not a special fetch implementation.
- Later changes may still add source-fetch helpers or tighter GitHub/GitLab-specific tooling.
