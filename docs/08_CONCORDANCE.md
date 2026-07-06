# SOL Concordance: Navigation Index

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Cross-reference index and semantic search guide

---

## Quick Navigation

### By Role
- **Newcomer:** Start → README.md → docs/00_CORE_PRIMITIVES.md
- **Engineer:** START → docs/04_DOMAIN_PACKS.md → docs/05_PATTERNS.md
- **AI Developer:** START → docs/07_AI_INTERLINGUA.md → docs/06_SYMPHONY.md
- **Researcher:** START → research/ → docs/

### By Primitive

#### [SOURCE] ●
**Definition:** `docs/00_CORE_PRIMITIVES.md#source`  
**Ontology:** `docs/01_ONTOLOGY.md#object-state-process`  
**Patterns Using:**
- REGULATOR: `docs/05_PATTERNS.md#pattern-1-regulator`
- BUFFER: `docs/05_PATTERNS.md#pattern-2-buffer`
- CASCADE: `docs/05_PATTERNS.md#pattern-3-cascade`

**Domain Examples:**
- SOL-MECH: Motor, pump inlet
- SOL-CAD: Geometry initiator
- SOL-AI: Goal/Query
- SOL-BIO: Neural command

**Related Files:** `docs/00_CORE_PRIMITIVES.md`, `docs/05_PATTERNS.md`, `docs/04_DOMAIN_PACKS.md`

---

#### [FLOW] →
**Definition:** `docs/00_CORE_PRIMITIVES.md#flow`  
**Topology Rules:** `docs/02_TOPOLOGY.md#topology-patterns`  
**Visual Symbol:** `docs/03_VISUAL_PRIMITIVES.md`

**Patterns Using:**
- LINEAR_FLOW: `docs/02_TOPOLOGY.md#pattern-1-linear-flow`
- CIRCULAR_FLOW: `docs/02_TOPOLOGY.md#pattern-2-circular-flow`
- CASCADE: `docs/05_PATTERNS.md#pattern-3-cascade`

**Domain Extensions:**
- SOL-MECH: Rotational, Linear, Torque flows
- SOL-HYDR: Pressure, Volumetric flows
- SOL-ELEC: Current flows
- SOL-BIO: Force, Neural, Circulatory flows

---

#### [CONSTRAINT] ⚙
**Definition:** `docs/00_CORE_PRIMITIVES.md#constraint`  
**Topology Rules:** `docs/02_TOPOLOGY.md#constraint-dominion-principle`  
**Conflict Resolution:** `docs/02_TOPOLOGY.md#conflict-resolution`

**Patterns Using:**
- All patterns (REGULATOR, BUFFER, CASCADE, etc.)

**Domain Extensions:**
- SOL-MECH: Joint, Bearing, Friction
- SOL-CAD: Planar, Cylindrical, Spherical
- SOL-BIO: Joint (synovial), Ligament, Tissue elasticity

---

#### [STORAGE] □
**Definition:** `docs/00_CORE_PRIMITIVES.md#storage`  
**Ontology:** `docs/01_ONTOLOGY.md#object-state-process`  
**Energy Balance:** `docs/06_SYMPHONY.md#law-2-energy-continuity`

**Patterns Using:**
- BUFFER: `docs/05_PATTERNS.md#pattern-2-buffer`
- REGULATOR: `docs/05_PATTERNS.md#pattern-1-regulator`
- STATE_MACHINE: `docs/05_PATTERNS.md#pattern-7-state_machine`

---

#### [DISSIPATE] ▽
**Definition:** `docs/00_CORE_PRIMITIVES.md#dissipate`  
**Energy Balance:** `docs/06_SYMPHONY.md#law-2-energy-continuity`  
**Patterns Using:**
- DISSIPATIVE_DAMPING: `docs/05_PATTERNS.md#pattern-6-dissipative_damping`

**Domain Manifestations:**
- SOL-MECH: Friction, Wear, Heat
- SOL-ELEC: Joule heating, Radiation
- SOL-BIO: Metabolic cost, Tissue wear

---

#### [TRANSFORM] ❖
**Definition:** `docs/00_CORE_PRIMITIVES.md#transform`  
**Topology:** `docs/02_TOPOLOGY.md#pattern-5-cascade`  
**Patterns Using:**
- CASCADE: `docs/05_PATTERNS.md#pattern-3-cascade`

**Domain Examples:**
- SOL-MECH: Gear, Pulley, Lever
- SOL-ELEC: Transformer, Converter
- SOL-AI: Inference, Translation

---

#### [FEEDBACK] ↺
**Definition:** `docs/00_CORE_PRIMITIVES.md#feedback`  
**Stability Rules:** `docs/06_SYMPHONY.md#law-4-feedback-stability`  
**Patterns Using:**
- REGULATOR: `docs/05_PATTERNS.md#pattern-1-regulator`
- STATE_MACHINE: `docs/05_PATTERNS.md#pattern-7-state_machine`

---

### By Domain Pack

#### SOL-MECH
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-mech-mechanical-engineering`  
**Use Cases:** Load paths, motion chains, mechanical design  
**Key Patterns:**
- Bearing analysis: CASCADE + DISSIPATE
- Transmission: CASCADE + TRANSFORM
- Speed control: REGULATOR + FEEDBACK

---

#### SOL-CAD
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-cad-computer-aided-design--topology`  
**Use Cases:** Geometric topology, constraint mapping, load paths  
**Key Concepts:**
- Geometric faces → [CONSTRAINT]
- Load paths → [FLOW]
- Relationships → [LINK]

---

#### SOL-AI
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-ai-agent-reasoning--symbolic-processing`  
**Protocol:** `docs/07_AI_INTERLINGUA.md`  
**Use Cases:** Multi-agent alignment, reasoning chains, goal representation

---

#### SOL-BIO
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-bio-biomechanical--physiological`  
**Use Cases:** Movement analysis, injury mechanisms, rehabilitation  
**Case Study:** Frozen shoulder (adhesive capsulitis) in `docs/04_DOMAIN_PACKS.md`

---

#### SOL-HYDR
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-hydr-hydraulics--fluid-systems`  
**Key Components:** Pump, Valve, Accumulator

---

#### SOL-ELEC
**Overview:** `docs/04_DOMAIN_PACKS.md#sol-elec-electrical-systems`  
**Key Components:** Source, Resistor, Capacitor, Inductor

---

### By Pattern Type

| Pattern | Document | Use Case |
|---------|----------|----------|
| REGULATOR | `docs/05_PATTERNS.md#pattern-1-regulator` | Setpoint control |
| BUFFER | `docs/05_PATTERNS.md#pattern-2-buffer` | Rate decoupling |
| CASCADE | `docs/05_PATTERNS.md#pattern-3-cascade` | Series transformation |
| MULTI-SOURCE | `docs/05_PATTERNS.md#pattern-4-multi-source` | Energy combination |
| BYPASS | `docs/05_PATTERNS.md#pattern-5-bypass` | Overflow protection |
| DISSIPATIVE_DAMPING | `docs/05_PATTERNS.md#pattern-6-dissipative_damping` | Vibration reduction |
| STATE_MACHINE | `docs/05_PATTERNS.md#pattern-7-state_machine` | Mode switching |

---

### By Concept

#### Energy Balance
- Theory: `docs/06_SYMPHONY.md#law-2-energy-continuity`
- Verification: `docs/06_SYMPHONY.md#rule-v2-energy-balance`
- Application: `docs/02_TOPOLOGY.md#energy-conservation-principle`

#### Causality
- Principle: `docs/02_TOPOLOGY.md#causality-principle`
- Verification: `docs/06_SYMPHONY.md#rule-v3-causality`
- Interlingua: `docs/07_AI_INTERLINGUA.md#layer-2-system-model-exchange`

#### Semantic Consistency
- Problem: README.md (Semantic Drift)
- Solution: `docs/00_CORE_PRIMITIVES.md#extension-rules`
- Verification: `docs/06_SYMPHONY.md` (All rules)

#### Feedback & Regulation
- Theory: `docs/00_CORE_PRIMITIVES.md#feedback`
- Stability: `docs/06_SYMPHONY.md#law-4-feedback-stability`
- Patterns: `docs/05_PATTERNS.md#pattern-1-regulator`

---

## Cross-Document References

### Backlinks: CORE_PRIMITIVES ← All docs
- Referenced by: ONTOLOGY, TOPOLOGY, VISUAL_PRIMITIVES, DOMAIN_PACKS, PATTERNS, SYMPHONY, AI_INTERLINGUA

### Backlinks: SYMPHONY ← PATTERNS, TOPOLOGY
- Validation rules sourced from Symphony
- Patterns verified against Symphony laws

### Backlinks: AI_INTERLINGUA ← TOPOLOGY
- Graph structure rules from Topology
- Constraint negotiation uses Topology principles

---

## Search Guide

### Find by Keyword

**"Bearing"** → SOL-MECH in `docs/04_DOMAIN_PACKS.md`, Example in `docs/05_PATTERNS.md#pattern-1-regulator`

**"Oscillation"** → Feedback stability in `docs/06_SYMPHONY.md#law-4-feedback-stability`, Pattern in `docs/05_PATTERNS.md#pattern-6-dissipative_damping`

**"Load Path"** → Topology in `docs/02_TOPOLOGY.md`, SOL-CAD in `docs/04_DOMAIN_PACKS.md`

**"Constraint Conflict"** → `docs/02_TOPOLOGY.md#conflict-resolution`, `docs/07_AI_INTERLINGUA.md#layer-3-constraint-exchange--negotiation`

**"Semantic Drift"** → Problem statement in README.md, Solution in `docs/00_CORE_PRIMITIVES.md`

---

## File Dependency Graph

```
README.md (hub)
  ├─ docs/00_CORE_PRIMITIVES.md (canonical)
  │  ├─ docs/01_ONTOLOGY.md
  │  ├─ docs/02_TOPOLOGY.md
  │  ├─ docs/03_VISUAL_PRIMITIVES.md
  │  ├─ docs/04_DOMAIN_PACKS.md
  │  ├─ docs/05_PATTERNS.md
  │  ├─ docs/06_SYMPHONY.md
  │  └─ docs/07_AI_INTERLINGUA.md
  │
  ├─ docs/02_TOPOLOGY.md
  │  ├─ docs/05_PATTERNS.md
  │  └─ docs/06_SYMPHONY.md
  │
  ├─ docs/05_PATTERNS.md
  │  └─ docs/06_SYMPHONY.md
  │
  └─ docs/07_AI_INTERLINGUA.md
     └─ docs/02_TOPOLOGY.md
```

---

## Status Indicators

| Document | Status | Completeness | Notes |
|----------|--------|-------------|-------|
| CORE_PRIMITIVES | Canonical | 100% | Immutable, frozen |
| ONTOLOGY | Stable | 95% | Ready for application |
| TOPOLOGY | Stable | 95% | Ready for application |
| VISUAL_PRIMITIVES | Stable | 90% | Color coding optional |
| DOMAIN_PACKS | Stable | 85% | New domains can be added |
| PATTERNS | Stable | 85% | New patterns follow rules |
| SYMPHONY | Stable | 95% | Validation rules complete |
| AI_INTERLINGUA | Stable | 80% | Security review recommended |

---

**Status:** Stable  
**Last Updated:** 2026-06-04
