# Pitfall — timeout-fallback

## Trigger signals

- slow provider
- hanging HTTP call
- retry worker backlog
- missing fallback

## Failure mode

Workers stall on long external calls, retries pile up, and downstream systems receive inconsistent signals.

## Avoidance

- set explicit timeouts
- define fallback behavior
- keep retries inside approved boundaries

## Boundary

Does not cover pure in-process compute without external dependencies.
