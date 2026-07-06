"""
TDI_Runtime_Prototype.py
Прототип для расчета TDI (Tensor Divergence Index).
Используется для локализации конфликтов в нагрузочных путях.
"""
import math

class TDIEvaluator:
    @staticmethod
    def calculate(p_vec, c_vec):
        """Расчет дивергенции: |P x C| / (|P|*|C|)"""
        x = p_vec[1]*c_vec[2] - p_vec[2]*c_vec[1]
        y = p_vec[2]*c_vec[0] - p_vec[0]*c_vec[2]
        z = p_vec[0]*c_vec[1] - p_vec[1]*c_vec[0]
        
        cross_mag = math.sqrt(x**2 + y**2 + z**2)
        p_mag = math.sqrt(sum(i**2 for i in p_vec))
        c_mag = math.sqrt(sum(i**2 for i in c_vec))
        
        return cross_mag / (p_mag * c_mag) if (p_mag * c_mag) > 0 else 0

if __name__ == "__main__":
    # Пример: Подшипник [BRG]
    prop = (1.0, 0.0, 0.0) 
    constr = (0.0, 0.5, 0.5)
    print(f"TDI Score: {TDIEvaluator.calculate(prop, constr):.4f}")