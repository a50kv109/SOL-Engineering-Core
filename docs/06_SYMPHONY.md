# SOL Symphony: Composition & Validation Rules

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Orchestrate primitives into valid, coherent systems

---

## Overview

Symphony defines the "score" for composing SOL primitives into systems. Like a musical symphony, each primitive plays a role, and composition rules ensure the entire system harmonizes without dissonance or collapse.

---

## Fundamental Laws

### Law 1: Conservation of Causality
**Statement:** Every FLOW must originate from SOURCE or STORAGE.

**Verification:**
```
For each [FLOW] node:
  IF source(FLOW) ≠ [SOURCE] AND source(FLOW) ≠ [STORAGE]
  THEN INVALID
```

**Consequence:** No orphan flows; every system is causally complete.

---

### Law 2: Energy Continuity
**Statement:** Energy is conserved at each node.

**Formula:**
```
∑INPUT_ENERGY = ∑OUTPUT_ENERGY + ∑STORED_DELTA + ∑DISSIPATED
```

**At time t:**
```
E_in(t) = E_out(t) + dE_storage/dt + E_dissipated(t)
```

---

### Law 3: Constraint Integrity
**Statement:** CONSTRAINT boundaries cannot be violated without external modification.

**Verification:**
```
For each [CONSTRAINT] node:
  IF FLOW_magnitude > CONSTRAINT_capacity
  THEN require_external_modification OR system_failure
```

---

### Law 4: Feedback Stability
**Statement:** All FEEDBACK loops must have sufficient dissipation to prevent instability.

**Verification:**
```
For each [FEEDBACK] loop:
  gain × delay < critical_threshold OR
  dissipation_present
```

---

## Composition Sequence (How to Build Systems)

### Step 1: Identify SOURCE
**Question:** What initiates the system?

**Answer:** Define [SOURCE] with initial energy/information

**Example:** `[SOURCE:MOTOR:rated_power:10kW]`

---

### Step 2: Identify CONSTRAINT (Topology)
**Question:** What defines the system boundary?

**Answer:** Define primary [CONSTRAINT] nodes

**Example:** `[CONSTRAINT:BEARING:RADIAL_LOAD:5000N]`

---

### Step 3: Define FLOW Path
**Question:** How does energy flow from SOURCE to CONSTRAINT?

**Answer:** Connect SOURCE → FLOW → CONSTRAINT

**Example:** `[SOURCE:MOTOR] → [FLOW:TORQUE] → [CONSTRAINT:BEARING]`

---

### Step 4: Add STORAGE
**Question:** Where is energy accumulated?

**Answer:** Insert [STORAGE] nodes for buffering or accumulation

**Example:** `[SOURCE] → [FLOW] → [STORAGE:FLYWHEEL] → [CONSTRAINT]`

---

### Step 5: Model DISSIPATE
**Question:** Where is energy lost?

**Answer:** Add [DISSIPATE] nodes at loss points

**Example:** `[CONSTRAINT] → [DISSIPATE:FRICTION]`

---

### Step 6: Add FEEDBACK (If Needed)
**Question:** Does the system need regulation?

**Answer:** Close loop via [FEEDBACK] if setpoint control required

**Example:** `[STORAGE] ↺ [FEEDBACK:SENSOR] → [CONSTRAINT]`

---

### Step 7: Validate Entire Graph
**Apply all verification rules** (see below)

---

## Verification Checklist

### Rule V1: No Orphan Primitives
**Check:** Every primitive (except SOURCE) has at least one INPUT.

```python
for primitive in system.nodes:
    if primitive.type ≠ SOURCE:
        assert len(primitive.inputs) > 0, "Orphan: " + primitive.name
```

---

### Rule V2: Energy Balance
**Check:** Energy is conserved at each node.

```python
for node in system.nodes:
    input_energy = sum(e.power for e in node.inputs)
    output_energy = sum(e.power for e in node.outputs)
    storage_delta = node.storage.power_accumulation if node.type == STORAGE else 0
    dissipated = node.dissipation if node.type == DISSIPATE else 0
    
    assert input_energy ≥ output_energy + storage_delta + dissipated
```

---

### Rule V3: Causality
**Check:** All FLOW nodes trace back to SOURCE or STORAGE.

```python
def trace_to_source(node, visited=set()):
    if node in visited:
        return False  # Cycle without SOURCE
    visited.add(node)
    if node.type == SOURCE or node.type == STORAGE:
        return True
    for input_node in node.inputs:
        if trace_to_source(input_node, visited):
            return True
    return False

for flow_node in system.flows:
    assert trace_to_source(flow_node)
```

---

### Rule V4: Feedback Closure
**Check:** FEEDBACK nodes connect STORAGE back to SOURCE or CONSTRAINT.

```python
for feedback_node in system.feedbacks:
    assert feedback_node.source.type in [STORAGE]
    assert feedback_node.target.type in [SOURCE, CONSTRAINT]
```

---

### Rule V5: No Circular Constraints
**Check:** Constraints cannot modify each other without external intervention.

```python
for constraint in system.constraints:
    for path in constraint.outputs:
        assert path.target.type ≠ CONSTRAINT or \
               path.has_external_source()  # New SOURCE or FEEDBACK
```

---

## Valid Patterns (Pre-Validated Compositions)

These patterns are pre-verified and safe to use:

✓ `[SOURCE] → [FLOW] → [CONSTRAINT]`  
✓ `[SOURCE] → [FLOW] → [STORAGE]`  
✓ `[STORAGE] → [FLOW] → [CONSTRAINT]`  
✓ `[SOURCE] → [FLOW] → [TRANSFORM] → [CONSTRAINT]`  
✓ `[FLOW] → [CONSTRAINT] → [DISSIPATE]`  
✓ `[STORAGE] ↺ [FEEDBACK] → [CONSTRAINT]`  
✓ `[SOURCE] → [FLOW] → [BUFFER] → [FLOW] → [CONSTRAINT]`  

---

## Invalid Patterns (To Reject)

✗ `[DISSIPATE] → [STORAGE]` (entropy cannot decrease)  
✗ `[CONSTRAINT] → [SOURCE]` (constraints don't initiate)  
✗ `[FLOW]` with no SOURCE (orphan)  
✗ Unregulated positive FEEDBACK (runaway)  
✗ `[STORAGE] → [STORAGE] → ...` (chain without output)  

---

## Reconciliation Algorithm

When composing new systems:

```
1. Define SOURCE nodes
2. Define CONSTRAINT nodes (topology skeleton)
3. Connect SOURCE → CONSTRAINT via FLOW paths
4. Identify loss points, add DISSIPATE
5. Identify buffering needs, add STORAGE
6. Verify energy balance at each node
7. IF regulation needed: Add FEEDBACK
8. Run full verification suite
9. IF FAIL: Diagnose violation and remediate
```

---

## Diagnostic Questions (For Invalid Systems)

**Q: Flow trace stops before SOURCE?**  
A: Add missing STORAGE or reconnect to valid SOURCE

**Q: Energy exceeds constraints?**  
A: Add TRANSFORM to reduce or CONSTRAINT to limit

**Q: System oscillates?**  
A: Add DISSIPATE damping or reduce FEEDBACK gain

**Q: Orphan STORAGE node?**  
A: Connect to output path or remove

**Q: Circular CONSTRAINT dependency?**  
A: Add external FEEDBACK or break cycle

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Primitive definitions
- `docs/02_TOPOLOGY.md` — Connection rules
- `docs/05_PATTERNS.md` — Pre-validated compositions

**Used By:** System validation and design verification

---

**Status:** Stable  
**Last Updated:** 2026-06-04