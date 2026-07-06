"""
EPMS Adapter: Spring
Status: STABLE
"""

def map_spring(load_n: float, compression_speed: float, cycles: int, resonance_margin: float) -> dict:
    MAX_LOAD = 5000.0
    MAX_SPEED = 2.0
    MAX_CYCLES = 1000000
    IDEAL_MARGIN = 50.0

    return {
        "effort": min(max(load_n / MAX_LOAD, 0.0), 1.0),
        "velocity": min(max(compression_speed / MAX_SPEED, 0.0), 1.0),
        "wear": min(max(cycles / MAX_CYCLES, 0.0), 1.0),
        "stability": min(max(resonance_margin / IDEAL_MARGIN, 0.0), 1.0)
    }