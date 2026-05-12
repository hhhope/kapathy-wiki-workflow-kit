## 1. Baseline

- [x] 1.1 Add failing focused tests for product-status fields in the wiki
      status manifest and markdown output.
- [x] 1.2 Confirm the tests fail before implementation because no
      `product_status` object or `Product Status` markdown section exists.

<!-- Evidence: RED tests failed with KeyError: 'product_status' for manifest tests and missing '## Product Status' for markdown before implementation. -->

## 2. Product Status Contract

- [x] 2.1 Add `product-status-contract` spec requirements for object types,
      target states, source layers, readiness labels, evidence requirements,
      score type boundaries, and status transitions.
- [x] 2.2 Extend `wiki-status-surface` spec requirements so generated status
      exposes the minimal product-status summary without changing status scope.

<!-- Evidence: openspec validate add-product-status-contract --strict passed. -->

## 3. Status Implementation

- [x] 3.1 Extract product-status helper logic before expanding
      `scripts/build_wiki_status.py` beyond its current responsibilities.
- [x] 3.2 Extend wiki status generation with conservative product object,
      source-layer, identity/relation coverage, and readiness classification.
- [x] 3.3 Render the `Product Status` section in `wiki/status/wiki-status.md`.
- [x] 3.4 Regenerate `wiki/status/manifest.json` and
      `wiki/status/wiki-status.md`.

<!-- Evidence: PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_wiki_status.py wrote both status artifacts; rg found product_status, Product Status, Contract version, and Unresolved Product Status. -->

## 4. Verification

- [x] 4.1 Run focused wiki status tests.
- [x] 4.2 Run full unit tests.
- [x] 4.3 Run `openspec validate add-product-status-contract --strict`.
- [x] 4.4 Run `openspec validate --all`.
- [x] 4.5 Inspect git status and commit only task-related files.

<!-- Evidence: PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_wiki_status passed 11/11; PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests passed 73/73; openspec validate --all passed 47/47; git diff --check passed. -->
