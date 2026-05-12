## Why

The repository has strong local gates: source intake, learning capture, public
report quality review, behavior replay, OpenSpec archive review, and wiki
runtime surfaces. Those gates are useful, but they do not share a product-level
status contract.

That gap causes repeated drift. A local artifact can look complete because its
own test, score, or gate passed, while the product target is still unclear:
source evidence may not feed learning, learning may not constrain output,
output may not carry behavior replay, and behavior may not appear in status.

The next step should make the operating backbone explicit and computable:

```text
Source -> Learning -> Structure -> Output -> Behavior -> Status
```

The first implementation slice should define the contract and expose a minimal
status summary through the existing wiki status surface. It should not jump
straight into a graph UI, semantic scoring rewrite, or task queue.

## What Changes

- Add a `product-status-contract` spec that defines:
  - product object types;
  - target states and source layers;
  - readiness labels;
  - evidence requirements;
  - score type boundaries;
  - status transitions across the product backbone.
- Extend the generated wiki status manifest with a minimal product-status
  summary.
- Extend `wiki/status/wiki-status.md` so humans and agents can see product
  readiness counts, explicit-frontmatter relation/identity coverage, and
  unresolved status pressure.
- Add focused tests for the new contract fields and status rendering.

## Impact

- Affects `scripts/build_wiki_status.py`.
- Affects `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
- Adds or updates focused wiki status tests.
- Adds OpenSpec coverage for `product-status-contract` and `wiki-status-surface`.
- Does not modify public report, learning capture, visual output, graph,
  Feishu sync, or archive behavior rules.
