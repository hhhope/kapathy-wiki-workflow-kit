#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PRESSURE = ROOT / "pressure"
WIKI = PRESSURE / "wiki"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_pages():
    pages = {}
    for path in WIKI.rglob("*.md"):
        rel = path.relative_to(WIKI).as_posix()
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^Keywords:\s*(.+)$", text, re.MULTILINE)
        keywords = []
        if match:
            keywords = [k.strip().lower() for k in match.group(1).split(",") if k.strip()]
        pages[rel] = {
            "text": text.lower(),
            "keywords": keywords,
        }
    return pages


def score_query(query: str, pages: dict[str, dict[str, object]]):
    query_l = query.lower()
    ranked = []
    for rel, data in pages.items():
        score = 0
        for kw in data["keywords"]:
            if kw and kw in query_l:
                score += 3
        title = rel.replace("/", " ").replace(".md", " ")
        for token in re.findall(r"[a-z0-9-]+", title.lower()):
            if token and token in query_l:
                score += 1
        if score > 0:
            ranked.append((score, rel))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    return [rel for _, rel in ranked[:3]]


def percentile(values: list[int], pct: int) -> int:
    if not values:
      return 0
    ordered = sorted(values)
    idx = math.ceil((pct / 100) * len(ordered)) - 1
    idx = max(0, min(idx, len(ordered) - 1))
    return ordered[idx]


def run_retrieval(pages):
    queries = load_json(PRESSURE / "queries.json")
    similar_total = 0
    similar_hits = 0
    noise_total = 0
    noise_hits = 0
    rows = []

    for item in queries:
        top = score_query(item["query"], pages)
        expected = set(item["expected_core_pages"])
        forbidden = set(item["forbidden_pages"])
        hit = bool(expected.intersection(top))
        noisy = bool(forbidden.intersection(top))
        if item["category"] in {"similar", "edge"}:
            similar_total += 1
            if hit:
                similar_hits += 1
        if item["category"] == "noise":
            noise_total += 1
            if noisy:
                noise_hits += 1
        rows.append({
            "id": item["id"],
            "category": item["category"],
            "top": top,
            "hit": hit,
            "noisy": noisy,
        })

    recall = similar_hits / similar_total if similar_total else 0.0
    noise = noise_hits / noise_total if noise_total else 0.0
    return {
        "rows": rows,
        "similar_total": similar_total,
        "similar_hits": similar_hits,
        "noise_total": noise_total,
        "noise_hits": noise_hits,
        "recall": recall,
        "noise": noise,
    }


def run_weekly_review():
    logs = load_json(PRESSURE / "weekly-review-logs.json")
    reviewed = sum(1 for item in logs if item["reviewed"])
    absorbed = sum(1 for item in logs if item["accepted"])
    discarded = sum(1 for item in logs if not item["accepted"])
    accepted_with_dest = sum(1 for item in logs if item["accepted"] and item["absorbed_to"])
    reviewed_with_absorbed_to = sum(1 for item in logs if item["reviewed"] and item["absorbed_to"])
    destinations = Counter(item["destination_type"] for item in logs if item["accepted"])
    absorption = accepted_with_dest / absorbed if absorbed else 0.0
    absorbed_to_completion = reviewed_with_absorbed_to / reviewed if reviewed else 0.0
    return {
        "reviewed": reviewed,
        "absorbed": absorbed,
        "discarded": discarded,
        "accepted": absorbed,
        "accepted_with_dest": accepted_with_dest,
        "absorption": absorption,
        "absorbed_to_completion": absorbed_to_completion,
        "destinations": destinations,
    }


def run_startup():
    scenarios = load_json(PRESSURE / "startup-scenarios.json")
    counts = [len(item["pages"]) for item in scenarios]
    return {
        "scenarios": len(scenarios),
        "counts": counts,
        "p50": percentile(counts, 50),
        "p90": percentile(counts, 90),
        "max": max(counts) if counts else 0,
    }


def verdict(ok: bool) -> str:
    return "Pass" if ok else "Fail"


def render_markdown(retrieval, weekly, startup):
    lines = []
    lines.append("# Lore Pressure Results")
    lines.append("")
    lines.append("Date: 2026-04-11")
    lines.append("Branch: `feat-lore-wiki-openspec`")
    lines.append("")
    lines.append("This file records the second-pass corpus-driven pressure run for retrieval, weekly review, and startup-budget metrics.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Result | Target | Verdict |")
    lines.append("|---|---:|---:|---|")
    lines.append(f"| Similar-task recall | {retrieval['similar_hits']}/{retrieval['similar_total']} = `{retrieval['recall']:.0%}` | `>= 80%` | {verdict(retrieval['recall'] >= 0.80)} |")
    lines.append(f"| Irrelevant-page noise | {retrieval['noise_hits']}/{retrieval['noise_total']} = `{retrieval['noise']:.0%}` | `<= 20%` | {verdict(retrieval['noise'] <= 0.20)} |")
    lines.append(f"| Log absorption success | {weekly['accepted_with_dest']}/{weekly['accepted']} = `{weekly['absorption']:.0%}` | `>= 90%` | {verdict(weekly['absorption'] >= 0.90)} |")
    lines.append(f"| `absorbed-to` completion | {weekly['reviewed'] - weekly['discarded']}/{weekly['reviewed']} = `{weekly['absorbed_to_completion']:.0%}` | weekly review metrics required | {verdict(weekly['absorbed_to_completion'] >= 0.80)} |")
    lines.append(f"| Startup context budget P50 | `{startup['p50']}` pages | `3-4` | {verdict(3 <= startup['p50'] <= 4)} |")
    lines.append(f"| Startup context budget P90 | `{startup['p90']}` pages | `<= 6` | {verdict(startup['p90'] <= 6)} |")
    lines.append("")
    lines.append("## Weekly review metrics block")
    lines.append("")
    lines.append(f"- reviewed logs: `{weekly['reviewed']}`")
    lines.append(f"- absorbed logs: `{weekly['absorbed']}`")
    lines.append(f"- discarded logs: `{weekly['discarded']}`")
    lines.append(f"- `absorbed-to` completion rate: `{weekly['absorbed_to_completion']:.0%}`")
    lines.append(f"- absorption success rate: `{weekly['absorption']:.0%}`")
    lines.append(f"- destination page types: `{dict(weekly['destinations'])}`")
    lines.append("")
    lines.append("## Retrieval sample details")
    lines.append("")
    lines.append("| Query id | Category | Top results | Hit | Noisy |")
    lines.append("|---|---|---|---|---|")
    for row in retrieval["rows"]:
        top = ", ".join(row["top"]) if row["top"] else "(none)"
        hit_text = "n/a" if row["category"] == "noise" else verdict(row["hit"])
        noisy_text = verdict(not row["noisy"]) if row["category"] == "noise" else ("No" if not row["noisy"] else "Yes")
        lines.append(f"| `{row['id']}` | {row['category']} | `{top}` | {hit_text} | {noisy_text} |")
    lines.append("")
    lines.append("## Startup budget distribution")
    lines.append("")
    lines.append(f"- scenario count: `{startup['scenarios']}`")
    lines.append(f"- page counts: `{startup['counts']}`")
    lines.append(f"- P50: `{startup['p50']}`")
    lines.append(f"- P90: `{startup['p90']}`")
    lines.append(f"- max: `{startup['max']}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Retrieval recall and noise now have a measured corpus instead of a tiny walkthrough only.")
    lines.append("- Weekly review now has a mandatory metrics block, not only page diffs.")
    lines.append("- Startup-budget evidence is based on 10 scenarios, not one medium example.")
    return "\n".join(lines) + "\n"


def main():
    pages = load_pages()
    retrieval = run_retrieval(pages)
    weekly = run_weekly_review()
    startup = run_startup()

    md = render_markdown(retrieval, weekly, startup)
    (ROOT / "PRESSURE-RESULTS.md").write_text(md, encoding="utf-8")
    summary = {
        "recall": retrieval["recall"],
        "noise": retrieval["noise"],
        "absorption": weekly["absorption"],
        "absorbed_to_completion": weekly["absorbed_to_completion"],
        "startup_p50": startup["p50"],
        "startup_p90": startup["p90"],
        "startup_max": startup["max"],
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
