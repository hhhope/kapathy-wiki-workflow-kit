# Continuation State Gate

Use before continuing an Atlas-triggered task after short approval, repair, or
completion pressure.

## Trigger

Run this gate when:

- the user says `continue`, `继续`, `可以`, `确认`, `做吧`, `修吧`, `过`, or a
  similar short continuation phrase
- the current artifact is a stateful learning/report collaboration
- confirmed anchors, rejected framings, evidence boundaries, visual decisions,
  selected output shape, or drift history exist

Do not run this gate for simple one-off work with no durable artifact or
confirmed-anchor state.

## Required Block

Emit the state block before acting:

```text
- `Using atlas`
- `Current Object`:
- `Current Phase`:
- `Confirmed Anchors`:
- `Allowed Actions`:
- `Blocked Actions`:
- `Open Gaps`:
- `Worker Route`:
- `Next Output`:
```

Keep it short. This is a control read-back, not a new long plan.

## Unknown Phase

If the phase is not clear:

```text
Current Phase: unclear
Allowed Actions: clarify or re-anchor only
Blocked Actions: draft, edit delivery artifact, implement, publish, sync
```

Stop after the block and ask or produce the smallest re-anchor artifact.

## Blocked Action

If the requested next action conflicts with confirmed anchors:

- name the conflicting anchor
- name the blocked action
- return the smallest decision point
- do not continue into drafting, visual production, H5 edits, or skill edits

## Examples

### Report

```text
Current Object: Stripe sharing稿
Current Phase: structure_lock
Confirmed Anchors: 1-3 chapters locked; each chapter needs screen content,
talk track, evidence boundary, and transition
Allowed Actions: expand chapters 4-7 in the same format
Blocked Actions: rename chapters 1-3; compress talk track into summary bullets
Worker Route: public-report-quality-gate
Next Output: chapter 4 sample only
```

### H5

```text
Current Object: Stripe AI payment sharing H5
Current Phase: visual_binding
Confirmed Anchors: every section needs its own visual proof task
Allowed Actions: map section 7 visuals
Blocked Actions: replace per-section visuals with one generic overview image
Worker Route: public-report-quality-gate -> visual-agent
Next Output: section 7 visual binding table
```

### Skill Change

```text
Current Object: Atlas skill
Current Phase: implementation
Confirmed Anchors: SS plan is active; OpenSpec route is blocked unless reopened
Allowed Actions: implement Task 2 only
Blocked Actions: edit OpenSpec change artifacts; edit unrelated skills
Worker Route: skill-authoring gate
Next Output: compact SKILL.md skeleton
```

### One-Off Negative Case

```text
No Atlas route: the user asks for a direct shell result and no durable
learning/report artifact or confirmed-anchor state exists.
```
