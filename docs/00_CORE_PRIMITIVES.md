# SOL-Core: Canonical Primitives

**Status:** Canonical  
**Version:** v7.0  
**Last Updated:** 2026-06-04  
**Purpose:** Irreducible foundation of SOL semantic system

---

## Overview

The SOL-Core consists of **7 irreducible primitives**. Any engineering system—mechanical, electrical, biological, or informational—can be decomposed into these primitives without loss of causal information.

These primitives are **immutable**. No domain pack may redefine them. All extensions reference these definitions.

---

## Canonical Primitives

### 1. SOURCE `●`

**Definition:** The initiation point of energy, information, or matter flow.

**Characteristics:**
- Generates or introduces potential (pressure, voltage, signal, kinetic energy)
- Initiates all causal chains
- Has **no inputs** in the primitive model (inputs are external boundary conditions)

**Physical Manifestations:**
- Pump inlet (hydraulic)
- Power supply (electrical)
- Muscle contraction initiation (biological)
- Database query initiator (informational)

**Failure Mode:** SOURCE failure = No initiation possible; system becomes inert.

**Symbol:** `●`  
**Notation:** `[SOURCE]` or `[SRC]`

---

### 2. FLOW `→`

**Definition:** The directed transmission of energy, matter, or signal between nodes.

**Characteristics:**
- Vector quantity: has magnitude and direction
- Can be linear, rotational, or informational
- Carries causality through the system
- Energy is lost only when passing through `[DISSIPATE]` or `[CONSTRAINT]`

**Physical Manifestations:**
- Fluid velocity through pipe (hydraulic)
- Electric current through conductor (electrical)
- Force transmission through joint (mechanical)
- Neural impulse propagation (biological)
- Data packet routing (informational)

**Failure Mode:** FLOW interruption = Chain breaks; no propagation downstream.

**Symbol:** `→`  
**Notation:** `[FLOW]` or `[FLW]`

---

### 3. CONSTRAINT `⚙`

**Definition:** A boundary, rule, or physical limit that modifies the path or magnitude of FLOW without storing energy.

**Characteristics:**
- Reduces degrees of freedom (DOF)
- Introduces resistance without dissipating energy (ideal case)
- Can be rigid (kinematic joint) or flexible (filter)
- Defines topology of system

**Physical Manifestations:**
- Valve opening (hydraulic control)
- Resistor (electrical)
- Kinematic joint (mechanical)
- Synaptic cleft transmission delay (biological)
- Routing rules (informational)

**Failure Mode:** CONSTRAINT violation = Uncontrolled FLOW; system cascades to failure.

**Symbol:** `⚙`  
**Notation:** `[CONSTRAINT]` or `[CON]`

---

### 4. STORAGE `□`

**Definition:** Accumulation of state over time; integration of FLOW into potential energy.

**Characteristics:**
- Integrates FLOW: `dE/dt = FLOW - DISSIPATE`
- Holds state between discrete time steps
- Enables delay and buffering
- Can release stored state as FLOW

**Physical Manifestations:**
- Fluid tank (hydraulic)
- Capacitor or inductor (electrical)
- Spring or flywheel (mechanical)
- Short-term memory (biological)
- Cache or queue (informational)

**Failure Mode:** STORAGE overflow/underflow = Loss of state or cascade collapse.

**Symbol:** `□`  
**Notation:** `[STORAGE]` or `[STR]`

---

### 5. DISSIPATE `▽`

**Definition:** Conversion of ordered energy into entropy (heat, noise, wear, data loss).

**Characteristics:**
- Irreversible (does not store energy)
- Converts kinetic/potential energy to thermal or frictional
- All real systems require dissipation
- Accumulates cost to system health

**Physical Manifestations:**
- Friction in bearing (mechanical)
- Joule heating in resistor (electrical)
- Viscous damping (hydraulic)
- Metabolic waste production (biological)
- Packet loss or computation errors (informational)

**Failure Mode:** Insufficient DISSIPATE = Energy accumulation, thermal runaway, system destruction.

**Symbol:** `▽`  
**Notation:** `[DISSIPATE]` or `[DIS]`

---

### 6. TRANSFORM `❖`

**Definition:** Conversion of FLOW characteristics (e.g., impedance, ratio, modality) without storing or dissipating energy.

**Characteristics:**
- Preserves power: `P_in = P_out` (ideal case)
- Changes flow type (e.g., linear → rotational)
- Introduces local impedance matching
- Allows domain transitions

**Physical Manifestations:**
- Gear box (mechanical ratio change)
- Electrical transformer (voltage/current ratio)
- Hydraulic pump (pressure/flow ratio)
- Neural encoding (analog → discrete signal)
- API layer (format transformation)

**Failure Mode:** TRANSFORM mismatch = Impedance discontinuity; FLOW reflection or loss.

**Symbol:** `❖`  
**Notation:** `[TRANSFORM]` or `[TRF]`

---

### 7. FEEDBACK `↺`

**Definition:** Recursive coupling where the state in STORAGE modifies SOURCE behavior to regulate or stabilize the system.

**Characteristics:**
- Closes loops; enables self-regulation
- Reads from STORAGE, writes to SOURCE or CONSTRAINT
- Can be positive (amplification) or negative (regulation)
- Introduces delay and potential for oscillation

**Physical Manifestations:**
- Thermostat PID loop (temperature regulation)
- Speed governor (mechanical)
- Immune system response (biological)
- Neural feedback loops (cognitive)
- Process control systems (industrial)

**Failure Mode:** FEEDBACK failure = Loss of regulation; uncontrolled growth or collapse.

**Symbol:** `↺`  
**Notation:** `[FEEDBACK]` or `[FBK]`

---

## Composition Rules (Law of Conservation)

### Universal Balance Equation

```
[SOURCE] → [FLOW] → [CONSTRAINT] → [STORAGE] ↺ [FEEDBACK]
                          ↓
                    [DISSIPATE]
```

**Energy Balance (Fundamental):**
```
SOURCE_ENERGY = STORED_ENERGY + DISSIPATED_ENERGY + WORK_OUTPUT
```

### Valid Primitive Sequences

✓ `[SOURCE] → [FLOW] → [CONSTRAINT] → [DISSIPATE]`  
✓ `[SOURCE] → [FLOW] → [TRANSFORM] → [STORAGE]`  
✓ `[STORAGE] → [FLOW] → [CONSTRAINT]` (release)  
✓ `[STORAGE] ↺ [FEEDBACK] → [CONSTRAINT]` (regulation)  

### Invalid Sequences

✗ `[DISSIPATE] → [STORAGE]` (No reverse flow)  
✗ `[CONSTRAINT] → [SOURCE]` (Constraints don't initiate)  
✗ `[FLOW]` with no SOURCE or STORAGE source (Orphan flow)  

---

## Extension Rules (Domain Packs)

New primitives are **NOT allowed** in SOL-Core.

Domain-specific extensions must:
1. Reference a core primitive (e.g., `[CONSTRAINT:BEARING]`)
2. Specify the domain (e.g., `[SOL-MECH]`)
3. Not redefine the core primitive

**Example:**
```
[BEARING] ≡ [CONSTRAINT:RADIAL] + [CONSTRAINT:AXIAL] + [DISSIPATE:FRICTION]
```

---

## Symbol Reference

| Primitive | Symbol | Alt | Use In |
|-----------|--------|-----|---------|
| SOURCE | `●` | `🔴` | diagrams |
| FLOW | `→` | `⇒` | causal chains |
| CONSTRAINT | `⚙` | `🔒` | topology |
| STORAGE | `□` | `📦` | buffers |
| DISSIPATE | `▽` | `🔥` | loss nodes |
| TRANSFORM | `❖` | `⚡` | converters |
| FEEDBACK | `↺` | `🔄` | loops |

---

## Cross-References

**Related Documents:**
- `docs/01_ONTOLOGY.md` — Semantic layers built on these primitives
- `docs/02_TOPOLOGY.md` — Rules for connecting primitives
- `docs/03_VISUAL_PRIMITIVES.md` — Visual symbol standardization
- `docs/04_DOMAIN_PACKS.md` — Domain-specific extensions
- `docs/05_PATTERNS.md` — Common primitive compositions

**Related Domains:**
- SOL-MECH: Mechanical systems
- SOL-CAD: Geometric topology
- SOL-AI: Agent reasoning
- SOL-BIO: Biomechanical systems

**Used By:** All other SOL documents

---

**Status:** Canonical (Immutable)  
**Last Verified:** 2026-06-04
