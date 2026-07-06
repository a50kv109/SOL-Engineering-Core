# SOL Topology: System Structure and Causality

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Define rules for connecting SOL primitives into valid systems

---

## Overview

Topology governs how primitives can be legally connected, ensuring that systems remain physically realizable and causally consistent. Invalid topologies produce "ghost primitives" or causally impossible systems.

---

## Fundamental Principles

### 1. Causality Principle
**Rule:** FLOW always originates from SOURCE (directly or through STORAGE).

**Invalid:** `[FLOW] → [SOURCE]` (flow cannot initiate from downstream)

**Valid:** `[SOURCE] → [FLOW] → ... → [STORAGE] → [FLOW]` (storage can release flow)

---

### 2. Energy Conservation Principle
**Rule:** Energy entering a system must either be stored, dissipated, or flow out.

**Formula:**
```
INPUT_ENERGY = STORED_DELTA + DISSIPATED + OUTPUT_WORK
```

**Check:** At each node, account for all energy.

---

### 3. Constraint Dominion Principle
**Rule:** A CONSTRAINT cannot change without external intervention (FEEDBACK or new SOURCE).

**Example:** 
- A bearing gap is fixed until explicitly modified
- Cannot have `[CONSTRAINT] → [TRANSFORM] → [CONSTRAINT]` (self-modification forbidden)

---

### 4. Immutability of Primitives
**Rule:** The 7 core primitives cannot be subdivided or redefined within their layer.

**Valid:** Extensions in domain packs (e.g., `[CONSTRAINT:BEARING:RADIAL]`)  
**Invalid:** New primitive types in SOL-Core

---

## Topology Patterns

### Pattern 1: Linear Flow (Open System)

```
[SOURCE] → [FLOW] → [CONSTRAINT] → [STORAGE] → [DISSIPATE]
```

**Characteristics:**
- No feedback
- System reaches equilibrium when SOURCE stops
- Unidirectional causality

**Examples:**
- Water flowing through pipe to tank
- Electricity charging capacitor
- Impact force in collision

---

### Pattern 2: Circular Flow (Closed System)

```
      ┌─────────────────┐
      ↓                 │
[SOURCE] → [FLOW] → [STORAGE]
                      ↓
                [DISSIPATE]
```

**Characteristics:**
- Circular causality
- STORAGE maintains state between cycles
- Common in mechanical oscillations

**Examples:**
- Rotating shaft in bearing
- AC electrical current
- Pendulum motion

---

### Pattern 3: Regulated System (with FEEDBACK)

```
[SOURCE] → [FLOW] → [CONSTRAINT]
                        ↓
                    [STORAGE]
                        ↓
                    [FEEDBACK]
                        ↑
              (controls SOURCE or CONSTRAINT)
```

**Characteristics:**
- STORAGE state fed back to regulate SOURCE or CONSTRAINT
- Enables stability and control
- Can oscillate if feedback delay too high

**Examples:**
- Thermostat maintaining temperature
- Voltage regulator
- PID controller

---

### Pattern 4: Buffered System (with STORAGE)

```
[SOURCE₁] → [STORAGE]  ← decoupling
                   ↓
              [FLOW] → [CONSTRAINT] → [DISSIPATE]
              (controlled by OUTPUT demand)
```

**Characteristics:**
- INPUT and OUTPUT rates can differ
- STORAGE acts as shock absorber
- Failure mode: Overflow/Underflow

---

### Pattern 5: Cascade (Multiple Stages)

```
[SOURCE] → [FLOW] → [TRANSFORM]₁ → [CONSTRAINT]₁ 
               → [FLOW] → [TRANSFORM]₂ → [CONSTRAINT]₂
               → [FLOW] → [CONSTRAINT]ₙ → [DISSIPATE]
```

**Characteristics:**
- Multiple sequential transformations
- Each stage can introduce impedance mismatch
- Failure propagates downstream

**Examples:**
- Gear train
- Signal amplifier chain
- Multi-joint kinetic chain

---

## Hierarchy Rules

### Node (Atomic)
A single SOL primitive with one INPUT and one OUTPUT slot.

```
INPUT ──→ [PRIMITIVE] ──→ OUTPUT
```

### Branch (Two-way Node)
A primitive with decision logic; primitive selects output path based on state.

```
           ┌──→ [PATH_A]
INPUT ──→ [BRANCH] 
           └──→ [PATH_B]
```

**Rules:**
- At most one output path active at time `t`
- CONSTRAINT defines branch logic
- Used in conditional flows

---

### Cluster (Grouped Nodes)
Multiple connected primitives forming a subsystem.

```
┌─────────────────────────┐
│  [SOURCE] → [STORAGE]   │
│           ↓             │
│      [FEEDBACK]         │
└─────────────────────────┘
```

**Rules:**
- Has one external INPUT (SOURCE) and one OUTPUT (FLOW)
- Can be treated as black-box NODE in higher-level topology
- Enables hierarchical design

---

### System (Complete Graph)
All clusters connected without orphan nodes.

```
[SYSTEM] = {CLUSTER₁, CLUSTER₂, ..., LINK}

where LINK ∈ [FLOW]ₛ between clusters
```

---

## Conflict Resolution

### Conflict Type 1: Impedance Mismatch
**Symptom:** [FLOW] amplitude incompatible with [CONSTRAINT]

**Solution:** Insert [TRANSFORM] to match impedance

```
[FLOW:HIGH] → [TRANSFORM:REDUCE] → [CONSTRAINT:TIGHT] → OK
```

---

### Conflict Type 2: Path Fragmentation
**Symptom:** [FLOW] splits into incompatible branches

**Solution:** Use [CONSTRAINT] to route flow properly

```
BEFORE (Invalid):
[SOURCE] → [FLOW] → [BRANCH A & B simultaneously]

AFTER (Valid):
[SOURCE] → [FLOW] → [CONSTRAINT:SELECT_PATH] → [BRANCH A or B]
```

---

### Conflict Type 3: Causal Loop (Positive Feedback Instability)
**Symptom:** Unregulated positive feedback → runaway

**Solution:** Add dissipation or negative feedback

```
BEFORE (Unstable):
[SOURCE] → [AMPLIFIER:×2] ↺ [POSITIVE_FEEDBACK]

AFTER (Stable):
[SOURCE] → [AMPLIFIER:×2] ↺ [NEGATIVE_FEEDBACK] → OK
```

---

## Verification Rules

### Rule V1: No Orphan Flows
Every [FLOW] must trace back to a [SOURCE] or [STORAGE].

### Rule V2: No Ghost Primitives
Every primitive must have at least one INPUT or one OUTPUT (except SOURCE which has no input).

### Rule V3: Energy Conservation
For every node, `INPUT_ENERGY ≤ OUTPUT_ENERGY + STORED_DELTA + DISSIPATED`.

### Rule V4: Causal Completeness
Every [STORAGE] must have a path to [DISSIPATE] (directly or through FEEDBACK loop).

### Rule V5: Constraint Integrity
No [CONSTRAINT] may be violated without explicit external modification.

---

## Visualization Rules

### Graph Representation

**Nodes:** Primitives  
**Edges:** [FLOW] connections  
**Arrows:** Direction of causality  
**Backarrow:** [FEEDBACK] return

```
Standard:    ●──→○──→□

Feedback:    ●──→○ ↺ (backarrow to modify SOURCE or CONSTRAINT)
```

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Primitive definitions
- `docs/02_ONTOLOGY.md` — Semantic concepts
- `docs/05_PATTERNS.md` — System archetypes
- `docs/06_SYMPHONY.md` — Composition rules

**Used By:** All topology-dependent analyses

---

**Status:** Stable  
**Last Updated:** 2026-06-04
