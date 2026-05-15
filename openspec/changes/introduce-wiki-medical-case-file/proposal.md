# Proposal: introduce wiki medical case file

## Summary

Make each LLM-WIKI medical-loop run preserve one canonical case file as the
human review entry point.

Doctor, confirm, treatment, surgery, and recovery records may still exist as
stage evidence, but they must not become competing sources of truth. The case
file owns the current diagnosis, confirmed decisions, approved actions,
surgery plan, recovery result, proof boundary, and next action.

## Problem

The medical loop is now presented as:

```text
doctor -> confirm -> treatment -> surgery -> recovery -> archive
诊断 -> 确诊 -> 治疗 -> 手术 -> 复查 -> 归档
```

The current implementation can write separate stage records. That is useful for
evidence, but it creates a drift risk: later stages can accidentally treat the
newest generated record as the authority instead of tracing back to the
confirmed case context.

The problem became visible during surgery planning. The surgery stage generated
a plan from script output, but the reviewable human intent and source-of-truth
boundary were not preserved in the same durable object. That made it unclear
whether humans should review the confirmed decisions, the generated surgery
record, or both.

## Scope

In scope:

- Define a canonical `wiki-medical-case` record model.
- Make the case file the primary review surface for the medical loop.
- Require surgery plans to derive from the case file's confirmed decisions.
- Preserve stage records as attachments or evidence snapshots.
- Define proof boundaries for treatment, surgery, recovery, and archive.
- Add tests or replay evidence proving the case file prevents stage-record
  authority drift.

Out of scope:

- Applying frontmatter, relation fields, taxonomy config, MOC files, ADRs, or
  OpenSpec lifecycle state.
- Reworking all historical doctor, confirm, treatment, or surgery records.
- Removing stage records entirely.
- Implementing automatic relation repair.

## Success Criteria

- A medical-loop run can be opened through one case file under
  `wiki/ops/wiki-medical-cases/`.
- The case file includes doctor, confirm, treatment, surgery, recovery, and
  archive sections, even when some sections are pending.
- Surgery planning cites confirmed case decisions instead of re-diagnosing from
  raw script output.
- Stage records are linked as evidence attachments and cannot silently override
  the case decisions.
- Human review guidance is clear: review case decisions first, then verify that
  the surgery plan faithfully implements those decisions.
- Existing stage CLIs retain stdout/debug modes while supporting the case-file
  workflow.
