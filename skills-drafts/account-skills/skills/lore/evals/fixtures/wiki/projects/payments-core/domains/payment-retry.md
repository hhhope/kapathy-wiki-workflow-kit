# Domain — payment-retry

## Scope

Retry workers, retry backoff, provider calls, and timeout boundaries.

## Current facts

- workers call external providers
- retry behavior must not create duplicate downstream writes

## Risks and watchpoints

- provider calls that hang without timeout
- retries that cross service boundaries without fallback

## Related pitfalls

- [[pitfalls/timeout-fallback]]

## Related principles

- [[principles/boundary-first]]
