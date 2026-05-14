# Proposal: formalize LLM-WIKI medical loop

## Summary

Formalize the LLM-WIKI self-evolution lifecycle as a medical loop:

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

The change defines vocabulary, artifact expectations, and escalation boundaries.
It does not add write automation.

## Problem

The repository now has diagnostic capability through `wiki-doctor` review
records, but the broader self-evolution process is still implicit in chat and
design notes. Without a formal lifecycle, later agents may confuse diagnosis,
human confirmation, repair, verification, and archive as interchangeable steps.

The repository needs a stable model that explains how LLM-assisted wiki
evolution moves from health signals to durable memory while preserving OpenSpec,
human review, and proof boundaries.

## Scope

In scope:

- Define the medical-loop lifecycle vocabulary.
- Define required artifact classes for each lifecycle stage.
- Define treatment versus surgery escalation rules.
- Define proof, approval, write, and archive boundaries.
- Add a repo-visible wiki ops model record.
- Add behavior replay evidence for future routing expectations.

Out of scope:

- New skills or commands.
- Automated treatment or surgery.
- Applying frontmatter, taxonomy, relation, MOC, ADR, AGENTS, or OpenSpec state
  changes.
- Implementing review-decision, treatment, surgery, or recovery workflows.
- Archiving this change.

## Success Criteria

- OpenSpec validation passes for `formalize-llm-wiki-medical-loop`.
- A wiki ops record explains the model for future agents.
- Requirements explicitly preserve `doctor` as diagnosis-only.
- Requirements explicitly state that treatment and surgery require later scoped
  approval before writes.
- Evaluation records behavior replay, prior-art dedupe, validation commands, and
  residual risk.
