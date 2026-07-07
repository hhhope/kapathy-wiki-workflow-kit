# Proposal

## Why

The repo mirror under `skills-drafts/account-skills/account-cr-agent/` no longer
matches the currently installed `account-cr-agent` skill bundle. The installed
bundle contains the CR coverage gate, rule config, replay fixtures, tests, and
formal-report profile behavior, while the repo mirror still contains an older
minimal `cr-agent` copy.

This makes the repository mirror a weak source for future promotion, evaluation,
or debugging work: a contributor reading the mirror would miss the current
coverage-gate contract and could reintroduce report-format conflicts.

## What Changes

- Sync the repo mirror of `account-cr-agent` from the currently installed local
  bundle.
- Preserve the mirror as ordinary repo content, not plugin-mode packaging and
  not active `.codex/skills` runtime registration.
- Include coverage-gate scripts, rules, replay fixtures, and tests in the
  mirrored `cr-agent` skill.
- Align mirrored `cr-report` and `release-diff-cr` content with the installed
  bundle for this machine.
- Add evaluation evidence that records source paths, before/after checks,
  pressure scenarios, validation commands, and residual rollout boundaries.

## What Does Not Change

- Does not install or publish any skill.
- Does not edit `.codex/skills/` in this repository.
- Does not change repo `AGENTS.md` routing.
- Does not claim future sessions use the mirror automatically.
- Does not resolve broader `open-code-review` candidate learning.
