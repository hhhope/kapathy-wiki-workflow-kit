# Pressure Wiki Index

## Projects

- [[projects/payments-core/overview]] — payment orchestration, callback safety, retry workers
- [[projects/settlements-core/overview]] — settlement reconciliation and replay safety
- [[projects/auth-core/overview]] — login, session refresh, redirect stability

## Pitfalls

- [[pitfalls/idempotency-keys]] — duplicate callbacks or replays cause duplicate writes
- [[pitfalls/timeout-fallback]] — external calls without timeout/fallback stall workers
- [[pitfalls/session-refresh-loop]] — auth refresh loops bounce users back to login

## Principles

- [[principles/boundary-first]] — stay inside approved external boundaries with explicit timeout and fallback
