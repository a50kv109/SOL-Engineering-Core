# SOL Ontology: Semantic Layers

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Map engineering concepts to SOL-Core primitives

---

## Overview

The Ontology layer bridges natural language engineering concepts to the SOL-Core primitives. It provides the semantic framework for understanding how real-world engineering maps to the 7 irreducible primitives.

---

## Layer 1: Conceptual Entities

These are high-level engineering concepts that decompose into SOL primitives:

### OBJECT
**Definition:** A discrete structural entity with defined boundaries.

**Maps To:** `[STORAGE] + [CONSTRAINT]`  
**Why:** Objects maintain state (STORAGE) and enforce geometric/topological limits (CONSTRAINT).

**Examples:**
- Bearing assembly (mechanical)
- Fluid tank (hydraulic)
- Processor core (computational)
- Tissue (biological)

---

### STATE
**Definition:** The configuration of an OBJECT at time `t`.

**Maps To:** Content of `[STORAGE]`  
**Why:** STATE is the instantaneous value held in STORAGE at a given moment.

**Examples:**
- Bearing clearance (mm)
- Tank fluid level (liters)
- Processor cache (bytes)
- Muscle tension (Newtons)

---

### PROCESS
**Definition:** A causal chain of transformations applied to OBJECTs over time.

**Maps To:** `[SOURCE] → [FLOW] → [TRANSFORM]* → [STORAGE]`  
**Why:** A process is a sequence of primitives that changes STATE.

**Examples:**
- Oil circulation through bearing (fluid flow)
- Current through circuit (electrical flow)
- Force transmission through joint (mechanical propagation)

---

### EVENT
**Definition:** A singular, discrete change in STATE.

**Maps To:** `[FLOW] → [STORAGE]` (instantaneous state transition)  
**Why:** Events are atomic state changes within a PROCESS.

**Examples:**
- Bearing contact switches to slip (mechanical EVENT)
- Capacitor charges to threshold (electrical EVENT)
- Nerve fires (biological EVENT)

---

### BOUNDARY
**Definition:** The interface between an OBJECT and its external environment.

**Maps To:** `[CONSTRAINT]` positioned at system edges  
**Why:** BOUNDARY defines what flows in/out and what is shielded.

**Examples:**
- Bearing seal (hydraulic BOUNDARY)
- Circuit insulation (electrical BOUNDARY)
- Cell membrane (biological BOUNDARY)

---

### LINK
**Definition:** A dependency or connection between two OBJECTs.

**Maps To:** `[FLOW]` between two `[STORAGE] + [CONSTRAINT]` pairs  
**Why:** LINKs are where FLOW propagates between distinct OBJECTs.

**Examples:**
- Oil channel connecting bearing to pump (hydraulic LINK)
- Wire connecting components (electrical LINK)
- Skeletal joint (mechanical LINK)

---

### SIGNAL
**Definition:** Information-carrying FLOW with negligible energy expenditure.

**Maps To:** Low-energy `[FLOW]`  
**Why:** SIGNALs propagate information without doing mechanical work.

**Examples:**
- Sensor reading (measurement SIGNAL)
- Control command (command SIGNAL)
- Neural impulse (biological SIGNAL)

---

## Layer 2: System Archetypes

These are recurring topological patterns in engineering systems:

### REGULATOR
**Pattern:** `[SOURCE] → [TRANSFORM] → [STORAGE] ↺ [FEEDBACK]`

**Purpose:** Maintain a set point in STORAGE by modifying SOURCE.

**Examples:**
- Thermostat (temperature regulation)
- Voltage regulator (electrical)
- Cruise control (mechanical)
- Homeostasis (biological)

---

### BUFFER
**Pattern:** `[SOURCE] → [STORAGE] → [FLOW]`

**Purpose:** Decouple input rate from output rate.

**Examples:**
- Fluid tank (hydraulic buffering)
- Capacitor (electrical buffering)
- Queue (informational buffering)

---

### CASCADE
**Pattern:** `[SOURCE] → [FLOW]₁ → [CONSTRAINT]₁ → [FLOW]₂ → [CONSTRAINT]₂ → ...`

**Purpose:** Serial transmission through multiple stages.

**Examples:**
- Gear train (mechanical cascade)
- Amplifier stages (electrical cascade)
- Kynetic chain (biological cascade)

---

### FEEDBACK_LOOP
**Pattern:** `[STORAGE] → [FEEDBACK] → [SOURCE]` or `[FEEDBACK] → [CONSTRAINT]`

**Purpose:** Enable self-regulation (negative) or amplification (positive).

**Examples:**
- PID controller (control feedback)
- Amplifier with feedback (electrical)
- Immune response (biological)

---

## Layer 3: Diagnostic Concepts

These concepts help identify system faults and anomalies:

### TENSION_VECTOR `[TEN]`
**Definition:** Mismatch between [FLOW] direction and [CONSTRAINT] direction.

**Calculated As:** `TEN = |FLOW × CONSTRAINT| / (|FLOW| · |CONSTRAINT|)`

**Interpretation:**
- TEN = 0: Perfect alignment (no conflict)
- TEN = 1: Maximum misalignment (critical conflict)
- TEN > 0.5: Anomaly detection threshold

**Physical Meaning:** Measure of "fighting forces"; indicates stress accumulation.

---

### COMPENSATION_PRESSURE `[COMP]`
**Definition:** Hidden energy cost of maintaining stability when CONSTRAINT is violated.

**Manifestation:** 
- System must expend extra energy from SOURCE
- DISSIPATE increases to absorb the mismatch
- Leads to accelerated wear

**Detection:** Increased DISSIPATE with constant SOURCE → COMP active

---

### DISSIPATION_INDEX `[TDI]`
**Definition:** Tensor Divergence Index; normalized measure of dissipative state.

**Formula:** `TDI = DISSIPATE_MEASURED / DISSIPATE_NOMINAL`

**Interpretation:**
- TDI = 1: Normal operation
- TDI > 1: Accelerated wear detected
- TDI >> 1: Critical failure imminent

---

## Layer 4: Domain Mappings

Each engineering domain uses the ontology differently:

### SOL-MECH (Mechanical Engineering)

| Ontology | SOL-Core | Mechanical |
|----------|----------|-----------|
| OBJECT | [STORAGE]+[CONSTRAINT] | Component |
| FLOW | [FLOW] | Force/Torque |
| STATE | [STORAGE] | Position/Velocity |
| PROCESS | [SOURCE]→[FLOW]→[STORAGE] | Motion sequence |

### SOL-CAD (Geometric Design)

| Ontology | SOL-Core | CAD |
|----------|----------|-----|
| OBJECT | [CONSTRAINT] | Face/Edge/Vertex |
| FLOW | [FLOW] | Load path |
| LINK | [FLOW] | Connectivity |
| BOUNDARY | [CONSTRAINT] | Surface normal |

### SOL-BIO (Biomechanical)

| Ontology | SOL-Core | Biological |
|----------|----------|-----------|
| OBJECT | [STORAGE]+[CONSTRAINT] | Muscle/Joint |
| FLOW | [FLOW] | Force propagation |
| FEEDBACK | [FEEDBACK] | Proprioception |
| DISSIPATE | [DISSIPATE] | Metabolic cost |

---

## Composition Hierarchy

```
Level 0 (Atomic):     [SOURCE], [FLOW], [CONSTRAINT], [STORAGE], [DISSIPATE], [TRANSFORM], [FEEDBACK]
                      ↓
Level 1 (Entities):   OBJECT, STATE, PROCESS, EVENT, BOUNDARY, LINK, SIGNAL
                      ↓
Level 2 (Patterns):   REGULATOR, BUFFER, CASCADE, FEEDBACK_LOOP
                      ↓
Level 3 (Diagnostics): TENSION_VECTOR, COMPENSATION_PRESSURE, DISSIPATION_INDEX
                      ↓
Level 4 (Domains):    SOL-MECH, SOL-CAD, SOL-BIO, SOL-AI
```

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Foundation
- `docs/02_TOPOLOGY.md` — How entities connect
- `docs/04_DOMAIN_PACKS.md` — Domain-specific ontologies
- `docs/05_PATTERNS.md` — System archetypes

**Used By:** All domain-specific extensions

---

**Status:** Stable  
**Last Updated:** 2026-06-04
