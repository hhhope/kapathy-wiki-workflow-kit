# Close visual-agent runtime loop

## Why

The previous visual-agent changes improved the controller text, but the repo
runtime still drifts:

- `.codex/skills/visual-agent` is installed locally without the visual worker
  skills it routes to;
- the installed repo-local controller lags behind the account-skills branch
  wording;
- behavior evidence proves controller wording but not runtime discovery after
  local installation;
- the live drift trace is not connected to the actual repo-local repair.

This makes the user-visible failure plausible even after a package branch is
pushed: account-skills may contain workers, but this repository runtime still
cannot discover them.

## What Changes

- Bring the repo-local `.codex/skills/visual-agent` runtime card and evaluation
  in line with the bundled-worker model.
- Add the visual worker skill directories that the repo-local controller routes
  to under `.codex/skills/`.
- Add runtime discovery and fixed-phrase pressure evidence to this change's
  `evaluation.md`.
- Update the visual-agent drift trace with the repair result and remaining
  account-skills follow-up boundary.

## Out of Scope

- Editing `/mnt/d/skills/account-skills` in this repo-local phase.
- Producing visual assets.
- Archiving older visual-agent changes.
- Changing global user-scope skills under `/home/yan/.codex/skills`.

