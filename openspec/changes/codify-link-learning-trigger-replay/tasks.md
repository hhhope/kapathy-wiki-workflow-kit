## 1. OpenSpec

- [x] 1.1 Add spec delta for link-trigger replay strategy.
  Evidence: `specs/learning-capture-routing/spec.md` defines replay scenarios
  for bare article links, WeChat links, repo/README links, raw fetch requests,
  unclear bare links, durable capture, non-capture, and promotion boundaries.
- [x] 1.2 Validate the change with `openspec validate --strict`.
  Evidence: `openspec validate codify-link-learning-trigger-replay --strict`
  passed on 2026-05-07; PostHog DNS flush noise occurred after validation.

## 2. Runtime Artifacts

- [ ] 2.1 Update repo-visible learning-capture guidance so the replay matrix is discoverable.
- [ ] 2.2 Preserve negative paths: raw fetch, news/fact lookup, unclear bare link, low-scoring source.
- [ ] 2.3 Preserve promotion boundary: no AGENTS/spec/skill hard rule without evidence gate.

## 3. Evaluation

- [ ] 3.1 Add RED/GREEN-style replay evidence for the five input shapes.
- [ ] 3.2 Confirm a future answer can cite repo artifacts instead of chat memory.

## 4. Closeout

- [ ] 4.1 Review dirty tree and stage only task-related files.
- [ ] 4.2 Commit the completed, verified change step.
