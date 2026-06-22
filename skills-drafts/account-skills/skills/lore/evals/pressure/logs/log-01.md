---
id: log-01
project: payments-core
reviewed: false
---

# Log — payment retry timeout default

## Deviation signal
Retry worker used provider default timeout and stalled the queue.

## What happened
The worker assumed the provider SDK timeout was safe and skipped an explicit timeout/fallback decision.

## Why it matters
This is durable domain guidance for payment retry workers.

