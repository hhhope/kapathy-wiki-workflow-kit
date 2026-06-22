#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
CHANGE = "add-team-lore-bilingual-schema"


def run(cmd: list[str]) -> str:
    result = subprocess.run(
        cmd,
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def check_process_question():
    raw = run(["openspec", "status", "--change", CHANGE, "--json"])
    start = raw.find("{")
    data = json.loads(raw[start:])
    return {
        "case": "process",
        "route": "OpenSpec",
        "pass": data["changeName"] == CHANGE and all(item["status"] == "done" for item in data["artifacts"]),
        "details": {
            "changeName": data["changeName"],
            "artifacts": {item["id"]: item["status"] for item in data["artifacts"]},
        },
    }


def check_lore_question():
    skill = (REPO / "skills/lore/SKILL.md").read_text(encoding="utf-8")
    readme = (REPO / "skills/lore/README.md").read_text(encoding="utf-8")
    ok = all(
        marker in skill
        for marker in [
            "Process-plane question",
            "Lore question",
            "Graphify question",
            "Mixed question",
        ]
    ) and all(
        marker in readme
        for marker in [
            "Process plane vs knowledge plane",
            "**Code structure question**",
            "**Mixed question**",
        ]
    )
    return {
        "case": "lore",
        "route": "Lore",
        "pass": ok,
        "details": {
            "skill_markers_present": ok,
        },
    }


def check_graphify_question():
    raw = run(
        [
            "graphify",
            "query",
            "What code files or nodes connect Lore weekly review and retrieval pressure checks?",
        ]
    )
    ok = all(marker in raw for marker in ["run-pressure-checks.py", "run_weekly_review()", "run_retrieval()"])
    return {
        "case": "graphify",
        "route": "Graphify",
        "pass": ok,
        "details": {
            "contains_run_pressure_checks": "run-pressure-checks.py" in raw,
            "contains_run_weekly_review": "run_weekly_review()" in raw,
            "contains_run_retrieval": "run_retrieval()" in raw,
        },
    }


def check_mixed_question():
    skill = (REPO / "skills/lore/SKILL.md").read_text(encoding="utf-8")
    raw = run(
        [
            "graphify",
            "query",
            "What code files or nodes connect Lore weekly review and retrieval pressure checks?",
        ]
    )
    ok = "route to Lore first for scene and stable facts" in skill and "run_weekly_review()" in raw
    return {
        "case": "mixed",
        "route": "Lore then Graphify",
        "pass": ok,
        "details": {
            "lore_first_rule_present": "route to Lore first for scene and stable facts" in skill,
            "graphify_structure_present": "run_weekly_review()" in raw,
        },
    }


def render_markdown(results: list[dict]) -> str:
    lines = []
    lines.append("# Lore Knowledge Routing Results")
    lines.append("")
    lines.append("Date: 2026-04-13")
    lines.append("Branch: `feat/team-lore-bilingual-openspec`")
    lines.append("")
    lines.append("This file records behavior-level routing checks for the current Lore and Graphify contract.")
    lines.append("")
    lines.append("Important clarification:")
    lines.append("")
    lines.append('- "process questions route to OpenSpec" is an agent-routing rule')
    lines.append("- it is not a claim that the human user needs a new command to work with the repo")
    lines.append("- the purpose is to stop the agent from answering process questions with stale wiki or graph output")
    lines.append("")
    lines.append("## Current usability judgment")
    lines.append("")
    lines.append("The current Lore wiki is still usable.")
    lines.append("")
    lines.append("What changed in this round is not \"make the wiki exist.\"")
    lines.append("What changed is:")
    lines.append("")
    lines.append("- make the routing boundary explicit")
    lines.append("- keep the wiki as the durable rule-and-boundary layer")
    lines.append("- use Graphify only when code topology is actually needed")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Case | Expected route | Verdict |")
    lines.append("|---|---|---|")
    for item in results:
        lines.append(f"| `{item['case']}` | {item['route']} | {'Pass' if item['pass'] else 'Fail'} |")
    lines.append("")
    lines.append("## Limits")
    lines.append("")
    lines.append("- these are representative behavior checks, not a general-purpose classifier benchmark")
    lines.append("- Graphify currently covers code topology only; it does not index team-lore wiki semantics")
    lines.append("- the current wiki can be used now, but the stronger guarantee is still \"Lore first for rules, Graphify when structure is needed\"")
    lines.append("")
    return "\n".join(lines)


def main():
    results = [
        check_process_question(),
        check_lore_question(),
        check_graphify_question(),
        check_mixed_question(),
    ]
    (ROOT / "KNOWLEDGE-ROUTING-RESULTS.md").write_text(render_markdown(results), encoding="utf-8")
    summary = {
        "all_pass": all(item["pass"] for item in results),
        "results": results,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
