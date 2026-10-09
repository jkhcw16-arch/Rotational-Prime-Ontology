from typing import Literal

Operator = Literal["+", "-"]
Role = Literal[1, 2]

def delta(operator: Operator, role: Role) -> int:
    """
    Δ(O,R) = 0 if O = -
             R if O = +
    """
    if operator == "-":
        return 0
    return int(role)

def apply_delta(exponent: int, operator: Operator, role: Role) -> int:
    return exponent + delta(operator, role)
