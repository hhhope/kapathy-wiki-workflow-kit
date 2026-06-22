# Lore Workflow Contract Results

Date: 2026-04-13
Branch: `feat/team-lore-bilingual-openspec`

This file records before/after evidence for tightening Lore and Lore Bootstrap workflow wording around the agent-memory contract.

## RED — Before workflow update

Observed workflow gaps:

- `skills/lore/SKILL.md` told the agent what pages to read, but not what retrieval-ready operating sections should be preferred on first load
- `skills/lore/SKILL.md` required weekly review to absorb durable knowledge, but did not require destination pages to improve retrieval surfaces
- `skills/lore-bootstrap/SKILL.md` treated bootstrap completion primarily as a file-and-path outcome, not an agent-ready starter-page outcome

Why this failed:

- an agent could follow the workflow and still load prose-heavy pages first
- weekly review could succeed while future context loading remained expensive
- bootstrap could be reported complete even when starter pages were only placeholder shells with weak operating surfaces

## GREEN — After workflow update

Updated workflow wording now requires:

- retrieval to prefer first-screen operating sections such as `Scope`, `Applies When`, `Not For`, `Top Facts`, and `Watchpoints`
- weekly review to improve retrieval-first operating sections rather than relying on prose-only append
- bootstrap verification to include retrieval-ready starter sections, not file existence alone

## Verification

Manual check:

- `skills/lore/SKILL.md` now mentions retrieval-first operating sections during task start
- `skills/lore/SKILL.md` now states that weekly review should improve operating sections and not rely on prose-only durable promotion
- `skills/lore-bootstrap/SKILL.md` now states that bootstrap starter pages must be retrieval-ready and verifies those sections explicitly

## Limits

- This verifies wording and workflow intent, not runtime enforcement
- Script-level or fixture-level enforcement updates remain separate follow-up work
- Existing historical wiki pages still need migration to the new shape
