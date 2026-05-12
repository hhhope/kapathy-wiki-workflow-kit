# Archive Review

## Decision

Archive with `--skip-specs`.

## Reason

The change is complete and validated, but normal archive spec replay is blocked
by a stale removal delta:

- `repo-skill-namespace-surface` no longer contains
  `Repo SHALL avoid namespaced OpenSpec runtime skills`.
- The current main spec already states that OpenSpec helpers are repo-local
  under `.codex/skills/openspec-*`.
- The follow-up change `remove-root-runtime-skill-duplicates` owns the remaining
  root/user-scope duplicate boundary.

The failed normal archive attempt made no file changes.

## Verification

- `openspec list` reports the change as complete.
- `openspec validate restore-repo-local-runtime-skills --strict` passed.
- `openspec validate --all` passed: 53 items, 0 failed.

PostHog DNS flush errors were telemetry noise after local validation results.

## Residual Risk

This review does not claim the historical delta can be replayed from an older
spec baseline. It records that the current main specs already carry the intended
repo-local runtime direction, while the follow-up duplicate-removal change
owns the stricter cleanup rule.
