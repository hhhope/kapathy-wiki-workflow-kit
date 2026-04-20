# Evaluation

## Pressure Scenarios

1. A semantic skill change includes `evaluation.md`, but the file only has descriptive before/after headings and no explicit pressure-test sections.
2. A semantic skill change includes explicit local pressure-test headings and should pass the repo gate without requiring multi-end proof.
3. A recently completed skill-governance change must be rewritten from descriptive evidence into explicit `Pressure Scenarios / RED Baseline / GREEN Result`.

## RED Baseline

- Before this change, the repo health check accepted the old section contract:
  - `Baseline Scenarios`
  - `Before Results`
  - `After Results`
  - `Residual Risks`
- That meant a skill change could pass with descriptive evidence and no explicit pressure-test framing.
- The failing unit test captured this gap by expecting:
  - old-format evidence to fail
  - new-format evidence to pass
  and seeing the opposite result under the old health-check rule.

## GREEN Result

- The repo health check now requires:
  - `Pressure Scenarios`
  - `RED Baseline`
  - `GREEN Result`
  - `Residual Risks`
- The tests now distinguish the two cases correctly:
  - old descriptive headings fail
  - explicit local pressure-test headings pass
- `harden-skill-authoring-contract` and `add-principle-skills-layer` were backfilled to the new format, so the repo remains green under the stronger gate.

## Residual Risks

- This change strengthens the evidence format, not the realism of every scenario. A weak pressure scenario can still be written badly.
- Multi-session or rollout-level validation remains optional follow-up proof and is not enforced by this gate.
