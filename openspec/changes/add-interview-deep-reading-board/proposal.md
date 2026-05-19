## Why

The Li Xiang and Luo Yonghao interview deep-reading workflow exposed a
repeatable routing gap. A request that began with a word cloud was actually a
request for full interview deep reading: source-order continuity, speaker-turn
logic, a draggable temperature axis, keyword-to-evidence links, and protection
for user-highlighted passages.

The first output treated the word cloud as the main artifact. That compressed
the interview into fragmented keywords and hid important passages, including
the section about code volume, Feishu, internal Coworker, a stable employee
Agent, subagents, data, and MCP.

The repository has strong parent gates for material processing and public
report output, but it does not yet have an interview-specific module that asks
whether this output type should be used before building a reader-facing H5 or
word-cloud artifact.

## What Changes

- Add a repo-local `interview-deep-reading-board` skill for interview,
  podcast-transcript, dialogue, and Q&A deep-reading workflows.
- Require the skill to ask the user whether to create a full-window interview
  reading board when interview-like material meets compression-sensitive output
  triggers.
- Add an H5 output-shape reference for source-order windows, temperature axis,
  keyword index, timeline, and evidence panel behavior.
- Preserve the Li Xiang interview H5 as a validated example and preserve the
  earlier word-cloud artifact as a counterexample.
- Update `public-report-quality-gate` so reader-facing interview H5, timeline,
  word-cloud, and draggable evidence outputs delegate to
  `interview-deep-reading-board` before ordinary report or HTML production.
- Update `AGENTS.md` with a lightweight route to the new skill without copying
  the full skill rules into the repo entrypoint.
- Record behavior-asset evaluation evidence, including RED/GREEN pressure
  scenarios, prior-art/common-rule dedupe, behavior replay, and residual risks.

## Impact

- Future interview deep-reading requests should not silently degrade into a
  small keyword cloud or summary card set.
- Reader-facing interview H5 work still routes through the public report gate;
  the new skill is a module, not a replacement parent gate.
- The H5 produced in the triggering incident becomes reusable reference
  material for future agents.
- The change does not publish, sync, or regenerate the Li Xiang H5 by itself.
  It only formalizes the workflow and routing needed for future work.
