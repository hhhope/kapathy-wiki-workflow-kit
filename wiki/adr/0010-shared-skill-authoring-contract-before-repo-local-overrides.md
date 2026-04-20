# ADR-0010 Shared Skill Authoring Contract Before Repo-Local Overrides

## Status

Accepted

## Context

Recent skill failures in this repo were not caused only by repo-local workflow gaps. The upstream skill-authoring chain was also underspecified:

- there was no hard default saying behavior assets should stay English-first
- repo-local delivery constraints such as Feishu requirements were not mandatory inputs before writing a repo-local skill
- `SKILL.md` bodies were free to absorb repeated repo policy and long examples, increasing token cost

Treating that as only a repo-local workflow problem led to the wrong fix layer.

## Decision

- Shared skill-authoring guidance should define the default contract for behavior assets:
  - English-first governing text
  - mandatory scan of repo-local `AGENTS.md` and delivery constraints before authoring repo-local skills
  - compact `SKILL.md` bodies with longer material moved to linked references
- Repo-local `AGENTS.md` should add only the repo-specific boundary:
  - wiki language policy
  - delivery-specific rules such as Feishu workflow constraints
  - repo-specific workflow contracts

## Consequences

- Future fixes for generic skill-authoring drift should first be evaluated at the shared guidance layer, not only inside this repo.
- Repo-local skills remain free to preserve non-English output labels or trigger phrases when the workflow requires them, but the governing body should stay English-first.
- Repo-local workflow skills should reference repo policy instead of duplicating large sections of repo governance inline.
