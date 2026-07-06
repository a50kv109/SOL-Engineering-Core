# SOL AST Structure v1.0
**Signature: AAM-V2_ARTSYBASHEV_UA_KHARKIV_AST**

## 1. Введение
Настоящий документ описывает структуру **Абстрактного Синтаксического Графа** (Abstract Syntax Graph, ASG/AST) языка SOL. В отличие от линейных деревьев, AST в SOL спроектировано как сетевая структура, способная выражать сложные инженерные зависимости.

---

## 2. Базовый узел (BaseASTNode)
Все узлы графа наследуют общие свойства:
- `node_id`: Уникальный строковый идентификатор.
- `guna_weight`: Весовой коэффициент гуны (0.0 - 1.0).
- `metadata`: Коллекция META-данных (ключ=значение).
- `source_ref`: Ссылка на диапазон строк в исходном коде (для отладки).

---

## 3. Типы узлов

### 3.1 `RootNode`
Верхнеуровневый контейнер проекта.
- **Связи:** Список `DefinitionNode`, `ConnectionNode`, `MetadataNode`.

### 3.2 `DefinitionNode` (Узел Определения)
Создает экземпляр или спецификацию в графе.
- **Поля:** 
  - `entity_type`: (ENTITY | PROPERTY | RELATION | CONSTRAINT | STATE | EVENT | PROCESS | RESOURCE | CAPABILITY | MEASUREMENT | SPECIFICATION).
  - `is_template`: Флаг (True если это Specification).
- **Связи:** 
  - `ports`: Список `PortNode`.
  - `attributes`: Список вложенных свойств.

### 3.3 `PortNode` (Узел Порта)
Точка взаимодействия между узлами.
- **Поля:**
  - `direction`: (IN | OUT).
  - `kind`: (POTENTIAL | METRIC | STATE | ASSET).
- **Связи:** Ссылки на `ConnectionNode`.

### 3.4 `ConnectionNode` (Узел Связи / CON)
Ребро графа, описывающее поток или зависимость.
- **Поля:**
  - `protocol`: Версия протокола (по умолчанию CON v1.0).
- **Связи:**
  - `source`: Ссылка на выходной `PortNode`.
  - `target`: Ссылка на входной `PortNode`.

### 3.5 `ConstraintNode` (Узел Ограничения)
Предикат, накладываемый на узел.
- **Поля:**
  - `expression_tree`: Вложенное дерево логического выражения.
- **Связи:** Ссылка на `TargetNode` (на что наложено ограничение).

---

## 4. Графовые свойства AST
1. **Node Reusability:** Один и тот же узел `PropertyNode` может быть связан с несколькими `EntityNode`.
2. **Ciclicity:** Допускаются циклы в связях (например, обратная связь в процессах).
3. **Reference-based:** Узлы хранят не "копии", а "ссылки" (ID) на другие узлы.
