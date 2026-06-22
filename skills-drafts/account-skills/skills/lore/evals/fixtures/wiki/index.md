# Lore Wiki Index

## Projects

- [[projects/payments-core/overview]] — payment orchestration, retry workers, callback safety

## Pitfalls

- [[pitfalls/idempotency-keys]] — repeated callbacks or retries can double-write state
- [[pitfalls/timeout-fallback]] — provider calls without timeout/fallback stall workers

## Principles

- [[principles/boundary-first]] — call only approved external boundaries and degrade safely
