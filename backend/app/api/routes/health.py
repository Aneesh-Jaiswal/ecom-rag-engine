"""Health & Analytics routes."""

from fastapi import APIRouter, Request
import time
from app.models.schemas import HealthResponse, AnalyticsResponse
from app.core.config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health(request: Request):
    uptime = time.time() - request.app.state.start_time
    return HealthResponse(
        status="healthy",
        uptime_seconds=round(uptime, 2),
        vector_store=settings.VECTOR_STORE,
        llm_model=settings.LLM_MODEL,
        cache_enabled=True,
    )


@router.get("/analytics", response_model=AnalyticsResponse)
async def analytics(request: Request):
    return request.app.state.metrics.get_summary()
