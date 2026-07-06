# SOL (Structural Operational Language)

SOL (Structural Operational Language) - инженерная языковая платформа на базе ведической архитектуры.

SOL is the canonical, minimal semantic vocabulary for engineering systems, expanded in V2 with a typed execution core (SPC:2.0), conflict arbitration, and evidence-driven diagnostics.

## Что в проекте
- `src/core`: исполняемое ядро SPC:2.0 (Compiler, Runtime, ConflictResolver, Evidence Layer).
- `docs/specifications`: формальные спецификации языка и AST.
- `docs/foundation`: фундаментальные документы и протоколы.
- `tests`: место для автотестов по примитивам и сценариям конфликтов.

## Quick links
- Foundation: `docs/foundation/SOL_CORE_FOUNDATION.md`
- Scope: `docs/foundation/SOL_SCOPE.md`
- Relations Map: `docs/foundation/SOL_RELATIONS_MAP.md`
- Specifications index: `docs/specifications/`

## Ключевая спецификация
- `METAMODEL.md`: [docs/specifications/METAMODEL.md](docs/specifications/METAMODEL.md)

## Быстрый запуск
```bash
python3 src/core/deepseek_python_20260706_2d88da.py
```

License: See repository LICENSE.
