# Evaluation

## Baseline Scenarios

1. The user asks to implement the personal global AGENTS / skill / harness plan
   after a chat-level design.
2. The agent treats the chat plan as sufficient and prepares to edit behavior
   assets directly.
3. The agent treats wiki publication as either the default landing zone or an
   out-of-scope action, without explaining which learning still needs to land.
4. The design describes harness broadly enough that it can be mistaken for a
   hook, CI gate, runtime gate, or automatic compliance mechanism.
5. The design says the candidate model is reviewable but does not define
   measurable review boundaries.

## Before Results

- The implementation path was under-specified: the plan described the desired
  collaboration model but did not first bind it to the active OpenSpec change.
- The previous design compressed rules, skills, and harness evidence into an
  incomplete `AGENTS.md` / `SKILL.md` / replay-harness model.
- The first follow-up needed re-anchoring because "implement the plan" could
  mean root dotfile edits, repo wiki publication, skill authoring, or design
  artifact updates.
- Candidate routing was written too close to a settled operating model, even
  though the final responsibility split remained open.
- Wiki landing was ambiguous: the active change correctly blocked wiki method
  publication, but the learning trace itself was left unclear.
- Harness shape was too abstract; it did not clearly state the minimum
  artifacts, phased path, or proof boundary.
- The design lacked quantified criteria for deciding whether the repair stayed
  inside reviewable design scope.

## After Results

- The active change records a candidate hybrid ownership model for review
  instead of treating the model as accepted.
- The design records the SDD-first gate before any root dotfile, skill, rule, or
  wiki method change.
- The design now records the full candidate governance stack: root `AGENTS`,
  rules, skills, OpenSpec, harness evidence, and wiki/ADR/retro durable layers.
- Harness v1 is limited to manual replay evidence: `replay-harness.md`,
  fixture, and `evaluation.md`; checker work is explicitly deferred to Phase 2.
- Quantified review criteria now state that this change makes 0 root dotfile
  edits, 0 repo skill edits, 0 root rule edits, and 0 wiki method page edits.
- The existing `codex-global-agents-md` intake now records the learning
  conclusion and explains why the previous run did not land wiki material.
- Routing examples are preserved as candidate examples, not final operating
  decisions.

## Residual Risks

- No root dotfile has been edited yet, so runtime behavior has not changed.
- No skill has been authored or modified, so skill trigger behavior remains
  untested.
- Root rules and behavior-asset routing have not been changed, so this repair
  does not alter execution constraints.
- Replay-harness v1 remains evidence only; it has not been converted into a
  hook, CI gate, runtime gate, or enforcement path for this topic.
- The final root/repo alignment model, ownership responsibility, and six-layer
  responsibility split remain open pending review.
- The optional minimum sync tasks remain open and must not be treated as done
  until root-level edits, if any, are separately accepted and verified.
