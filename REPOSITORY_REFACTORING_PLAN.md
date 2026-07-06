# SOL REPOSITORY REFACTORING PLAN
**Status:** Approved for Execution  
**Date:** 2026-06-04  
**Objective:** Transform into unified engineering knowledge system without knowledge loss

---

## KNOWLEDGE PRESERVATION MATRIX

| File | Classification | Action | Destination | Rationale |
|------|-----------------|--------|-------------|-----------|
| README.md | CANONICAL | Update & Consolidate | `README.md` | Central hub |
| gemini-code-1780047190811.md | SUPPORTING | Merge → CANONICAL | docs/ as reference | Architecture overview |
| gemini-code-1780047296189.md | CANONICAL | Extract → CORE | docs/00_CORE_PRIMITIVES.md | Primitive definitions |
| gemini-code-1780047368228.md | SUPPORTING | Archive | research/ | Benchmark plan (experimental) |
| gemini-code-1780047413079.py | TOOLING | Preserve | src/tdi_validator.py | TDI calculation engine |
| gemini-code-1780047698416.md | SUPPORTING | Merge | docs/ | Redundant overview |
| gemini-code-1780047740107.md | SUPPORTING | Extract | docs/02_TOPOLOGY.md | Architecture layers |
| gemini-code-1780047764885.md | CANONICAL | Extract → CORE | docs/00_CORE_PRIMITIVES.md | Primitive definitions (duplicate) |
| gemini-code-1780047780804.py | TOOLING | Preserve | src/tdi_validator.py | TDI calculation (consolidate) |
| sol_repository_builder.py | TOOLING | Preserve | src/sol_parser.py | Repository builder utility |
| sol_repository_builder (1).py | DUPLICATE | Archive | archive/duplicates/ | Exact duplicate |
| SOL v1.2 Specification PDF | CANONICAL | Reference | docs/_SPECIFICATION_PDF/ | Preserve PDF source |

---

## EXECUTION PHASES

### PHASE 1: CREATE CANONICAL CORE (10 files)

**Objective:** Establish SOL reference specification

```
docs/00_CORE_PRIMITIVES.md          (NEW - Merged from gemini-code-*.md)
docs/01_ONTOLOGY.md                 (NEW - From chat proposals)
docs/02_TOPOLOGY.md                 (NEW - From gemini-code-1780047740107.md + chat)
docs/03_VISUAL_PRIMITIVES.md        (NEW - From chat visual atlas)
docs/04_DOMAIN_PACKS.md             (NEW - From chat domain extensions)
docs/05_PATTERNS.md                 (NEW - From chat pattern catalog)
docs/06_SYMPHONY.md                 (NEW - From chat composition rules)
docs/07_AI_INTERLINGUA.md           (NEW - From chat interlingua section)
docs/08_CONCORDANCE.md              (NEW - Auto-generated index)
docs/SEMANTIC_AUDIT_REPORT.md       (NEW - Audit findings)
```

### PHASE 2: REORGANIZE SUPPORTING DOCS

```
research/
├── 01_ACP_BIOMECHANICAL_NOTES.md   (NEW - Experimental concepts)
├── 02_ARCHITECTURAL_NOTES.md       (NEW - From chat sections)
├── 03_BENCHMARK_PLAN.md            (NEW - From gemini-code-1780047368228.md)
└── STATUS_EXPERIMENTAL.md          (NEW - Research status tracking)

examples/
├── bearing_analysis_example.md     (NEW - Mechanical case study)
├── cad_topology_mapping.md         (NEW - CAD integration example)
└── biomechanical_propagation.md    (NEW - Medical case study)
```

### PHASE 3: ORGANIZE TOOLING

```
src/
├── sol_parser.py                   (FROM sol_repository_builder.py)
├── tdi_validator.py                (MERGED from gemini-code-*.py files)
└── concordance_index.py            (NEW - Search/navigation helper)

tests/
└── test_primitives.py              (NEW - Validation suite)
```

### PHASE 4: ARCHIVE HISTORICAL ARTIFACTS

```
archive/
├── gemini_ai_fragments/
│   ├── gemini-code-1780047190811.md
│   ├── gemini-code-1780047368228.md
│   ├── gemini-code-1780047698416.md
│   └── [others]
│
├── duplicates/
│   └── sol_repository_builder (1).py
│
└── specification_sources/
    └── SOL_v1.2_Specification_PDF/
```

### PHASE 5: UPDATE README

**Consolidated entry point** with:
- Navigation hierarchy
- Progressive learning path (Level 0-6)
- Repository structure diagram
- Quick reference table

---

## CONTENT CONSOLIDATION RULES

### RULE 1: No Duplication
- Primitives defined in ONE place: `docs/00_CORE_PRIMITIVES.md`
- All other docs reference with backlinks
- Examples cross-reference from examples/

### RULE 2: Progressive Disclosure
- README → Quick start
- Level 1 → Core concepts
- Level 2 → System structure
- Level 3+ → Advanced topics

### RULE 3: Knowledge Graph
Every doc includes:
```yaml
Status: [Canonical|Stable|Experimental|Draft]
Purpose: [One sentence]
Dependencies: [List of required reads]
Used By: [List of documents that depend on this]
Related Primitives: [List of SOL primitives]
Related Domains: [SOL-MECH, SOL-CAD, SOL-AI, SOL-BIO]
```

### RULE 4: Bidirectional Links
- Every forward link has a backlink
- Backlinks listed at end of document
- Links use markdown: `[Topic](path#anchor)`

---

## DEPENDENCY RESOLUTION

```
README.md (hub)
  ├─→ docs/00_CORE_PRIMITIVES.md
  ├─→ docs/01_ONTOLOGY.md
  │    └─→ docs/00_CORE_PRIMITIVES.md
  ├─→ docs/02_TOPOLOGY.md
  │    └─→ docs/00_CORE_PRIMITIVES.md
  ├─→ docs/03_VISUAL_PRIMITIVES.md
  │    └─→ docs/00_CORE_PRIMITIVES.md
  ├─→ docs/04_DOMAIN_PACKS.md
  │    ├─→ docs/00_CORE_PRIMITIVES.md
  │    └─→ docs/01_ONTOLOGY.md
  ├─→ docs/05_PATTERNS.md
  │    ├─→ docs/00_CORE_PRIMITIVES.md
  │    └─→ docs/02_TOPOLOGY.md
  ├─→ docs/06_SYMPHONY.md
  │    └─→ [all above]
  ├─→ docs/07_AI_INTERLINGUA.md
  │    ├─→ docs/00_CORE_PRIMITIVES.md
  │    ├─→ docs/02_TOPOLOGY.md
  │    └─→ docs/06_SYMPHONY.md
  ├─→ docs/08_CONCORDANCE.md (index)
  │    └─→ [all docs]
  └─→ examples/
       └─→ references docs/
```

---

## EXECUTION SAFEGUARDS

✓ **No files deleted** - archived instead  
✓ **No concepts lost** - consolidated and cross-referenced  
✓ **All tooling preserved** - moved to src/  
✓ **History maintained** - archive/ contains originals  
✓ **Backlinks enabled** - every document linkable  
✓ **Progressive learning** - README→Level1→...→Level6  

---

## QUALITY GATES

| Gate | Pass Criteria |
|------|---------------|
| **Completeness** | 10/10 canonical docs created |
| **No Loss** | All original files archived or integrated |
| **Cross-Reference** | 100% of forward links have backlinks |
| **Consistency** | All primitives referenced from CORE only |
| **Navigation** | README links to all major docs |
| **Readability** | Each doc has Status/Purpose/Dependencies header |

---

## IMPLEMENTATION STATUS

- [ ] Phase 1: Create canonical core (10 files)
- [ ] Phase 2: Reorganize supporting docs (research/ + examples/)
- [ ] Phase 3: Organize tooling (src/)
- [ ] Phase 4: Archive historical artifacts
- [ ] Phase 5: Update README (consolidated hub)
- [ ] Phase 6: Validate all cross-links
- [ ] Phase 7: Generate CONCORDANCE index
- [ ] Final: Publish reorganized repository

---

**READY FOR EXECUTION**

Proceeding with Phase 1...
