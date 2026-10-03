from src.core.models import Embedding


def build_cps_embedding(case_data: dict) -> Embedding:
    # Example feature extraction (stub)
    vector = {
        "risk_intensity": float(case_data.get("risk_intensity", 0.0)),
        "vulnerability_index": float(case_data.get("vulnerability_index", 0.0)),
        "protective_strength": float(case_data.get("protective_strength", 0.0)),
    }

    invariants = {
        "domain_integrity": True,
        "normalized_values": all(0.0 <= v <= 1.0 for v in vector.values()),
    }

    return Embedding(domain="CPS", vector=vector, invariants=invariants)
