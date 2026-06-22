#!/usr/bin/env python3
"""Normalize an OpenSpec change folder into a Superpowers-friendly planning brief."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


REQUIREMENT = re.compile(
    r"^###\s+Requirement:\s*(.+)$", re.MULTILINE | re.IGNORECASE
)
SCENARIO = re.compile(
    r"^####\s+Scenario:\s*(.+)$", re.MULTILINE | re.IGNORECASE
)
TASK_ITEM = re.compile(r"^-\s+\[([ xX])\]\s+(.+)$", re.MULTILINE)
HEADING = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


@dataclass
class SpecSlice:
    path: Path
    requirements: list[dict[str, object]] = field(default_factory=list)


def read_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8").strip()


def parse_spec(content: str) -> list[dict[str, object]]:
    reqs: list[dict[str, object]] = []
    current_delta = "UNKNOWN"
    for line in content.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip().upper()
            if "REQUIREMENT" in heading:
                current_delta = heading.split()[0] if heading.split() else heading
        if not line.startswith("### Requirement:"):
            continue
        title = line.split(":", 1)[1].strip()
        reqs.append({"title": title, "delta": current_delta, "_line": line})

    for i, meta in enumerate(reqs):
        # Re-scan for block boundaries using REQUIREMENT regex for stable excerpts
        title = meta["title"]
        pattern = re.compile(
            rf"^###\s+Requirement:\s*{re.escape(title)}\s*$",
            re.MULTILINE | re.IGNORECASE,
        )
        match = pattern.search(content)
        if not match:
            continue
        start = match.start()
        next_req = REQUIREMENT.search(content, match.end())
        end = next_req.start() if next_req else len(content)
        block = content[start:end]
        scenarios = [m.group(1).strip() for m in SCENARIO.finditer(block)]
        reqs[i] = {
            "title": title,
            "delta": meta["delta"],
            "scenarios": scenarios,
            "body_excerpt": block.strip()[:1200],
        }
    return reqs


def parse_tasks(content: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for match in TASK_ITEM.finditer(content):
        done = match.group(1).lower() == "x"
        items.append({"done": str(done).lower(), "text": match.group(2).strip()})
    return items


def extract_sections(content: str, labels: tuple[str, ...]) -> dict[str, str]:
    """Pull ## Section bodies for common OpenSpec headings (case-insensitive)."""
    found: dict[str, str] = {}
    if not content:
        return found
    for match in HEADING.finditer(content):
        level = len(match.group(1))
        title = match.group(2).strip()
        if level != 2:
            continue
        key = title.lower()
        if key not in labels:
            continue
        start = match.end()
        next_h2 = re.search(r"^##\s+", content[start:], re.MULTILINE)
        end = start + next_h2.start() if next_h2 else len(content)
        found[key] = content[start:end].strip()
    return found


def try_openspec_status(repo: Path, change_name: str) -> dict | None:
    try:
        raw = subprocess.run(
            ["openspec", "status", "--change", change_name, "--json"],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    start = raw.find("{")
    if start < 0:
        return None
    return json.loads(raw[start:])


def infer_change_name(change_dir: Path) -> str:
    name = change_dir.name
    if name.startswith("2026-") or name.startswith("20"):
        # dated folder: 2026-04-14-foo -> foo or full slug
        parts = name.split("-", 3)
        if len(parts) >= 4:
            return "-".join(parts[3:])
    return name


def collect_specs(change_dir: Path) -> list[SpecSlice]:
    specs_root = change_dir / "specs"
    slices: list[SpecSlice] = []
    if not specs_root.is_dir():
        return slices
    for path in sorted(specs_root.rglob("spec.md")):
        text = read_text(path) or ""
        slices.append(SpecSlice(path=path, requirements=parse_spec(text)))
    return slices


def build_brief(change_dir: Path, repo: Path | None = None) -> str:
    change_dir = change_dir.resolve()
    repo = repo or change_dir
    while repo != repo.parent and not (repo / "openspec").is_dir():
        repo = repo.parent

    proposal = read_text(change_dir / "proposal.md") or ""
    design = read_text(change_dir / "design.md") or ""
    tasks_md = read_text(change_dir / "tasks.md") or ""
    explore = read_text(change_dir / "explore-notes.md")

    proposal_sections = extract_sections(
        proposal,
        (
            "why",
            "what changes",
            "capabilities",
            "impact",
            "goal",
            "outcome",
            "non-goals",
        ),
    )
    design_sections = extract_sections(
        design,
        (
            "context",
            "goals / non-goals",
            "goals/non-goals",
            "decisions",
            "risks / trade-offs",
            "acceptance boundary",
            "summary",
        ),
    )

    specs = collect_specs(change_dir)
    tasks = parse_tasks(tasks_md)
    change_name = infer_change_name(change_dir)
    status = try_openspec_status(repo, change_name)

    lines: list[str] = []
    lines.append("# OpenSpec → Superpowers Planning Brief")
    lines.append("")
    lines.append(f"- **Change directory:** `{change_dir}`")
    lines.append(f"- **Inferred change id:** `{change_name}`")
    lines.append("- **Generated by:** `skills/openspec-superpowers-bridge/scripts/build-planning-brief.py`")
    lines.append("")
    lines.append("> Feed this file to `superpowers:writing-plans` as the **only** OpenSpec source.")
    lines.append("> Implement via Superpowers TDD (`test-driven-development` + `executing-plans`), **not** `/opsx:apply`.")
    lines.append("")

    lines.append("## 1. Proposal (intent and motivation)")
    if not proposal and not explore:
        lines.append("_Missing `proposal.md` — cannot bridge._")
        lines.append("")
    if explore:
        lines.append("### Explore supplement (`explore-notes.md`)")
        lines.append(explore)
        lines.append("")
    if proposal and not proposal_sections:
        lines.append("### Full `proposal.md`")
        lines.append(proposal[:6000])
        lines.append("")
    for key in ("why", "goal"):
        if key in proposal_sections:
            lines.append(f"### proposal — {key.title()}")
            lines.append(proposal_sections[key])
            lines.append("")
    for key in ("what changes", "capabilities"):
        if key in proposal_sections:
            lines.append(f"### proposal — {key.title()}")
            lines.append(proposal_sections[key])
            lines.append("")
    if "context" in design_sections and "why" not in proposal_sections:
        lines.append("### design — Context (when proposal has no Why)")
        lines.append(design_sections["context"])
        lines.append("")

    lines.append("## 2. Scope and constraints")
    for key, label in (
        ("impact", "Impact"),
        ("outcome", "Outcome"),
        ("non-goals", "Non-goals"),
    ):
        if key in proposal_sections:
            lines.append(f"### {label}")
            lines.append(proposal_sections[key])
            lines.append("")
    for key in ("goals / non-goals", "goals/non-goals", "acceptance boundary"):
        if key in design_sections:
            lines.append(f"### Design — {key.title()}")
            lines.append(design_sections[key])
            lines.append("")

    lines.append("## 3. Technical decisions (for plan architecture section)")
    for key in ("summary", "decisions", "risks / trade-offs"):
        if key in design_sections:
            lines.append(f"### {key.title()}")
            lines.append(design_sections[key])
            lines.append("")
    if design and not design_sections:
        lines.append(design[:4000])
        lines.append("")

    lines.append("## 4. Normative requirements (flattened from delta specs)")
    if not specs:
        lines.append("_No `specs/**/spec.md` found — writing-plans must treat design + proposal as spec._")
        lines.append("")
    req_index = 0
    for spec in specs:
        rel = spec.path.relative_to(change_dir).as_posix()
        lines.append(f"### Spec file: `{rel}`")
        if not spec.requirements:
            body = read_text(spec.path) or ""
            lines.append(body[:2000] if body else "_empty_")
            lines.append("")
            continue
        for req in spec.requirements:
            req_index += 1
            rid = f"R{req_index}"
            lines.append(f"#### {rid}: [{req['delta']}] {req['title']}")
            for i, scenario in enumerate(req["scenarios"], 1):
                lines.append(f"- **S{req_index}.{i}:** {scenario}")
            if not req["scenarios"]:
                lines.append("- _No explicit scenarios — implement from requirement title and excerpt._")
            lines.append("")
            lines.append("<details><summary>Requirement excerpt</summary>")
            lines.append("")
            lines.append(str(req["body_excerpt"]))
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines.append("## 5. OpenSpec task checklist (coarse — decompose in writing-plans)")
    if not tasks:
        lines.append("_No checkbox tasks in `tasks.md`._")
    else:
        for i, task in enumerate(tasks, 1):
            mark = "x" if task["done"] == "true" else " "
            lines.append(f"- [{mark}] **T{i}:** {task['text']}")
    lines.append("")
    lines.append(
        "_OpenSpec `tasks.md` is planning-only. `writing-plans` expands each unfinished T*n* into "
        "2–5 minute TDD steps; **execution** tracks plan checkboxes, not `/opsx:apply`._"
    )
    lines.append("")

    lines.append("## 6. Traceability seed (requirement → OpenSpec task)")
    lines.append("| Req | Suggested OpenSpec task anchors | Notes |")
    lines.append("|-----|----------------------------------|-------|")
    if req_index == 0:
        for i, task in enumerate(tasks, 1):
            lines.append(f"| _unmapped_ | T{i} | Map manually during writing-plans |")
    else:
        for r in range(1, req_index + 1):
            anchor = f"T{min(r, len(tasks))}" if tasks else "—"
            lines.append(f"| R{r} | {anchor} | Refine mapping while planning |")
    lines.append("")

    if status:
        lines.append("## 7. OpenSpec CLI status (optional)")
        lines.append("```json")
        lines.append(json.dumps(status, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")

    lines.append("## 8. Source manifest")
    for label, path in (
        ("proposal", change_dir / "proposal.md"),
        ("design", change_dir / "design.md"),
        ("tasks", change_dir / "tasks.md"),
        ("explore-notes", change_dir / "explore-notes.md"),
    ):
        flag = "present" if path.is_file() else "missing"
        lines.append(f"- `{path.name}`: **{flag}**")
    for spec in specs:
        lines.append(f"- `{spec.path.relative_to(change_dir).as_posix()}`: **present**")
    lines.append("")

    lines.append("## 9. Handoff checklist for writing-plans")
    lines.append("- [ ] Every **R*** requirement has at least one implementation task in the final plan")
    lines.append("- [ ] Every **Scenario** has a test or verification step")
    lines.append("- [ ] Acceptance boundary / non-goals appear in plan header or explicit out-of-scope")
    lines.append("- [ ] OpenSpec `tasks.md` checkboxes are not copied verbatim — they are decomposed")
    lines.append("- [ ] Plan saved under `docs/superpowers/plans/` per writing-plans skill")
    lines.append("- [ ] Implementation will use `test-driven-development` + `executing-plans`, not `/opsx:apply`")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "change_dir",
        type=Path,
        help="Path to openspec/changes/<change> (active or archive)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output path (default: <change_dir>/planning-brief-for-superpowers.md)",
    )
    parser.add_argument(
        "--repo",
        type=Path,
        help="Repository root for optional openspec status (default: auto-detect)",
    )
    args = parser.parse_args()
    if not args.change_dir.is_dir():
        print(f"error: not a directory: {args.change_dir}", file=sys.stderr)
        return 1
    out = args.output or args.change_dir / "planning-brief-for-superpowers.md"
    brief = build_brief(args.change_dir, args.repo)
    out.write_text(brief, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
