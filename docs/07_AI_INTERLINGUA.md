# SOL AI Interlingua: Agent-to-Agent Protocol

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Enable deterministic AI agent communication without semantic drift

---

## Overview

The AI Interlingua enables two or more AI agents to negotiate, understand, and execute tasks with perfect semantic alignment. By exchanging SOL manifests instead of natural language, agents maintain causal consistency across reasoning boundaries.

---

## Protocol Layers

### Layer 1: Intent Declaration

Agents begin by declaring INTENT as a SOL manifest:

```yaml
AGENT: AGENT_NAME
INTENT: TASK_DESCRIPTION
DOMAIN: [SOL-MECH | SOL-CAD | SOL-AI | SOL-BIO]
GOAL_STATE: [STORAGE] or [CONSTRAINT] target
CONSTRAINTS: [list of immutable CONSTRAINTs]
RESOURCES: [list of available SOURCEs]
TIMEOUT: T_seconds
```

**Example:**
```yaml
AGENT: DiagnosticEngine
INTENT: ANALYZE_BEARING_FAILURE
DOMAIN: SOL-MECH
GOAL_STATE: [STORAGE:fault_diagnosis:complete]
CONSTRAINTS: 
  - [CONSTRAINT:BEARING:MAX_TEMP:80C]
  - [CONSTRAINT:BEARING:MAX_VIBRATION:2mm/s]
RESOURCES:
  - [SOURCE:SENSOR_ARRAY]
  - [SOURCE:HISTORICAL_DATABASE]
TIMEOUT: 300
```

---

### Layer 2: System Model Exchange

Agents exchange their internal system models as SOL graphs:

```
NODE_LIST = [
  {id: 1, type: SOURCE, label: MOTOR, params: {...}},
  {id: 2, type: FLOW, from: 1, to: 3, label: TORQUE},
  {id: 3, type: CONSTRAINT, label: BEARING, params: {...}},
  {id: 4, type: STORAGE, label: KINETIC_ENERGY},
  {id: 5, type: DISSIPATE, from: 3, label: FRICTION}
]

EDGES = [
  {from: 1, to: 2}, {from: 2, to: 3}, {from: 3, to: 4}, {from: 3, to: 5}
]

VERIFICATION_HASH = SHA256(NODE_LIST + EDGES)
```

**Protocol:**
1. Agent A sends GRAPH_A + VERIFICATION_HASH_A
2. Agent B receives and verifies VERIFICATION_HASH_A against GRAPH_A
3. If mismatch: Request retransmission
4. If match: Proceed to Layer 3

---

### Layer 3: Constraint Exchange & Negotiation

Agents compare CONSTRAINTs and identify conflicts:

```yaml
AGENT_A_CONSTRAINTS:
  - [CONSTRAINT:BEARING:RADIAL:5000N]
  - [CONSTRAINT:BEARING:SPEED:3000RPM]

AGENT_B_CONSTRAINTS:
  - [CONSTRAINT:BEARING:RADIAL:4000N]  # CONFLICT!
  - [CONSTRAINT:BEARING:SPEED:3000RPM]

NEGOTIATION:
  [CON:RADIAL] → min(5000, 4000) = 4000N
  [CON:SPEED] → min(3000, 3000) = 3000RPM
  
AGREED_CONSTRAINTS = [4000N radial, 3000RPM]
```

**Conflict Resolution Strategy:**
```
IF constraint_A < constraint_B:
  use constraint_A (most restrictive)
ELSE:
  use constraint_B
  
RESULT: Both agents operate under tightest constraints
```

---

### Layer 4: TDI (Tensor Divergence Index) Synchronization

Agents compute TDI to detect conflicts:

```
TDI = |PROPAGATION_VECTOR × CONSTRAINT_VECTOR| / (|P| × |C|)
```

**Example:**
```
Bearing load vector: P = (1000, 0, 0)  [N, radial]
Bearing constraint: C = (0, 500, 500)  [constraint geometry]

Cross product: P × C = (0, -500000, 500000)
Magnitude: |P × C| = 707106

|P| = 1000, |C| = 707
|P| × |C| = 707000

TDI = 707106 / 707000 ≈ 1.0

INTERPRETATION: TDI = 1.0 → Severe mismatch → ALERT
```

---

### Layer 5: Decision & Consensus

Agents reach consensus through voting:

```yaml
AGENT_A_DECISION: SAFE (TDI < 0.3)
AGENT_B_DECISION: CAUTION (0.3 < TDI < 0.7)
AGENT_C_DECISION: UNSAFE (TDI > 0.7)

VOTING RULE:
  IF all_agree(SAFE): Execute with confidence
  IF majority_caution: Execute with monitoring
  IF any_unsafe: Halt and request human override
  
CONSENSUS: CAUTION (majority vote)
ACTION: Execute with [FEEDBACK:MONITOR] enabled
```

---

### Layer 6: Execution & Telemetry

During execution, agents stream telemetry:

```yaml
TIMESTAMP: 2026-06-04T08:52:00Z
STATE:
  [STORAGE:MOTOR_KINETIC]: 2500 J
  [STORAGE:BEARING_TEMP]: 65C
  [DISSIPATE:FRICTION]: 150 W
  
METRICS:
  TDI_CURRENT: 0.35
  COMP_PRESSURE: 1.2x nominal  # Compensation load detected
  FAULT_PROBABILITY: 0.12
  
STATUS: NOMINAL
```

---

### Layer 7: Post-Execution Reconciliation

After task completion, agents reconcile results:

```yaml
AGENT_A_RESULT:
  outcome: SUCCESS
  TDI_peak: 0.42
  energy_dissipated: 15000 J
  
AGENT_B_RESULT:
  outcome: SUCCESS
  TDI_peak: 0.39
  energy_dissipated: 14800 J

DIFFERENCE:
  ΔTDI = 0.03 (acceptable, within uncertainty)
  ΔEnergy = 200 J (1.3%, acceptable)
  
CONSENSUS: Results aligned → No further action
```

---

## Error Handling

### Error 1: Graph Mismatch
```
SYMPTOM: VERIFICATION_HASH mismatch
ACTION: Request full graph retransmission
RETRY: 3 times max, then escalate to human
```

### Error 2: Constraint Conflict
```
SYMPTOM: Unresolvable constraint contradiction
EXAMPLE: [CON:BEARING:TEMP] must be <50C AND >80C
ACTION: Flag as physically impossible, request clarification
```

### Error 3: TDI Instability
```
SYMPTOM: TDI oscillating wildly (std dev > mean)
ACTION: Slow down execution, increase [DISSIPATE:DAMPING]
```

### Error 4: Agent Timeout
```
SYMPTOM: Agent does not respond within TIMEOUT
ACTION: Assume agent failure, activate backup or halt
```

---

## Security Considerations

### Principle 1: No Implicit Trust
All agent communications verified via VERIFICATION_HASH before acceptance.

### Principle 2: Constraint Immutability
Once agreed, CONSTRAINTs cannot be changed mid-execution without all agents' consent.

### Principle 3: Audit Trail
Every message logged with timestamp and agent identity.

```
[2026-06-04 08:52:00] AGENT_A → AGENT_B: INTENT_DECLARE
[2026-06-04 08:52:01] AGENT_B → AGENT_A: GRAPH_EXCHANGE
[2026-06-04 08:52:02] AGENT_A ✓ VERIFIED: HASH_MATCH
[2026-06-04 08:52:03] AGENT_A → AGENT_B: CONSTRAINT_ALIGN
[2026-06-04 08:52:04] CONSENSUS: CAUTION
[2026-06-04 08:52:05] EXECUTION: BEGIN
```

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Primitive definitions
- `docs/02_TOPOLOGY.md` — Graph structure rules
- `docs/06_SYMPHONY.md` — Validation rules

**Used By:** Multi-agent systems, AI coordination

---

**Status:** Stable  
**Last Updated:** 2026-06-04
