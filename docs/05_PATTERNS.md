# SOL Patterns: System Archetypes

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Canonical system compositions combining SOL primitives

---

## Overview

Patterns are proven topological compositions of SOL primitives that solve recurring engineering problems. They enable code reuse and architectural understanding across domains.

---

## Pattern Catalog

### Pattern 1: REGULATOR

**Topology:**
```
[SOURCE] → [TRANSFORM] → [STORAGE] ↺ [FEEDBACK] → [CONSTRAINT]
```

**Purpose:** Maintain a set point in STORAGE by feedback regulation

**Characteristics:**
- Reads from STORAGE
- Feedback modulates SOURCE or CONSTRAINT
- Enables stability and setpoint tracking
- Can oscillate if feedback delay too high

**Examples:**
- Thermostat (temperature setpoint)
- Voltage regulator (constant voltage)
- Cruise control (speed setpoint)
- Homeostasis (biological parameter maintenance)

**Failure Modes:**
- Loss of feedback → runaway
- Excessive feedback gain → oscillation
- Dead band too wide → accuracy loss

---

### Pattern 2: BUFFER

**Topology:**
```
[SOURCE:INPUT] → [STORAGE] → [CONSTRAINT] → [FLOW:OUTPUT]
```

**Purpose:** Decouple input and output rates

**Characteristics:**
- STORAGE accumulates from SOURCE
- OUTPUT demand independent of INPUT rate
- Acts as shock absorber
- Smooths transients

**Examples:**
- Fluid tank (hydraulic decoupling)
- Capacitor (electrical buffering)
- Queue (data buffering)
- Muscle (mechanical energy storage)

**Failure Modes:**
- Overflow (STORAGE full)
- Underflow (STORAGE empty)
- Rate mismatch too severe

---

### Pattern 3: CASCADE

**Topology:**
```
[SOURCE] → [TRANSFORM:1] → [CONSTRAINT:1]
         → [TRANSFORM:2] → [CONSTRAINT:2]
         → [TRANSFORM:n] → [CONSTRAINT:n]
         → [DISSIPATE]
```

**Purpose:** Serial transformation through multiple stages

**Characteristics:**
- Each stage has transformation ratio
- Impedance must match between stages
- Failure in one stage affects all downstream
- Cumulative losses

**Examples:**
- Gear train (mechanical ratios)
- Amplifier chain (signal gain)
- Supply chain (material transformation)
- Kinetic chain (force propagation)

**Failure Modes:**
- Impedance mismatch → reflection, loss
- Broken link → complete cascade failure
- Cumulative tolerance stack-up

---

### Pattern 4: MULTI-SOURCE

**Topology:**
```
[SOURCE:1] ⟍
[SOURCE:2] ─→ [CONSTRAINT:MERGE] → [STORAGE]
[SOURCE:n] ⟋
```

**Purpose:** Combine multiple energy sources

**Characteristics:**
- Multiple SOURCEs feed one path
- CONSTRAINT acts as merge point
- Can be cooperative or competitive
- Requires priority/arbitration logic

**Examples:**
- Power grid (multiple generators)
- Multi-motor system
- Multi-input controller
- Muscle synergy (multiple muscles one action)

**Failure Modes:**
- Source conflict (competing priorities)
- Phase mismatch (synchronization loss)
- Unequal load sharing

---

### Pattern 5: BYPASS

**Topology:**
```
         ┌─→ [CONSTRAINT:NOMINAL] → MAIN_PATH
[SOURCE] ┤
         └─→ [CONSTRAINT:BYPASS] → ALT_PATH
```

**Purpose:** Provide alternative paths under specific conditions

**Characteristics:**
- Two or more parallel paths
- CONSTRAINT selects active path
- Enables redundancy and graceful degradation
- Used for overflow/overload protection

**Examples:**
- Bypass valve (pressure relief)
- Dual cooling system
- Redundant power supply
- Muscle agonist/antagonist patterns

**Failure Modes:**
- Unintended path activation
- Path priority conflicts
- Leakage through inactive paths

---

### Pattern 6: DISSIPATIVE_DAMPING

**Topology:**
```
[SOURCE] → [FLOW] → [DISSIPATE] (proportional to velocity)
           ↓
      [STORAGE] (damped)
```

**Purpose:** Add controlled dissipation to prevent oscillation

**Characteristics:**
- DISSIPATE proportional to FLOW rate
- Removes energy from system
- Reduces overshoot and oscillation
- Adds latency (damping effect)

**Examples:**
- Shock absorber (mechanical damping)
- Resistor (electrical damping)
- Viscous damping (hydraulic)
- Friction (energy dissipation)

**Failure Modes:**
- Over-damping → sluggish response
- Under-damping → oscillation
- Damper failure → uncontrolled motion

---

### Pattern 7: STATE_MACHINE

**Topology:**
```
┌─→ [STATE:A] → [CONSTRAINT:GATE_AB] → [STATE:B] ─┐
│                                                    │
└─ [STATE:D] ← [CONSTRAINT:GATE_AD] ← [STATE:C] ←─┘
```

**Purpose:** Model systems with discrete states

**Characteristics:**
- Multiple discrete STORAGE states
- CONSTRAINTs gate transitions
- FEEDBACK determines state transitions
- Common in control systems

**Examples:**
- Finite state machine
- Pump on/off cycles
- Multi-mode controller
- Behavioral patterns (rest/active/exhausted)

**Failure Modes:**
- Stuck state (transition gate locked)
- Race condition (simultaneous transitions)
- Deadlock (no exit transitions)

---

## Pattern Selection Guide

| Problem | Pattern | Why |
|---------|---------|-----|
| Maintain setpoint | REGULATOR | Feedback closes loop |
| Rate decoupling | BUFFER | STORAGE absorbs difference |
| Series transformation | CASCADE | Multi-stage multiplication |
| Energy combination | MULTI-SOURCE | Multiple inputs |
| Overflow protection | BYPASS | Alternative path |
| Vibration reduction | DISSIPATIVE_DAMPING | Energy removal |
| Mode switching | STATE_MACHINE | Discrete states |

---

## Pattern Composition (Nesting)

Patterns can be combined:

**Example:** Regulated buffer
```
[SOURCE] → [REGULATOR:outer] → [BUFFER:inner] → OUTPUT
```

**Example:** Redundant cascade
```
[CASCADE:1] ─┐
            ├→ [MERGE] → OUTPUT
[CASCADE:2] ─┘
```

---

## Anti-Patterns (To Avoid)

### Anti-Pattern 1: Orphan Flow
```
✗ [FLOW] with no SOURCE or STORAGE source
```

### Anti-Pattern 2: Circular Dependency
```
✗ [SOURCE] ← [FEEDBACK] ← [SOURCE] (creates causal loop without regulation)
```

### Anti-Pattern 3: Missing Dissipation
```
✗ [STORAGE] → ∞ accumulation (no DISSIPATE path)
```

### Anti-Pattern 4: Ghost Constraint
```
✗ [CONSTRAINT] with no FLOW passing through it
```

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Primitive definitions
- `docs/02_TOPOLOGY.md` — Connection rules
- `docs/04_DOMAIN_PACKS.md` — Domain-specific patterns
- `docs/06_SYMPHONY.md` — Composition validation

**Used By:** System design and analysis

---

**Status:** Stable  
**Last Updated:** 2026-06-04