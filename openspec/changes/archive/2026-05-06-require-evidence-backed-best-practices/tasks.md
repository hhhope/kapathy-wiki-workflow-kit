## 1. Setup

- [x] 1.1 Decide landing layer.
  <!-- 2026-05-06 — repo AGENTS.md, not skill. This is an always-on promotion gate, not a trigger-specific capability. -->
- [x] 1.2 Confirm current `compress-root-agents-budget` remains separate.
  <!-- 2026-05-06 — current root-context change stays focused on root AGENTS; this change owns repo default constraint. -->

## 2. Implementation

- [x] 2.1 Add the evidence-backed best-practice gate to repo `AGENTS.md`.
- [x] 2.2 Add spec delta to `example-driven-wiki-capture`.
- [x] 2.3 Keep skill creation/editing out of scope.

## 3. Validation

- [x] 3.1 Confirm `AGENTS.md` states candidate learning may be captured but not promoted without evidence.
- [x] 3.2 Confirm accepted evidence shapes are exactly: external-document excerpt, local demo/fixture, git-like project comparison.
- [x] 3.3 Run `openspec validate require-evidence-backed-best-practices --strict`.
  <!-- PASS 2026-05-06 — validate returned "Change 'require-evidence-backed-best-practices' is valid"; PostHog DNS noise only -->

## 4. Self-Check

- [x] 4.1 Structural: OpenSpec artifacts exist and validate.
- [x] 4.2 Semantic: landing layer is repo default governance, not a skill.
- [x] 4.3 Evidence: change records why promotion requires evidence.
- [x] 4.4 Boundary: no root dotfile, skill, or wiki method page changed.
