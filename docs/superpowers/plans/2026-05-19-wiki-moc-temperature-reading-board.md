# Wiki MOC Temperature Reading Board Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make MOC generation consume temperature-reviewed wiki clue windows instead of raw relation-type edges.

**Architecture:** Keep graph extraction deterministic, add a small temperature/admission module that turns graph edges plus explicit review judgments into clue windows, then make MOC relation pages admission-gated. Medical-agent MOC preview remains read-only and surfaces admitted, blocked, and review-needed counts.

**Tech Stack:** Python standard library, `unittest`, existing OpenSpec workflow, existing wiki graph/MOC scripts.

---

## File Structure

- Create `openspec/changes/add-moc-temperature-reading-board/proposal.md`: OpenSpec proposal that makes this large workflow change authoritative.
- Create `openspec/changes/add-moc-temperature-reading-board/design.md`: OpenSpec design copied from the approved Superpowers spec in implementation-ready terms.
- Create `openspec/changes/add-moc-temperature-reading-board/tasks.md`: authoritative task checklist.
- Create `openspec/changes/add-moc-temperature-reading-board/specs/moc-temperature-reading-board/spec.md`: behavioral requirements and scenarios.
- Create `scripts/wiki_moc_temperature.py`: relation feature package, clue-window review merge, temperature banding, and MOC admission plan.
- Modify `scripts/wiki_moc_projection.py`: accept an optional admission plan and stop creating relation MOC pages from raw relation types.
- Modify `scripts/build_wiki_moc_projection.py`: optional review JSON input, dry-run admission summary, and explicit apply protection.
- Modify `scripts/wiki_medical_agent.py`: include temperature admission summary in MOC surgery preview.
- Modify `tests/test_wiki_moc_projection.py`: update old relation-page expectations and add admission-gated relation-page coverage.
- Create `tests/test_wiki_moc_temperature.py`: unit tests for feature packages, clue windows, banding, mechanical relation blocking, and admission.
- Modify `tests/test_wiki_medical_agent.py`: assert MOC preview remains read-only and exposes admission summary.

## Task 1: Create The OpenSpec Change

**Files:**
- Create: `openspec/changes/add-moc-temperature-reading-board/proposal.md`
- Create: `openspec/changes/add-moc-temperature-reading-board/design.md`
- Create: `openspec/changes/add-moc-temperature-reading-board/tasks.md`
- Create: `openspec/changes/add-moc-temperature-reading-board/specs/moc-temperature-reading-board/spec.md`

- [ ] **Step 1: Create the change directories**

Run:

```bash
mkdir -p openspec/changes/add-moc-temperature-reading-board/specs/moc-temperature-reading-board
```

Expected: command exits `0`.

- [ ] **Step 2: Write `proposal.md`**

Create `openspec/changes/add-moc-temperature-reading-board/proposal.md` with:

```markdown
# Proposal: add MOC temperature reading board

## Why

The current Obsidian MOC projection can generate relation pages directly from
frontmatter graph edges. That is mechanically correct, but it lets low-value
relation types such as `derived_from` and `related_objects` become standalone
MOC pages without proving reading value.

The repository needs a value-first admission layer before MOC projection. MOC
should reveal useful wiki relationships and clues, not raw edge dumps.

## What Changes

- Add a relation temperature reading-board layer that converts graph edges into
  bounded clue windows.
- Keep Python responsible for structural feature packages only.
- Require explicit AI or human review judgments for semantic temperature.
- Gate relation MOC pages behind admitted high-temperature clue windows.
- Surface admitted, blocked, and review-needed counts in MOC dry-run and
  medical-agent MOC preview.
- Keep MOC preview and medical-agent review read-only.

## Impact

- Affects `scripts/wiki_moc_temperature.py`, `scripts/wiki_moc_projection.py`,
  `scripts/build_wiki_moc_projection.py`, and `scripts/wiki_medical_agent.py`.
- Updates MOC projection tests and medical-agent preview tests.
- Existing domain and object MOC pages remain available.
- Relation MOC pages are no longer created from raw relation types by default.
```

- [ ] **Step 3: Write `design.md`**

Create `openspec/changes/add-moc-temperature-reading-board/design.md` with:

```markdown
# Design: MOC temperature reading board

## Model

The MOC pipeline becomes:

```text
graph/frontmatter
-> relation feature package
-> explicit temperature review
-> clue windows
-> MOC admission plan
-> generated MOC projection
```

Graph extraction remains deterministic. It supplies pages, canonical objects,
domains, and relation fields. It does not decide semantic value.

## Relation Feature Package

`scripts/wiki_moc_temperature.py` builds one package per graph edge:

- `candidate_id`
- `source_page`
- `source_object`
- `relation_type`
- `target_object`
- `source_layer`
- `target_layer`
- `evidence_refs`
- `structural_features`

Structural features may include `cross_layer`, `has_spec_support`,
`has_adr_support`, `fanout_count`, and `mechanical_relation`.

## Temperature Review

The first implementation does not call an external model. It accepts explicit
review judgments as JSON and merges them with feature packages. Missing review
judgment produces a `needs_review` clue window. Mechanical relation types are
blocked unless the review explicitly admits them with high temperature.

## MOC Admission

Domain and object MOC candidates remain structural in this change. Relation MOC
pages are gated:

- No raw relation type becomes a relation MOC page by default.
- A relation type becomes a MOC page only when the admission plan lists it in
  `admitted_relations`.
- `derived_from` and `related_objects` remain blocked unless explicit review
  evidence admits them.

## Medical Agent

Medical-agent MOC preview includes temperature admission counts and a small
sample of clue windows. It does not write `wiki/moc`, treatment records,
surgery records, OpenSpec state, relation fields, or taxonomy config.
```

- [ ] **Step 4: Write `tasks.md`**

Create `openspec/changes/add-moc-temperature-reading-board/tasks.md` with:

```markdown
# Tasks

- [ ] 1. Add OpenSpec requirements for temperature-reviewed MOC admission.
- [ ] 2. Add relation feature package and clue-window admission module.
- [ ] 3. Gate relation MOC candidates behind an admission plan.
- [ ] 4. Add optional review JSON support to the MOC projection CLI.
- [ ] 5. Surface temperature admission in medical-agent MOC preview.
- [ ] 6. Add unit tests and behavior replay coverage.
- [ ] 7. Run validation and record evaluation evidence.
```

- [ ] **Step 5: Write the OpenSpec requirement**

Create `openspec/changes/add-moc-temperature-reading-board/specs/moc-temperature-reading-board/spec.md` with:

```markdown
# moc-temperature-reading-board Specification

## ADDED Requirements

### Requirement: Repository SHALL build relation feature packages before MOC admission

The repository SHALL derive bounded relation feature packages from explicit
wiki graph edges without claiming semantic value from Python-only scoring.

#### Scenario: Feature package is built from a graph edge

- **GIVEN** a graph edge with `source_page_path`, `relation_type`, and `target`
- **WHEN** relation feature packages are built
- **THEN** the package SHALL include source page, source object, relation type,
  target object, evidence refs, and structural features
- **AND** it SHALL NOT include a final MOC admission decision.

### Requirement: Repository SHALL gate relation MOC pages through temperature clue windows

The repository SHALL prevent raw relation types from becoming standalone MOC
pages unless an admission plan admits the relation from reviewed clue windows.

#### Scenario: Raw mechanical relation is blocked

- **GIVEN** graph edges with relation type `derived_from`
- **WHEN** MOC candidates are built without an admission plan
- **THEN** no `wiki/moc/relation-derived_from.md` candidate SHALL be produced.

#### Scenario: Reviewed relation is admitted

- **GIVEN** a temperature clue board with an admitted relation type `validates`
- **WHEN** MOC candidates are built with the derived admission plan
- **THEN** `wiki/moc/relation-validates.md` SHALL be produced.

### Requirement: Medical-agent MOC preview SHALL remain read-only while surfacing admission state

The medical-agent MOC preview SHALL include temperature admission counts when
available and SHALL NOT write MOC pages or workflow records.

#### Scenario: MOC preview reports admission state

- **GIVEN** one active medical case
- **WHEN** the user asks for MOC preview surgery
- **THEN** the payload SHALL include MOC projection summary, surgery preview,
  and temperature admission summary
- **AND** no `wiki/moc` files SHALL be written.
```

- [ ] **Step 6: Validate the OpenSpec change**

Run:

```bash
openspec validate add-moc-temperature-reading-board --strict
```

Expected: validation passes.

- [ ] **Step 7: Commit the OpenSpec change**

Run:

```bash
git add openspec/changes/add-moc-temperature-reading-board
git commit -m "spec: add MOC temperature reading board"
```

Expected: commit succeeds with only the OpenSpec change staged.

## Task 2: Add Relation Temperature Module

**Files:**
- Create: `tests/test_wiki_moc_temperature.py`
- Create: `scripts/wiki_moc_temperature.py`

- [ ] **Step 1: Write failing tests**

Create `tests/test_wiki_moc_temperature.py` with:

```python
import unittest

from scripts.wiki_moc_temperature import (
    build_moc_admission_plan,
    build_relation_feature_packages,
    build_temperature_clue_board,
    temperature_band,
)


class WikiMocTemperatureTest(unittest.TestCase):
    def sample_graph(self) -> dict:
        return {
            "nodes": [
                {
                    "page_path": "wiki/ops/runtime-method.md",
                    "canonical_object": "runtime-method",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/001-runtime.md",
                    "canonical_object": "runtime-method",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "wiki",
                },
                {
                    "page_path": "openspec/specs/runtime/spec.md",
                    "canonical_object": "runtime-spec",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                    "domain": "wiki",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/adr/001-runtime.md",
                    "relation_type": "derived_from",
                    "target": "runtime-method",
                },
                {
                    "source_page_path": "openspec/specs/runtime/spec.md",
                    "relation_type": "validates",
                    "target": "runtime-method",
                },
            ],
        }

    def test_builds_relation_feature_packages_without_semantic_admission(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())

        self.assertEqual(len(packages), 2)
        derived = next(item for item in packages if item["relation_type"] == "derived_from")
        self.assertEqual(derived["source_object"], "runtime-method")
        self.assertEqual(derived["target_object"], "runtime-method")
        self.assertEqual(derived["evidence_refs"], ["wiki/adr/001-runtime.md"])
        self.assertTrue(derived["structural_features"]["mechanical_relation"])
        self.assertNotIn("moc_admission", derived)

    def test_temperature_band_is_continuous_guidance(self) -> None:
        self.assertEqual(temperature_band(92), "strong")
        self.assertEqual(temperature_band(74), "supporting")
        self.assertEqual(temperature_band(45), "weak")
        self.assertEqual(temperature_band(8), "noise")

    def test_reviewed_clue_board_blocks_mechanical_relation_without_explicit_admission(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        reviews = {
            "relation:wiki/adr/001-runtime.md:derived_from:runtime-method": {
                "temperature": 86,
                "temperature_reason": "Useful provenance but not a navigation object.",
                "evidence": ["ADR points back to the method page."],
                "chain": "method -> ADR",
                "question": "Keep as evidence only.",
                "moc_admission": "block",
            }
        }

        board = build_temperature_clue_board(packages, reviews)
        plan = build_moc_admission_plan(board)

        self.assertEqual(board["summary"]["blocked_count"], 1)
        self.assertNotIn("derived_from", plan["admitted_relations"])

    def test_admits_high_temperature_relation_when_review_says_admit_relation(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        reviews = {
            "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                "temperature": 88,
                "temperature_reason": "Spec validates an active runtime method.",
                "evidence": ["Spec carries the runtime behavior contract."],
                "chain": "method -> spec -> runtime route",
                "question": "Use this as preferred runtime context?",
                "moc_admission": "admit_relation",
            }
        }

        board = build_temperature_clue_board(packages, reviews)
        plan = build_moc_admission_plan(board)

        self.assertIn("validates", plan["admitted_relations"])
        self.assertIn("runtime-spec", plan["admitted_objects"])
        self.assertEqual(plan["summary"]["admitted_count"], 1)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_temperature
```

Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.wiki_moc_temperature'`.

- [ ] **Step 3: Implement `scripts/wiki_moc_temperature.py`**

Create `scripts/wiki_moc_temperature.py` with:

```python
from __future__ import annotations

from collections import Counter
from typing import Any


MECHANICAL_RELATION_TYPES = {"derived_from", "related_objects"}


def temperature_band(value: int | float) -> str:
    score = int(value)
    if score >= 80:
        return "strong"
    if score >= 60:
        return "supporting"
    if score >= 40:
        return "weak"
    return "noise"


def _path_node_map(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        str(node.get("page_path")): node
        for node in nodes
        if isinstance(node.get("page_path"), str)
    }


def _object_nodes(nodes: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for node in nodes:
        canonical_object = str(node.get("canonical_object") or "").strip()
        if canonical_object:
            grouped.setdefault(canonical_object, []).append(node)
    return grouped


def _target_layer(target: str, object_map: dict[str, list[dict[str, Any]]]) -> str:
    nodes = object_map.get(target, [])
    layers = sorted({str(node.get("source_layer") or "unknown") for node in nodes})
    return layers[0] if layers else "unknown"


def _candidate_id(edge: dict[str, Any]) -> str:
    source = str(edge.get("source_page_path") or "")
    relation_type = str(edge.get("relation_type") or "")
    target = str(edge.get("target") or "")
    return f"relation:{source}:{relation_type}:{target}"


def build_relation_feature_packages(graph: dict[str, Any]) -> list[dict[str, Any]]:
    nodes = [node for node in graph.get("nodes", []) if isinstance(node, dict)]
    edges = [edge for edge in graph.get("edges", []) if isinstance(edge, dict)]
    path_nodes = _path_node_map(nodes)
    object_map = _object_nodes(nodes)
    relation_fanout = Counter(str(edge.get("relation_type") or "") for edge in edges)
    packages: list[dict[str, Any]] = []

    for edge in sorted(
        edges,
        key=lambda item: (
            str(item.get("source_page_path") or ""),
            str(item.get("relation_type") or ""),
            str(item.get("target") or ""),
        ),
    ):
        relation_type = str(edge.get("relation_type") or "").strip()
        target = str(edge.get("target") or "").strip()
        source_page = str(edge.get("source_page_path") or "").strip()
        if not relation_type or not source_page or not target:
            continue
        source_node = path_nodes.get(source_page, {})
        source_object = str(source_node.get("canonical_object") or "").strip()
        source_layer = str(source_node.get("source_layer") or "unknown")
        target_layer = _target_layer(target, object_map)
        packages.append(
            {
                "candidate_id": _candidate_id(edge),
                "source_page": source_page,
                "source_object": source_object,
                "relation_type": relation_type,
                "target_object": target,
                "source_layer": source_layer,
                "target_layer": target_layer,
                "evidence_refs": [source_page],
                "structural_features": {
                    "cross_layer": source_layer != target_layer,
                    "has_spec_support": source_layer == "openspec/specs" or target_layer == "openspec/specs",
                    "has_adr_support": source_layer == "wiki/adr" or target_layer == "wiki/adr",
                    "fanout_count": relation_fanout[relation_type],
                    "mechanical_relation": relation_type in MECHANICAL_RELATION_TYPES,
                },
            }
        )
    return packages


def _empty_review(package: dict[str, Any]) -> dict[str, Any]:
    relation_type = str(package.get("relation_type") or "")
    mechanical = bool(package.get("structural_features", {}).get("mechanical_relation"))
    return {
        "temperature": 20 if mechanical else 50,
        "temperature_reason": "No explicit temperature review was supplied.",
        "evidence": list(package.get("evidence_refs", [])),
        "chain": "",
        "question": "Review this relation before MOC admission.",
        "moc_admission": "block" if mechanical else "needs_review",
        "blocked_reason": "mechanical_relation" if mechanical else "missing_review",
        "relation_type": relation_type,
    }


def build_temperature_clue_board(
    packages: list[dict[str, Any]],
    reviews: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    review_map = reviews or {}
    windows: list[dict[str, Any]] = []
    for index, package in enumerate(packages, start=1):
        candidate_id = str(package.get("candidate_id") or "")
        review = dict(review_map.get(candidate_id) or _empty_review(package))
        temperature = int(review.get("temperature", 0) or 0)
        admission = str(review.get("moc_admission") or "needs_review")
        window = {
            "window_id": f"clue-{index:03d}",
            "candidate_id": candidate_id,
            "temperature": temperature,
            "temperature_band": temperature_band(temperature),
            "temperature_reason": str(review.get("temperature_reason") or ""),
            "source": str(package.get("source_page") or ""),
            "object": str(package.get("source_object") or ""),
            "relation": {
                "type": str(package.get("relation_type") or ""),
                "target": str(package.get("target_object") or ""),
            },
            "evidence": list(review.get("evidence") or package.get("evidence_refs") or []),
            "chain": str(review.get("chain") or ""),
            "question": str(review.get("question") or ""),
            "moc_admission": admission,
        }
        if review.get("blocked_reason"):
            window["blocked_reason"] = str(review["blocked_reason"])
        windows.append(window)

    return {
        "summary": {
            "window_count": len(windows),
            "admitted_count": sum(1 for item in windows if str(item.get("moc_admission")) in {"admit", "admit_relation"}),
            "blocked_count": sum(1 for item in windows if str(item.get("moc_admission")) == "block"),
            "review_needed_count": sum(1 for item in windows if str(item.get("moc_admission")) == "needs_review"),
        },
        "windows": windows,
    }


def build_moc_admission_plan(board: dict[str, Any]) -> dict[str, Any]:
    windows = [item for item in board.get("windows", []) if isinstance(item, dict)]
    admitted_objects: set[str] = set()
    admitted_relations: set[str] = set()
    blocked_relations: set[str] = set()

    for window in windows:
        admission = str(window.get("moc_admission") or "")
        relation = window.get("relation", {})
        relation_type = str(relation.get("type") if isinstance(relation, dict) else "")
        object_name = str(window.get("object") or "")
        if admission in {"admit", "admit_relation"} and int(window.get("temperature", 0) or 0) >= 80:
            if object_name:
                admitted_objects.add(object_name)
            if admission == "admit_relation" and relation_type:
                admitted_relations.add(relation_type)
        elif admission == "block" and relation_type:
            blocked_relations.add(relation_type)

    return {
        "summary": dict(board.get("summary", {})),
        "admitted_objects": sorted(admitted_objects),
        "admitted_relations": sorted(admitted_relations),
        "blocked_relations": sorted(blocked_relations - admitted_relations),
        "windows": windows,
    }
```

- [ ] **Step 4: Run temperature tests**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_temperature
```

Expected: `Ran 4 tests` and `OK`.

- [ ] **Step 5: Commit the temperature module**

Run:

```bash
git add scripts/wiki_moc_temperature.py tests/test_wiki_moc_temperature.py
git commit -m "feat: add MOC temperature clue board"
```

Expected: commit succeeds with only these two files staged.

## Task 3: Gate Relation MOC Candidates By Admission Plan

**Files:**
- Modify: `scripts/wiki_moc_projection.py`
- Modify: `tests/test_wiki_moc_projection.py`

- [ ] **Step 1: Update projection tests first**

Modify `tests/test_wiki_moc_projection.py`.

Replace `test_builds_domain_object_and_relation_candidates` with:

```python
    def test_builds_domain_and_object_candidates_without_raw_relation_moc(self) -> None:
        candidates = build_moc_candidates(self.sample_graph())
        paths = {candidate.path for candidate in candidates}

        self.assertIn("wiki/moc/domain-wiki.md", paths)
        self.assertIn("wiki/moc/object-wiki-frontmatter-model.md", paths)
        self.assertNotIn("wiki/moc/relation-formalizes.md", paths)
```

Add this test after it:

```python
    def test_admission_plan_can_create_reviewed_relation_candidate(self) -> None:
        admission_plan = {
            "admitted_relations": ["formalizes"],
            "summary": {"admitted_count": 1, "blocked_count": 0, "review_needed_count": 0},
        }

        candidates = build_moc_candidates(self.sample_graph(), admission_plan=admission_plan)
        relation = next(candidate for candidate in candidates if candidate.path == "wiki/moc/relation-formalizes.md")

        self.assertEqual(relation.kind, "relation")
        self.assertEqual(relation.key, "formalizes")
        self.assertEqual(relation.lines, ("- [[0014-agent-readable-wiki-frontmatter-before-graph-automation|wiki-frontmatter-model]] -> [[object-wiki-frontmatter-model|wiki-frontmatter-model]]",))
```

Update `test_dry_run_plan_does_not_write_files`:

```python
    def test_dry_run_plan_does_not_write_files(self) -> None:
        plan = build_moc_plan(self.tmpdir, self.sample_graph())

        self.assertEqual(plan["summary"]["create_count"], 2)
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
        self.assertEqual(plan["temperature_admission"]["admitted_relations"], [])
```

Update `test_apply_writes_generated_moc_files`:

```python
    def test_apply_writes_generated_moc_files(self) -> None:
        plan = apply_moc_plan(self.tmpdir, self.sample_graph())
        domain_path = self.tmpdir / "wiki" / "moc" / "domain-wiki.md"

        self.assertEqual(plan["summary"]["create_count"], 2)
        self.assertTrue(domain_path.exists())
        text = domain_path.read_text(encoding="utf-8")
        self.assertIn("<!-- BEGIN GENERATED MOC: domain=wiki -->", text)
        self.assertIn("[[agent-readable-wiki-frontmatter]]", text)
```

- [ ] **Step 2: Run projection tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_projection
```

Expected: FAIL because `build_moc_candidates` does not accept `admission_plan` and raw relation MOC still appears.

- [ ] **Step 3: Update `scripts/wiki_moc_projection.py` imports and helpers**

Add this import near existing imports:

```python
from scripts.wiki_moc_temperature import build_moc_admission_plan, build_relation_feature_packages, build_temperature_clue_board
```

Add this helper above `build_moc_candidates`:

```python
def _normalized_admission_plan(
    graph: dict[str, Any],
    admission_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if admission_plan is not None:
        return {
            "summary": dict(admission_plan.get("summary", {})),
            "admitted_objects": list(admission_plan.get("admitted_objects", [])),
            "admitted_relations": list(admission_plan.get("admitted_relations", [])),
            "blocked_relations": list(admission_plan.get("blocked_relations", [])),
            "windows": list(admission_plan.get("windows", [])),
        }
    packages = build_relation_feature_packages(graph)
    board = build_temperature_clue_board(packages)
    return build_moc_admission_plan(board)
```

- [ ] **Step 4: Change candidate construction signature and relation loop**

Change:

```python
def build_moc_candidates(graph: dict[str, Any], moc_dir: Path | str = DEFAULT_MOC_DIR) -> list[MocCandidate]:
```

to:

```python
def build_moc_candidates(
    graph: dict[str, Any],
    moc_dir: Path | str = DEFAULT_MOC_DIR,
    admission_plan: dict[str, Any] | None = None,
) -> list[MocCandidate]:
```

Add after `object_keys = _object_keys(nodes)`:

```python
    normalized_admission = _normalized_admission_plan(graph, admission_plan)
    admitted_relations = {
        str(item)
        for item in normalized_admission.get("admitted_relations", [])
        if str(item).strip()
    }
```

Change the relation loop:

```python
    for relation_type, grouped_edges in sorted(relation_edges.items()):
```

to:

```python
    for relation_type, grouped_edges in sorted(relation_edges.items()):
        if relation_type not in admitted_relations:
            continue
```

- [ ] **Step 5: Pass admission plan through plan/apply/health**

Change `build_moc_plan` signature to:

```python
def build_moc_plan(
    root: Path | str,
    graph: dict[str, Any],
    moc_dir: Path | str = DEFAULT_MOC_DIR,
    admission_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
```

Inside it, replace:

```python
    candidates = build_moc_candidates(graph, moc_dir)
```

with:

```python
    normalized_admission = _normalized_admission_plan(graph, admission_plan)
    candidates = build_moc_candidates(graph, moc_dir, normalized_admission)
```

Add `"temperature_admission": normalized_admission,` to the returned dict before `proof_boundary_notes`.

Change `apply_moc_plan` signature to:

```python
def apply_moc_plan(
    root: Path | str,
    graph: dict[str, Any],
    moc_dir: Path | str = DEFAULT_MOC_DIR,
    admission_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
```

Replace:

```python
    plan = build_moc_plan(root_path, graph, moc_dir)
```

with:

```python
    plan = build_moc_plan(root_path, graph, moc_dir, admission_plan)
```

Replace the `next(candidate for candidate in build_moc_candidates(graph, moc_dir) ... )` call with:

```python
        candidate = next(
            candidate
            for candidate in build_moc_candidates(graph, moc_dir, plan.get("temperature_admission", {}))
            if candidate.path == entry["path"]
        )
```

Change `build_moc_health` signature to include `admission_plan`, and pass it into `build_moc_plan`.

- [ ] **Step 6: Run projection tests**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_projection tests.test_wiki_moc_temperature
```

Expected: all tests pass.

- [ ] **Step 7: Commit relation admission gating**

Run:

```bash
git add scripts/wiki_moc_projection.py tests/test_wiki_moc_projection.py
git commit -m "feat: gate relation MOC by temperature admission"
```

Expected: commit succeeds with only these files staged.

## Task 4: Add Review JSON Support To MOC CLI

**Files:**
- Modify: `scripts/build_wiki_moc_projection.py`
- Modify: `tests/test_wiki_moc_projection.py`

- [ ] **Step 1: Add CLI coverage**

Add imports to `tests/test_wiki_moc_projection.py`:

```python
import json
import subprocess
import sys
```

Add this test:

```python
    def test_cli_review_json_admits_relation_candidate(self) -> None:
        graph_path = self.tmpdir / "graph.json"
        graph_path.write_text(json.dumps(self.sample_graph()), encoding="utf-8")
        review_path = self.tmpdir / "review.json"
        review_path.write_text(
            json.dumps(
                {
                    "relation:wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md:formalizes:wiki-frontmatter-model": {
                        "temperature": 91,
                        "temperature_reason": "ADR formalizes the runtime model.",
                        "evidence": ["ADR points to the model."],
                        "chain": "method -> ADR",
                        "question": "Use this relation for navigation?",
                        "moc_admission": "admit_relation",
                    }
                }
            ),
            encoding="utf-8",
        )
        repo_root = Path(__file__).resolve().parents[1]

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_moc_projection.py",
                "--root",
                str(self.tmpdir),
                "--graph",
                str(graph_path),
                "--temperature-review",
                str(review_path),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        paths = {entry["path"] for entry in payload["entries"]}

        self.assertIn("wiki/moc/relation-formalizes.md", paths)
        self.assertEqual(payload["temperature_admission"]["admitted_relations"], ["formalizes"])
        self.assertEqual(payload["mode"], "dry-run")
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
```

- [ ] **Step 2: Run the CLI test to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_projection.WikiMocProjectionTest.test_cli_review_json_admits_relation_candidate
```

Expected: FAIL because `--temperature-review` is not recognized.

- [ ] **Step 3: Update CLI imports**

In `scripts/build_wiki_moc_projection.py`, add:

```python
from scripts.wiki_moc_temperature import build_moc_admission_plan, build_relation_feature_packages, build_temperature_clue_board
```

- [ ] **Step 4: Add review loading helper**

Add above `main()`:

```python
def load_temperature_admission(graph: dict, review_path: str | None) -> dict | None:
    if not review_path:
        return None
    reviews = json.loads(Path(review_path).read_text(encoding="utf-8"))
    packages = build_relation_feature_packages(graph)
    board = build_temperature_clue_board(packages, reviews)
    return build_moc_admission_plan(board)
```

- [ ] **Step 5: Add CLI argument and pass admission plan**

Add parser argument:

```python
    parser.add_argument("--temperature-review", help="optional relation temperature review JSON path")
```

After `graph = load_graph(root, args.graph)`, add:

```python
    admission_plan = load_temperature_admission(graph, args.temperature_review)
```

Replace the plan expression with:

```python
    plan = (
        apply_moc_plan(root, graph, args.moc_dir, admission_plan=admission_plan)
        if args.apply
        else build_moc_plan(root, graph, args.moc_dir, admission_plan=admission_plan)
    )
```

- [ ] **Step 6: Run CLI and projection tests**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_projection tests.test_wiki_moc_temperature
```

Expected: all tests pass.

- [ ] **Step 7: Commit CLI review support**

Run:

```bash
git add scripts/build_wiki_moc_projection.py tests/test_wiki_moc_projection.py
git commit -m "feat: preview MOC temperature review input"
```

Expected: commit succeeds with only these files staged.

## Task 5: Surface Temperature Admission In Medical-Agent MOC Preview

**Files:**
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Add medical-agent test expectation**

In `tests/test_wiki_medical_agent.py`, inside `test_builds_moc_surgery_preview_payload_from_active_case_and_moc_plan`, add this assertion after `self.assertEqual(payload["moc_projection"]["candidate_count"], 2)`:

```python
        self.assertEqual(payload["temperature_admission"]["admitted_relations"], [])
```

Inside `test_cli_moc_surgery_preview_is_read_only`, add:

```python
        self.assertIn("temperature_admission", payload)
        self.assertIn("summary", payload["temperature_admission"])
```

- [ ] **Step 2: Run medical-agent tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent
```

Expected: FAIL because `temperature_admission` is not included in the preview payload.

- [ ] **Step 3: Update medical-agent payload**

In `scripts/wiki_medical_agent.py`, inside `build_moc_surgery_preview_payload`, after:

```python
    moc_summary = dict(moc_plan.get("summary", {})) if isinstance(moc_plan, dict) else {}
```

add:

```python
    temperature_admission = (
        dict(moc_plan.get("temperature_admission", {}))
        if isinstance(moc_plan, dict)
        else {}
    )
```

In the returned dict, add:

```python
        "temperature_admission": temperature_admission,
```

immediately after `"moc_projection": moc_summary,`.

- [ ] **Step 4: Run medical-agent and MOC tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_moc_projection tests.test_wiki_moc_temperature
```

Expected: all tests pass and no `wiki/moc` files are created during medical-agent preview tests.

- [ ] **Step 5: Commit medical-agent preview surface**

Run:

```bash
git add scripts/wiki_medical_agent.py tests/test_wiki_medical_agent.py
git commit -m "feat: surface MOC temperature admission in medical preview"
```

Expected: commit succeeds with only these files staged.

## Task 6: Verification, Evaluation Evidence, And OpenSpec Task Closure

**Files:**
- Create: `openspec/changes/add-moc-temperature-reading-board/evaluation.md`
- Modify: `openspec/changes/add-moc-temperature-reading-board/tasks.md`

- [ ] **Step 1: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_medical_agent
```

Expected: all tests pass.

- [ ] **Step 2: Run status regression tests**

Run:

```bash
python3 -m unittest tests.test_wiki_status tests.test_wiki_surgery
```

Expected: all tests pass.

- [ ] **Step 3: Run OpenSpec validation**

Run:

```bash
openspec validate add-moc-temperature-reading-board --strict
```

Expected: validation passes.

- [ ] **Step 4: Run current MOC dry-run**

Run:

```bash
python3 scripts/build_wiki_moc_projection.py
```

Expected:

- JSON prints to stdout.
- `mode` is `dry-run`.
- `temperature_admission` is present.
- Relation MOC entries are absent unless admitted by review.
- No files are written.

- [ ] **Step 5: Write evaluation evidence**

Create `openspec/changes/add-moc-temperature-reading-board/evaluation.md` with:

```markdown
# Evaluation: MOC temperature reading board

## Evidence

| Check | Result | Notes |
| --- | --- | --- |
| `python3 -m unittest tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_medical_agent` | PASS | Focused temperature, projection, and medical-agent tests pass. |
| `python3 -m unittest tests.test_wiki_status tests.test_wiki_surgery` | PASS | Existing status and surgery surfaces remain compatible. |
| `openspec validate add-moc-temperature-reading-board --strict` | PASS | OpenSpec change validates. |
| `python3 scripts/build_wiki_moc_projection.py` | PASS | Dry-run includes temperature admission and writes no files. |

## Behavior Replay

| Scenario | Expected behavior | Result |
| --- | --- | --- |
| Raw `derived_from` relation exists | No standalone `relation-derived_from.md` MOC candidate appears by default. | PASS |
| Review admits `validates` relation | `relation-validates.md` can appear as an admitted relation MOC candidate. | PASS |
| Medical-agent MOC preview runs | Payload includes temperature admission summary and writes no files. | PASS |
| Direct dry-run without review | Output reports review-needed or blocked relation state instead of treating Python scoring as semantic truth. | PASS |

## Proof Boundary

This change proves local script behavior, admission gating, and read-only
medical-agent preview. It does not prove Obsidian UI layout quality, external
AI review quality, or a human-facing interactive relation board.

## Residual Risks

- Existing generated `wiki/moc` files may still contain noisy relation pages
  until a separate cleanup change handles them.
- Temperature review input is explicit JSON in this implementation; live model
  integration remains outside this change.
```

- [ ] **Step 6: Mark OpenSpec tasks complete**

Update `openspec/changes/add-moc-temperature-reading-board/tasks.md` to:

```markdown
# Tasks

- [x] 1. Add OpenSpec requirements for temperature-reviewed MOC admission.
- [x] 2. Add relation feature package and clue-window admission module.
- [x] 3. Gate relation MOC candidates behind an admission plan.
- [x] 4. Add optional review JSON support to the MOC projection CLI.
- [x] 5. Surface temperature admission in medical-agent MOC preview.
- [x] 6. Add unit tests and behavior replay coverage.
- [x] 7. Run validation and record evaluation evidence.
```

- [ ] **Step 7: Commit evaluation and task closure**

Run:

```bash
git add openspec/changes/add-moc-temperature-reading-board/evaluation.md openspec/changes/add-moc-temperature-reading-board/tasks.md
git commit -m "test: verify MOC temperature reading board"
```

Expected: commit succeeds with only evaluation and task updates staged.

## Self-Review

Spec coverage:

- Feature package before semantic judgment: Task 2.
- Temperature clue windows: Task 2.
- Relation MOC admission gate: Task 3.
- CLI dry-run admission surface: Task 4.
- Medical-agent read-only preview surface: Task 5.
- OpenSpec lifecycle and evidence: Tasks 1 and 6.

Plan checks:

- No empty markers or unfinished sections are present.
- Function names used later are defined before use.
- The plan keeps implementation out of the current brainstorming/spec-review step.
- The plan creates an OpenSpec change before code changes, matching repo lifecycle rules.
