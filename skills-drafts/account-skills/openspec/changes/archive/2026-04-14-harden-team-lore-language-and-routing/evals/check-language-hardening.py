#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    ROOT / "drafts/wiki/index.md",
    ROOT / "drafts/projects/account-skills/overview.md",
    ROOT / "drafts/pitfalls/behavior-assets-without-evidence.md",
]

REQUIRED_SECTIONS = ["Summary", "Applies When", "Top Facts", "Load Next"]
ZH_RE = re.compile(r"[\u4e00-\u9fff]")
EN_RE = re.compile(r"[A-Za-z]")


def extract_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


def evaluate_file(path: Path) -> dict:
    if not path.exists():
        return {
            "file": str(path.relative_to(ROOT)),
            "pass": False,
            "missing_file": True,
            "missing_sections": REQUIRED_SECTIONS,
            "sections_with_bilingual_support": [],
        }

    sections = extract_sections(path.read_text(encoding="utf-8"))
    missing_sections = [name for name in REQUIRED_SECTIONS if name not in sections]
    bilingual_sections = []
    for name in REQUIRED_SECTIONS:
        body = sections.get(name, "")
        if body and ZH_RE.search(body) and EN_RE.search(body):
            bilingual_sections.append(name)
    ok = not missing_sections and len(bilingual_sections) == len(REQUIRED_SECTIONS)
    return {
        "file": str(path.relative_to(ROOT)),
        "pass": ok,
        "missing_file": False,
        "missing_sections": missing_sections,
        "sections_with_bilingual_support": bilingual_sections,
    }


def main() -> int:
    results = [evaluate_file(path) for path in TARGETS]
    summary = {"all_pass": all(item["pass"] for item in results), "results": results}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
