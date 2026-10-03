from src.core.models import Embedding


def build_crime_embedding(crime_data: dict) -> Embedding:
    vector = {
        "offense_harm": float(crime_data.get("offense_harm", 0.0)),
        "mens_rea_level": float(crime_data.get("mens_rea_level", 0.0)),
        "evidence_strength": float(crime_data.get("evidence_strength", 0.0)),
        "victim_vulnerability": float(crime_data.get("victim_vulnerability", 0.0)),
    }

    invariants = {
        "domain_integrity": True,
        "normalized_values": all(0.0 <= v <= 1.0 for v in vector.values()),
    }

    return Embedding(domain="Crime", vector=vector, invariants=invariants)
