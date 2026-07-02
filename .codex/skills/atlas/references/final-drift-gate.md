# Final Drift Gate

Run before claiming a stateful learning/report artifact is done, fixed,
review-ready, synced, publish-ready, or complete.

## Required Inputs

- active object
- confirmed anchors
- current output shape
- allowed and blocked actions
- open evidence gaps
- visual decisions
- worker blockers

## Checks

| Check | Failure |
|---|---|
| Confirmed anchors | A confirmed title, section, talk track, visual decision, evidence boundary, or rejected framing disappeared. |
| Chapter and section names | Names, count, order, or purpose changed without approval. |
| Talk track and transition | Talk track, screen content, or chapter transition was compressed away. |
| Evidence boundary | A load-bearing claim lacks required source role, sample size, proof boundary, or method fit. |
| Visual compression | Approved per-section visuals became one generic visual or decorative layout. |
| Output shape | Report, H5, PPT, markdown, wiki, or Feishu target changed without approval. |
| Custom-to-generic boundary | A Stripe-specific rule became universal behavior without evidence. |
| Generic learning capture | A reusable collaboration rule was not captured as a candidate governance signal when required. |

## Failure Behavior

If any hard check fails:

- do not say done
- name the failed gate
- name the smallest repair target
- return to the matching phase
- route to the worker that owns the blocker

Use this shape:

```text
Final Drift Gate: failed
Failed gate:
Anchor or evidence affected:
Repair phase:
Allowed repair:
Blocked action:
```

## Pass Behavior

Only after passing, say what was checked and what residual risk remains.

Do not claim:

- globally proven behavior
- OpenSpec archive readiness
- future drift is impossible
- unrelated report/H5 artifacts are fixed
