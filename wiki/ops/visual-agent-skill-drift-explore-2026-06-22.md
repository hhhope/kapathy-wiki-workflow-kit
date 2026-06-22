---
title: Visual Agent Skill Drift Explore
layer: ops
domain: agent-harness
ops_area: workflow-trace
canonical_object: visual-agent-skill-drift
artifact_type: explore-trace
created: 2026-06-22
status: exploring
trace_mode: openspec-explore
source_path: chat://openspec-explore/visual-agent-skill-drift/2026-06-22
related_artifacts:
  - /mnt/d/skills/account-skills
  - /mnt/d/cloud/account-meeting-lore/.codex/skills/visual-agent/SKILL.md
  - wiki/ops/visual-output-routing-drift-explore-2026-05-11.md
---

# Visual Agent Skill Drift Explore

## Trigger

The user invoked `$report-wiki-portfolio:openspec-explore` after repeated drift
while repairing `visual-agent` and related visual skills in
`D:\skills\account-skills`.

## Current Question

- What exactly changed in the visual skill package?
- Which changes still risk routing drift?
- Did the repair follow the repo's skill-writing and migration gates?
- Why did the conversation keep drifting into wrong repos, wrong branches, CR
  Agent work, draft state, and fixed colloquial trigger wording?

## Boundary

This is an explore trace only. It records the investigation anchor before more
analysis continues. It does not approve additional skill edits, branch changes,
or rollout claims.

## Findings

### 1. Package repair and runtime repair are different

`D:\skills\account-skills` branch `feat/visual-agent` now contains a newer
`skills/visual-agent/SKILL.md` than this repo's installed
`.codex/skills/visual-agent/SKILL.md`.

The account-skills branch describes bundled visual workers. The currently
installed repo-local runtime copy still describes only `svg-flow-diagram` as
bundled and treats the other visual workers as companions.

### 2. Worker directories were bundled, but the installer/readme path is not closed

The account-skills branch added ordinary visual worker directories under
`skills/`, but package-level README and integration-kit guidance still contain
older plugin/CR-agent-oriented explanations and old skill-writing examples that
emphasize fixed trigger words.

This means a user or future agent can install or follow the package through a
path that does not actually install or teach the visual bundle correctly.

### 3. Old visual skill names still leak through the governance kit

The branch still has references to `xiaohongshu-retro-grid-content` in
`codex-integration-kit/README.md` and `feishu-doc-writing` material, while the
visual package renamed the local worker to `visual-knowledge-onepager`.

That creates a split identity: the visual-agent route table points at the new
worker name, but adjacent governance docs can still route humans or agents to
the old channel-specific name.

### 4. Skill-authoring evidence exists but is incomplete

`skills/visual-agent/evaluation.md` now records RED/GREEN behavior for worker
bundling and fixed-phrase trigger cleanup. That is useful evidence, but it does
not cover all package-level behavior:

- direct install into a target Codex home;
- runtime skill discovery after install;
- package README examples no longer teaching fixed trigger lists;
- host repo installed copy matching the account-skills branch;
- OpenSpec proposal/design/tasks coverage for a behavior-asset change.

### 5. Current report-wiki runtime still has only visual-agent installed

In this repo, `find .codex/skills -maxdepth 2 -name SKILL.md` shows
`visual-agent` but not the newly bundled visual workers. Therefore current
runtime behavior can still miss the intended child workers even though the
account-skills branch contains them.

## 2026-06-22 Repo-Local Repair

The repo-local phase created OpenSpec change
`openspec/changes/close-visual-agent-runtime-loop` and installed the visual
worker surface under `.codex/skills/`.

The repo-local runtime discovery check now finds:

- `visual-agent`
- `knowledge-article-visual`
- `infographic-onepager`
- `visual-knowledge-onepager`
- `svg-flow-diagram`
- `sequence-diagram`
- `architecture-diagram`
- `frontend-visual-governor`
- `project-weekly-report-gantt-map`
- `lark-whiteboard`

The fixed-trigger scan no longer finds route-controlling old colloquial trigger
rows or the old `xiaohongshu-retro-grid-content` name in the repo-local visual
runtime surface. Remaining scan hits are style-reference wording inside
`lark-whiteboard`, not route rules.

The account-skills branch still needs a later package-level cleanup for README,
integration-kit, install guidance, and old skill-name references.

## Frontmatter Gate Note

`python3 scripts/wiki_gate_precheck.py --mode frontmatter --target
wiki/ops/visual-agent-skill-drift-explore-2026-06-22.md` was run before and
after creating this trace. The precheck reported existing full-repo blockers in
legacy `wiki/reports` files and returned `target.entry_count=0` for this new
file. This trace therefore should not be treated as full taxonomy-compliance
proof; it is only the required repo-visible explore anchor.
