---
name: cr-branch-governance
description: Use only inside cr-agent to validate CR branch, baseline, version range, and release package trust.
---

Validate that the review range is trustworthy before technical CR proceeds.

Checks:

- release CR uses previous online mainline version to production target
- merge CR uses feature range to target branch
- start ref is an ancestor of end ref unless explicitly marked as archaeology
- mainline direct commits are identified
- production commit is covered by UAT evidence or the gap is recorded
- test, UAT, release, and master branches are compared when refs are provided
- non-merge commits have ticket or approved exception evidence
- cherry-pick, revert, conflict-resolution, and long-lived branch risks are surfaced
- code, SQL, config, scripts, and rollback assets are checked for package completeness

Hard blockers:

- wrong baseline for the declared CR type
- unclear release range
- feature-branch CR presented as release gate
- mainline direct commit without approval or validation evidence
- production commit not covered by UAT evidence for release CR
- unrelated commits in release range without explicit disposition
