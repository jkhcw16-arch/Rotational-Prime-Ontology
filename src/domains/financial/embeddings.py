from src.core.models import Embedding


def build_financial_embedding(market_data: dict) -> Embedding:
    vector = {
        "volatility": float(market_data.get("volatility", 0.0)),
        "liquidity": float(market_data.get("liquidity", 0.0)),
        "debt_load": float(market_data.get("debt_load", 0.0)),
        "growth_potential": float(market_data.get("growth_potential", 0.0)),
    }

    invariants = {
        "domain_integrity": True,
        "normalized_values": all(0.0 <= v <= 1.0 for v in vector.values()),
    }

    return Embedding(domain="Financial", vector=vector, invariants=invariants)
