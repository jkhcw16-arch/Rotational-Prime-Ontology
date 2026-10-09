from typing import Dict
from .operator_role import Operator, Role, apply_delta

def correct_anomaly(exponents: Dict[int, int],
                    prime: int,
                    operator: Operator,
                    role: Role) -> Dict[int, int]:
    """
    M_corrected = M' · p^{Δ(O,R)}
    """
    new_exps = dict(exponents)
    new_exps[prime] = apply_delta(new_exps.get(prime, 0), operator, role)
    return new_exps
