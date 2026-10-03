from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Embedding:
    domain: str
    vector: Dict[str, float]
    invariants: Dict[str, bool]


@dataclass
class ProjectionResult:
    domain: str
    stage: str  # "phi1" | "phi2" | "phi3"
    data: Dict[str, Any]


@dataclass
class FusionResult:
    domains: Dict[str, ProjectionResult]
    fused_metrics: Dict[str, float]
    invariants: Dict[str, bool]


@dataclass
class GovernanceDecision:
    authorized: bool
    predicates: Dict[str, bool]
    reason: str
    trace_id: str
