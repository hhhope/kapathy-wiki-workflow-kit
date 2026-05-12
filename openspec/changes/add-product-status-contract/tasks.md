## 1. Baseline

- [ ] 1.1 Add failing focused tests for product-status fields in the wiki
      status manifest and markdown output.
- [ ] 1.2 Confirm the tests fail before implementation because no
      `product_status` object or `Product Status` markdown section exists.

## 2. Product Status Contract

- [ ] 2.1 Add `product-status-contract` spec requirements for object types,
      target states, source layers, readiness labels, evidence requirements,
      score type boundaries, and status transitions.
- [ ] 2.2 Extend `wiki-status-surface` spec requirements so generated status
      exposes the minimal product-status summary without changing status scope.

## 3. Status Implementation

- [ ] 3.1 Extract product-status helper logic before expanding
      `scripts/build_wiki_status.py` beyond its current responsibilities.
- [ ] 3.2 Extend wiki status generation with conservative product object,
      source-layer, identity/relation coverage, and readiness classification.
- [ ] 3.3 Render the `Product Status` section in `wiki/status/wiki-status.md`.
- [ ] 3.4 Regenerate `wiki/status/manifest.json` and
      `wiki/status/wiki-status.md`.

## 4. Verification

- [ ] 4.1 Run focused wiki status tests.
- [ ] 4.2 Run full unit tests.
- [ ] 4.3 Run `openspec validate add-product-status-contract --strict`.
- [ ] 4.4 Run `openspec validate --all`.
- [ ] 4.5 Inspect git status and commit only task-related files.
