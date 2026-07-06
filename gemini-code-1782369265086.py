"""
EPMS Adapter: Bolt
Status: STABLE
"""

def map_bolt(torque_nm: float, vibration_hz: float, thread_damage: float, pretension: float) -> dict:
    MAX_TORQUE = 150.0
    MAX_VIB = 100.0
    MAX_DAMAGE = 1.0
    REQ_PRETENSION = 10.0

    return {
        "effort": min(max(torque_nm / MAX_TORQUE, 0.0), 1.0),
        "velocity": min(max(vibration_hz / MAX_VIB, 0.0), 1.0),
        "wear": min(max(thread_damage / MAX_DAMAGE, 0.0), 1.0),
        "stability": min(max(pretension / REQ_PRETENSION, 0.0), 1.0)
    }