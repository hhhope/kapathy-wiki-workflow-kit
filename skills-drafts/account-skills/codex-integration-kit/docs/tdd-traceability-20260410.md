# TDD Traceability: Governance Asset Alignment

Date: 2026-04-10  
Branch: `codex-integration-kit-governance-tune`

## Scope

- `codex-integration-kit/templates/global/AGENTS.base.md`
- `codex-integration-kit/skills/jira-integration/SKILL.md`

## Why This Exists

These are semantic behavior-asset changes. The verification result must be traceable in-repo instead of existing only in chat memory.

## RED Scenarios

### Scenario 1: Skill-edit routing is missing from the global baseline

Expected behavior:
- When a user creates or semantically edits any `skills/*` content, the baseline must route to `writing-skills` and `test-driven-development`.
- When a user adopts an external skill, the baseline must route to `migrating-skills`.

Baseline evidence before the fix:
- `rg -n "writing-skills|test-driven-development|migrating-skills|starter card|localize" codex-integration-kit/templates/global/AGENTS.base.md codex-integration-kit/skills/jira-integration/SKILL.md`
- Result: no matches in either target file.

Failure observed:
- `AGENTS.base.md` could route migration work and Jira work, but not the semantic skill-edit workflow required by governance.
- An external skill could still be treated as locally available without an explicit local-install/localization gate.

### Scenario 2: Jira skill can be mistaken for repository truth

Expected behavior:
- The Jira card must declare itself a starter card.
- It must require local workflow/field/status localization before governance wiring.

Baseline evidence before the fix:
- Same `rg` command above returned no `starter card`, `Localize Before Use`, or `localize` markers in `jira-integration/SKILL.md`.

Failure observed:
- A downstream repo could copy the card and treat its placeholder fields and workflow assumptions as final local policy.

### Scenario 3: Traceability requirement is not encoded in constraints

Expected behavior:
- The governance constraints must require semantic behavior-asset verification evidence to be written into repository files.
- The rule must reject chat-only verification as insufficient for completion.

Baseline evidence before the fix:
- `rg -n 'traceable|traceability|in-repo|existing only in chat memory|behavior-asset|semantic edits' codex-integration-kit/rules/common/development-workflow.md codex-integration-kit/templates/global/AGENTS.base.md`
- Result: no matches in either target file.

Failure observed:
- The kit described TDD traceability in a documentation note, but did not yet encode that requirement as a reusable constraint.

## GREEN Changes

### Change Set

- Added global routing for:
  - skill creation/modification -> `writing-skills` + `test-driven-development`
  - external skill adoption/localization -> `migrating-skills`
- Added explicit baseline rules that:
  - semantic `skills/*` edits must use the TDD validation loop
  - external skills are not locally available until installed and path/name dependencies are verified
- Added explicit constraint-level traceability rules that:
  - semantic edits to `AGENTS.md`, `rules/*`, and `skills/*` require in-repo verification evidence
  - chat-only verification is not sufficient
  - `docs/`, `evals/`, or `logs/` are the preferred persistence locations
- Converted `jira-integration` into an explicit starter card with:
  - a localize-first introduction
  - a `Do Not` rule against treating placeholders as repository truth
  - a `Localize Before Use` section
  - a boundary note for customized Jira workflows or alternate issue trackers

## GREEN Verification

### Verification Command 1

```bash
rg -n "writing-skills|test-driven-development|migrating-skills|external skill" \
  codex-integration-kit/templates/global/AGENTS.base.md
```

Expected pass condition:
- Matches exist for all required routing and governance gates.

Observed result after the fix:
- `AGENTS.base.md` contains routing rows for `writing-skills`, `test-driven-development`, and `migrating-skills`.
- `AGENTS.base.md` states that semantic `skills/*` edits must use the TDD validation loop.
- `AGENTS.base.md` states that external skills are not local until installed and verified.

### Verification Command 1b

```bash
rg -n 'traceable|traceability|chat-only|behavior asset|semantic behavior-asset|repository file' \
  codex-integration-kit/rules/common/development-workflow.md \
  codex-integration-kit/templates/global/AGENTS.base.md
```

Expected pass condition:
- Matches exist that make traceability an explicit reusable constraint.

Observed result after the fix:
- `development-workflow.md` treats `AGENTS.md`, `rules/*`, and `skills/*` as behavior assets and requires in-repo traceability for semantic changes.
- `AGENTS.base.md` requires semantic behavior-asset verification to be written into repository files and rejects chat-only verification.

### Verification Command 2

```bash
rg -n "starter card|Localize Before Use|localize|workflow assumptions|different issue tracker|repository truth" \
  codex-integration-kit/skills/jira-integration/SKILL.md
```

Expected pass condition:
- Matches exist for starter/localization boundary markers.

Observed result after the fix:
- `jira-integration/SKILL.md` declares itself a starter card.
- `jira-integration/SKILL.md` contains `Localize Before Use`.
- `jira-integration/SKILL.md` forbids treating placeholders as repository truth.
- `jira-integration/SKILL.md` calls out customized Jira workflows and alternate issue trackers as adaptation points.

## Refactor Note

While verifying GREEN, a structural regression was found in `AGENTS.base.md`: duplicate `Rules:` blocks and a misplaced table row. That defect was corrected before finalizing this trace record.

## Related Commits

- `1b0e72b chore: add project metadata bootstrap`
- `1f7be63 docs: align codex integration kit governance`
- `35414dc docs: add governance tdd traceability`

The current turn adds follow-up TDD traceability on top of those earlier governance-alignment commits.
