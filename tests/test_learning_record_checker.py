from __future__ import annotations

import tempfile
from pathlib import Path

from scripts.check_learning_record import check_learning_record


def write_yaml(text: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="learning-record-")) / "record.yaml"
    tmp.write_text(text, encoding="utf-8")
    return tmp


def test_l2_record_requires_core_fields() -> None:
    record = write_yaml(
        """
learning_level: L2
learning_type: Technical
methods_used:
  - triangulation
input_inventory:
  - repo README
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1]
value_judgment: Reusable controller pattern.
proof_boundary: Local architecture fit still needs implementation replay.
"""
    )

    assert check_learning_record(record) == []


def test_l3_record_requires_reconstruction_and_output_plan() -> None:
    record = write_yaml(
        """
learning_level: L3
learning_type: Company Case
methods_used:
  - case study research
  - process tracing
  - triangulation
input_inventory:
  - annual letters
research_reconstruction_model:
  object: Stripe
  time_span: "2010-2026"
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1, S2]
value_judgment: Payment infrastructure capability accumulated over phases.
output_transformation_plan:
  article_intent_contract: Explain the company path.
proof_boundary: Future judgment remains bounded by available public sources.
"""
    )

    assert check_learning_record(record) == []


def test_l3_record_without_proof_boundary_fails() -> None:
    record = write_yaml(
        """
learning_level: L3
learning_type: Company Case
methods_used:
  - process tracing
input_inventory:
  - annual letters
research_reconstruction_model:
  object: Stripe
evidence_matrix:
  - claim_id: C1
    status: promoted
    evidence_ids: [S1]
value_judgment: Capability accumulated.
output_transformation_plan:
  article_intent_contract: Explain the path.
"""
    )

    messages = check_learning_record(record)

    assert "missing required field: proof_boundary" in messages
