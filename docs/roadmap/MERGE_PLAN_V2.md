# MERGE_PLAN_V2

## Контекст
Локальная ветка `migration/upgrade-to-v2` опубликована и содержит нормализованную структуру V2 (`src`, `docs`, `tests`) с ядром SPC:2.0, ConflictResolver и Evidence Layer.

## Важное техническое замечание
Истории `origin/main` и локальной ветки изначально несвязаны (`no merge base`).
Для анализа использовалось прямое сравнение деревьев: `git diff origin/main HEAD`.

## Критические расхождения с текущей архитектурой V2

1. Старое semantic-core описание (v7, 7 primitives) конфликтует с текущим онтологическим каркасом V2.
- Файл: `docs/00_CORE_PRIMITIVES.md` (origin/main)
- Проблема: канонизирует модель `[SOURCE, FLOW, CONSTRAINT, STORAGE, DISSIPATE, TRANSFORM, FEEDBACK]` как единственный базис.
- Почему конфликт: в V2 действуют `METAMODEL + AST + SPC:2.0 + Evidence Protocol`, где семантическое ядро расширено типами/узлами и инженерными событиями.

2. Старый слой онтологии использует другую карту концептов.
- Файл: `docs/01_ONTOLOGY.md` (origin/main)
- Проблема: слой OBJECT/STATE/PROCESS в старом формате и связки к старому primitive stack.
- Почему конфликт: новая версия задает формальный контур через `docs/specifications/METAMODEL.md` и `docs/specifications/AST_STRUCTURE.md`.

3. Неструктурированные корневые артефакты мешают промышленной поставке.
- Файлы: множественные `gemini-code-*.md|*.py`, `sol_repository_builder*.py`, а также наборы временных/черновых документов.
- Проблема: шум в корне, слабая портативность и низкая трассируемость релизов.

## План миграции

### Удалить (или перенести в `archive/legacy-main/`)
- `docs/00_CORE_PRIMITIVES.md`
- `docs/01_ONTOLOGY.md`
- `docs/02_TOPOLOGY.md` ... `docs/08_CONCORDANCE.md`
- временные артефакты `gemini-code-*`, `sol_repository_builder*.py`, вспомогательные черновики в корне

### Обновить/оставить как канон V2
- `README.md`
- `src/core/deepseek_python_20260706_2d88da.py`
- `docs/specifications/*`
- `docs/foundation/evidence_protocol.md`
- `core/ontology/PRECEDENT_INDEX.md`
- `.gitignore`

### Проверки перед merge в main
1. `python3 -m py_compile src/core/deepseek_python_20260706_2d88da.py`
2. smoke-тесты конфликтов:
   - `√tulā(5, 0)` => `PHYSICAL`
   - `√man(1, 2, 3)` => `ARCHITECTURAL` + precedent recommendation
3. Ручная проверка ссылок в `README.md` и `docs/REPORT_CHIEF_ARCHITECT.md`

## Итог
Рекомендуется merge через Pull Request из `migration/upgrade-to-v2` в `main` с пометкой:
- `breaking-structure-change`
- `architecture-v2`
- `spc2-evidence-ready`
