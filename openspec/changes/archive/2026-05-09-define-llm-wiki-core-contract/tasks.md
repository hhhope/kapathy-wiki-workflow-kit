## 1. Change Setup

- [x] 1.1 Create proposal, design, tasks, evaluation, and spec delta artifacts.
- [x] 1.2 Preserve the user's correction that LLM Wiki is the core value and
  agent self-service learning is an enhancement.

## 2. Product Contract

- [x] 2.1 Add `wiki/ops/llm-wiki-core-product-contract.md`.
- [x] 2.2 Define the four-part core loop: Capture, Compile, Retrieve, Apply.
- [x] 2.3 Reframe `obsidian-wiki` comparison under the core loop.
- [x] 2.4 Separate core gaps from enhancement backlog.
- [x] 2.5 Update `wiki/ops/index.md` with the new contract entry.

## 3. Evaluation

- [x] 3.1 Verify OpenSpec strict validation.
  <!-- 2026-05-09 — `openspec validate define-llm-wiki-core-contract --strict` passed; PostHog DNS flush noise ignored after valid result -->
- [x] 3.2 Verify the product contract states core versus enhancement
  boundaries.
  <!-- 2026-05-09 — rg confirmed durable compiled context, core loop, Core Versus Enhancement, and P2 learning-to-change boundary -->
- [x] 3.3 Verify no implementation-only backlog item was accidentally
  implemented in this change.
  <!-- 2026-05-09 — touched files limited to OpenSpec artifacts, product contract page, and ops index link; no manifest/query/scorecard/graph implementation added -->
- [x] 3.4 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: db9ac65 docs: trace product alignment drift; dirty tree includes pre-existing unrelated paths plus this change -->

## 4. Stop Boundary

- [x] 4.1 Stop after the product contract and validation evidence are complete.
- [x] 4.2 Do not implement manifest, query, scorecard, graph, or
  learning-to-change orchestration in this change.
