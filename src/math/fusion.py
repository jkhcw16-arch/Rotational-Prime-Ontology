from src.core.models import ProjectionResult, FusionResult
from typing import Dict


def fuse(projections: Dict[str, ProjectionResult]) -> FusionResult:
    fused_metrics = {}

    for domain, result in projections.items():
        for k, v in result.data.items():
            fused_metrics[k] = fused_metrics.get(k, 0.0) + float(v)

    invariants = {
        "fusion_integrity": True,
        "domains_count": len(projections),
    }

    return FusionResult(domains=projections, fused_metrics=fused_metrics, invariants=invariants)
