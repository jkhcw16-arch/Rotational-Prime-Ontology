from typing import Dict

def temporal_risk_equilibrium(exponents: Dict[int, int],
                              risk: float,
                              alpha: float = 1.0,
                              beta: float = 1.0,
                              prime_for_delta: int = 3) -> float:
    """
    E = α·Δr_p + β·risk
    """
    delta_r = exponents.get(prime_for_delta, 0)
    return alpha * delta_r + beta * risk

def should_escalate(E: float, threshold: float) -> bool:
    return E > threshold
