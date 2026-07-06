# PRECEDENT_INDEX

Реестр инженерных прецедентов для разрешения архитектурных конфликтов в SOL.

## Формат записи
- `precedent_id`: Уникальный ID прецедента.
- `source`: Источник (`BOOK-NAV` или `DRAWING-NAV`).
- `asset_ref`: Ссылка на артефакт (книга/чертеж/раздел).
- `conflict_type`: Тип конфликта (`ARCHITECTURAL`, `PHYSICAL`, `EXISTENTIAL`).
- `pattern`: Короткий паттерн для сопоставления.
- `solution`: Рекомендуемое инженерное решение.
- `applicability`: Условия применимости.

## Прецеденты

### PRC-ARCH-001
- `precedent_id`: `PRC-ARCH-001`
- `source`: `BOOK-NAV`
- `asset_ref`: `BOOK-NAV/docs/architecture/ports-and-contracts.md`
- `conflict_type`: `ARCHITECTURAL`
- `pattern`: `missing_interface|CON_not_defined|signature_mismatch`
- `solution`: "Добавьте явный CON-интерфейс между узлами и выровняйте сигнатуру вызова по контракту METAMODEL."
- `applicability`: "Когда у операции отсутствует объявленный канал связи или нарушено количество аргументов dhatu."

### PRC-ARCH-002
- `precedent_id`: `PRC-ARCH-002`
- `source`: `DRAWING-NAV`
- `asset_ref`: `DRAWING-NAV/docs/interfaces/shaft-gear-coupling.md`
- `conflict_type`: `ARCHITECTURAL`
- `pattern`: `interface_absent|connection_undefined`
- `solution`: "Вставьте промежуточный адаптер (CON node), зафиксируйте тип портов IN/OUT и повторно прогоните Validator."
- `applicability`: "Когда объекты совместимы по домену, но не имеют формально определенной связи."
