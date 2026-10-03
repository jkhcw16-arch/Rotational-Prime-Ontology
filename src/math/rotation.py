from src.core.models import Embedding
from typing import Dict


def theta(p: int) -> Dict[str, float]:
    # Stub: prime-indexed weights
    return {"weight": float(p)}


def rotate(embedding: Embedding, p: int) -> Embedding:
    weights = theta(p)
    factor = weights["weight"]

    rotated_vector = {k: v * factor for k, v in embedding.vector.items()}

    invariants = dict(embedding.invariants)
    invariants["rotation_applied"] = True

    return Embedding(
        domain=embedding.domain,
        vector=rotated_vector,
        invariants=invariants,
    )
