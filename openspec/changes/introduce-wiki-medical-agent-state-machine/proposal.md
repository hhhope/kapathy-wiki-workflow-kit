# Proposal: introduce wiki medical agent state machine

## Summary

Introduce `wiki-medical-agent` as the single normal user-facing entry point for
the LLM-WIKI medical loop. The agent diagnoses user intent, resolves the active
medical case file, validates state transitions, delegates to existing stage
workers, writes results back to the same case file, and reports the next action.

## Problem

The repository now has a canonical wiki medical case file, but the workflow is
not closed. Some stage skills and scripts can still behave as independent
entry points, recovery is not case-file-aware, and treatment apply does not
guarantee recovery plus next-action classification.

This leaves the workflow vulnerable to authority drift:

```text
stage record -> another stage record -> latest generated output looks authoritative
```

## Scope

In scope:

- Add `wiki-medical-agent` skill and CLI.
- Add intent diagnosis before execution.
- Add active case resolution and multiple-active-case blocking.
- Add case state transition validation.
- Require case-file authority for treatment apply, surgery planning, and
  recovery closure.
- Update treatment apply to run recovery through the agent.
- Downgrade old stage skills to internal or explicit legacy/debug entry points.
- Add replay evidence for the current "apply 10 treatment candidates" flow.

Out of scope:

- Automatic relation repair.
- Automatic governance, ADR, OpenSpec, or MOC changes.
- Rewriting historical stage records.
- Applying real wiki treatments outside explicit user approval.

## Success Criteria

- Ordinary users can start with
  `$report-wiki-portfolio:wiki-medical-agent <intent>`.
- The agent output includes intent, case, state, allowed or blocked action, and
  next action.
- Treatment apply requires case-file confirmed decisions and automatically runs
  recovery afterward.
- Recovery results update the same case file and produce one of:
  `archive_ready`, `awaiting_confirmation`, `surgery_required`, `blocked`, or
  `followup_required`.
- Old stage skills redirect ordinary usage to `wiki-medical-agent`.
- Tests prove legacy stage outputs cannot become authoritative without a case.
