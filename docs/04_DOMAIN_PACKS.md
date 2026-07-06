# SOL Domain Packs: Specialized Extensions

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Domain-specific extensions referencing SOL-Core primitives

---

## Overview

Domain Packs are specializations of SOL for specific engineering disciplines. They extend the core 7 primitives without modifying them, following the constraint: `EXTENSION = CORE_PRIMITIVE + DOMAIN_CONTEXT`.

---

## Pack Structure

Each domain pack follows:

```yaml
Domain: [Name]
Acronym: [SOL-XXX]
Purpose: [Domain focus]
Base Primitives: [Which core primitives are primary]
Extended Concepts: [Domain-specific refinements]
```

---

## SOL-MECH (Mechanical Engineering)

**Purpose:** Mechanical systems analysis, load paths, motion chains

**Extended Primitives:**

| Core | Extension | Meaning |
|------|-----------|----------|
| SOURCE | `[SOURCE:MOTOR]`, `[SOURCE:PRESSURE]` | Rotational or linear energy source |
| FLOW | `[FLOW:ROTATIONAL]`, `[FLOW:LINEAR]`, `[FLOW:TORQUE]` | Motion type classification |
| CONSTRAINT | `[CONSTRAINT:JOINT]`, `[CONSTRAINT:BEARING]`, `[CONSTRAINT:FRICTION]` | Kinematic or resistance limits |
| STORAGE | `[STORAGE:KINETIC]`, `[STORAGE:POTENTIAL]` | Energy buffering types |
| DISSIPATE | `[DISSIPATE:FRICTION]`, `[DISSIPATE:WEAR]`, `[DISSIPATE:HEAT]` | Loss mechanisms |
| TRANSFORM | `[TRANSFORM:GEAR]`, `[TRANSFORM:PULLEY]` | Mechanical ratio changes |
| FEEDBACK | `[FEEDBACK:GOVERNOR]`, `[FEEDBACK:SENSOR]` | Mechanical control loops |

**Example Expression:**
```
[SOURCE:MOTOR] → [FLOW:ROTATIONAL] → [CONSTRAINT:BEARING:RADIAL] 
    → [STORAGE:KINETIC] ↺ [FEEDBACK:GOVERNOR]
```

---

## SOL-CAD (Computer-Aided Design / Topology)

**Purpose:** Geometric topology extraction, constraint mapping, load paths in CAD models

**Extended Primitives:**

| Core | Extension | CAD Equivalent |
|------|-----------|----------------|
| CONSTRAINT | `[CONSTRAINT:PLANAR]`, `[CONSTRAINT:CYLINDRICAL]`, `[CONSTRAINT:SPHERICAL]` | Geometric faces |
| FLOW | `[FLOW:LOAD_PATH]` | Stress propagation through geometry |
| STORAGE | `[STORAGE:VOLUME]`, `[STORAGE:MASS]` | Physical space/properties |
| LINK | `[LINK:TANGENT]`, `[LINK:COINCIDENT]`, `[LINK:CONCENTRIC]` | Geometric relationships |

**Example:** CAD-to-SOL translation
```
CAD Model: Bearing mounted on shaft
    → [CONSTRAINT:CYLINDRICAL] (bore) ↔ [CONSTRAINT:CYLINDRICAL] (shaft)
    → [FLOW:LOAD_PATH] through [STORAGE:VOLUME]
    → [LINK:TANGENT] between surfaces
```

---

## SOL-AI (Agent Reasoning / Symbolic Processing)

**Purpose:** AI-to-AI communication, goal/intent representation, reasoning chains

**Extended Primitives:**

| Core | Extension | AI Equivalent |
|------|-----------|---------------|
| SOURCE | `[SOURCE:GOAL]`, `[SOURCE:QUERY]`, `[SOURCE:INTENT]` | Initial task |
| FLOW | `[FLOW:REASONING]`, `[FLOW:DATA]` | Information propagation |
| CONSTRAINT | `[CONSTRAINT:RULE]`, `[CONSTRAINT:AXIOM]` | Logical boundaries |
| STORAGE | `[STORAGE:STATE]`, `[STORAGE:KNOWLEDGE_BASE]` | Computational memory |
| TRANSFORM | `[TRANSFORM:INFERENCE]`, `[TRANSFORM:TRANSLATION]` | Logical operations |
| FEEDBACK | `[FEEDBACK:VALIDATION]`, `[FEEDBACK:CORRECTION]` | Self-correction loops |

**Example:** Multi-agent agreement
```
AGENT_A.INTENT → [SOURCE:TASK] → [FLOW:REASONING] 
    → [CONSTRAINT:AXIOMS] → [STORAGE:LOCAL_STATE] ↺ [FEEDBACK:VALIDATE]
    → AGREEMENT_SIGNAL
```

---

## SOL-BIO (Biomechanical / Physiological)

**Purpose:** Human/animal movement analysis, injury mechanisms, rehabilitation

**Extended Primitives:**

| Core | Extension | Biological |
|------|-----------|------------|
| SOURCE | `[SOURCE:NEURAL]`, `[SOURCE:MUSCULAR]` | Motor command |
| FLOW | `[FLOW:FORCE]`, `[FLOW:NEURAL_IMPULSE]`, `[FLOW:CIRCULATORY]` | Transmission types |
| CONSTRAINT | `[CONSTRAINT:JOINT]`, `[CONSTRAINT:LIGAMENT]`, `[CONSTRAINT:TISSUE_ELASTICITY]` | Anatomical limits |
| STORAGE | `[STORAGE:POTENTIAL_ENERGY]`, `[STORAGE:FATIGUE]` | Physical state |
| DISSIPATE | `[DISSIPATE:METABOLIC]`, `[DISSIPATE:HEAT]`, `[DISSIPATE:TISSUE_WEAR]` | Biological costs |
| FEEDBACK | `[FEEDBACK:PROPRIOCEPTION]`, `[FEEDBACK:PAIN]` | Sensory loops |

**Example:** Frozen shoulder (adhesive capsulitis)
```
[CONSTRAINT:SHOULDER_CAPSULE] becomes [CONSTRAINT:RIGID]
    → [FLOW:FORCE] blocked
    → [STORAGE:COMPENSATION_LOAD] in trapezius
    → [DISSIPATE:METABOLIC_COST] increases
    → PAIN feedback
```

---

## SOL-HYDR (Hydraulics / Fluid Systems)

**Purpose:** Fluid power systems, pressure/flow networks

**Extended Primitives:**

| Core | Extension | Hydraulic |
|------|-----------|----------|
| SOURCE | `[SOURCE:PUMP]` | Pressure/flow generator |
| FLOW | `[FLOW:PRESSURE]`, `[FLOW:VOLUMETRIC]` | Fluid transmission |
| CONSTRAINT | `[CONSTRAINT:VALVE]`, `[CONSTRAINT:ORIFICE]` | Flow control |
| STORAGE | `[STORAGE:ACCUMULATOR]` | Energy buffering |
| DISSIPATE | `[DISSIPATE:VISCOUS_DRAG]`, `[DISSIPATE:HEAT]` | Fluid losses |

---

## SOL-ELEC (Electrical Systems)

**Purpose:** Circuit analysis, power distribution

**Extended Primitives:**

| Core | Extension | Electrical |
|------|-----------|------------|
| SOURCE | `[SOURCE:VOLTAGE]`, `[SOURCE:CURRENT]` | EMF source |
| FLOW | `[FLOW:CURRENT]` | Electron flow |
| CONSTRAINT | `[CONSTRAINT:RESISTANCE]`, `[CONSTRAINT:IMPEDANCE]` | Ohmic/reactive |
| STORAGE | `[STORAGE:CAPACITIVE]`, `[STORAGE:INDUCTIVE]` | Reactive storage |
| DISSIPATE | `[DISSIPATE:JOULE_HEAT]`, `[DISSIPATE:RADIATION]` | Power loss |
| TRANSFORM | `[TRANSFORM:TRANSFORMER]`, `[TRANSFORM:CONVERTER]` | Impedance matching |

---

## Extension Rules (Mandatory)

### Rule 1: No Redefinition
All extensions MUST reference core primitives.

```
VALID:     [BEARING] ≡ [CONSTRAINT:RADIAL] + [CONSTRAINT:AXIAL] + [DISSIPATE:FRICTION]
INVALID:   [BEARING] = new primitive (forbidden)
```

### Rule 2: Domain Isolation
Domain packs do not interfere with each other.

```
SOL-MECH:BEARING does not conflict with SOL-HYDR:BEARING
They coexist via different [CONSTRAINT] specializations
```

### Rule 3: Reusability
A specialized concept can be used in multiple domains.

```
[FEEDBACK:LOOP] works in MECH, AI, BIO, HYDR
```

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Core definitions
- `docs/01_ONTOLOGY.md` — Semantic mappings
- `docs/05_PATTERNS.md` — System patterns
- `docs/08_CONCORDANCE.md` — Cross-domain index

**Used By:** Domain-specific analysis and specification

---

**Status:** Stable  
**Last Updated:** 2026-06-04