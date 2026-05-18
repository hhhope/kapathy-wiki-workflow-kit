# Medical Agent MOC Surgery Preview Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a read-only `moc_surgery_preview` route to `$report-wiki-portfolio:wiki-medical-agent` so MOC dry-run output enters surgery preview instead of treatment preview.

**Architecture:** Keep MOC generation in the existing MOC projection layer and keep surgery judgment in the existing surgery layer. The medical agent only classifies the request, resolves the active case, builds a dry-run MOC plan, passes it to `build_surgery_plan_from_case`, and returns compact summary/sample payload fields.

**Tech Stack:** Python 3 standard library, existing OpenSpec artifacts, `unittest`, repo-local scripts under `scripts/`.

---

## File Structure

- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/proposal.md`
  - Defines why this route belongs in the medical agent and why it is preview-only.
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/design.md`
  - Mirrors the approved Superpowers design and names the code units.
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`
  - Authoritative OpenSpec implementation ledger.
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/specs/wiki-medical-agent/spec.md`
  - Adds the medical-agent behavior requirement.
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/evaluation.md`
  - Filled after implementation with RED/GREEN and validation evidence.
- Modify: `tests/test_wiki_medical_agent.py`
  - Add RED tests for MOC classification, no-case blocking, one-case preview payload, CLI boundary, and treatment regression.
- Modify: `scripts/wiki_medical_agent.py`
  - Add MOC intent detection, action validation, dry-run MOC plan builder, surgery preview payload builder.
- No default change: `scripts/build_wiki_medical_agent.py`
  - It should keep calling `build_status_payload`; no `--apply` path is required for MOC.
- No write change: `scripts/wiki_moc_projection.py`
  - Use existing `build_moc_plan`; do not alter `apply_moc_plan`.
- No write change: `scripts/wiki_surgery.py`
  - Reuse `build_surgery_plan_from_case(case_package, moc_plan=...)`.

MOC boundary to preserve throughout:

- MOC does not enter `treatment_preview`.
- MOC does not write a treatment record.
- `moc-apply-review-2026-05-18.md`-style pages are review/surgery evidence, not treatment.
- `moc_surgery_preview` does not create `wiki/moc`, does not update the case file, and does not mutate `Confirmed Decisions`.

---

### Task 1: Create OpenSpec Change

**Files:**
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/proposal.md`
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/design.md`
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/specs/wiki-medical-agent/spec.md`

- [ ] **Step 1: Create OpenSpec artifacts**

Add `openspec/changes/add-medical-agent-moc-surgery-preview/proposal.md`:

```markdown
# Proposal: medical-agent MOC surgery preview

## Summary

Add a read-only `moc_surgery_preview` route to the wiki medical agent.

## Problem

The MOC generator can already produce dry-run object lifecycle previews, but
the normal `$report-wiki-portfolio:wiki-medical-agent` entry point does not
recognize MOC preview requests. A request such as `moc preview status` is
currently classified as `treatment_preview`, which is the wrong medical-loop
route.

MOC is structurally sensitive. It should not be treated as treatment, because
MOC create/update/orphan actions are generated navigation changes that require
surgery review.

## Scope

In scope:

- Add a read-only `moc_surgery_preview` intent.
- Route explicit MOC preview/surgery/review requests before generic treatment
  preview matching.
- Build a MOC dry-run plan and pass it to existing surgery preview logic.
- Return compact MOC and surgery summaries in the medical-agent payload.
- Add tests proving MOC preview does not write `wiki/moc` or update the case.

Out of scope:

- Writing `wiki/moc`.
- Running MOC `--apply`.
- Writing treatment records.
- Writing surgery records.
- Updating the active case file.
- Mutating `Confirmed Decisions`, taxonomy config, ADRs, AGENTS, skills, or
  OpenSpec lifecycle state.

## Success Criteria

- `moc preview surgery` routes to `moc_surgery_preview`.
- `preview apply confirmed treatments` still routes to `treatment_preview`.
- With one active case, the medical-agent payload includes `moc_projection` and
  `surgery_preview`.
- With no active case, the route blocks with `no_active_case`.
- Preview creates no `wiki/moc` directory and does not modify the case file.
```

Add `openspec/changes/add-medical-agent-moc-surgery-preview/design.md`:

```markdown
# Design: medical-agent MOC surgery preview

## Architecture

Add one read-only route inside `scripts/wiki_medical_agent.py`:

```text
classify_medical_intent
  -> moc_surgery_preview
  -> resolve_active_case
  -> build_moc_plan from extracted graph
  -> build_surgery_plan_from_case(case, moc_plan)
  -> compact payload
```

The medical agent remains the user-facing controller. MOC generation remains
owned by `scripts/wiki_moc_projection.py`. Surgery classification remains owned
by `scripts/wiki_surgery.py`.

## Intent Rules

MOC routing must run before generic preview routing.

MOC signals: `moc`, `obsidian`, `图谱导航`, `知识地图`.

Review signals: `preview`, `预览`, `surgery`, `手术`, `分流`, `审`.

## Payload

When allowed, append:

- `moc_projection`: copy of MOC plan summary.
- `surgery_preview`: compact object containing `moc_projection_count` and up to
  five `sample_items`.

`next_action` is `review_moc_surgery_preview` when create/update/orphan items
exist and `moc_projection_clean` when the MOC plan has no surgery items.

## Boundaries

The route is preview-only. It must not write `wiki/moc`, treatment records,
surgery records, or case-file updates.
```

Add `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec change artifacts.
- [ ] 2. Add RED tests for MOC intent and medical-agent preview boundaries.
- [ ] 3. Implement MOC intent classification and action validation.
- [ ] 4. Implement compact MOC surgery preview payload.
- [ ] 5. Run CLI and unit verification.
- [ ] 6. Add evaluation evidence and mark tasks complete.
```

Add `openspec/changes/add-medical-agent-moc-surgery-preview/specs/wiki-medical-agent/spec.md`:

```markdown
# wiki-medical-agent Specification Delta

## ADDED Requirements

### Requirement: Medical agent SHALL route MOC preview requests to surgery preview

The medical agent SHALL recognize explicit MOC preview, review, and surgery
requests and route them to a read-only `moc_surgery_preview` action.

#### Scenario: User requests MOC surgery preview with one active case

- **WHEN** the user asks for MOC preview, MOC review, MOC surgery, Obsidian graph
  preview, or knowledge-map review
- **AND** exactly one active medical case exists
- **THEN** the medical agent SHALL return intent `moc_surgery_preview`
- **AND** it SHALL build a MOC dry-run plan
- **AND** it SHALL pass the MOC plan into surgery preview
- **AND** it SHALL return compact `moc_projection` and `surgery_preview` payload
  fields
- **AND** it SHALL NOT write `wiki/moc`.

#### Scenario: User requests MOC preview without an active case

- **WHEN** no active medical case exists
- **THEN** the medical agent SHALL block `moc_surgery_preview`
- **AND** it SHALL return `blocked_reason: no_active_case`.

#### Scenario: User requests ordinary treatment preview

- **WHEN** the user asks to preview confirmed treatment candidates
- **AND** the request does not contain a MOC signal
- **THEN** the medical agent SHALL keep routing to `treatment_preview`.

### Requirement: MOC surgery preview SHALL preserve medical-loop boundaries

The medical agent SHALL treat MOC projection changes as surgery preview items,
not treatment items.

#### Scenario: MOC surgery preview runs

- **WHEN** `moc_surgery_preview` is allowed
- **THEN** the medical agent SHALL NOT write treatment records
- **AND** it SHALL NOT write surgery records
- **AND** it SHALL NOT update the active case file
- **AND** it SHALL NOT mutate `Confirmed Decisions`.
```

- [ ] **Step 2: Validate the new OpenSpec change**

Run:

```bash
openspec validate add-medical-agent-moc-surgery-preview --strict
```

Expected:

```text
Change 'add-medical-agent-moc-surgery-preview' is valid
```

Network-only PostHog DNS warnings may appear after validation; record them in
evaluation if they do.

- [ ] **Step 3: Commit OpenSpec skeleton**

Run:

```bash
git add openspec/changes/add-medical-agent-moc-surgery-preview/proposal.md \
  openspec/changes/add-medical-agent-moc-surgery-preview/design.md \
  openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md \
  openspec/changes/add-medical-agent-moc-surgery-preview/specs/wiki-medical-agent/spec.md
git commit -m "docs: propose medical agent MOC surgery preview"
```

Expected commit summary:

```text
docs: propose medical agent MOC surgery preview
```

---

### Task 2: Add RED Medical-Agent Tests

**Files:**
- Modify: `tests/test_wiki_medical_agent.py`

- [ ] **Step 1: Add imports**

In `tests/test_wiki_medical_agent.py`, extend the import from
`scripts.wiki_medical_agent`:

```python
from scripts.wiki_medical_agent import (
    apply_confirmed_treatment_and_recover,
    build_moc_surgery_preview_payload,
    build_status_payload,
    classify_medical_intent,
    resolve_active_case,
    validate_case_action,
)
```

- [ ] **Step 2: Add intent classification RED tests**

Add these methods inside `WikiMedicalAgentTest` after
`test_classifies_preview_before_apply`:

```python
    def test_classifies_moc_preview_as_surgery_preview_before_treatment_preview(self) -> None:
        self.assertEqual(
            classify_medical_intent("moc preview surgery").intent,
            "moc_surgery_preview",
        )
        self.assertEqual(
            classify_medical_intent("Obsidian 知识地图 预览分流").intent,
            "moc_surgery_preview",
        )
        self.assertEqual(
            classify_medical_intent("preview apply confirmed treatments").intent,
            "treatment_preview",
        )
```

- [ ] **Step 3: Add no-case and multiple-case RED tests**

Add these methods near the existing status payload tests:

```python
    def test_moc_surgery_preview_blocks_without_active_case(self) -> None:
        payload = build_status_payload(self.tmpdir, "moc preview surgery")

        self.assertEqual(payload["intent"], "moc_surgery_preview")
        self.assertEqual(payload["case_path"], "")
        self.assertEqual(payload["state"], "no_case")
        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "no_active_case")
        self.assertEqual(payload["next_action"], "diagnose")

    def test_moc_surgery_preview_blocks_with_multiple_active_cases(self) -> None:
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:03+00:00")
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:04+00:00")

        payload = build_status_payload(self.tmpdir, "moc preview surgery")

        self.assertEqual(payload["intent"], "moc_surgery_preview")
        self.assertEqual(payload["state"], "multiple_active_cases")
        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "multiple_active_cases")
        self.assertEqual(payload["next_action"], "select_active_case")
        self.assertEqual(len(payload["candidate_cases"]), 2)
```

- [ ] **Step 4: Add one-case payload RED test with a fake MOC plan**

Add this method near the other status payload tests:

```python
    def test_builds_moc_surgery_preview_payload_from_active_case_and_moc_plan(self) -> None:
        case_path = self._write_case(
            self._case_package(status="archive_ready"),
            "2026-05-15T01:02:03+00:00",
        )
        moc_plan = {
            "summary": {
                "candidate_count": 2,
                "create_count": 1,
                "update_count": 1,
                "noop_count": 0,
                "orphan_count": 0,
            },
            "entries": [
                {
                    "action": "create",
                    "kind": "object",
                    "key": "agent-governance-gate-gap",
                    "path": "wiki/moc/object-agent-governance-gate-gap.md",
                    "link_count": 2,
                },
                {
                    "action": "update",
                    "kind": "relation",
                    "key": "validates",
                    "path": "wiki/moc/relation-validates.md",
                    "link_count": 9,
                },
            ],
        }

        payload = build_moc_surgery_preview_payload(self.tmpdir, case_path, moc_plan)

        self.assertEqual(payload["moc_projection"]["candidate_count"], 2)
        self.assertEqual(payload["surgery_preview"]["moc_projection_count"], 2)
        self.assertEqual(len(payload["surgery_preview"]["sample_items"]), 2)
        self.assertEqual(payload["next_action"], "review_moc_surgery_preview")
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
```

- [ ] **Step 5: Add CLI boundary RED test**

Add this method near the existing CLI tests:

```python
    def test_cli_moc_surgery_preview_is_read_only(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        case_package = self._case_package(status="archive_ready")
        case_path = self._write_case(case_package, "2026-05-15T01:02:03+00:00")
        before = case_path.read_text(encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "moc preview surgery",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "moc_surgery_preview")
        self.assertTrue(payload["allowed"])
        self.assertEqual(payload["allowed_action"], "preview_moc_surgery_plan")
        self.assertIn("moc_projection", payload)
        self.assertIn("surgery_preview", payload)
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())
        self.assertEqual(case_path.read_text(encoding="utf-8"), before)
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-treatment-runs").exists())
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-surgery-runs").exists())
```

- [ ] **Step 6: Run RED tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent
```

Expected failure examples:

```text
AssertionError: 'treatment_preview' != 'moc_surgery_preview'
ImportError: cannot import name 'build_moc_surgery_preview_payload'
```

Commit nothing in RED unless your local workflow requires a test-only commit.

---

### Task 3: Implement Intent Classification And Validation

**Files:**
- Modify: `scripts/wiki_medical_agent.py`
- Modify: `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`

- [ ] **Step 1: Add MOC helper constants**

In `scripts/wiki_medical_agent.py`, after `READ_ONLY_INTENTS`, replace:

```python
READ_ONLY_INTENTS = {"status", "diagnose"}
```

with:

```python
READ_ONLY_INTENTS = {"status", "diagnose"}
MOC_SIGNALS = ("moc", "obsidian", "图谱导航", "知识地图")
MOC_REVIEW_SIGNALS = ("preview", "预览", "surgery", "手术", "分流", "审")
```

- [ ] **Step 2: Add MOC classifier helper**

Add below the constants:

```python
def _is_moc_surgery_preview_request(lowered: str) -> bool:
    has_moc = any(signal in lowered for signal in MOC_SIGNALS)
    has_review = any(signal in lowered for signal in MOC_REVIEW_SIGNALS)
    return has_moc and has_review
```

- [ ] **Step 3: Route MOC before treatment preview**

In `classify_medical_intent`, insert this block before the generic preview
block:

```python
    if _is_moc_surgery_preview_request(lowered):
        return IntentResult(
            "moc_surgery_preview",
            expected_count,
            "user requested MOC surgery preview",
        )
```

The top of the function should now contain:

```python
def classify_medical_intent(text: str) -> IntentResult:
    lowered = text.lower()
    count_match = re.search(r"(\d+)", text)
    expected_count = int(count_match.group(1)) if count_match else None
    if "legacy" in lowered or "debug" in lowered:
        return IntentResult("legacy_debug", expected_count, "explicit legacy/debug request")
    if _is_moc_surgery_preview_request(lowered):
        return IntentResult(
            "moc_surgery_preview",
            expected_count,
            "user requested MOC surgery preview",
        )
    if any(token in lowered for token in ["preview", "dry-run", "dry run", "预览"]):
        return IntentResult("treatment_preview", expected_count, "user requested treatment preview")
```

- [ ] **Step 4: Add validation branch**

In `validate_case_action`, add this branch before `treatment_preview`:

```python
    if intent == "moc_surgery_preview":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="preview_moc_surgery_plan",
            executable_count=treatment_count,
        )
```

Do not add `moc_surgery_preview` to `READ_ONLY_INTENTS`. It still requires an
active case through `validate_resolved_case_action`.

- [ ] **Step 5: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_classifies_moc_preview_as_surgery_preview_before_treatment_preview \
  tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_moc_surgery_preview_blocks_without_active_case \
  tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_moc_surgery_preview_blocks_with_multiple_active_cases
```

Expected:

```text
OK
```

The payload and CLI tests may still fail until Task 4.

---

### Task 4: Implement Compact MOC Surgery Preview Payload

**Files:**
- Modify: `scripts/wiki_medical_agent.py`

- [ ] **Step 1: Add imports**

At the top of `scripts/wiki_medical_agent.py`, add:

```python
from scripts.build_wiki_moc_projection import load_graph
from scripts.wiki_moc_projection import build_moc_plan
from scripts.wiki_surgery import build_surgery_plan_from_case
```

Keep existing imports unchanged.

- [ ] **Step 2: Add compact sample helper**

Add this helper above `build_status_payload`:

```python
def _sample_moc_items(plan: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    items = plan.get("moc_projection_items", [])
    if not isinstance(items, list):
        return []
    sample: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        sample.append(
            {
                "action": str(item.get("action", "")),
                "kind": str(item.get("kind", "")),
                "key": str(item.get("key", "")),
                "path": str(item.get("path", "")),
                "link_count": int(item.get("link_count", 0) or 0),
            }
        )
        if len(sample) >= limit:
            break
    return sample
```

- [ ] **Step 3: Add payload builder**

Add this function below `_sample_moc_items`:

```python
def build_moc_surgery_preview_payload(
    root: Path | str,
    case_path: Path | str,
    moc_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    case_file = Path(case_path).resolve()
    if root_path not in case_file.parents and case_file != root_path:
        raise ValueError("case path escapes root")
    case_package = load_medical_case_file(case_file)
    case_package["case_path"] = case_file.as_posix()
    if moc_plan is None:
        graph = load_graph(root_path, None)
        moc_plan = build_moc_plan(root_path, graph)
    surgery_plan = build_surgery_plan_from_case(case_package, moc_plan=moc_plan)
    moc_summary = dict(moc_plan.get("summary", {})) if isinstance(moc_plan, dict) else {}
    surgery_summary = surgery_plan.get("summary", {})
    moc_projection_count = 0
    if isinstance(surgery_summary, dict):
        moc_projection_count = int(surgery_summary.get("moc_projection_count", 0) or 0)
    return {
        "moc_projection": moc_summary,
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

- [ ] **Step 4: Enrich `build_status_payload`**

In `build_status_payload`, after:

```python
    if resolution.case_package is not None:
        archive = resolution.case_package.get("archive_next_action", {})
        next_action = archive.get("next_action") if isinstance(archive, dict) else ""
        payload["executable_count"] = validation.executable_count
        payload["expected_count"] = validation.expected_count
        if validation.allowed and next_action:
            payload["next_action"] = str(next_action)
```

replace it with:

```python
    if resolution.case_package is not None:
        archive = resolution.case_package.get("archive_next_action", {})
        next_action = archive.get("next_action") if isinstance(archive, dict) else ""
        payload["executable_count"] = validation.executable_count
        payload["expected_count"] = validation.expected_count
        if validation.allowed and intent.intent == "moc_surgery_preview" and resolution.case_path is not None:
            payload.update(build_moc_surgery_preview_payload(root, resolution.case_path))
        elif validation.allowed and next_action:
            payload["next_action"] = str(next_action)
```

This keeps archive next action from overwriting the MOC preview next action.

- [ ] **Step 5: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_builds_moc_surgery_preview_payload_from_active_case_and_moc_plan \
  tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_cli_moc_surgery_preview_is_read_only
```

Expected:

```text
OK
```

If the CLI test creates `wiki/moc`, stop and inspect calls for accidental
`apply_moc_plan`.

---

### Task 5: Full Verification And Evaluation

**Files:**
- Modify: `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`
- Create: `openspec/changes/add-medical-agent-moc-surgery-preview/evaluation.md`

- [ ] **Step 1: Run required tests**

Run:

```bash
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_surgery tests.test_wiki_moc_projection
```

Expected:

```text
OK
```

- [ ] **Step 2: Run current-repo CLI smoke test**

Run:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "moc preview surgery"
```

Expected JSON fields:

```json
{
  "intent": "moc_surgery_preview",
  "allowed_action": "preview_moc_surgery_plan"
}
```

If the current repo has no active case or multiple active cases, record that
actual boundary result in `evaluation.md` instead of forcing state changes.

- [ ] **Step 3: Verify no MOC directory was created**

Run:

```bash
test -d wiki/moc
```

Expected:

```text
exit code 1
```

An exit code of 1 means `wiki/moc` does not exist and preview did not apply MOC.

- [ ] **Step 4: Run OpenSpec validation**

Run:

```bash
openspec validate add-medical-agent-moc-surgery-preview --strict
```

Expected:

```text
Change 'add-medical-agent-moc-surgery-preview' is valid
```

- [ ] **Step 5: Fill evaluation**

Create `openspec/changes/add-medical-agent-moc-surgery-preview/evaluation.md`:

```markdown
# Evaluation: medical-agent MOC surgery preview

## Evidence

| Check | Result | Notes |
| --- | --- | --- |
| `python3 -m unittest tests.test_wiki_medical_agent.WikiMedicalAgentTest.test_classifies_moc_preview_as_surgery_preview_before_treatment_preview` before implementation | RED | MOC preview routed to `treatment_preview` or missing helper imports failed. |
| `python3 -m unittest tests.test_wiki_medical_agent` after implementation | PASS | Medical-agent tests passed. |
| `python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_surgery tests.test_wiki_moc_projection` | PASS | Confirms medical-agent, surgery, and MOC projection integration. |
| `python3 scripts/build_wiki_medical_agent.py --intent-text "moc preview surgery"` | PASS | Returned the expected MOC surgery preview boundary or documented active-case blocker. |
| `test -d wiki/moc` | PASS boundary | Exit code 1 confirms no `wiki/moc` directory was created. |
| `openspec validate add-medical-agent-moc-surgery-preview --strict` | PASS | Change validates locally. |

## Boundary

This change makes MOC visible inside `$report-wiki-portfolio:wiki-medical-agent`
as surgery preview. It does not make MOC treatment, does not write MOC pages,
does not update case files, and does not create review records.

## Residual Risks

- Full MOC page previews remain available through the MOC generator, not the
  compact medical-agent payload.
- Durable review evidence for MOC surgery preview can be added later through an
  explicit surgery-record workflow.
```

Adjust rows with actual command counts and any PostHog DNS warning if observed.

- [ ] **Step 6: Mark OpenSpec tasks complete**

Update `openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md`:

```markdown
# Tasks

- [x] 1. Create OpenSpec change artifacts.
- [x] 2. Add RED tests for MOC intent and medical-agent preview boundaries.
- [x] 3. Implement MOC intent classification and action validation.
- [x] 4. Implement compact MOC surgery preview payload.
- [x] 5. Run CLI and unit verification.
- [x] 6. Add evaluation evidence and mark tasks complete.
```

- [ ] **Step 7: Commit implementation**

Run:

```bash
git add tests/test_wiki_medical_agent.py \
  scripts/wiki_medical_agent.py \
  openspec/changes/add-medical-agent-moc-surgery-preview/tasks.md \
  openspec/changes/add-medical-agent-moc-surgery-preview/evaluation.md
git commit -m "feat: add medical agent MOC surgery preview"
```

Expected commit summary:

```text
feat: add medical agent MOC surgery preview
```

---

## Self-Review

Spec coverage:

- MOC requests no longer fall into treatment preview: Task 2 and Task 3.
- Medical-agent payload includes MOC/surgery preview: Task 2 and Task 4.
- Route is read-only and does not write `wiki/moc`: Task 2 and Task 5.
- Existing treatment behavior remains unchanged: Task 2 regression and Task 5 full tests.
- OpenSpec lifecycle is present: Task 1 and Task 5.

Placeholder scan:

- Placeholder scan passed.
- The only future-looking work is explicitly in residual risk and not required
  for this implementation.

Type consistency:

- `moc_surgery_preview` is the single new intent string.
- `preview_moc_surgery_plan` is the single allowed action string.
- `build_moc_surgery_preview_payload(root, case_path, moc_plan=None)` is the
  new helper name used in tests and implementation.
