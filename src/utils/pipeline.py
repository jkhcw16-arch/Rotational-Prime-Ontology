from src.domains.cps.embedding import build_cps_embedding
from src.domains.financial.embedding import build_financial_embedding
from src.domains.crime.embedding import build_crime_embedding
from src.math.rotation import rotate
from src.math.projection import phi1_analysis, phi2_alignment, phi3_response
from src.math.fusion import fuse
from src.governance.predicates import authorize


def run_full_pipeline(cps_data, financial_data, crime_data, p: int):
    cps = rotate(build_cps_embedding(cps_data), p)
    fin = rotate(build_financial_embedding(financial_data), p)
    crm = rotate(build_crime_embedding(crime_data), p)

    projections = {
        "CPS": phi3_response(cps),
        "Financial": phi3_response(fin),
        "Crime": phi3_response(crm),
    }

    fusion = fuse(projections)
    decision = authorize(fusion)
    return fusion, decision
