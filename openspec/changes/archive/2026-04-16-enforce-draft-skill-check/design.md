## Context

The repository already made two policy moves:

- formal project-local skills publish from `.codex/skills/`
- `skills-drafts/` cannot remain a runtime surface

Those policies are now visible in AGENTS, ADRs, and OpenSpec artifacts, but they are not yet enforced by code. That leaves a gap between documented behavior and repeatable verification.

The simplest high-signal executable guard is to ban active `SKILL.md` files under `skills-drafts/`. This directly targets the prior failure mode without introducing a broader linting framework.

## Goals / Non-Goals

**Goals**

- Provide a repo-local script that checks whether forbidden draft skills exist.
- Make the check callable from tests and from manual verification.
- Keep the scope narrow to the already-decided draft-skill boundary.

**Non-Goals**

- Build a general repository linter for every workflow rule.
- Enforce archive-review policy in the same script.
- Add CI wiring that does not yet exist in this repository.

## Decisions

### Decision: Check the filesystem directly instead of parsing ADR or AGENTS text

The risky state is concrete: an active `SKILL.md` exists under `skills-drafts/`. A direct filesystem check is more reliable and less ambiguous than inferring compliance from prose.

Alternative considered:
- Lint AGENTS and ADR wording only.
  - Rejected because wording can remain correct while the filesystem regresses.

### Decision: Keep the checker importable and CLI-runnable

The checker should serve two paths:

- unit tests import it as a function
- contributors can run it as a small CLI for manual verification

Alternative considered:
- Shell-only grep command in docs.
  - Rejected because it is harder to test and easier to drift.

## Evaluation Plan

### Baseline scenario

- Add a test that creates `skills-drafts/example/SKILL.md` in a temporary repo and expects the checker to report a violation.
- Before implementation, the test fails because the checker module does not exist.

### After-change expectation

- The same scenario reports the draft skill path as a violation.
- A clean temporary repo with no draft skill files passes with no violations.

## Risks / Trade-offs

- [Risk] The checker is narrow and will not enforce every workflow policy. -> Mitigation: keep scope explicit and extend with separate changes when needed.
- [Risk] Future draft experiments may want files under `skills-drafts/`. -> Mitigation: only ban `SKILL.md`; other draft notes remain allowed.
