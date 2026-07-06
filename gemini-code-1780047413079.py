"""
TDI_Runtime_Prototype.py
Прототип для расчета индекса тензорной дивергенции (TDI).
Используется для локализации конфликтов ограничений в узлах.
"""

import math

class TDIEvaluator:
    @staticmethod
    def calculate(prop_vector, constr_vector):
        """TDI = |Propagation × Constraint| / (|P|*|C|)"""
        # Векторное произведение
        x = prop_vector[1]*constr_vector[2] - prop_vector[2]*constr_vector[1]
        y = prop_vector[2]*constr_vector[0] - prop_vector[0]*constr_vector[2]
        z = prop_vector[0]*constr_vector[1] - prop_vector[1]*constr_vector[0]
        
        cross_mag = math.sqrt(x**2 + y**2 + z**2)
        p_mag = math.sqrt(sum(i**2 for i in prop_vector))
        c_mag = math.sqrt(sum(i**2 for i in constr_vector))
        
        return cross_mag / (p_mag * c_mag) if (p_mag * c_mag) > 0 else 0

def run_diagnostic():
    print("--- SOL-CAD Diagnostic Runtime ---")
    # Пример: Подшипник ([BRG])
    prop = (1.0, 0.0, 0.0)  # Вращательный поток
    constr = (0.0, 0.5, 0.5) # Конфликт ограничения
    
    tdi = TDIEvaluator.calculate(prop, constr)
    status = "CRITICAL" if tdi > 0.5 else "NOMINAL"
    
    print(f"Metric: TDI = {tdi:.4f}")
    print(f"Diagnostic Status: {status}")

if __name__ == "__main__":
    run_diagnostic()