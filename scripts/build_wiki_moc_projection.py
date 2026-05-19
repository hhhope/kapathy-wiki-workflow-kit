#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRAPH_EXTRACTOR = ROOT / "scripts" / "extract_wiki_graph.py"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.wiki_moc_projection import apply_moc_plan, build_moc_plan
from scripts.wiki_moc_temperature import (
    build_moc_admission_plan,
    build_relation_feature_packages,
    build_temperature_clue_board,
)


REQUIRED_REVIEW_FIELDS = {
    "candidate_id",
    "temperature",
    "moc_admission",
    "rationale",
    "reviewer",
    "reviewed_at",
}


def load_graph(root: Path, graph_path: str | None) -> dict:
    if graph_path:
        return json.loads(Path(graph_path).read_text(encoding="utf-8"))
    completed = subprocess.run(
        [sys.executable, str(GRAPH_EXTRACTOR)],
        check=True,
        capture_output=True,
        text=True,
        cwd=root,
    )
    return json.loads(completed.stdout)


def load_temperature_admission(graph: dict, review_path: str | None) -> dict | None:
    if review_path is None:
        return None

    reviews = json.loads(Path(review_path).read_text(encoding="utf-8"))
    if not isinstance(reviews, dict):
        raise ValueError("temperature review JSON must be a keyed mapping from candidate_id strings to review objects")
    if REQUIRED_REVIEW_FIELDS.intersection(reviews):
        raise ValueError(
            "temperature review JSON must be a keyed mapping from candidate_id strings to review objects, not a single review object"
        )
    for candidate_id, review in reviews.items():
        if not isinstance(candidate_id, str):
            raise ValueError("temperature review JSON keys must be candidate_id strings")
        if not isinstance(review, dict):
            raise ValueError(
                f"temperature review JSON value for {candidate_id!r} must be a review object"
            )
        missing_fields = sorted(REQUIRED_REVIEW_FIELDS - set(review))
        if missing_fields:
            raise ValueError(
                f"temperature review JSON value for {candidate_id!r} missing required field(s): {', '.join(missing_fields)}"
            )
        if review["candidate_id"] != candidate_id:
            raise ValueError(
                f"temperature review JSON candidate_id mismatch for {candidate_id!r}: review candidate_id must match mapping key"
            )

    packages = build_relation_feature_packages(graph)
    board = build_temperature_clue_board(packages, reviews)
    return build_moc_admission_plan(board)


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview or apply Obsidian MOC projection.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--graph", help="optional graph JSON path")
    parser.add_argument("--moc-dir", default="wiki/moc")
    parser.add_argument("--temperature-review", help="optional review JSON keyed by candidate_id")
    parser.add_argument("--apply", action="store_true", help="write generated MOC blocks")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    graph = load_graph(root, args.graph)
    try:
        admission_plan = load_temperature_admission(graph, args.temperature_review)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(f"--temperature-review: {exc}")
    plan = (
        apply_moc_plan(root, graph, args.moc_dir, admission_plan=admission_plan)
        if args.apply
        else build_moc_plan(root, graph, args.moc_dir, admission_plan=admission_plan)
    )
    plan["generated_at"] = datetime.now(timezone.utc).isoformat()
    plan["mode"] = "apply" if args.apply else "dry-run"
    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
