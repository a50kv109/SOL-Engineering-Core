# ============================================================
# SOLO CORE: SANSCRIT PRIMITIVE COMPILER (SPC) v2.0
# TYPE_SAFE + PHYSICAL + CONTEXT + TRACE
# ============================================================

import re
import math
from typing import Any, Dict, List, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json


# ============================================================
# ЧАСТЬ 1: СИСТЕМА ТИПОВ (PHYSICAL TYPES)
# ============================================================

class Dimension(Enum):
    """Физические размерности"""
    DIMENSIONLESS = "1"
    LENGTH = "m"
    MASS = "kg"
    TIME = "s"
    CURRENT = "A"
    TEMPERATURE = "K"
    LUMINOSITY = "cd"
    AMOUNT = "mol"
    
    # Производные
    VELOCITY = "m/s"
    ACCELERATION = "m/s²"
    FORCE = "kg·m/s²"  # Н
    ENERGY = "kg·m²/s²"  # Дж
    POWER = "kg·m²/s³"  # Вт
    PRESSURE = "kg/(m·s²)"  # Па
    FREQUENCY = "1/s"  # Гц
    VOLTAGE = "kg·m²/(s³·A)"  # В
    RESISTANCE = "kg·m²/(s³·A²)"  # Ом


class Guna(Enum):
    """Ведические гуны"""
    SATTVA = ("Sattva", 0.2)   # Мета-структура / Ясность
    RAJAS = ("Rajas", 0.5)     # Активность / Преобразование
    TAMAS = ("Tamas", 0.9)      # Инерция / Фиксация


class ConflictType(Enum):
    """Типы инженерных конфликтов"""
    PHYSICAL = "PHYSICAL"         # Нарушение физики/математики
    ARCHITECTURAL = "ARCHITECTURAL" # Структурное несоответствие
    EXISTENTIAL = "EXISTENTIAL"     # Логический тупик


@dataclass
class EngineeringEvent:
    """Инженерное событие (инцидент)"""
    event_id: str
    type: ConflictType
    message: str
    nodes: List[str]
    trace: List[Any]
    correction_prompt: Optional[str] = None
    evidence_package: Dict = field(default_factory=dict)


class ConflictResolver:
    """Арбитражный слой для разрешения противоречий"""
    
    @staticmethod
    def generate_evidence(event: EngineeringEvent, node_ast: Dict) -> Dict:
        """Сгенерировать пакет доказательств для инцидента"""
        evidence = {
            "formal_layer": {},
            "heuristic_layer": {},
            "precedent_layer": "SEARCHING_IN_NAV_SYSTEMS..."
        }
        
        dhatu = node_ast.get("name", "Unknown")
        sig = SanskritPrimitivesV2.get_signature(dhatu)
        
        if event.type == ConflictType.PHYSICAL:
            # Формальный слой: Физика и размерности
            evidence["formal_layer"] = {
                "rule": "Physics > Model",
                "expected_dimensions": [d.value for d in sig["args"]],
                "violation": event.message
            }
            evidence["heuristic_layer"] = {
                "analogy": f"Попытка приложения потенциала к узлу {dhatu} без соблюдения закона сохранения размерности."
            }
            
        elif event.type == ConflictType.ARCHITECTURAL:
            # Формальный слой: Контракт метамодели
            evidence["formal_layer"] = {
                "rule": "METAMODEL_COMPLIANCE",
                "dhatu_signature": {
                    "args_count": len(sig["args"]),
                    "return_type": sig["return"].value
                }
            }
            evidence["heuristic_layer"] = {
                "analogy": f"Вызов {dhatu} не соответствует его функциональной роли в онтологии SOL."
            }
            evidence["precedent_layer"] = SanskritPrimitivesV2.fetch_precedent(
                conflict_type=event.type.value,
                query=event.message
            )
            
        return evidence

    @staticmethod
    def classify_conflict(error_msg: str, node: Dict) -> Tuple[ConflictType, str]:
        """Классифицировать конфликт по сообщению об ошибке"""
        msg = error_msg.lower()
        
        # PHYSICAL
        if "division by zero" in msg or "dimension" in msg or "cannot add" in msg or "cannot subtract" in msg:
            correction = "Проверьте входные параметры на соответствие физическим законам."
            if "dimension" in msg:
                correction = "Размерности аргументов не совпадают. Приоритет: Физика > Модель."
            return ConflictType.PHYSICAL, correction
            
        # ARCHITECTURAL
        if "ожидает" in msg and "аргументов" in msg:
            return ConflictType.ARCHITECTURAL, f"Сигнатура {node['name']} нарушена. Требуется соответствие METAMODEL.md."
            
        # EXISTENTIAL (По умолчанию для неизвестных ошибок)
        return ConflictType.EXISTENTIAL, "Обнаружен логический тупик. Требуется внешняя декомпозиция."


@dataclass
class TypedValue:
    """Типизированное значение с размерностью"""
    value: float
    dimension: Dimension
    unit: str = ""
    guna: Guna = Guna.RAJAS  # По умолчанию для значений - Rajas
    
    def __post_init__(self):
        if not self.unit:
            self.unit = self.dimension.value
    
    def __mul__(self, other: 'TypedValue') -> 'TypedValue':
        return TypedValue(
            value=self.value * other.value,
            dimension=self._combine_dimensions(self.dimension, other.dimension, "mul")
        )
    
    def __truediv__(self, other: 'TypedValue') -> 'TypedValue':
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        return TypedValue(
            value=self.value / other.value,
            dimension=self._combine_dimensions(self.dimension, other.dimension, "div")
        )
    
    def __add__(self, other: 'TypedValue') -> 'TypedValue':
        if self.dimension != other.dimension:
            raise TypeError(f"Cannot add {self.dimension} and {other.dimension}")
        return TypedValue(value=self.value + other.value, dimension=self.dimension)
    
    def __sub__(self, other: 'TypedValue') -> 'TypedValue':
        if self.dimension != other.dimension:
            raise TypeError(f"Cannot subtract {self.dimension} and {other.dimension}")
        return TypedValue(value=self.value - other.value, dimension=self.dimension)
    
    @staticmethod
    def _combine_dimensions(d1: Dimension, d2: Dimension, op: str) -> Dimension:
        """Комбинировать размерности"""
        # Упрощённая версия — в реальности нужно парсить строки
        if op == "mul":
            # Перемножение размерностей
            return Dimension.DIMENSIONLESS  # упрощённо
        else:
            return Dimension.DIMENSIONLESS  # упрощённо


# ============================================================
# ЧАСТЬ 2: ПРИМИТИВЫ С ТИПАМИ (32 DHATU)
# ============================================================

class SanskritPrimitivesV2:
    """Реестр всех 32 санскритских примитивов с типами"""
    
    # СИГНАТУРЫ ТИПОВ
    SIGNATURES = {
        # Базовые (21)
        "√man": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√tulā": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√gaṇana": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√yuj": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√bhaj": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√kṛ": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√hṛ": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√kamp": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√sāmya": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√śās": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√dṛṣṭi": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√liṅga": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√anukaraṇa": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√saha-bhāra": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√gati-jñāna": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√dik-jñāna": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√sthiti": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√vicāra": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√smṛti": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√parīkṣā": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√śaṅkā": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        
        # FLOW:: (7)
        "√srota": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√vidyut": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√tāpa": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√vāta": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        
        # Śilpaśāstra (4)
        "√stambha": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√bhitti": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√pranālī": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√vāstu": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        
        # Sūtra (2)
        "√sūtra": {"args": [Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        "√pramāṇa": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS},
        
        # Yantra (1)
        "√sthāpana": {"args": [Dimension.DIMENSIONLESS, Dimension.DIMENSIONLESS], "return": Dimension.DIMENSIONLESS}
    }
    
    # МАППИНГ ГУН ДЛЯ DHATU
    GUNAS = {
        # Sattva (Ясность/Мета/Измерение)
        "√man": Guna.SATTVA, "√gaṇana": Guna.SATTVA, "√dṛṣṭi": Guna.SATTVA, 
        "√liṅga": Guna.SATTVA, "√sthiti": Guna.SATTVA, "√vicāra": Guna.SATTVA, 
        "√parīkṣā": Guna.SATTVA, "√pramāṇa": Guna.SATTVA, "√smṛti": Guna.SATTVA,
        
        # Rajas (Энергия/Действие/Трансформация)
        "√yuj": Guna.RAJAS, "√bhaj": Guna.RAJAS, "√kṛ": Guna.RAJAS, "√hṛ": Guna.RAJAS,
        "√kamp": Guna.RAJAS, "√sāmya": Guna.RAJAS, "√śās": Guna.RAJAS, 
        "√anukaraṇa": Guna.RAJAS, "√srota": Guna.RAJAS, "√vidyut": Guna.RAJAS,
        "√tāpa": Guna.RAJAS, "√vāta": Guna.RAJAS, "√sūtra": Guna.RAJAS,
        
        # Tamas (Инерция/Фиксация/Материя/Ограничение)
        "√tulā": Guna.TAMAS, "√saha-bhāra": Guna.TAMAS, "√gati-jñāna": Guna.TAMAS,
        "√dik-jñāna": Guna.TAMAS, "√śaṅkā": Guna.TAMAS, "√stambha": Guna.TAMAS,
        "√bhitti": Guna.TAMAS, "√pranālī": Guna.TAMAS, "√vāstu": Guna.TAMAS,
        "√sthāpana": Guna.TAMAS
    }
    
    @staticmethod
    def get_guna(dhatu: str) -> Guna:
        """Получить гуну для dhatu"""
        return SanskritPrimitivesV2.GUNAS.get(dhatu, Guna.RAJAS)

    @staticmethod
    def get_signature(dhatu: str) -> Dict:
        """Получить сигнатуру типа для dhatu"""
        return SanskritPrimitivesV2.SIGNATURES.get(dhatu, {"args": [], "return": Dimension.DIMENSIONLESS})

    @staticmethod
    def fetch_precedent(conflict_type: str, query: str = "") -> Dict:
        """Имитация поиска прецедента в BOOK-NAV / DRAWING-NAV."""
        normalized = (query or "").lower()
        if conflict_type == ConflictType.ARCHITECTURAL.value:
            if "ожидает" in normalized or "аргументов" in normalized or "signature" in normalized:
                return {
                    "precedent_id": "PRC-ARCH-001",
                    "source": "BOOK-NAV",
                    "asset_ref": "BOOK-NAV/docs/architecture/ports-and-contracts.md",
                    "recommendation": "Добавьте явный CON-интерфейс и выровняйте сигнатуру dhatu по контракту METAMODEL.",
                    "confidence": 0.93
                }
            return {
                "precedent_id": "PRC-ARCH-002",
                "source": "DRAWING-NAV",
                "asset_ref": "DRAWING-NAV/docs/interfaces/shaft-gear-coupling.md",
                "recommendation": "Добавьте промежуточный CON-адаптер, задайте типы портов IN/OUT и повторите Validator.",
                "confidence": 0.88
            }

        return {
            "precedent_id": "PRC-NONE",
            "source": "NONE",
            "asset_ref": None,
            "recommendation": "Релевантный прецедент не найден.",
            "confidence": 0.0
        }
    
    @staticmethod
    def apply(dhatu: str, *args) -> Any:
        """Применить примитив с проверкой типов"""
        # Проверка типов
        sig = SanskritPrimitivesV2.get_signature(dhatu)
        if len(args) != len(sig["args"]):
            raise TypeError(f"{dhatu} ожидает {len(sig['args'])} аргументов, получено {len(args)}")
        
        # Проверка размерностей
        for i, arg in enumerate(args):
            if isinstance(arg, TypedValue):
                expected = sig["args"][i]
                if arg.dimension != expected:
                    raise TypeError(f"{dhatu} аргумент {i+1}: ожидается {expected}, получено {arg.dimension}")
        
        # Выполнение
        handlers = {
            "√man": lambda x: TypedValue(float(x) if not isinstance(x, TypedValue) else x.value, Dimension.DIMENSIONLESS),
            "√tulā": lambda a, b: TypedValue(
                (a.value if isinstance(a, TypedValue) else a) / (b.value if isinstance(b, TypedValue) else b) if b != 0 else float('inf'),
                Dimension.DIMENSIONLESS
            ),
            "√gaṇana": lambda items: TypedValue(len(items) if isinstance(items, list) else 1, Dimension.DIMENSIONLESS),
            "√yuj": lambda *args: TypedValue(
                math.prod([a.value if isinstance(a, TypedValue) else a for a in args]),
                Dimension.DIMENSIONLESS
            ),
            "√bhaj": lambda a, b: TypedValue(
                (a.value if isinstance(a, TypedValue) else a) / (b.value if isinstance(b, TypedValue) else b) if b != 0 else float('inf'),
                Dimension.DIMENSIONLESS
            ),
            "√kṛ": lambda state: {**state, "transformed": True},
            "√hṛ": lambda value, limit: TypedValue(
                min(value.value if isinstance(value, TypedValue) else value, limit.value if isinstance(limit, TypedValue) else limit),
                Dimension.DIMENSIONLESS
            ),
            "√kamp": lambda raw, ratio=0.7: TypedValue(
                (raw.value if isinstance(raw, TypedValue) else raw) * (1 - (ratio.value if isinstance(ratio, TypedValue) else ratio)),
                Dimension.DIMENSIONLESS
            ),
            "√sāmya": lambda weights, deltas: SanskritPrimitivesV2._balance(weights, deltas),
            "√śās": lambda risk, lce: {**lce, "N": max(2, lce.get("N", 6) - 0.05 * ((risk.value if isinstance(risk, TypedValue) else risk) > 0.7))},
            "√dṛṣṭi": lambda obs: {"pattern": "observed", "confidence": min(0.6, len(obs) * 0.15)} if obs else {"pattern": None, "confidence": 0.0},
            "√liṅga": lambda symbols: SanskritPrimitivesV2._read(symbols),
            "√anukaraṇa": lambda n, l: [n_i * 0.5 + l_i * 0.5 for n_i, l_i in zip(n, l)],
            "√saha-bhāra": lambda local, neighbors: SanskritPrimitivesV2._distribute(local, neighbors),
            "√gati-jñāna": lambda local, neighbors: sum(neighbors) / len(neighbors) * 0.15 if neighbors else local,
            "√dik-jñāna": lambda local, neighbors: SanskritPrimitivesV2._align(local, neighbors),
            "√sthiti": lambda placement: SanskritPrimitivesV2._analyze(placement),
            "√vicāra": lambda test: {"probe_success": test.get("success", False), "confidence": test.get("confidence", 0.5)},
            "√smṛti": lambda key, value=None: SanskritPrimitivesV2._memory(key, value),
            "√parīkṣā": lambda dev: {"diagnosis": [k for k, v in dev.items() if v > 0.5], "status": "OK" if all(v <= 0.5 for v in dev.values()) else "FAILED"},
            "√śaṅkā": lambda conf: 1.0 - (sum(conf) / len(conf)) if conf else 1.0,
            
            # FLOW::
            "√srota": lambda rate: {"flow": "liquid", "rate": float(rate)},
            "√vidyut": lambda voltage, resistance: voltage / resistance if resistance != 0 else float('inf'),
            "√tāpa": lambda heat: {"flow": "heat", "value": float(heat)},
            "√vāta": lambda gas: {"flow": "gas", "value": float(gas)},
            
            # Śilpaśāstra
            "√stambha": lambda *args: {"support": True, "args": args},
            "√bhitti": lambda boundary: {"boundary": boundary},
            "√pranālī": lambda channel: {"channel": channel},
            "√vāstu": lambda site: {"site": site},
            
            # Sūtra
            "√sūtra": lambda steps: {"algorithm": steps, "type": "SŪTRA"},
            "√pramāṇa": lambda value, norm: {"value": value, "norm": norm, "pass": value <= norm},
            
            # Yantra
            "√sthāpana": lambda site, design: {"deployed": True, "site": site, "design": design}
        }
        
        handler = handlers.get(dhatu)
        if handler:
            return handler(*args)
        raise ValueError(f"Unknown dhatu: {dhatu}")
    
    # ============================================
    # ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ (как в SPC:1.0)
    # ============================================
    
    @staticmethod
    def _balance(weights, deltas):
        import math
        alpha = 1.0
        w = [w.value if isinstance(w, TypedValue) else w for w in weights]
        d = [d.value if isinstance(d, TypedValue) else d for d in deltas]
        raw = [wi * math.exp(-alpha * di**2) for wi, di in zip(w, d)]
        total = sum(raw)
        return [r / total for r in raw] if total > 0 else weights
    
    @staticmethod
    def _read(symbols):
        if not symbols or "weight" not in symbols:
            return {"explicit_constraints": None, "confidence": 0.0}
        return {"explicit_constraints": {"weight": symbols.get("weight")}, "confidence": 0.95}
    
    @staticmethod
    def _distribute(local, neighbors):
        if not neighbors:
            return local
        avg = sum(neighbors) / len(neighbors)
        return max(0.2, min(0.9, local + (avg - local) * 0.25))
    
    @staticmethod
    def _align(local, neighbors):
        if not neighbors:
            return local
        avg_x = sum(v[0] for v in neighbors) / len(neighbors)
        avg_y = sum(v[1] for v in neighbors) / len(neighbors)
        weight = 0.15
        return [local[0] + (avg_x - local[0]) * weight,
                local[1] + (avg_y - local[1]) * weight]
    
    @staticmethod
    def _analyze(placement):
        confidence_map = {"pallet_top": 0.6, "pallet_bottom": 0.3, "stacked_top": 0.7}
        return {"inferred_load_history": placement, "confidence": confidence_map.get(placement, 0.3)}
    
    _memory = {}
    
    @staticmethod
    def _memory(key, value=None):
        if value is not None:
            SanskritPrimitivesV2._memory[key] = value
            return value
        return SanskritPrimitivesV2._memory.get(key)


# ============================================================
# ЧАСТЬ 3: УЛУЧШЕННЫЙ КОМПИЛЯТОР (С ТРАССИРОВКОЙ)
# ============================================================

@dataclass
class TraceStep:
    """Шаг трассировки"""
    step_id: int
    expression: str
    dhatu: str
    args: List[Any]
    result: Any
    guna: Guna
    node_id: str
    timestamp: float = field(default_factory=lambda: math.time() if hasattr(math, 'time') else 0)


class SanskritCompilerV2:
    """Компилятор с трассировкой"""
    
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.node_counter = 0
        self.trace = []
        self.trace_counter = 0
    
    def compile(self, source: str, trace: bool = True) -> Dict:
        """Скомпилировать с трассировкой"""
        self.nodes = []
        self.edges = []
        self.node_counter = 0
        self.trace = []
        self.trace_counter = 0
        
        ast = self._parse(source)
        result = self._compile_ast(ast, trace=trace)
        
        return {
            "ast": ast,
            "eir": {"nodes": self.nodes, "edges": self.edges},
            "result": result,
            "trace": self.trace if trace else None
        }
    
    def _parse(self, source: str) -> Dict:
        source = source.strip()
        # Парсер поддерживает вложенные вызовы и не опирается на regex по ')'.
        if not source.startswith("√"):
            try:
                return {"type": "value", "value": float(source)}
            except ValueError:
                return {"type": "value", "value": source}

        open_idx = source.find("(")
        close_idx = source.rfind(")")
        if open_idx == -1 or close_idx == -1 or close_idx < open_idx:
            try:
                return {"type": "value", "value": float(source)}
            except ValueError:
                return {"type": "value", "value": source}

        dhatu = source[:open_idx]
        args_str = source[open_idx + 1:close_idx]
        
        args = []
        current = ""
        depth = 0
        
        for char in args_str:
            if char == '(':
                depth += 1
                current += char
            elif char == ')':
                depth -= 1
                current += char
            elif char == ',' and depth == 0:
                args.append(current.strip())
                current = ""
            else:
                current += char
        
        if current.strip():
            args.append(current.strip())
        
        parsed_args = []
        for arg in args:
            if arg.strip():
                parsed_args.append(self._parse(arg.strip()))
        
        return {"type": "dhatu", "name": dhatu, "args": parsed_args}
    
    def _compile_ast(self, ast: Dict, trace: bool = True) -> Any:
        if ast["type"] == "value":
            return ast["value"]
        
        node_id = f"NODE_{self.node_counter}"
        self.node_counter += 1
        
        compiled_args = []
        for arg_ast in ast["args"]:
            arg_result = self._compile_ast(arg_ast, trace=trace)
            if isinstance(arg_result, dict) and "node_id" in arg_result:
                compiled_args.append(arg_result.get("result"))
                self.edges.append({"from": arg_result["node_id"], "to": node_id, "type": "PRODUCES"})
            else:
                compiled_args.append(arg_result)
        
        # Проверка типов перед выполнением
        sig = SanskritPrimitivesV2.get_signature(ast["name"])
        typed_args = []
        for i, arg in enumerate(compiled_args):
            if i < len(sig["args"]):
                if isinstance(arg, (int, float)):
                    arg = TypedValue(float(arg), sig["args"][i])
                typed_args.append(arg)
            else:
                typed_args.append(arg)
        
        incident = None
        try:
            result = SanskritPrimitivesV2.apply(ast["name"], *typed_args)
            guna = SanskritPrimitivesV2.get_guna(ast["name"])
        except Exception as e:
            error_msg = str(e)
            conflict_type, correction = ConflictResolver.classify_conflict(error_msg, ast)
            guna = Guna.TAMAS # Ошибка - это инерция
            
            incident = EngineeringEvent(
                event_id=f"EVT_{math.time() if hasattr(math, 'time') else 0}",
                type=conflict_type,
                message=error_msg,
                nodes=[node_id],
                trace=[], # Будет заполнено позже
                correction_prompt=correction
            )
            incident.evidence_package = ConflictResolver.generate_evidence(incident, ast)
            result = {
                "error": error_msg,
                "conflict_type": conflict_type.value,
                "incident_id": incident.event_id,
                "evidence_link": f"SOL_EV_LOG://{incident.event_id}"
            }
        
        # Трассировка
        if trace:
            self.trace_counter += 1
            trace_step = TraceStep(
                step_id=self.trace_counter,
                expression=self._ast_to_string(ast),
                dhatu=ast["name"],
                args=compiled_args,
                result=result,
                guna=guna,
                node_id=node_id
            )
            self.trace.append(trace_step)
            if incident:
                incident.trace = self.trace.copy()
                print(f"\n[ENGINEERING EVENT] {incident.type.value}: {incident.message}")
                print(f"[CORRECTION] {incident.correction_prompt}")
                print(f"[EVIDENCE] Formal Layer: {incident.evidence_package.get('formal_layer', {})}")
                print(f"[EVIDENCE] Precedent Layer: {incident.evidence_package.get('precedent_layer', {})}")
        
        self.nodes.append({
            "id": node_id,
            "type": "OPERATION_NODE",
            "dhatu": ast["name"],
            "args": compiled_args,
            "result": result,
            "guna": guna.value[0],
            "guna_weight": guna.value[1],
            "evidence_link": result.get("evidence_link") if incident else None,
            "status": "COMPLETED" if not incident else "FAILED_CONFLICT"
        })
        
        return {"node_id": node_id, "result": result, "guna_weight": guna.value[1]}
    
    def _ast_to_string(self, ast: Dict) -> str:
        if ast["type"] == "value":
            return str(ast["value"])
        args_str = ", ".join([self._ast_to_string(a) for a in ast["args"]])
        return f"{ast['name']}({args_str})"


# ============================================================
# ЧАСТЬ 4: УЛУЧШЕННЫЙ RUNTIME (С КОНТЕКСТОМ)
# ============================================================

class SanskritRuntimeV2:
    """Runtime с контекстным состоянием"""
    
    def __init__(self):
        self.graph = None
        self.state = {}
        self.context = {}
        self.history = []
    
    def execute(self, compiled: Dict, context: Dict = None) -> Dict:
        """Выполнить с контекстом"""
        self.graph = compiled["eir"]
        if context:
            self.context.update(context)
        
        results = {}
        for node in self.graph["nodes"]:
            if "result" in node:
                results[node["id"]] = node["result"]
        
        self.state.update(results)
        self.history.append({
            "timestamp": math.time() if hasattr(math, 'time') else 0,
            "results": results,
            "context": self.context.copy()
        })
        
        return {
            "results": results,
            "state": self.state,
            "context": self.context,
            "history_count": len(self.history),
            "status": "COMPLETED"
        }
    
    def rollback(self, step: int) -> Dict:
        """Откат до указанного шага"""
        if step >= len(self.history):
            return {"error": f"Step {step} not found"}
        
        # Восстановление состояния до указанного шага
        self.state = {}
        for i in range(step + 1):
            self.state.update(self.history[i]["results"])
        
        return {
            "status": "ROLLBACK_COMPLETED",
            "step": step,
            "state": self.state
        }


# ============================================================
# ЧАСТЬ 5: УЛУЧШЕННОЕ SOLO-ЯДРО (SPC:2.0)
# ============================================================

class SanskritSoloCoreV2:
    """
    SOLO-ЯДРО SPC:2.0
    TYPE_SAFE + PHYSICAL + CONTEXT + TRACE
    """
    
    def __init__(self):
        self.core_id = "SPC:2.0"
        self.name = "Sanskrit Primitive Compiler (Type Safe)"
        self.version = "2.0"
        self.primitives = SanskritPrimitivesV2()
        self.compiler = SanskritCompilerV2()
        self.runtime = SanskritRuntimeV2()
        
        self.state = {}
        self.history = []
    
    def evaluate(self, expression: str, context: Dict = None) -> Dict:
        """Выполнить выражение с трассировкой и контекстом"""
        if context:
            # Подстановка context('key') до этапа компиляции.
            def _replace_context(match):
                key = match.group(1)
                value = context.get(key)
                if isinstance(value, (int, float)):
                    return str(value)
                return "0"

            expression = re.sub(r"context\('([^']+)'\)", _replace_context, expression)

        # Шаг 1: Компиляция с трассировкой
        compiled = self.compiler.compile(expression, trace=True)
        
        # Шаг 2: Исполнение с контекстом
        result = self.runtime.execute(compiled, context)
        
        # Шаг 3: Сохранение истории
        self.history.append({
            "expression": expression,
            "compiled": compiled,
            "result": result
        })
        
        return {
            "expression": expression,
            "result": result.get("results", {}),
            "graph": compiled["eir"],
            "trace": compiled["trace"],
            "state": self.runtime.state,
            "context": self.runtime.context,
            "status": "COMPLETED"
        }
    
    def rollback(self, step: int) -> Dict:
        """Откат до указанного шага"""
        return self.runtime.rollback(step)
    
    def get_trace(self) -> List:
        """Получить трассировку последнего выполнения"""
        if self.history:
            return self.history[-1]["compiled"]["trace"]
        return []
    
    def explain(self, dhatu: str) -> Dict:
        """Объяснить примитив с типами"""
        sig = SanskritPrimitivesV2.get_signature(dhatu)
        return {
            "dhatu": dhatu,
            "signature": sig,
            "available": dhatu in SanskritPrimitivesV2.SIGNATURES
        }


# ============================================================
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
# ============================================================

if __name__ == "__main__":
    core = SanskritSoloCoreV2()
    
    print("=" * 60)
    print(f"SOLO-ЯДРО SPC:2.0 АКТИВИРОВАНО")
    print(f"ID: {core.core_id}")
    print(f"Улучшения: TYPE_SAFE + PHYSICAL + CONTEXT + TRACE")
    print("=" * 60)
    
    # ТЕСТ 1: ТИПИЗИРОВАННОЕ ВЫРАЖЕНИЕ
    print("\n--- ТЕСТ 1: √yuj(5, 10) С ТИПАМИ ---")
    result = core.evaluate("√yuj(5, 10)")
    print(f"Результат: {result['result']}")
    print(f"Трассировка: {len(result['trace'])} шагов")
    
    # ТЕСТ 2: С КОНТЕКСТОМ
    print("\n--- ТЕСТ 2: С КОНТЕКСТОМ ---")
    result = core.evaluate("√yuj(context('power'), context('speed'))", 
                          context={"power": 5.5, "speed": 1500})
    print(f"Результат: {result['result']}")
    
    # ТЕСТ 3: ОШИБКА ТИПА
    print("\n--- ТЕСТ 3: ПРОВЕРКА ТИПОВ ---")
    try:
        result = core.evaluate("√yuj('string', 10)")
        print(f"Результат: {result['result']}")
    except Exception as e:
        print(f"Ошибка (ожидаемая): {e}")
    
    # ТЕСТ 4: ТРАССИРОВКА
    print("\n--- ТЕСТ 4: ТРАССИРОВКА ---")
    result = core.evaluate("√tulā(√man(10), 5)")
    trace = result['trace']
    for step in trace:
        print(f"  Шаг {step.step_id}: {step.expression} → {step.result}")
    
    # ТЕСТ 5: ОБЪЯСНЕНИЕ ПРИМИТИВА
    print("\n--- ТЕСТ 5: ОБЪЯСНЕНИЕ ---")
    expl = core.explain("√yuj")
    print(f"Сигнатура √yuj: {expl['signature']}")