## Context

The repository has recently improved skill governance:

- draft skills were retired from the runtime surface
- formal project-local skills now publish under `.codex/skills/`
- skill changes now require `evaluation.md`
- a principle-skills layer now exists

However, today's authoring flow still has three open failures:

### 1. Language contract is missing

No active rule currently states that project-local skills, agent templates, and rules should default to English while the wiki remains Chinese-first. As a result, the repository's Chinese working context can bleed into newly generated skills.

### 2. Repo-specific constraints are not inherited reliably

The current skill creation flow does not force authors to read the repository's own `AGENTS.md` and repo-specific delivery contracts before authoring a new skill. That causes omissions such as missing Feishu delivery boundaries.

### 3. Token compression is not a first-class requirement

Many skill bodies still contain:

- repeated repo context already present in `AGENTS.md`
- long explanatory prose in the main body
- examples embedded inline instead of moved to `references/`

This makes retrieval more expensive and reduces the value of the newly added high-frequency principle layer.

## Goals / Non-Goals

**Goals**

- Define the shared language, constraint-scan, and compression defaults used when authoring skills.
- Bind the repo to those shared defaults with its own language and delivery boundaries.
- Refactor the current repo-local skills that should become English-first and shorter.
- Leave behavior-level evaluation evidence rather than only structure proofs.

**Non-Goals**

- Change wiki language policy for ordinary project pages.
- Import the full `account-skills` governance kit as a hidden dependency.
- Create a cross-repo dependency on `/mnt/d/skills/account-skills`.

## Decisions

### Decision: Put the default authoring contract in shared guidance, not repo-only policy

The generic skill-authoring toolchain should carry the default contract for:

- behavior assets defaulting to English-first
- scanning repo-local constraints before authoring repo-local skills
- keeping `SKILL.md` compact and moving long examples to references

The repository then adds only its repo-specific boundary:

- `wiki/*` remains Chinese-first
- repo-specific delivery rules such as Feishu stay in repo `AGENTS.md`

Alternative considered:
- Keep this entirely repo-local.
  - Rejected because the failure pattern is generic to skill authoring, not unique to this repo.

### Decision: Separate wiki language from skill language

The repo should explicitly distinguish:

- `wiki/*` is Chinese-first
- `.codex/skills/*`, `agents/*`, and `rules/*` are English-first

This avoids letting the repository's content language implicitly control skill language.

Alternative considered:
- Keep language unspecified and rely on examples.
  - Rejected because examples already failed to create a stable default.

### Decision: Skill authors must read repo-local constraints before writing

Any new or edited repo-local skill should first read:

- repo `AGENTS.md`
- relevant repo policy pages when they affect the skill's output contract

This is especially important for Feishu-facing or reader-facing delivery rules.

Alternative considered:
- Let the generic skill-creator guidance handle this implicitly.
  - Rejected because generic skill-authoring guidance does not know repository-specific delivery boundaries.

### Decision: Treat token compression as a structural rule

The repository should adopt a compact skill-body model:

- trigger conditions and hard rules stay in `SKILL.md`
- long examples, templates, and edge-case guidance move to `references/`
- repo constraints are referenced rather than repeated

Alternative considered:
- Let each skill decide its own shape.
  - Rejected because that recreates drift and uneven token cost.

## Current Skill Problems To Fix

### Current repo-local skill issues

1. `meeting-note-output`
- Chinese body instead of English-first skill contract
- carries repo-specific Feishu and format constraints inline, but not in a clearly compressed structure

2. `material-collaboration-defaults`
- Chinese body instead of English-first skill contract
- repeats substantial repo behavior prose that overlaps with `AGENTS.md`

3. `clarify-before-acting`
4. `simplicity-first`
5. `surgical-changes`
6. `verify-before-claiming`
- all four are currently Chinese-bodied even though they are principle skills meant for high-frequency retrieval
- they should become the shortest and most English-first assets in the repo

### Current authoring toolchain issues

1. The generic `skill-creator` guidance is Chinese and does not force repo-local constraint scanning.
2. The repo has no explicit contract connecting skill generation to Feishu-facing delivery rules when those rules matter.
3. The health-check currently gates behavior evidence, but not language or structure contract.

## Implementation Shape

1. Update shared guidance:
   - `writing-skills`
   - `skill-creator`
   - the common development workflow rule
2. Update repo-local guidance only where the repo boundary matters:
   - repo `AGENTS.md`
3. Refactor current repo-local skills to match the contract:
   - principle skills
   - `meeting-note-output`
   - `material-collaboration-defaults`
   - `project-management-weekly-skill`
   - `weixin-reader`
4. Move long examples or format details into `references/` where needed.
5. Record evaluation evidence for baseline and after-change behavior.

## Migration Plan

1. Add a repo-local authoring contract for skill language and compression.
2. Add a repo-local requirement to scan delivery constraints before writing skills.
3. Define which repo-local skills need refactoring first.
4. Refactor the identified skills to the new contract and extend checks if needed.
