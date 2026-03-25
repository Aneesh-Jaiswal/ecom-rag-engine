"""Analytics route — thin wrapper around MetricsCollector."""
from fastapi import APIRouter, Request
from app.models.schemas import AnalyticsResponse

router = APIRouter()


@router.get("/analytics", response_model=AnalyticsResponse)
async def get_analytics(request: Request):
    """Return aggregated usage analytics."""
    return request.app.state.metrics.get_summary()
