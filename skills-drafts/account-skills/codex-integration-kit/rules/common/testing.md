# Testing Rules

## Verification Priorities

- Backend API/service/repository changes require at least endpoint-level or function-level verification.
- Frontend interaction changes should be validated on a real page or dev server when possible; a successful build alone is insufficient.
- DB migration changes should follow a `dry-run -> apply` mindset and verify row counts, ownership fields, and rollback boundaries.

## 409 / Concurrency Changes

- Do not verify by UI toast alone. Use real API requests to check status codes, final `version`, and backend logs.
- Validate stale-version absorption, retry behavior, and conflict messaging as separate behaviors.

## Sync / Notify Paths

For sync, process, and notification flows, verify at least:

- request placeholders are rendered into real values
- raw data is stored under the current team
- process filter/SQL output matches expectations
- bound notifiers send notifications, while unbound processes execute without accidental notification
- batch detail and logs expose key state transitions and failure reasons
