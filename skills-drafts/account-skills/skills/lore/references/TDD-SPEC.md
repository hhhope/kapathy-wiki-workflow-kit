# Lore Wiki TDD Spec

This file defines the first executable validation target for the Lore Wiki workflow.

Use it before claiming the workflow is reliable.

---

## Goal

Prove that Lore can work as a useful memory layer beside OpenSpec, with explicit gates, measurable retrieval quality, and a closed `log -> wiki -> reuse` loop.

---

## Hard gates

These are design constraints, not tuning targets.

### G1 — Propose gate

If a task is large and there is no approved OpenSpec change, apply must be blocked.

Pass rule:
- 10/10 blocked in gate scenarios

### G2 — Review/archive gate

If there are unreviewed or unabsorbed logs, archive must be blocked.

Pass rule:
- 10/10 blocked in gate scenarios

---

## Soft hypotheses

These are first-pass thresholds. Calibrate them with baseline runs instead of treating them as fixed truth.

### H1 — Similar-task recall

Target:
- `>= 80%`

Definition:
- A query counts as recalled if the expected core page is returned in the top result set.

### H2 — Irrelevant-page noise

Target:
- `<= 20%`

Definition:
- A query counts as noisy if the returned top result set contains a clearly unrelated page.

### H3 — Log absorption success

Target:
- `>= 90%`

Definition:
- For logs marked as worth keeping, the review process must update the intended wiki page and record the destination.

Weekly review report must also include:
- reviewed logs
- absorbed logs
- discarded logs
- `absorbed-to` completion rate
- dominant destination page types

### H4 — Startup context budget

Target:
- P50: `3-4` pages
- P90: `<= 6` pages

Definition:
- Count unique markdown pages read during task startup.

---

## Dataset design

### Query set

20 total queries:
- 5 Chinese similar-task queries
- 3 English similar-task queries
- 2 cross-domain similar-task queries
- 5 Chinese unrelated-task queries
- 3 English unrelated-task queries
- 2 edge-case ambiguous queries

### Log set

10 total logs:
- 3 reusable engineering lessons
- 2 project-specific domain lessons
- 2 noise / discard logs
- 2 user-description issues
- 1 PRD-misalignment issue

### Startup set

10 total startup scenarios:
- 4 simple tasks
- 4 medium tasks
- 2 large tasks

---

## Measurement rules

### Recall

```text
recall = matched_core_pages / similar_queries
```

### Noise

```text
noise = unrelated_queries_with_wrong_top_results / unrelated_queries
```

### Absorption

```text
absorption = accepted_logs_written_to_target_pages / accepted_logs
```

### Weekly review completeness

```text
absorbed_to_completion = reviewed_logs_with_absorbed_to / reviewed_logs
```

Track also:
- reviewed logs
- absorbed logs
- discarded logs
- destinations by page type

### Context budget

Track:
- pages per scenario
- P50
- P90
- max

---

## Red/Green workflow

### RED

Before changing the workflow:
- write or collect the test dataset
- run baseline scenarios
- record fails in `BASELINE-RESULTS.md`

### GREEN

After workflow updates:
- rerun the same scenarios
- compare metrics against thresholds

### REFACTOR

Once metrics pass:
- simplify wording
- remove duplicate steps
- tighten ambiguous instructions without changing behavior

---

## First-pass acceptance

The workflow is acceptable for first rollout only if:
- both hard gates pass
- no soft target is catastrophically below threshold
- the baseline document records exact gaps and next fixes
