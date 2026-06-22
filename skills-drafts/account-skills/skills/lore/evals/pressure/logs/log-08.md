---
id: log-08
project: payments-core
reviewed: false
---

# Log — worker fallback omitted

## Deviation signal
Retry worker timed out but had no defined fallback path.

## What happened
The worker retried blindly after timeout and left downstream state ambiguous.

## Why it matters
This is a reusable timeout/fallback pitfall.

