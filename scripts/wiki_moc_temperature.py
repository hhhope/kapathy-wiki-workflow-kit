from __future__ import annotations

from collections import Counter
from typing import Any


MECHANICAL_RELATION_TYPES = {"derived_from", "related_objects"}
ADMIT_DECISION = "admit"
VALID_MOC_ADMISSIONS = {"admit", "block", "needs_review"}


def temperature_band(value: int) -> str:
    if value >= 80:
        return "strong"
    if value >= 60:
        return "supporting"
    if value >= 40:
        return "weak"
    return "noise"


def _valid_temperature(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    if value < 0 or value > 100:
        return None
    return value


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
    raw_nodes = graph.get("nodes", [])
    raw_edges = graph.get("edges", [])
    nodes = [node for node in raw_nodes if isinstance(node, dict)] if isinstance(raw_nodes, list) else []
    edges = [edge for edge in raw_edges if isinstance(edge, dict)] if isinstance(raw_edges, list) else []
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


def _moc_admission(review: dict[str, Any]) -> str:
    requested = str(review.get("moc_admission") or "").strip()
    return requested if requested in VALID_MOC_ADMISSIONS else "needs_review"


def _window_status(package: dict[str, Any], moc_admission: str, temperature: Any) -> str:
    high_temperature = isinstance(temperature, int) and temperature >= 80
    mechanical = bool(package.get("structural_features", {}).get("mechanical_relation"))

    if moc_admission == ADMIT_DECISION and high_temperature:
        return "admitted"
    if moc_admission == "block" or mechanical:
        return "blocked"
    return "needs_review"


def _compat_admission(status: str, moc_admission: str) -> str:
    if status == "admitted":
        return moc_admission
    if status == "blocked":
        return "block"
    return "needs_review"


def build_temperature_clue_board(
    packages: list[dict[str, Any]],
    reviews: dict[str, Any] | None = None,
) -> dict[str, Any]:
    windows: list[dict[str, Any]] = []

    for package in packages:
        candidate_id = str(package["candidate_id"])
        review = _review_for(candidate_id, reviews)
        temperature = _valid_temperature(review.get("temperature"))
        moc_admission = _moc_admission(review)
        status = _window_status(package, moc_admission, temperature)
        window = {
            "candidate_id": candidate_id,
            "relation_type": package["relation_type"],
            "source_page": package["source_page"],
            "source_object": package["source_object"],
            "target_object": package["target_object"],
            "evidence_refs": package["evidence_refs"],
            "structural_features": package["structural_features"],
            "temperature": temperature,
            "temperature_band": temperature_band(temperature) if temperature is not None else None,
            "status": status,
            "moc_admission": moc_admission,
            "admission": _compat_admission(status, moc_admission),
            "rationale": str(review.get("rationale") or ""),
            "reviewer": review.get("reviewer"),
            "reviewed_at": review.get("reviewed_at"),
        }
        windows.append(window)

    admitted_count = sum(
        1 for window in windows if window["status"] == "admitted"
    )
    blocked_count = sum(1 for window in windows if window["status"] == "blocked")
    review_needed_count = sum(1 for window in windows if window["status"] == "needs_review")
    counts = {
        "admitted": admitted_count,
        "blocked": blocked_count,
        "needs_review": review_needed_count,
        "total": len(windows),
        "window_count": len(windows),
        "admitted_count": admitted_count,
        "blocked_count": blocked_count,
        "review_needed_count": review_needed_count,
    }

    return {
        "summary": counts,
        "counts": counts,
        "windows": windows,
        "clue_windows": windows,
    }


def _is_admitted(window: dict[str, Any]) -> bool:
    return window.get("status") == "admitted"


def build_moc_admission_plan(board: dict[str, Any]) -> dict[str, Any]:
    windows = [
        window
        for window in board.get("clue_windows", board.get("windows", []))
        if isinstance(window, dict)
    ]
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
            if _is_admitted(window)
        }
    )
    blocked_relations = sorted(
        {
            str(window.get("relation_type"))
            for window in windows
            if not _is_admitted(window) and window.get("status") == "blocked"
        }
    )
    review_needed_relations = sorted(
        {
            str(window.get("relation_type"))
            for window in windows
            if not _is_admitted(window) and window.get("status") == "needs_review"
        }
    )
    counts = dict(board.get("counts", board.get("summary", {})))

    return {
        "summary": counts,
        "counts": counts,
        "admitted_objects": admitted_objects,
        "admitted_relations": admitted_relations,
        "blocked_relations": blocked_relations,
        "review_needed_relations": review_needed_relations,
        "windows": windows,
        "clue_windows": windows,
    }
