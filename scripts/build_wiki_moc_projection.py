#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timezone
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
VALID_MOC_ADMISSIONS = {"admit", "block", "needs_review"}


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


def _required_non_empty_string(review: dict, field: str, candidate_id: str) -> str:
    value = review[field]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"temperature review JSON value for {candidate_id!r} field {field!r} must be a non-empty string"
        )
    return value


def _validate_reviewed_at(review: dict, candidate_id: str) -> None:
    value = _required_non_empty_string(review, "reviewed_at", candidate_id)
    try:
        date.fromisoformat(value)
        return
    except ValueError:
        pass

    normalized_value = f"{value[:-1]}+00:00" if value.endswith("Z") else value
    try:
        datetime.fromisoformat(normalized_value)
    except ValueError as exc:
        raise ValueError(
            f"temperature review JSON value for {candidate_id!r} field 'reviewed_at' must be an ISO-8601 date or timestamp"
        ) from exc


def _validate_review_object(candidate_id: str, review: dict) -> None:
    missing_fields = sorted(REQUIRED_REVIEW_FIELDS - set(review))
    if missing_fields:
        raise ValueError(
            f"temperature review JSON value for {candidate_id!r} missing required field(s): {', '.join(missing_fields)}"
        )

    review_candidate_id = _required_non_empty_string(review, "candidate_id", candidate_id)
    if review_candidate_id != candidate_id:
        raise ValueError(
            f"temperature review JSON candidate_id mismatch for {candidate_id!r}: review candidate_id must match mapping key"
        )

    temperature = review["temperature"]
    if isinstance(temperature, bool) or not isinstance(temperature, int) or not 0 <= temperature <= 100:
        raise ValueError(
            f"temperature review JSON value for {candidate_id!r} field 'temperature' must be an integer from 0 to 100"
        )

    moc_admission = review["moc_admission"]
    if not isinstance(moc_admission, str) or moc_admission not in VALID_MOC_ADMISSIONS:
        raise ValueError(
            f"temperature review JSON value for {candidate_id!r} field 'moc_admission' must be one of admit, block, needs_review"
        )

    _required_non_empty_string(review, "rationale", candidate_id)
    _required_non_empty_string(review, "reviewer", candidate_id)
    _validate_reviewed_at(review, candidate_id)


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
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            raise ValueError("temperature review JSON keys must be non-empty candidate_id strings")
        if not isinstance(review, dict):
            raise ValueError(
                f"temperature review JSON value for {candidate_id!r} must be a review object"
            )
        _validate_review_object(candidate_id, review)

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
