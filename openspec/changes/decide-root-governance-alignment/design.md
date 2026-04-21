## Context

Phase 0 explicitly deferred root dotfiles. That was the correct move for repo
acceptance, but it was also a deferral, not a permanent closure.

If the whole `agents-governance-drift` topic is to be closed, the repository
still needs to answer:

- should root dotfiles align to the repo mainline
- should they remain intentionally different
- if different, what is the principled split

## Goals / Non-Goals

**Goals**

- Resolve repo-vs-root governance alignment as a stable decision.
- Preserve a clear ownership split between repo policy and root defaults.
- Avoid leaving root drift as an unspoken tail.

**Non-Goals**

- Do not merge repo and root guidance into one file.
- Do not redesign all personal/global tooling defaults.
- Do not reopen repo Phase 0.

## Decisions To Resolve

### Decision: Alignment model

Possible end states:

- full alignment for shared governance statements
- intentional split with explicit ownership
- hybrid model where only some governance layers sync

### Decision: Update burden

If alignment is required, define the minimum update set rather than a broad
rewrite.
