# Proposal: resolve frontmatter producer warning gate

## Why

`repair-legacy-wiki-frontmatter-batches` cleared page-level frontmatter
blockers:

- `blocking_count: 0`
- `summary.error: 0`
- `python3 scripts/check_wiki_frontmatter.py` exits 0

But `scripts/wiki_gate_precheck.py --mode frontmatter` still exits nonzero
because 5 `possible_unregistered_producer` warnings reduce the score to
75/100. The wiki recovery workflow uses that precheck exit code, so recovery
remains `blocked_by_recovery_findings` even though there are no blocking
frontmatter errors.

This is no longer a page repair problem. It is a producer-warning gate semantics
problem.

## What Changes

- Decide how producer warnings should affect the frontmatter recovery gate.
- Register legitimate frontmatter-producing scripts, or adjust the precheck
  pass condition so non-blocking warnings do not block recovery.
- Preserve warning visibility in reports.
- Add regression evidence showing page errors still block recovery while
  producer warnings alone do not.

## Out of Scope

- Adding or changing wiki page frontmatter.
- Changing taxonomy vocabulary.
- Applying wiki treatment or surgery.
- Archiving the previous repair change before this gate decision is verified.

## Acceptance

- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10` exits 0
  when `blocking_count: 0` and only non-blocking warnings remain.
- Producer warnings remain visible in output.
- A page with a real blocking frontmatter error still exits nonzero.
- Wiki recovery no longer reports `blocked_by_recovery_findings` solely because
  producer warnings exist.
