from src.core.models import FusionResult, GovernanceDecision
import uuid


def adequacy(fusion: FusionResult) -> bool:
    return fusion.fused_metrics.get("analysis_score", 0.0) > 0.0


def minimal_intrusion(fusion: FusionResult) -> bool:
    return fusion.fused_metrics.get("response_intensity", 0.0) <= 1.0


def policy_compliance(fusion: FusionResult) -> bool:
    return True  # Stub: hook to policy engine


def authorize(fusion: FusionResult) -> GovernanceDecision:
    preds = {
        "adequacy": adequacy(fusion),
        "minimal_intrusion": minimal_intrusion(fusion),
        "policy_compliance": policy_compliance(fusion),
    }

    authorized = all(preds.values())

    return GovernanceDecision(
        authorized=authorized,
        predicates=preds,
        reason="All predicates satisfied" if authorized else "One or more predicates failed",
        trace_id=str(uuid.uuid4()),
    )
