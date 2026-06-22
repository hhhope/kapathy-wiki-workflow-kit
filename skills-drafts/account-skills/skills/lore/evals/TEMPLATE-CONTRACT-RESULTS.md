# Lore Template Contract Results

Date: 2026-04-13
Branch: `feat/team-lore-bilingual-openspec`

This file records before/after evidence for updating the Lore page templates toward the agent-memory contract.

## RED — Before template update

Observed template gaps:

- `PROJECT-OVERVIEW-template.md` lacked explicit `Applies When`, `Not For`, `Top Facts`, and `Load Next`
- `DOMAIN-template.md` lacked explicit `Applies When`, `Not For`, `Top Facts`, and `Load Next`
- `PITFALL-template.md` lacked a low-cost operating summary such as `Top Checks` and lacked explicit exclusion guidance
- `PRINCIPLE-template.md` lacked explicit `Not For`, `Top Facts`, and directional next-hop guidance

Why this failed the agent-memory contract:

- bootstrap could generate structurally valid pages that still required prose interpretation before an agent could decide applicability
- adjacent pages could overlap without explicit exclusion cues
- first-load context depended on reading longer narrative blocks instead of a minimal operating surface

## GREEN — After template update

Updated template sections now include:

- `Scope`
- `Applies When`
- `Not For`
- retrieval-first summaries such as `Top Facts` or `Top Checks`
- `Watchpoints`
- directional next-hop guidance such as `Load Next`
- `Notes` for longer rationale separated from operating context

## Verification

Manual check:

- all four templates now expose explicit retrieval-first operating sections before long-form explanation
- all four templates now include at least one exclusion or boundary-oriented section
- project and domain templates now include directional next-hop guidance rather than links alone
- pitfall and principle templates now support low-cost first-load use before deeper rationale

## Limits

- This verifies template readiness, not migration of existing historical pages
- This does not yet prove weekly review or bootstrap enforce the new shape
- Workflow-level enforcement remains follow-up work under the same OpenSpec change
