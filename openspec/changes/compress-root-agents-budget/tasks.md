## 1. Setup

- [ ] 1.1 Confirm target files: `~/.codex/AGENTS.md` plus at most one
  root-local routing support file under `~/.codex/`.
- [ ] 1.2 Record baseline counts and section headings in `evaluation.md`.
- [ ] 1.3 Confirm repo dirty tree unrelated files stay excluded from this
  change's commits.

## 2. Compression

- [ ] 2.1 Extract Global Rule Routing detail from `~/.codex/AGENTS.md` into
  `~/.codex/rule-routing.md` or equivalent root-local support file.
- [ ] 2.2 Replace the extracted table in `AGENTS.md` with a compact load
  instruction.
- [ ] 2.3 Consolidate `Execution discipline` and `Git discipline` into one
  section without weakening dirty-tree, commit, branch, resume, push, or
  truth-source behavior.
- [ ] 2.4 Remove duplicated wording introduced by the consolidation.
- [ ] 2.5 Keep deferred routing-table rows out of scope.

## 3. Validation

- [ ] 3.1 Record after counts and percentage delta in `evaluation.md`.
- [ ] 3.2 Confirm `AGENTS.md` is at or below 220 lines, or record why the
  overshoot remains Root-pattern compliant.
- [ ] 3.3 Confirm the support file contains only root-local routing detail and
  no repo-specific policy.
- [ ] 3.4 Confirm no repo `AGENTS.md`, repo `.codex/skills/`, repo `wiki/`,
  repo `rules/`, or `~/.claude/CLAUDE.md` file was edited.
- [ ] 3.5 Run `openspec validate compress-root-agents-budget --strict`.

## 4. Self-Check

- [ ] 4.1 Structural: OpenSpec artifacts exist and validate.
- [ ] 4.2 Semantic: target layer remains Root AGENTS; extracted support file is
  a reference, not a new governance layer.
- [ ] 4.3 Evidence: before/after counts and residual risks are recorded.
- [ ] 4.4 Boundary: no new Pattern Catalog pattern, checklist item, skill, wiki
  method page, or repo policy is introduced.
