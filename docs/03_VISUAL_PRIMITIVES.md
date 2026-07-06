# SOL Visual Primitives: Symbol Standardization

**Status:** Stable  
**Version:** v2.0  
**Purpose:** Standardized visual representation for SOL primitives across all media

---

## Overview

Visual symbols enable human engineers and AI systems to recognize SOL primitives instantly in diagrams, code, and specifications. These symbols are standardized to prevent semantic drift through visual encoding.

---

## Canonical Symbol Set

| Primitive | Primary | Alt 1 | Alt 2 | Unicode | Use Context |
|-----------|---------|-------|-------|---------|----------|
| **SOURCE** | `●` | `🔴` | `[SRC]` | U+25CF | Diagrams, flowcharts |
| **FLOW** | `→` | `⇒` | `[FLW]` | U+2192 | Arrows, causality |
| **CONSTRAINT** | `⚙` | `🔒` | `[CON]` | U+2699 | Topology, limits |
| **STORAGE** | `□` | `📦` | `[STR]` | U+25A1 | Buffers, memory |
| **DISSIPATE** | `▽` | `🔥` | `[DIS]` | U+25BD | Loss nodes, heat |
| **TRANSFORM** | `❖` | `⚡` | `[TRF]` | U+2756 | Converters, ratio |
| **FEEDBACK** | `↺` | `🔄` | `[FBK]` | U+21BA | Loops, regulation |

---

## Composite Symbols

These combine primitives for common patterns:

### Regulated System
```
●──→⚙ ↺
```
Meaning: SOURCE → CONSTRAINT with FEEDBACK regulation

### Buffered Flow
```
●──→□──→⚙
```
Meaning: SOURCE → STORAGE (buffer) → CONSTRAINT

### Dissipative Process
```
●──→⚙──→▽
```
Meaning: SOURCE → CONSTRAINT → DISSIPATE (lossy system)

---

## Notation Standards

### Full Notation
```
[PRIMITIVE:DOMAIN:DETAIL:INSTANCE]
```

**Example:** `[CONSTRAINT:BEARING:RADIAL:BRG_6204]`

### Compact Notation
```
[PRIMITIVE]
```

**Example:** `[CON]`

### With Parameters
```
[PRIMITIVE:param1:param2]
```

**Example:** `[STR:capacity:100L]` or `[FLW:rate:50mL/s]`

---

## Visual Grammar Rules

### Rule 1: Direction Always Left-to-Right
Primary flow runs left → right (following natural reading order).

```
CORRECT:   [SRC] → [CON] → [STR]
AVOID:     [STR] ← [CON] ← [SRC]
```

### Rule 2: Feedback Always Up-Down-Up
Feedback returns from right-side (vertical) to close loop.

```
CORRECT:   [SRC] → [CON]
                      ↓
                    [STR]
                      ↑ ← feedback
```

### Rule 3: Hierarchy Uses Indentation
Sub-primitives indented under parent.

```
[CONSTRAINT]
  ├─ [CON:RADIAL]
  ├─ [CON:AXIAL]
  └─ [CON:THERMAL]
```

### Rule 4: Symbols Never Modified
Symbols remain identical regardless of context. Only notation changes.

```
CORRECT:   [CON:BEARING], [CON:VALVE], [CON:RESISTOR]
AVOID:     [CON_BEARING], [CON*], [CON!]
```

---

## Symbol Consistency Checklist

- [ ] All SOURCE nodes use `●`
- [ ] All FLOW connections use `→`
- [ ] All CONSTRAINT nodes use `⚙`
- [ ] All STORAGE use `□`
- [ ] All DISSIPATE use `▽`
- [ ] All TRANSFORM use `❖`
- [ ] All FEEDBACK use `↺`
- [ ] No modified or variant symbols introduced
- [ ] Notation always uses square brackets `[...]`

---

## Cross-References

**Related Documents:**
- `docs/00_CORE_PRIMITIVES.md` — Symbol origins
- `docs/05_PATTERNS.md` — Common composite patterns
- `docs/06_SYMPHONY.md` — Composition rules using symbols

**Used By:** All visual documentation

---

**Status:** Stable  
**Last Updated:** 2026-06-04