from __future__ import annotations

from collections import Counter
from typing import Any


MECHANICAL_RELATION_TYPES = {"derived_from", "related_objects"}
ADMIT_DECISIONS = {"admit", "admit_relation"}


def temperature_band(value: int) -> str:
    if value >= 80:
        return "strong"
    if value >= 60:
        return "supporting"
    if value >= 40:
        return "weak"
    return "noise"


def _nodes_by_page(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        str(node.get("page_path")): node
        for node in nodes
        if isinstance(node.get("page_path"), str)
    }


def _nodes_by_object(nodes: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    by_object: dict[str, list[dict[str, Any]]] = {}
    for node in nodes:
        canonical_object = str(node.get("canonical_object") or "").strip()
        if canonical_object:
            by_object.setdefault(canonical_object, []).append(node)
    return by_object


def _target_node(
    target: str,
    by_page: dict[str, dict[str, Any]],
    by_object: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    if target in by_page:
        return by_page[target]
    candidates = by_object.get(target, [])
    return (
        sorted(
            candidates,
            key=lambda node: (
                0 if node.get("artifact_type") == "method" else 1,
                str(node.get("page_path", "")),
            ),
        )[0]
        if candidates
        else {}
    )


def _candidate_id(source_page: str, relation_type: str, target_object: str) -> str:
    return f"relation:{source_page}:{relation_type}:{target_object}"


def build_relation_feature_packages(graph: dict[str, Any]) -> list[dict[str, Any]]:
    nodes = [node for node in graph.get("nodes", []) if isinstance(node, dict)]
    edges = [edge for edge in graph.get("edges", []) if isinstance(edge, dict)]
    by_page = _nodes_by_page(nodes)
    by_object = _nodes_by_object(nodes)
    fanout = Counter(str(edge.get("source_page_path") or "") for edge in edges)

    packages: list[dict[str, Any]] = []
    for edge in edges:
        source_page = str(edge.get("source_page_path") or "").strip()
        relation_type = str(edge.get("relation_type") or "").strip()
        target = str(edge.get("target") or "").strip()
        if not source_page or not relation_type or not target:
            continue

        source_node = by_page.get(source_page, {})
        target_node = _target_node(target, by_page, by_object)
        source_object = str(source_node.get("canonical_object") or source_page)
        target_object = str(target_node.get("canonical_object") or target)
        source_layer = str(source_node.get("source_layer") or "unknown")
        target_layer = str(target_node.get("source_layer") or "unknown")
        evidence_refs = [source_page]
        target_page = str(target_node.get("page_path") or "")
        evidence_refs.append(target_page or target)

        packages.append(
            {
                "candidate_id": _candidate_id(source_page, relation_type, target_object),
                "source_page": source_page,
                "source_object": source_object,
                "relation_type": relation_type,
                "target_object": target_object,
                "source_layer": source_layer,
                "target_layer": target_layer,
                "evidence_refs": evidence_refs,
                "structural_features": {
                    "cross_layer": source_layer != target_layer,
                    "has_spec_support": "openspec/specs" in {source_layer, target_layer},
                    "has_adr_support": "wiki/adr" in {source_layer, target_layer},
                    "fanout_count": fanout[source_page],
                    "mechanical_relation": relation_type in MECHANICAL_RELATION_TYPES,
                },
            }
        )

    return packages


def _review_for(candidate_id: str, reviews: dict[str, Any] | None) -> dict[str, Any]:
    if not reviews:
        return {}
    review = reviews.get(candidate_id, {})
    return review if isinstance(review, dict) else {}


def _final_admission(package: dict[str, Any], review: dict[str, Any]) -> str:
    requested = str(review.get("admission") or review.get("moc_admission") or "").strip()
    temperature = review.get("temperature")
    high_temperature = isinstance(temperature, int) and temperature >= 80
    mechanical = bool(package.get("structural_features", {}).get("mechanical_relation"))

    if requested in ADMIT_DECISIONS and high_temperature:
        return requested
    if mechanical:
        return "block"
    return requested if requested in {"needs_review", "block"} else "needs_review"


def build_temperature_clue_board(
    packages: list[dict[str, Any]],
    reviews: dict[str, Any] | None = None,
) -> dict[str, Any]:
    windows: list[dict[str, Any]] = []

    for package in packages:
        candidate_id = str(package["candidate_id"])
        review = _review_for(candidate_id, reviews)
        temperature = review.get("temperature")
        admission = _final_admission(package, review)
        window = {
            "candidate_id": candidate_id,
            "relation_type": package["relation_type"],
            "source_page": package["source_page"],
            "source_object": package["source_object"],
            "target_object": package["target_object"],
            "evidence_refs": package["evidence_refs"],
            "structural_features": package["structural_features"],
            "temperature": temperature if isinstance(temperature, int) else None,
            "temperature_band": temperature_band(temperature) if isinstance(temperature, int) else None,
            "admission": admission,
            "rationale": str(review.get("rationale") or ""),
            "reviewer": review.get("reviewer"),
            "reviewed_at": review.get("reviewed_at"),
        }
        windows.append(window)

    admitted_count = sum(
        1
        for window in windows
        if window["admission"] in ADMIT_DECISIONS
        and isinstance(window["temperature"], int)
        and window["temperature"] >= 80
    )
    blocked_count = sum(1 for window in windows if window["admission"] == "block")
    review_needed_count = sum(1 for window in windows if window["admission"] == "needs_review")

    return {
        "summary": {
            "window_count": len(windows),
            "admitted_count": admitted_count,
            "blocked_count": blocked_count,
            "review_needed_count": review_needed_count,
        },
        "windows": windows,
    }


def _is_admitted(window: dict[str, Any]) -> bool:
    return (
        window.get("admission") in ADMIT_DECISIONS
        and isinstance(window.get("temperature"), int)
        and int(window["temperature"]) >= 80
    )


def build_moc_admission_plan(board: dict[str, Any]) -> dict[str, Any]:
    windows = [window for window in board.get("windows", []) if isinstance(window, dict)]
    admitted_objects = sorted(
        {
            str(window.get("target_object"))
            for window in windows
            if _is_admitted(window) and str(window.get("target_object") or "").strip()
        }
    )
    admitted_relations = sorted(
        {
            str(window.get("relation_type"))
            for window in windows
            if _is_admitted(window) and window.get("admission") == "admit_relation"
        }
    )
    blocked_relations = sorted(
        {
            str(window.get("relation_type"))
            for window in windows
            if not _is_admitted(window) and window.get("admission") == "block"
        }
    )
    review_needed_relations = sorted(
        {
            str(window.get("relation_type"))
            for window in windows
            if not _is_admitted(window) and window.get("admission") == "needs_review"
        }
    )

    return {
        "summary": dict(board.get("summary", {})),
        "admitted_objects": admitted_objects,
        "admitted_relations": admitted_relations,
        "blocked_relations": blocked_relations,
        "review_needed_relations": review_needed_relations,
        "windows": windows,
    }
