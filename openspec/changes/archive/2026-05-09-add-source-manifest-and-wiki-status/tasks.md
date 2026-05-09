## 1. Change Setup

- [x] 1.1 Create proposal, design, spec delta, tasks, and evaluation artifacts.
- [x] 1.2 Confirm this change starts from P0 source manifest/wiki status, not
  query, scorecard, graph, or change queue.

## 2. Test First

- [x] 2.1 Add failing tests for source manifest and OpenSpec status behavior.
- [x] 2.2 Verify the tests fail before implementation.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status` failed with ModuleNotFoundError before script implementation -->

## 3. Implementation

- [x] 3.1 Add `scripts/build_wiki_status.py`.
- [x] 3.2 Generate `wiki/status/manifest.json`.
- [x] 3.3 Generate `wiki/status/wiki-status.md`.
- [x] 3.4 Add `wiki/status/index.md` and navigation entry.

## 4. Evaluation

- [x] 4.1 Run targeted unit tests.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status` passed: 4 tests -->
- [x] 4.2 Run `openspec validate add-source-manifest-and-wiki-status --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid result -->
- [x] 4.3 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for OpenSpec artifacts, script, tests, wiki/status, and wiki/index.md -->
- [x] 4.4 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: e62cc36 docs: define llm wiki core contract; dirty tree includes pre-existing unrelated paths plus this change -->

## 5. Stop Boundary

- [x] 5.1 Stop after manifest/status script, generated baseline artifacts,
  tests, and validation are complete.
- [x] 5.2 Do not implement query, scorecard, graph UI, or change queue in this
  change.
