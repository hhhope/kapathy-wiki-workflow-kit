## 1. OpenSpec

- [x] 1.1 Add spec delta for link-trigger replay strategy.
  Evidence: `specs/learning-capture-routing/spec.md` defines replay scenarios
  for bare article links, WeChat links, repo/README links, raw fetch requests,
  unclear bare links, durable capture, non-capture, and promotion boundaries.
- [x] 1.2 Validate the change with `openspec validate --strict`.
  Evidence: `openspec validate codify-link-learning-trigger-replay --strict`
  passed on 2026-05-07; PostHog DNS flush noise occurred after validation.

## 2. Runtime Artifacts

- [x] 2.1 Update repo-visible learning-capture guidance so the replay matrix is discoverable.
  Evidence: `.codex/skills/learning-capture/references/routing.md` now has
  `Link Trigger Replay`; `wiki/ops/learning-capture-routing.md` now has
  `Link Trigger Replay 治理锚点`.
- [x] 2.2 Preserve negative paths: raw fetch, news/fact lookup, unclear bare link, low-scoring source.
  Evidence: both replay artifacts keep raw fetch/news/fact lookup and no-context
  bare links out of durable learning capture by default.
- [x] 2.3 Preserve promotion boundary: no AGENTS/spec/skill hard rule without evidence gate.
  Evidence: wiki governance boundary and spec promotion scenario block
  unsupported promotion.

## 3. Evaluation

- [x] 3.1 Add RED/GREEN-style replay evidence for the five input shapes.
  Evidence: `evaluation.md` covers bare article link, WeChat link, GitHub/README
  link, raw fetch/news/fact lookup, and bare link with no learning context.
- [x] 3.2 Confirm a future answer can cite repo artifacts instead of chat memory.
  Evidence: `evaluation.md` lists the three artifact citations future answers
  can use.

## 4. Closeout

- [x] 4.1 Review dirty tree and stage only task-related files.
  Evidence: dirty tree includes unrelated `wiki/ops/agent-harness-article-learning.md`,
  `wiki/reports/nirvana-phase1-direct-sales-brief.html`, and local untracked
  files; only link-trigger replay files are staged for this step.
- [x] 4.2 Commit the completed, verified change step.
  Evidence: commit `9b4af5f docs: codify link learning replay runtime`.
