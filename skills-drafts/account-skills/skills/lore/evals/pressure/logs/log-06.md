---
id: log-06
project: auth-core
reviewed: false
---

# Log — session refresh redirect loop

## Deviation signal
Silent refresh failure caused repeated redirect to login.

## What happened
Route guard and refresh logic disagreed on expired token behavior.

## Why it matters
This should become auth domain guidance.

