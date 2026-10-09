from .primes import PRIMES
from typing import Dict, List

def encode_event(exponents: Dict[int, int]) -> int:
    """
    Encode an event as a composite integer:
    M = ∏ p^{r_p}
    exponents: {prime: exponent}
    """
    value = 1
    for p in PRIMES:
        r = exponents.get(p, 0)
        if r != 0:
            value *= p ** r
    return value

def decode_event(value: int) -> Dict[int, int]:
    """
    Factor composite integer back into prime exponents.
    """
    exps: Dict[int, int] = {}
    for p in PRIMES:
        r = 0
        while value % p == 0:
            value //= p
            r += 1
        if r > 0:
            exps[p] = r
    return exps
