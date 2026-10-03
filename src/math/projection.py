from src.core.models import Embedding, ProjectionResult


def phi1_analysis(embedding: Embedding) -> ProjectionResult:
    return ProjectionResult(
        domain=embedding.domain,
        stage="phi1",
        data={"analysis_score": sum(embedding.vector.values())},
    )


def phi2_alignment(embedding: Embedding) -> ProjectionResult:
    return ProjectionResult(
        domain=embedding.domain,
        stage="phi2",
        data={"alignment_score": max(embedding.vector.values())},
    )


def phi3_response(embedding: Embedding) -> ProjectionResult:
    return ProjectionResult(
        domain=embedding.domain,
        stage="phi3",
        data={"response_intensity": min(embedding.vector.values())},
    )
