# wiki-medical-agent MOC Prediagnosis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a bounded read-only MOC temperature prediagnosis section to `wiki-medical-agent` MOC surgery preview responses.

**Architecture:** Create a new OpenSpec change first, then keep implementation inside the existing medical-agent route. `moc_surgery_preview` remains the user-facing intent; `prediagnosis.kind: moc_temperature` is only a non-authoritative interpretation section derived from existing MOC plan evidence.

**Tech Stack:** Python standard library, `unittest`, existing OpenSpec workflow, existing wiki MOC/medical-agent scripts.

---

## File Structure

- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/proposal.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/design.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/tasks.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/specs/wiki-medical-agent/spec.md`
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/evaluation.md`

This plan does not edit `.codex/skills/wiki-medical-agent/SKILL.md`; the skill already defines the response authority and read-only prediagnosis rule. The implementation makes the script payload support that existing contract.

## Task 1: Create The OpenSpec Change

**Files:**
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/proposal.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/design.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/tasks.md`
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/specs/wiki-medical-agent/spec.md`

- [ ] **Step 1: Create the change directories**

Run:

```bash
mkdir -p openspec/changes/add-medical-agent-moc-prediagnosis/specs/wiki-medical-agent
```

Expected: command exits `0`.

- [ ] **Step 2: Write `proposal.md`**

Create `openspec/changes/add-medical-agent-moc-prediagnosis/proposal.md` with:

```markdown
# Proposal: add medical-agent MOC prediagnosis

## Why

`wiki-medical-agent` can already route explicit MOC review requests to the
read-only `moc_surgery_preview` path, and the lower-level MOC temperature gate
already blocks raw relation MOC generation by default.

The current user-facing payload still exposes raw worker internals such as
`temperature_admission` and large `clue_windows` arrays. That makes the user
experience feel like Python/JSON tooling instead of medical-agent diagnosis.

## What Changes

- Keep `moc_surgery_preview` as the user-facing medical-agent intent.
- Add `prediagnosis.kind: moc_temperature` to allowed MOC surgery preview
  payloads.
- Summarize MOC projection and temperature admission evidence without dumping
  raw clue windows.
- Mark `derived_from` and `related_objects` as blocked mechanical relation
  families by default.
- Surface review-needed clue candidates with candidate temperature, rationale,
  evidence refs, and confirmation questions.
- Surface orphan relation MOC pages only as surgery candidates.

## Out of Scope

- No new normal user entry point.
- No independent MOC review skill.
- No automatic MOC admission.
- No admitted review JSON generation.
- No writes to `wiki/moc`, relation frontmatter, ADRs, AGENTS, skills,
  taxonomy config, or OpenSpec lifecycle state from the preview.
```

- [ ] **Step 3: Write `design.md`**

Create `openspec/changes/add-medical-agent-moc-prediagnosis/design.md` with:

```markdown
# Design: medical-agent MOC prediagnosis

## Route

The route remains:

```text
user natural language
-> wiki-medical-agent
-> intent: moc_surgery_preview
-> active case validation
-> bounded MOC dry-run worker
-> prediagnosis.kind: moc_temperature
-> confirmation point
```

`prediagnosis.kind` is not a new lifecycle authority. It is a read-only section
derived from existing worker evidence.

## Payload

Allowed `moc_surgery_preview` responses add:

```json
{
  "prediagnosis": {
    "kind": "moc_temperature",
    "script_result_summary": {},
    "interpreted_live_intent": "",
    "mechanical_relation_families": [],
    "review_needed_clues": [],
    "orphan_relation_moc_pages": [],
    "confirmation_points": [],
    "write_boundary": "read_only_no_files_written"
  }
}
```

The existing `temperature_admission` field may remain for compatibility, but
large `clue_windows` must not be copied into `prediagnosis`.

## Interpretation Rules

- `derived_from` and `related_objects` are mechanical relation families and
  stay blocked by default.
- Review-needed clue candidates come from bounded samples of
  `temperature_admission.clue_windows`.
- Candidate temperature is copied from explicit review data when present. When
  missing, use `null` plus `temperature_band: "unreviewed"`.
- Rationale is copied from review data when present. When missing, use a short
  structural rationale that does not claim admission.
- Orphan relation MOC pages come from surgery preview sample items with
  `action: orphan` and `kind: relation`.

## Boundaries

The implementation must not write files, update case files, generate review
JSON, admit clues, or run cleanup surgery.
```

- [ ] **Step 4: Write `tasks.md`**

Create `openspec/changes/add-medical-agent-moc-prediagnosis/tasks.md` with:

```markdown
# Tasks

- [ ] 1. Create OpenSpec proposal, design, tasks, and spec delta.
- [ ] 2. Add RED tests for MOC prediagnosis routing and payload shape.
- [ ] 3. Implement bounded MOC prediagnosis helpers in `scripts/wiki_medical_agent.py`.
- [ ] 4. Attach prediagnosis to allowed `moc_surgery_preview` responses.
- [ ] 5. Add CLI read-only regression coverage.
- [ ] 6. Run unit tests and OpenSpec validation.
- [ ] 7. Record evaluation evidence and commit verified work.
```

- [ ] **Step 5: Write the spec delta**

Create `openspec/changes/add-medical-agent-moc-prediagnosis/specs/wiki-medical-agent/spec.md` with:

```markdown
# wiki-medical-agent Specification Delta

## ADDED Requirements

### Requirement: MOC surgery preview SHALL include read-only temperature prediagnosis

When `moc_surgery_preview` is allowed, the medical agent SHALL include a bounded
read-only prediagnosis section that interprets MOC temperature evidence without
expanding write authority.

#### Scenario: User asks for MOC temperature clues

- **GIVEN** exactly one active medical case exists
- **WHEN** the user asks the medical agent to inspect MOC temperature clues
- **THEN** the medical agent SHALL return intent `moc_surgery_preview`
- **AND** it SHALL include `prediagnosis.kind: moc_temperature`
- **AND** it SHALL include script result summary, interpreted live intent,
  blocked mechanical relation families, review-needed clues, orphan relation
  MOC pages, confirmation points, and write boundary
- **AND** it SHALL NOT write `wiki/moc`.

#### Scenario: Mechanical relation families are blocked by default

- **GIVEN** temperature admission contains `derived_from` and `related_objects`
  as blocked relations
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL mark those relation families as mechanical
  and blocked by default
- **AND** it SHALL NOT mark them as admitted.

#### Scenario: Review-needed clue windows are summarized

- **GIVEN** temperature admission contains many `clue_windows`
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL include bounded clue candidates
- **AND** it SHALL NOT dump the full `clue_windows` array into the
  prediagnosis section.

#### Scenario: Orphan relation MOC pages are surgery candidates only

- **GIVEN** surgery preview contains orphan relation MOC sample items
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL surface those pages as surgery candidates
- **AND** it SHALL NOT clean them up.
```

- [ ] **Step 6: Validate the OpenSpec change**

Run:

```bash
openspec validate add-medical-agent-moc-prediagnosis --strict
```

Expected: validation exits `0`. A telemetry warning is acceptable only if validation itself reports the change as valid.

- [ ] **Step 7: Commit OpenSpec scaffolding**

Run:

```bash
git add openspec/changes/add-medical-agent-moc-prediagnosis
git commit -m "spec: add medical-agent MOC prediagnosis"
```

Expected: commit includes only the new OpenSpec change files.

## Task 2: Add RED Tests For Prediagnosis

**Files:**
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Add imports only if needed**

Open `tests/test_wiki_medical_agent.py`. It already imports `json`, `subprocess`, `sys`, `tempfile`, `Path`, `build_moc_surgery_preview_payload`, `build_status_payload`, and `classify_medical_intent`; no new imports are required.

- [ ] **Step 2: Add classifier coverage for MOC temperature language**

Add this test after `test_classifies_moc_preview_as_surgery_preview_before_treatment_preview`:

```python
    def test_classifies_moc_temperature_clues_as_surgery_preview(self) -> None:
        self.assertEqual(
            classify_medical_intent("MOC 温度线索 先不要写").intent,
            "moc_surgery_preview",
        )
        self.assertEqual(
            classify_medical_intent("MOC 哪些关系值得进图").intent,
            "moc_surgery_preview",
        )
        self.assertEqual(
            classify_medical_intent("看一下 derived_from / related_objects 是不是噪音").intent,
            "moc_surgery_preview",
        )
```

- [ ] **Step 3: Add payload-shape RED test**

Add this test after `test_builds_moc_surgery_preview_payload_from_active_case_and_moc_plan`:

```python
    def test_moc_surgery_preview_adds_bounded_temperature_prediagnosis(self) -> None:
        case_path = self._write_case(
            self._case_package(status="archive_ready"),
            "2026-05-15T01:02:03+00:00",
        )
        moc_plan = {
            "summary": {
                "candidate_count": 4,
                "create_count": 0,
                "update_count": 0,
                "noop_count": 2,
                "orphan_count": 2,
            },
            "temperature_admission": {
                "counts": {
                    "admitted": 0,
                    "blocked": 2,
                    "needs_review": 2,
                    "total": 4,
                },
                "admitted_relations": [],
                "blocked_relations": ["derived_from", "related_objects"],
                "review_needed_relations": ["formalizes", "validates"],
                "clue_windows": [
                    {
                        "candidate_id": "relation:wiki/ops/a.md:formalizes:case-file",
                        "relation_type": "formalizes",
                        "source_page": "wiki/ops/a.md",
                        "source_object": "medical-agent-design",
                        "target_object": "case-file",
                        "evidence_refs": ["wiki/ops/a.md", "openspec/specs/wiki-medical-agent/spec.md"],
                        "temperature": 72,
                        "temperature_band": "supporting",
                        "status": "needs_review",
                        "rationale": "Links a design decision to a stable contract.",
                    },
                    {
                        "candidate_id": "relation:wiki/ops/b.md:validates:medical-agent",
                        "relation_type": "validates",
                        "source_page": "wiki/ops/b.md",
                        "source_object": "moc-temperature-review",
                        "target_object": "medical-agent",
                        "evidence_refs": ["wiki/ops/b.md"],
                        "temperature": None,
                        "temperature_band": None,
                        "status": "needs_review",
                        "rationale": "",
                    },
                    {
                        "candidate_id": "relation:wiki/ops/c.md:derived_from:source",
                        "relation_type": "derived_from",
                        "source_page": "wiki/ops/c.md",
                        "source_object": "source-note",
                        "target_object": "source",
                        "evidence_refs": ["wiki/ops/c.md"],
                        "temperature": None,
                        "temperature_band": None,
                        "status": "blocked",
                        "rationale": "",
                    },
                ],
            },
        }
        payload = build_moc_surgery_preview_payload(self.tmpdir, case_path, moc_plan)

        prediagnosis = payload["prediagnosis"]
        self.assertEqual(prediagnosis["kind"], "moc_temperature")
        self.assertEqual(prediagnosis["write_boundary"], "read_only_no_files_written")
        self.assertEqual(
            prediagnosis["script_result_summary"]["moc_projection"]["candidate_count"],
            4,
        )
        self.assertEqual(
            prediagnosis["script_result_summary"]["temperature_admission"]["blocked"],
            2,
        )
        self.assertEqual(
            [item["relation_type"] for item in prediagnosis["mechanical_relation_families"]],
            ["derived_from", "related_objects"],
        )
        self.assertEqual(
            [item["relation_type"] for item in prediagnosis["review_needed_clues"]],
            ["formalizes", "validates"],
        )
        self.assertEqual(prediagnosis["review_needed_clues"][0]["temperature"], 72)
        self.assertEqual(prediagnosis["review_needed_clues"][0]["temperature_band"], "supporting")
        self.assertIn("confirm", prediagnosis["review_needed_clues"][0]["confirmation_question"])
        self.assertNotIn("clue_windows", prediagnosis)
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
```

- [ ] **Step 4: Add orphan relation prediagnosis RED test**

Add this test after the payload-shape test:

```python
    def test_moc_prediagnosis_surfaces_orphan_relation_pages_as_surgery_candidates(self) -> None:
        case_path = self._write_case(
            self._case_package(status="archive_ready"),
            "2026-05-15T01:02:03+00:00",
        )
        moc_plan = {
            "summary": {
                "candidate_count": 2,
                "create_count": 0,
                "update_count": 0,
                "noop_count": 0,
                "orphan_count": 2,
            },
            "moc_projection_items": [
                {
                    "action": "orphan",
                    "kind": "relation",
                    "key": "derived_from",
                    "path": "wiki/moc/relation-derived_from.md",
                    "link_count": 0,
                },
                {
                    "action": "orphan",
                    "kind": "relation",
                    "key": "validates",
                    "path": "wiki/moc/relation-validates.md",
                    "link_count": 0,
                },
            ],
            "temperature_admission": {
                "counts": {"admitted": 0, "blocked": 1, "needs_review": 1, "total": 2},
                "blocked_relations": ["derived_from"],
                "review_needed_relations": ["validates"],
                "clue_windows": [],
            },
        }

        payload = build_moc_surgery_preview_payload(self.tmpdir, case_path, moc_plan)

        orphans = payload["prediagnosis"]["orphan_relation_moc_pages"]
        self.assertEqual(
            [(item["relation_type"], item["path"], item["surgery_candidate"]) for item in orphans],
            [
                ("derived_from", "wiki/moc/relation-derived_from.md", True),
                ("validates", "wiki/moc/relation-validates.md", True),
            ],
        )
        self.assertEqual(payload["next_action"], "review_moc_surgery_preview")
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
```

- [ ] **Step 5: Run the targeted tests to confirm RED**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent
```

Expected: fails because `prediagnosis` does not exist and classifier does not route all MOC clue phrases yet.

- [ ] **Step 6: Commit RED tests**

Run:

```bash
git add tests/test_wiki_medical_agent.py
git commit -m "test: cover medical-agent MOC prediagnosis"
```

Expected: commit contains only the failing test changes.

## Task 3: Implement Prediagnosis Helpers

**Files:**
- Modify: `scripts/wiki_medical_agent.py`

- [ ] **Step 1: Extend MOC review signals**

In `scripts/wiki_medical_agent.py`, replace `MOC_REVIEW_SIGNALS` with:

```python
MOC_REVIEW_SIGNALS = (
    "preview",
    "review",
    "temperature",
    "clue",
    "clues",
    "noise",
    "value",
    "worth",
    "预览",
    "surgery",
    "手术",
    "分流",
    "审核",
    "审查",
    "复核",
    "温度",
    "线索",
    "噪音",
    "价值",
    "值得",
    "进图",
    "不要写",
)
```

- [ ] **Step 2: Add relation-type route signals**

Add this constant below `MOC_REVIEW_SIGNALS`:

```python
MOC_RELATION_SIGNALS = ("derived_from", "related_objects", "formalizes", "validates")
```

Replace `_is_moc_surgery_preview_request` with:

```python
def _is_moc_surgery_preview_request(lowered: str) -> bool:
    has_moc = _has_moc_signal(lowered)
    has_review = any(signal in lowered for signal in MOC_REVIEW_SIGNALS)
    has_relation_signal = any(signal in lowered for signal in MOC_RELATION_SIGNALS)
    return (has_moc and has_review) or (has_relation_signal and has_review)
```

- [ ] **Step 3: Add normalization helpers**

Add these helpers above `_sample_moc_items`:

```python
MECHANICAL_RELATION_FAMILIES = {"derived_from", "related_objects"}


def _safe_int(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        return 0
    return value


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return sorted({item.strip() for item in value if isinstance(item, str) and item.strip()})


def _temperature_value(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    if value < 0 or value > 100:
        return None
    return value


def _temperature_band(value: Any) -> str:
    if isinstance(value, str) and value.strip():
        return value.strip()
    temperature = _temperature_value(value)
    if temperature is None:
        return "unreviewed"
    if temperature >= 80:
        return "strong"
    if temperature >= 60:
        return "supporting"
    if temperature >= 40:
        return "weak"
    return "noise"
```

- [ ] **Step 4: Add clue compaction helpers**

Add these helpers below the normalization helpers:

```python
def _clue_sort_key(window: dict[str, Any]) -> tuple[int, str, str]:
    status_rank = 0 if str(window.get("status", "")) == "needs_review" else 1
    temperature = _temperature_value(window.get("temperature"))
    return (
        status_rank,
        -(temperature if temperature is not None else -1),
        str(window.get("relation_type") or window.get("relation") or ""),
    )


def _compact_clue(window: dict[str, Any]) -> dict[str, Any]:
    relation_type = str(window.get("relation_type") or window.get("relation") or "").strip()
    source_page = str(window.get("source_page") or "").strip()
    source_object = str(window.get("source_object") or source_page).strip()
    target_object = str(window.get("target_object") or "").strip()
    evidence_refs = window.get("evidence_refs", [])
    if not isinstance(evidence_refs, list):
        evidence_refs = []
    clean_refs = [str(item) for item in evidence_refs if isinstance(item, str) and item.strip()]
    temperature = _temperature_value(window.get("temperature"))
    band = _temperature_band(window.get("temperature_band") or temperature)
    rationale = str(window.get("rationale") or "").strip()
    if not rationale:
        rationale = "Needs human review before it can become a MOC admission."
    return {
        "candidate_id": str(window.get("candidate_id") or ""),
        "relation_type": relation_type,
        "source_page": source_page,
        "source_object": source_object,
        "target_object": target_object,
        "evidence_refs": clean_refs[:3],
        "temperature": temperature,
        "temperature_band": band,
        "rationale": rationale,
        "confirmation_question": f"confirm whether {relation_type} should be admitted as a MOC clue",
    }
```

- [ ] **Step 5: Add prediagnosis builder**

Add this function below `_sample_moc_items`:

```python
def _build_moc_temperature_prediagnosis(
    moc_plan: dict[str, Any],
    surgery_sample_items: list[dict[str, Any]],
) -> dict[str, Any]:
    moc_summary = moc_plan.get("summary", {})
    if not isinstance(moc_summary, dict):
        moc_summary = {}
    admission = moc_plan.get("temperature_admission", {})
    if not isinstance(admission, dict):
        admission = {}
    counts = admission.get("counts", admission.get("summary", {}))
    if not isinstance(counts, dict):
        counts = {}
    blocked_relations = _string_list(admission.get("blocked_relations"))
    review_needed_relations = _string_list(admission.get("review_needed_relations"))
    admitted_relations = _string_list(admission.get("admitted_relations"))
    windows_value = admission.get("clue_windows", admission.get("windows", []))
    windows = [item for item in windows_value if isinstance(item, dict)] if isinstance(windows_value, list) else []
    review_windows = [
        window
        for window in windows
        if str(window.get("status", "")) == "needs_review"
        or str(window.get("relation_type") or window.get("relation") or "") in review_needed_relations
    ]
    compact_clues = [_compact_clue(window) for window in sorted(review_windows, key=_clue_sort_key)[:5]]
    mechanical_families = [
        {
            "relation_type": relation,
            "status": "blocked",
            "reason": "mechanical source/proximity relation; not a standalone MOC reading clue by default",
        }
        for relation in blocked_relations
        if relation in MECHANICAL_RELATION_FAMILIES
    ]
    orphan_relation_pages = [
        {
            "relation_type": str(item.get("key") or "").strip(),
            "path": str(item.get("path") or "").strip(),
            "surgery_candidate": True,
            "reason": "orphan generated relation MOC page; review as cleanup candidate, not active clue value",
        }
        for item in surgery_sample_items
        if item.get("action") == "orphan" and item.get("kind") == "relation"
    ]
    return {
        "kind": "moc_temperature",
        "script_result_summary": {
            "moc_projection": {
                "candidate_count": _safe_int(moc_summary.get("candidate_count")),
                "create_count": _safe_int(moc_summary.get("create_count")),
                "update_count": _safe_int(moc_summary.get("update_count")),
                "noop_count": _safe_int(moc_summary.get("noop_count")),
                "orphan_count": _safe_int(moc_summary.get("orphan_count")),
            },
            "temperature_admission": {
                "admitted": _safe_int(counts.get("admitted")),
                "blocked": _safe_int(counts.get("blocked")),
                "needs_review": _safe_int(counts.get("needs_review")),
                "total": _safe_int(counts.get("total")),
                "admitted_relations": admitted_relations,
                "blocked_relations": blocked_relations,
                "review_needed_relations": review_needed_relations,
            },
        },
        "interpreted_live_intent": (
            "The user is asking whether current MOC evidence contains real reading clues, "
            "not asking to apply MOC writes."
        ),
        "mechanical_relation_families": mechanical_families,
        "review_needed_clues": compact_clues,
        "orphan_relation_moc_pages": orphan_relation_pages,
        "confirmation_points": [
            "admit a specific clue candidate into review",
            "block a relation family",
            "route orphan relation MOC pages to cleanup surgery",
            "expand one object chain for deeper diagnosis",
            "keep everything read-only",
        ],
        "write_boundary": "read_only_no_files_written",
    }
```

- [ ] **Step 6: Run tests to see remaining failures**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent
```

Expected: classifier test passes; payload tests still fail until the prediagnosis builder is attached.

## Task 4: Attach Prediagnosis To MOC Preview

**Files:**
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Reuse surgery sample items once**

In `build_moc_surgery_preview_payload`, replace:

```python
    return {
        "moc_projection": moc_summary,
        "temperature_admission": temperature_admission,
        "surgery_preview": {
            "moc_projection_count": moc_projection_count,
            "sample_items": _sample_moc_items(surgery_plan),
        },
        "next_action": (
            "review_moc_surgery_preview"
            if moc_projection_count > 0
            else "moc_projection_clean"
        ),
    }
```

with:

```python
    sample_items = _sample_moc_items(surgery_plan)
    return {
        "moc_projection": moc_summary,
        "temperature_admission": temperature_admission,
        "surgery_preview": {
            "moc_projection_count": moc_projection_count,
            "sample_items": sample_items,
        },
        "prediagnosis": _build_moc_temperature_prediagnosis(moc_plan, sample_items),
        "next_action": (
            "review_moc_surgery_preview"
            if moc_projection_count > 0
            else "moc_projection_clean"
        ),
    }
```

- [ ] **Step 2: Update CLI read-only test assertions**

In `test_cli_moc_surgery_preview_is_read_only`, add these assertions after `self.assertIn("temperature_admission", payload)`:

```python
        self.assertEqual(payload["prediagnosis"]["kind"], "moc_temperature")
        self.assertEqual(payload["prediagnosis"]["write_boundary"], "read_only_no_files_written")
        self.assertNotIn("clue_windows", payload["prediagnosis"])
```

- [ ] **Step 3: Run targeted tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent
```

Expected: all tests in `tests.test_wiki_medical_agent` pass.

- [ ] **Step 4: Commit implementation**

Run:

```bash
git add scripts/wiki_medical_agent.py tests/test_wiki_medical_agent.py
git commit -m "feat: add medical-agent MOC prediagnosis"
```

Expected: commit contains only the medical-agent implementation and tests.

## Task 5: Full Verification And Evaluation

**Files:**
- Create: `openspec/changes/add-medical-agent-moc-prediagnosis/evaluation.md`
- Modify: `openspec/changes/add-medical-agent-moc-prediagnosis/tasks.md`

- [ ] **Step 1: Run related unit tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_surgery
```

Expected: all tests pass.

- [ ] **Step 2: Validate OpenSpec**

Run:

```bash
openspec validate add-medical-agent-moc-prediagnosis --strict
```

Expected: validation exits `0`. Record any non-blocking telemetry warning separately.

- [ ] **Step 3: Run live dry-run check**

Run:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "MOC 温度线索 先不要写"
```

Expected JSON facts:

```text
intent == "moc_surgery_preview"
allowed_action == "preview_moc_surgery_plan"
prediagnosis.kind == "moc_temperature"
prediagnosis.write_boundary == "read_only_no_files_written"
prediagnosis does not contain clue_windows
```

- [ ] **Step 4: Confirm no MOC writes happened**

Run:

```bash
git status --short wiki/moc wiki/ops/wiki-medical-cases wiki/ops/wiki-surgery-runs wiki/ops/wiki-treatment-runs
```

Expected: no new task-related writes from the dry-run command.

- [ ] **Step 5: Write evaluation evidence**

Create `openspec/changes/add-medical-agent-moc-prediagnosis/evaluation.md` with:

```markdown
# Evaluation: medical-agent MOC prediagnosis

## RED Baseline

- `tests.test_wiki_medical_agent` failed before implementation because
  `prediagnosis` did not exist on allowed `moc_surgery_preview` payloads.
- MOC temperature clue language did not all route to `moc_surgery_preview`.

## GREEN Result

- `python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_surgery`
  passed.
- `openspec validate add-medical-agent-moc-prediagnosis --strict` passed.
- `python3 scripts/build_wiki_medical_agent.py --intent-text "MOC 温度线索 先不要写"`
  returned `intent: moc_surgery_preview` and `prediagnosis.kind:
  moc_temperature`.

## Boundary Proof

- The prediagnosis section does not include raw `clue_windows`.
- The dry-run did not write `wiki/moc`.
- The dry-run did not write treatment or surgery records.
- Mechanical relations remain blocked by default and are not admitted.

## Residual Risk

- The prediagnosis is a bounded summary over existing worker evidence. It does
  not replace human confirmation or case-file authority.
```

- [ ] **Step 6: Mark OpenSpec tasks complete**

Update `openspec/changes/add-medical-agent-moc-prediagnosis/tasks.md` to:

```markdown
# Tasks

- [x] 1. Create OpenSpec proposal, design, tasks, and spec delta.
- [x] 2. Add RED tests for MOC prediagnosis routing and payload shape.
- [x] 3. Implement bounded MOC prediagnosis helpers in `scripts/wiki_medical_agent.py`.
- [x] 4. Attach prediagnosis to allowed `moc_surgery_preview` responses.
- [x] 5. Add CLI read-only regression coverage.
- [x] 6. Run unit tests and OpenSpec validation.
- [x] 7. Record evaluation evidence and commit verified work.
```

- [ ] **Step 7: Commit verification evidence**

Run:

```bash
git add openspec/changes/add-medical-agent-moc-prediagnosis
git commit -m "test: verify medical-agent MOC prediagnosis"
```

Expected: commit contains only OpenSpec task/evaluation updates.

## Self-Review

- Spec coverage: covered route, fixed medical-agent authority, read-only MOC prediagnosis, mechanical relation blocking, review-needed clue summaries, orphan relation surgery candidates, no write authority, and confirmation points.
- Placeholder scan: no placeholder markers or deferred-work wording are intentionally present.
- Type consistency: plan uses `prediagnosis.kind`, `script_result_summary`, `mechanical_relation_families`, `review_needed_clues`, `orphan_relation_moc_pages`, `confirmation_points`, and `write_boundary` consistently across tests and implementation.
- Scope check: this is one OpenSpec-backed implementation change, not a new user entry point or MOC review skill.
