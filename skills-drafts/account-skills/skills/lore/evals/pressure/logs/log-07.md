---
id: log-07
project: shared
reviewed: false
---

# Log — external dependency introduced late

## Deviation signal
An implementation added a new outbound call after design lock without explicit boundary review.

## What happened
Ownership and degradation behavior were both undefined until late review.

## Why it matters
This repeats across projects and should strengthen the shared boundary rule.

