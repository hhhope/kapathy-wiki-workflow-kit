# Add Learning Workflow Matrix

## Why

`learning-capture` currently routes external articles, repos, READMEs, and examples, but it does not define how to choose learning depth, learning type, evidence strength, research methods, or reader-facing output transformation.

The Stripe research discussion exposed this gap: a long company-path case with a source queue, process tracing, cross-validation, saturation judgment, and H5/report output cannot be handled as an ordinary source summary.

## What Changes

- Keep `learning-capture` as a compact controller.
- Add modular references for learning levels, learning types, research methods, evidence strength, source queues, output contracts, and public-writing transformation.
- Add structural validation for L2/L3 learning records.
- Add local pressure-test evidence for OCR-style technical learning, Stripe-style company reconstruction, public article/H5 transformation, and governance/agent workflow learning.

## Out Of Scope

- No full state machine or graph runtime in the first implementation.
- No function-calling runtime dependency.
- No `AGENTS.md` behavior change.
- No automatic source fetching or citation verification.
- No claim that Python validates business or technical judgment correctness.
