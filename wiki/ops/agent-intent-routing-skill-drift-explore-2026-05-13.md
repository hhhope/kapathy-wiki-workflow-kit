---
title: Agent Intent Routing Skill Drift Explore
layer: ops
domain: none
ops_area: workflow-trace
canonical_object: agent-intent-routing-skill-drift
artifact_type: explore-trace
---

# Agent Intent Routing Skill Drift Explore

## Trigger

The user questioned whether the recent Agent Intent Routing work drifted because
skill-writing constraints were not followed, or because the existing constraints
were unclear.

## Scope

This is an OpenSpec explore trace only. It records the live investigation target
before further exploration continues.

## Current Question

- Did the skill edit fail to follow the existing skill-authoring constraints?
- Or were the constraints insufficiently clear about how `Agent Intent Routing`
  should relate to `High-Frequency Skills`?
- Should the design be compressed so the routing preflight does not duplicate
  the skill index?

## Boundary

No behavior asset changes are made from this trace. Further changes require a
separate implementation step or a change adjustment.
