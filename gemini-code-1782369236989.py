"""
EPMS Adapter: Bearing
Status: STABLE
"""

def map_bearing(force_n: float, rpm: float, fatigue_hours: float, clearance_mm: float) -> dict:
    MAX_FORCE = 10000.0
    MAX_RPM = 3000.0
    MAX_FATIGUE = 50000.0
    MAX_CLEARANCE = 0.05

    return {
        "effort": min(max(force_n / MAX_FORCE, 0.0), 1.0),
        "velocity": min(max(rpm / MAX_RPM, 0.0), 1.0),
        "wear": min(max(fatigue_hours / MAX_FATIGUE, 0.0), 1.0),
        "stability": max(0.0, 1.0 - (clearance_mm / MAX_CLEARANCE))
    }