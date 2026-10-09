from typing import Dict
from .operator_role import Operator, Role

def rollback_exponent(exponent: int, operator: Operator, role: Role) -> int:
    """
    M_rollback = M · p^{-Δ(O,R)}
    """
    delta = - (0 if operator == "-" else int(role))
    return exponent + delta

def rollback_event(exponents: Dict[int, int],
                   prime: int,
                   operator: Operator,
                   role: Role) -> Dict[int, int]:
    new_exps = dict(exponents)
    new_exps[prime] = rollback_exponent(new_exps.get(prime, 0), operator, role)
    return new_exps
