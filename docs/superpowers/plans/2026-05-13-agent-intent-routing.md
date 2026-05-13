# Agent Intent Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add repo-local Agent Intent Routing so repo-public artifacts such as `README.md` route through `public-report-quality-gate` before editing.

**Architecture:** OpenSpec owns the workflow-change boundary. `AGENTS.md` gets the compact entry rule and minimal parent-gate routing map. `.codex/skills/public-report-quality-gate/SKILL.md` keeps ownership of reader-facing and repo-public output quality through a lightweight path, while tests and evaluation evidence prove the expected future route.

**Tech Stack:** Markdown, OpenSpec artifacts, repo-local Codex skills, Python `unittest` documentation tests.

---

## File Structure

- Create `openspec/changes/route-repo-public-artifacts-through-agent-intent/proposal.md`: scope and non-goals for the routing change.
- Create `openspec/changes/route-repo-public-artifacts-through-agent-intent/design.md`: implementation boundaries for Agent Intent Routing and public gate lightweight path.
- Create `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`: execution checklist.
- Create `openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing/spec.md`: OpenSpec requirements for repo-public artifact routing.
- Create `openspec/changes/route-repo-public-artifacts-through-agent-intent/evaluation.md`: RED/GREEN behavior replay evidence.
- Create `tests/test_agent_intent_routing.py`: documentation behavior tests for AGENTS, public gate, pressure scenarios, OpenSpec change, and evaluation evidence.
- Modify `AGENTS.md`: add a compact `Agent Intent Routing` section near high-frequency skills and output routing.
- Modify `.codex/skills/public-report-quality-gate/SKILL.md`: add repo-public artifact trigger semantics and lightweight path rules.
- Modify `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`: add replay scenarios for repo-public artifacts and non-interference with other gates.

---

### Task 1: Create OpenSpec Change Boundary

**Files:**
- Create: `openspec/changes/route-repo-public-artifacts-through-agent-intent/proposal.md`
- Create: `openspec/changes/route-repo-public-artifacts-through-agent-intent/design.md`
- Create: `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`
- Create: `openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing/spec.md`

- [ ] **Step 1: Create the OpenSpec directories**

Run:

```bash
mkdir -p openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing
```

Expected: command exits `0`.

- [ ] **Step 2: Add `proposal.md`**

Write `openspec/changes/route-repo-public-artifacts-through-agent-intent/proposal.md`:

```markdown
# route-repo-public-artifacts-through-agent-intent

## Why

The repository has strong delivery gates, but an agent can still treat a
repo-public writing request as an ordinary Markdown edit.

The observed failure was `readMe写一下`: the README was rewritten before the
agent clearly routed the request through `public-report-quality-gate` and before
it scanned README-specific repository requirements. The missing step was an
entry-layer intent classification before acting.

## What Changes

- Add an `Agent Intent Routing` section to `AGENTS.md`.
- Route repo-public artifacts such as `README.md`, `docs/*`, `examples/*`, and
  published templates through `public-report-quality-gate` lightweight path.
- Add repo-public artifact trigger semantics and lightweight path rules to
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Add pressure scenarios for repo-public routing and non-interference with
  external learning, wiki frontmatter, and reader-facing publication gates.
- Add behavior replay evidence for the README incident.

## Out of Scope

- A large generic output routing framework.
- Making `public-report-quality-gate` the router for all tasks.
- Requiring `wiki/ops/*-report-gate-review.md` for every small README or docs
  edit.
- Replacing wiki frontmatter taxonomy, skill authoring, OpenSpec lifecycle, or
  learning-capture gates.
- Batch rewriting existing public materials.

## Source Design

- `docs/superpowers/specs/2026-05-13-agent-intent-routing-design.md`
```

- [ ] **Step 3: Add `design.md`**

Write `openspec/changes/route-repo-public-artifacts-through-agent-intent/design.md`:

```markdown
# Design

## Entry Boundary

`AGENTS.md` owns the compact entry rule:

Before acting, classify the user intent. If the request writes, rewrites,
polishes, prepares, or updates an artifact that will be read outside the current
chat or worklog, route through the applicable parent gate before editing.

## Parent Gate Boundary

Agent Intent Routing only chooses the parent gate. It does not replace
specialized gates.

Minimum map:

- repo-public artifact -> `public-report-quality-gate` lightweight path
- reader-facing report / Feishu draft / H5 / share page ->
  `public-report-quality-gate` full path
- external article / repo / README used for learning -> `learning-capture`
- semantic skill edit -> skill authoring contract
- wiki frontmatter edit -> wiki frontmatter taxonomy gate

## Public Gate Lightweight Path

`public-report-quality-gate` continues to own reader-facing and public material
quality. A repo-public artifact enters a lightweight path that requires:

- reader and job-to-be-done identification
- artifact-specific constraint scan before drafting
- no accidental internal residue
- fresh verification before completion, review-ready, publish, or sync claims

The lightweight path does not require a `wiki/ops/*-report-gate-review.md`
artifact by default for small repo-public documentation edits.

## README Constraint Scan

For README work, the artifact-specific scan checks README-related constraints in:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/specs`
- `.codex/skills`
- `wiki/adr`
- `wiki/ops`

The scan is relevance-filtered. It does not require opening every unrelated
README mention.

## Proof Boundary

Tests and evaluation evidence prove repo-visible routing text and pressure
scenario coverage. They do not prove every future AI client will load the
correct skill unless that client honors repo `AGENTS.md` and skill routing.
```

- [ ] **Step 4: Add `tasks.md`**

Write `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts for Agent Intent Routing.
- [ ] 2. Add RED tests for repo-public artifact routing.
- [ ] 3. Add AGENTS intent routing and public gate lightweight path.
- [ ] 4. Add behavior replay evidence and mark tasks.
- [ ] 5. Run verification and commit final state.
```

- [ ] **Step 5: Add OpenSpec requirement deltas**

Write `openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing/spec.md`:

```markdown
## Purpose

Define repo-local Agent Intent Routing so agent actions enter the correct parent
gate before editing repo-public or reader-facing artifacts.

## Requirements

### Requirement: Repository SHALL classify agent intent before acting

The repository SHALL require agents to classify user intent before executing
tasks that may write, rewrite, polish, prepare, or update artifacts.

#### Scenario: Request changes an artifact read outside the current chat

- **WHEN** a user request writes or changes an artifact that will be read
  outside the current chat or worklog
- **THEN** the agent SHALL route through the applicable parent gate before
  editing
- **AND** the agent SHALL preserve specialized gates for frontmatter, skill
  authoring, OpenSpec lifecycle, and learning capture

### Requirement: Repo-public artifacts SHALL route through public gate lightweight path

The repository SHALL route repo-public artifacts through the lightweight path of
`public-report-quality-gate`.

#### Scenario: User asks to write README

- **WHEN** the user asks to write, rewrite, polish, or update `README.md`
- **THEN** the agent SHALL classify the request as a repo-public artifact
- **AND** the agent SHALL route through `public-report-quality-gate`
  lightweight path before editing
- **AND** the agent SHALL scan artifact-specific README constraints before
  drafting

#### Scenario: User asks for a small repo-public documentation edit

- **WHEN** the user asks for a small edit to `README.md`, `docs/*`,
  `examples/*`, or a published template
- **THEN** the agent SHALL identify reader and job-to-be-done
- **AND** the agent SHALL scan relevant artifact-specific constraints
- **AND** the agent SHALL NOT require a `wiki/ops/*-report-gate-review.md`
  artifact unless the output is review-ready, published, synced, complex,
  reference-shaped, or drift-corrected

### Requirement: Agent intent routing SHALL not steal specialized gates

Agent Intent Routing SHALL select the correct parent gate without weakening
existing specialized workflow gates.

#### Scenario: External README is used as learning input

- **WHEN** the user provides an external GitHub or GitLab README and asks what
  can be reused, learned, or adapted
- **THEN** the agent SHALL route to `learning-capture` and the README learning
  module
- **AND** it SHALL NOT treat the source-learning step as a repo-public artifact
  edit

#### Scenario: Wiki frontmatter is edited

- **WHEN** the user asks to create or modify wiki frontmatter
- **THEN** the agent SHALL route to the wiki frontmatter taxonomy gate
- **AND** the public gate SHALL NOT replace the taxonomy checker requirement

#### Scenario: Internal wiki ops page becomes a Feishu article

- **WHEN** the user asks to turn an internal `wiki/ops` page into a Feishu
  article, H5, share draft, or reader-facing report
- **THEN** the agent SHALL route through the full public report gate
- **AND** it SHALL NOT use the lightweight repo-public path as a substitute for
  publish, sync, visual, source, or judgment gates

### Requirement: Agent intent routing SHALL include behavior replay evidence

Changes to agent intent routing SHALL include repo-visible replay evidence.

#### Scenario: Runtime route changes

- **WHEN** the repository adds or changes Agent Intent Routing behavior
- **THEN** the change SHALL include RED baseline, GREEN result, pressure
  scenarios, repo-visible trigger artifacts, and residual risk
- **AND** the evidence SHALL state the proof boundary
```

- [ ] **Step 6: Commit OpenSpec artifacts**

Run:

```bash
git add openspec/changes/route-repo-public-artifacts-through-agent-intent
git commit -m "docs: propose agent intent routing gate"
```

Expected: commit includes only the new OpenSpec change directory.

---

### Task 2: Add RED Tests For Routing Behavior

**Files:**
- Create: `tests/test_agent_intent_routing.py`

- [ ] **Step 1: Add the test file**

Write `tests/test_agent_intent_routing.py`:

```python
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "AGENTS.md"
PUBLIC_SKILL = ROOT / ".codex/skills/public-report-quality-gate/SKILL.md"
PRESSURE = ROOT / ".codex/skills/public-report-quality-gate/references/pressure-scenarios.md"
CHANGE = ROOT / "openspec/changes/route-repo-public-artifacts-through-agent-intent"
SPEC = CHANGE / "specs/agent-intent-routing/spec.md"
EVALUATION = CHANGE / "evaluation.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_agents_declares_agent_intent_routing_entry_rule() -> None:
    text = read(AGENTS)

    assert "## Agent Intent Routing" in text
    assert "Before acting, classify the user intent" in text
    assert "repo-public artifact" in text
    assert ".codex/skills/public-report-quality-gate/SKILL.md" in text
    assert "wiki frontmatter taxonomy gate" in text


def test_public_gate_skill_defines_repo_public_lightweight_path() -> None:
    text = read(PUBLIC_SKILL)

    assert "repo-public artifact" in text
    assert "README.md" in text
    assert "docs/*" in text
    assert "examples/*" in text
    assert "lightweight path" in text
    assert "reader and job-to-be-done" in text
    assert "artifact-specific constraint scan" in text
    assert "does not require a `wiki/ops/*-report-gate-review.md`" in text


def test_pressure_scenarios_replay_agent_intent_routing() -> None:
    text = read(PRESSURE)

    assert "Agent Intent Routing Replay" in text
    assert "readMe写一下" in text
    assert "repo-public artifact" in text
    assert "README constraint scan" in text
    assert "这个外部 README 学一下能不能复用" in text
    assert "learning-capture" in text
    assert "改一下 wiki frontmatter" in text
    assert "wiki-frontmatter-taxonomy" in text


def test_openspec_change_requires_repo_public_routing() -> None:
    text = read(SPEC)

    assert "Repository SHALL classify agent intent before acting" in text
    assert "Repo-public artifacts SHALL route through public gate lightweight path" in text
    assert "Agent intent routing SHALL not steal specialized gates" in text
    assert "Agent intent routing SHALL include behavior replay evidence" in text


def test_evaluation_records_red_green_replay_and_residual_risk() -> None:
    text = read(EVALUATION)

    assert "RED Baseline" in text
    assert "GREEN Result" in text
    assert "readMe写一下" in text
    assert "repo-visible trigger artifacts" in text
    assert "Proof Boundary" in text
    assert "Residual Risks" in text
```

- [ ] **Step 2: Run the new tests and confirm RED**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing -v
```

Expected: failures show missing `Agent Intent Routing` text in `AGENTS.md`, missing repo-public lightweight path text in `public-report-quality-gate`, missing pressure scenarios, and missing `evaluation.md`.

- [ ] **Step 3: Commit the RED tests**

Run:

```bash
git add tests/test_agent_intent_routing.py
git commit -m "test: cover agent intent routing"
```

Expected: commit includes only `tests/test_agent_intent_routing.py`.

---

### Task 3: Add AGENTS Routing And Public Gate Lightweight Path

**Files:**
- Modify: `AGENTS.md`
- Modify: `.codex/skills/public-report-quality-gate/SKILL.md`
- Modify: `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
- Modify: `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`

- [ ] **Step 1: Add `Agent Intent Routing` to `AGENTS.md`**

Insert this section after `High-Frequency Skills` and before `Wiki Frontmatter Taxonomy Gate`:

```markdown
## Agent Intent Routing

- Before acting, classify the user intent.
- If the request writes, rewrites, polishes, prepares, or updates an artifact
  that will be read outside the current chat or worklog, route through the
  applicable parent gate before editing.
- Keep this section as a routing map only. Do not duplicate full skill bodies,
  taxonomy vocabulary, report scorecards, or long examples here.

Minimum routes:

| Intent shape | Parent gate |
|---|---|
| Repo-public artifact such as `README.md`, `docs/*`, `examples/*`, or published templates | `.codex/skills/public-report-quality-gate/SKILL.md` lightweight path |
| Reader-facing report, Feishu review draft, H5/share draft, or public material | `.codex/skills/public-report-quality-gate/SKILL.md` full path |
| External article, repo, README, or example used as learning or reference material | `.codex/skills/learning-capture/SKILL.md` and narrower module |
| Semantic edit to `.codex/skills/*` | Skill Authoring Contract |
| Wiki frontmatter, wiki templates, or repo-local frontmatter producers | Wiki frontmatter taxonomy gate |

Rules:

- Repo-public artifact work must identify the reader and job-to-be-done, then
  scan artifact-specific constraints before drafting.
- README work must scan relevant `README SHALL`, `README`, and `readme` hits in
  `AGENTS.md`, `PROJECT.md`, `openspec/specs`, `.codex/skills`, `wiki/adr`, and
  `wiki/ops` before drafting.
- Do not let the public gate replace specialized gates for frontmatter,
  semantic skill edits, OpenSpec lifecycle, or external learning.
```

- [ ] **Step 2: Add repo-public artifact trigger to `public-report-quality-gate`**

In `.codex/skills/public-report-quality-gate/SKILL.md`, extend the `When To Use` list by adding this bullet after the existing reader-facing bullets:

```markdown
- repo-public artifacts such as `README.md`, `docs/*`, `examples/*`, or
  published templates when they are written, rewritten, polished, prepared, or
  updated for readers outside the current chat or worklog
```

- [ ] **Step 3: Add lightweight path rules to `public-report-quality-gate`**

In `.codex/skills/public-report-quality-gate/SKILL.md`, add this section after `Outer Gate Role`:

```markdown
## Repo-Public Lightweight Path

When Agent Intent Routing classifies a request as a repo-public artifact, this
gate owns a lightweight path.

Use the lightweight path for `README.md`, `docs/*`, `examples/*`, and published
templates when the output is meant for future contributors, users, agents, or
other readers outside the current chat or worklog.

Required checks:

- Identify the reader and job-to-be-done before drafting.
- Run an artifact-specific constraint scan before drafting. For README work,
  scan relevant `README SHALL`, `README`, and `readme` hits in `AGENTS.md`,
  `PROJECT.md`, `openspec/specs`, `.codex/skills`, `wiki/adr`, and `wiki/ops`.
- Avoid internal residue unless the artifact intentionally documents repo
  mechanics for its readers.
- Use fresh evidence before claiming the artifact is complete, review-ready,
  published, or synced.

The lightweight path does not require a `wiki/ops/*-report-gate-review.md`
artifact by default for small repo-public documentation edits. Create or update
a gate-review artifact when the output is review-ready, published, synced to
Feishu, complex, reference-shaped, or drift-corrected.

This path must not replace specialized gates for wiki frontmatter, semantic
skill edits, OpenSpec lifecycle, or external learning capture.
```

- [ ] **Step 4: Add pressure scenarios**

Append this section to `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` before `## Validation Notes`:

```markdown
## Agent Intent Routing Replay

| Scenario | Expected Result |
|---|---|
| User says `readMe写一下` | Agent Intent Routing classifies the request as repo-public artifact work, loads the public gate lightweight path, identifies the README reader/job-to-be-done, and runs a README constraint scan before drafting |
| User says `把这个 wiki/ops 改成飞书文章` | Route to the full public report gate because the internal ops note is being rewritten for a reader-facing Feishu article |
| User says `这个外部 README 学一下能不能复用` | Route to `learning-capture` and the README learning module; do not treat the external source-learning step as a repo-public artifact edit |
| User says `改一下 wiki frontmatter` | Route to `wiki-frontmatter-taxonomy`; do not let the public gate replace the taxonomy checker |
| A small README typo fix is requested | Use the lightweight path with reader/job and relevant constraint awareness; do not require a gate-review artifact unless a review-ready, publish, sync, complex, reference-shaped, or drift-corrected claim is made |
```

- [ ] **Step 5: Mark implementation tasks through Task 3**

Edit `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md` so the first three task lines are checked:

```markdown
# Tasks

- [x] 1. Create OpenSpec change artifacts for Agent Intent Routing.
- [x] 2. Add RED tests for repo-public artifact routing.
- [x] 3. Add AGENTS intent routing and public gate lightweight path.
- [ ] 4. Add behavior replay evidence and mark tasks.
- [ ] 5. Run verification and commit final state.
```

- [ ] **Step 6: Run routing tests and public gate tests**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

Expected: `test_agent_intent_routing` may still fail only on missing `evaluation.md`. Existing `test_public_report_quality_gate` should pass.

- [ ] **Step 7: Commit routing assets**

Run:

```bash
git add AGENTS.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/public-report-quality-gate/references/pressure-scenarios.md openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md
git commit -m "docs: route repo public artifacts through public gate"
```

Expected: commit includes only the listed routing assets.

---

### Task 4: Add Behavior Replay Evidence

**Files:**
- Create: `openspec/changes/route-repo-public-artifacts-through-agent-intent/evaluation.md`
- Modify: `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`

- [ ] **Step 1: Add `evaluation.md`**

Write `openspec/changes/route-repo-public-artifacts-through-agent-intent/evaluation.md`:

```markdown
# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| `readMe写一下` | Agent Intent Routing -> repo-public artifact -> public gate lightweight path -> README constraint scan | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| `把这个 wiki/ops 改成飞书文章` | Full public report gate because an internal ops note becomes reader-facing Feishu content | `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` Agent Intent Routing Replay |
| `这个外部 README 学一下能不能复用` | `learning-capture` and README learning module, not repo-public artifact edit | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| `改一下 wiki frontmatter` | `wiki-frontmatter-taxonomy` gate remains responsible | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| Small README typo fix | Public gate lightweight path applies without default gate-review artifact requirement | `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` Agent Intent Routing Replay |

## Behavior Replay Evidence

| Replay Field | Evidence |
|---|---|
| Input or situation shape | User asks the agent to write, rewrite, polish, prepare, or update a repo-public artifact such as `README.md`, `docs/*`, `examples/*`, or a published template. |
| Trigger condition | Repo `AGENTS.md` contains `Agent Intent Routing` requiring intent classification before acting and routing repo-public artifacts to `.codex/skills/public-report-quality-gate/SKILL.md` lightweight path. |
| Expected route or stop behavior | Agent loads the public gate lightweight path, identifies reader/job-to-be-done, scans relevant artifact-specific constraints, then drafts. If the work is actually frontmatter, semantic skill editing, external learning, OpenSpec lifecycle, or full reader-facing publication, the specialized gate wins. |
| Repo-visible trigger artifacts | `AGENTS.md`, `.codex/skills/public-report-quality-gate/SKILL.md`, `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`, and `openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing/spec.md`. |
| Expected output or non-output | Repo-public drafts are not treated as ordinary Markdown edits. Small repo-public edits do not create gate-review artifacts by default. Review-ready, publish, Feishu sync, complex, reference-shaped, or drift-corrected outputs still require stronger gate evidence. |
| Promotion or non-promotion boundary | This change adds repo-local routing only. It does not promote the rule to global AGENTS, team lore, or root-scope skills. |
| Proof Boundary | Tests prove repo-visible routing text and pressure scenarios. They do not prove every future AI client will load the correct skill unless that client honors repo `AGENTS.md` and skill routing. |

## RED Baseline

- Before this change, `public-report-quality-gate` covered public materials and
  reader-facing outputs but did not explicitly name repo-public artifacts such
  as `README.md`, `docs/*`, `examples/*`, or published templates.
- Before this change, `AGENTS.md` did not include an entry-layer `Agent Intent
  Routing` section requiring intent classification before acting.
- Before this change, the README incident showed that a repo-public artifact
  could be rewritten before the agent explicitly routed through the public gate
  lightweight path or scanned README-specific constraints.
- The RED test run failed because `AGENTS.md`, `public-report-quality-gate`, and
  pressure scenarios did not contain the required repo-public routing terms, and
  `evaluation.md` did not exist.

## GREEN Result

- `AGENTS.md` contains `Agent Intent Routing` with a compact parent-gate map.
- `.codex/skills/public-report-quality-gate/SKILL.md` includes repo-public
  artifact trigger semantics and a lightweight path.
- `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
  includes Agent Intent Routing replay scenarios.
- The OpenSpec change contains requirements for intent classification,
  repo-public lightweight routing, specialized-gate preservation, and behavior
  replay evidence.
- Targeted tests pass:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

## Residual Risks

- Very small repo-public wording edits may feel heavy if the lightweight path is
  interpreted as the full report gate. The skill text states the lightweight
  path and gate-review artifact boundary to keep this bounded.
- README constraint scans can surface unrelated references. The design and gate
  text require relevant artifact-specific scanning rather than opening every
  hit.
- Future AI clients still need to honor repo `AGENTS.md` and skill routing.
  This change creates repo-visible routing evidence, not automatic enforcement
  across all clients.
```

- [ ] **Step 2: Mark Task 4 complete**

Edit `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec change artifacts for Agent Intent Routing.
- [x] 2. Add RED tests for repo-public artifact routing.
- [x] 3. Add AGENTS intent routing and public gate lightweight path.
- [x] 4. Add behavior replay evidence and mark tasks.
- [ ] 5. Run verification and commit final state.
```

- [ ] **Step 3: Run routing and public gate tests**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

Expected: all tests pass.

- [ ] **Step 4: Commit evaluation evidence**

Run:

```bash
git add openspec/changes/route-repo-public-artifacts-through-agent-intent/evaluation.md openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md
git commit -m "docs: evaluate agent intent routing"
```

Expected: commit includes only evaluation and tasks updates.

---

### Task 5: Final Verification And Completion Boundary

**Files:**
- Modify: `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`

- [ ] **Step 1: Run targeted verification**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

Expected: all tests pass.

- [ ] **Step 2: Run focused string checks**

Run:

```bash
rg -n "Agent Intent Routing|repo-public artifact|lightweight path|readMe写一下|README constraint scan" AGENTS.md .codex/skills/public-report-quality-gate openspec/changes/route-repo-public-artifacts-through-agent-intent tests/test_agent_intent_routing.py
```

Expected: matches appear in AGENTS, the public gate skill or pressure scenarios, the OpenSpec change, evaluation evidence, and tests.

- [ ] **Step 3: Mark all OpenSpec tasks complete**

Edit `openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec change artifacts for Agent Intent Routing.
- [x] 2. Add RED tests for repo-public artifact routing.
- [x] 3. Add AGENTS intent routing and public gate lightweight path.
- [x] 4. Add behavior replay evidence and mark tasks.
- [x] 5. Run verification and commit final state.
```

- [ ] **Step 4: Commit final task state**

Run:

```bash
git add openspec/changes/route-repo-public-artifacts-through-agent-intent/tasks.md
git commit -m "docs: complete agent intent routing change"
```

Expected: commit includes only `tasks.md`.

- [ ] **Step 5: Stop implementation**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected:

- Latest commit is `docs: complete agent intent routing change`.
- Existing unrelated dirty files may remain.
- No additional implementation, archive, broad cleanup, or adjacent automation is started after all checkboxes are complete. The default next action is archive review in a separate step.
