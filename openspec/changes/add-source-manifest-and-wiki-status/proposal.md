## Why

The LLM Wiki core contract now defines the first P0 gap as source manifest and
wiki status. Today the repository can store source pages, ops traces, reports,
and OpenSpec tasks, but it cannot compute a simple answer to:

- what wiki pages exist
- which inbox files are not represented by source records
- which OpenSpec changes are still active or complete-but-not-archived
- where a future agent should look for current wiki state

This keeps "还有什么任务" dependent on chat memory, manual grep, and recent git
archaeology.

## What Changes

- Add a minimal source/wiki manifest generator.
- Add a user-readable wiki status report.
- Add tests for inbox-source matching and OpenSpec task-state summary.
- Add generated baseline artifacts under `wiki/status/`.
- Keep the scope limited to status visibility, not query, scorecard, graph UI,
  or change orchestration.

## Impact

- Adds `scripts/build_wiki_status.py`.
- Adds `tests/test_wiki_status.py`.
- Adds `wiki/status/index.md`, `wiki/status/manifest.json`, and
  `wiki/status/wiki-status.md`.
- Updates wiki navigation to expose the status surface.
- Does not modify report delivery, Feishu behavior, scorecards, or graph
  extraction.
