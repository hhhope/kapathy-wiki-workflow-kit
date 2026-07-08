# Proposal

## Why

The repository mirror under `skills-drafts/account-skills/` has drifted from
the external source at `/mnt/d/skills/account-skills`. Recent work only synced
the CR-related subset, which left the broader `account-skills` tree outdated
and made the commit history misleading for readers expecting a full mirror
refresh.

## What Changes

- Refresh the non-plugin account-skills mirror from `/mnt/d/skills/account-skills`.
- Keep excluded local/plugin/generated state out of the repo mirror.
- Preserve the repo-specific mirror README files that document the no-plugin
  boundary.
- Record validation evidence and commit the refreshed mirror.

## What Does Not Change

- Does not create a `skills/account-skills/` directory.
- Does not install or publish a plugin.
- Does not register mirrored skills as active `.codex/skills` runtime routes.
- Does not semantically rewrite imported skills.
