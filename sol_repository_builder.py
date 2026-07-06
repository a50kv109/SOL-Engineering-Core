import os

# Структура репозитория и содержимое файлов SOL v1.2
REPO_DIR = "SOL-Protocol-Files"

files_data = {
    "SPECIFICATION.md": """# SOL Specification (v1.2)

## 1. Protocol Philosophy
Structural Operational Language (SOL) is fundamentally an **engineering cognitive stabilization protocol**.

## 2. Core Primitives and Syntax
1.  **Entities `[...]`**: Represent physical hardware, fluids, or materials.
2.  **Actions/Operators `(...)` or `[...]`**: Represent processes, diagnostics, or state changes.
3.  **Specifications `:`**: Bind parameters.
4.  **Causality `->`**: Denotes physical flow or logical progression.

Canonical Format: `[SOURCE] -> [INTERFACE] -> [TARGET]`
""",
    
    "CHANGELOG.md": """# Changelog
All notable changes to the SOL Protocol will be documented in this file.

## [v1.2] - 2026-05-28 (Experimental)
### Added
* Complete specification of the 4-layer architecture (SOL-H, SOL-A, SOL-IR, SOL-CAD/DW).
* Standardized core syntax primitives (`[]`, `()`, `:`, `->`).
""",
    
    "ROADMAP.md": """# Roadmap
The SOL protocol is under active development. 

## Phase 1: Core Protocol Maturation (Current)
- [x] Define syntax primitives.
- [x] Establish the 4-layer architectural boundaries.
- [ ] Finalize standard library for common mechanical components.
""",
    
    "VALIDATION.md": """# Validation Methodology
**Status:** Experimental and Ongoing.

## Proposed Benchmark Categories
1. Semantic Drift Tests
2. Multi-Agent Transfer (SOL-A)
3. Topological Preservation
""",
    
    "docs/SOL-H.md": """# SOL-H (Human Layer)
## Purpose
Optimized strictly for **human engineers** to facilitate cognitive acceleration and visual readability.
Allows emoji operators: `🔍` (Analyze), `⚠️` (Warn), `🔧` (Repair), `✅` (Stable).
""",

    "docs/SOL-A.md": """# SOL-A (Agent Protocol Layer)
## Purpose
Standardized interchange layer designed for **stable inter-agent communication**. 
Emoji shorthand is strictly forbidden. Uses canonical text tokens (e.g., `[ANALYZE]`).
""",

    "docs/SOL-IR.md": """# SOL-IR (Internal Representation Layer)
## Purpose
Internal AI reasoning substrate. Enforces that the **canonical meaning and topology remain invariant** during the model's internal transformations.
""",

    "docs/SOL-CAD-DW.md": """# SOL-CAD/DW (Spatial & Drawing Layer)
## Purpose
Semantic/topological bridge between spatial engineering data (2D drawings, 3D CAD) and abstract engineering reasoning.
*Not a geometry engine.* Extracts topology of constraints.
""",

    "docs/TOKENS.md": """# Entity Tokens
* `[BRG*]` : Rolling-element bearing
* `[SFT]` : Shaft
* `[FLU]` : Fluid medium
* `[SENS]` : Sensor
""",

    "docs/OPERATORS.md": """# Action and Diagnostic Operators
* `->` : Causal flow
* `[ANALYZE]` : Diagnostic check
* `[WARN]` : Anomaly detection
* `[REPAIR]` : Maintenance action
""",

    "docs/EXAMPLES/bearing_example.md": """# Example: Bearing Failure Detection Chain
`[SFT:DRIVE] -> [BRG*:6204] -> [SENS:VIB:ACCEL] -> [ANALYZE]:FFT_SPECTRUM -> [WARN]:BPFO_DETECTED -> [REPAIR]:REPLACE_BRG -> [STABLE]`
""",

    "benchmarks/semantic_drift_test.md": """# Benchmark Methodology: Semantic Drift Test
Measures the degradation of engineering constraints in an LLM over a long context window.
"""
}

def build_repo():
    print(f"Инициализация создания структуры SOL (AAM-V1)...")
    
    # Создаем корневую папку
    if not os.path.exists(REPO_DIR):
        os.makedirs(REPO_DIR)
        
    for filepath, content in files_data.items():
        # Формируем полный путь
        full_path = os.path.join(REPO_DIR, filepath)
        
        # Создаем подпапки (docs, benchmarks и т.д.), если они нужны
        directory = os.path.dirname(full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        # Записываем файл
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Создан файл: {filepath}")

    print(f"\nУспешно! Все файлы сгенерированы в папке '{REPO_DIR}'.")
    print("Теперь вы можете перетащить эту папку в браузер (GitHub: Add file -> Upload files).")

if __name__ == "__main__":
    build_repo()