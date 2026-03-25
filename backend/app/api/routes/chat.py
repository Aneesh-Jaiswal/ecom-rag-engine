"""
Chat API Routes
- POST /chat        — standard Q&A
- POST /chat/stream — streaming SSE response
"""

from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import StreamingResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
import logging
import json

from app.models.schemas import ChatRequest, RAGResponse
from app.core.rag_pipeline import RAGPipeline
from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


def get_rag_pipeline(request: Request) -> RAGPipeline:
    """Dependency: lazily instantiate RAGPipeline per request."""
    if not hasattr(request.app.state, "rag_pipeline"):
        request.app.state.rag_pipeline = RAGPipeline(request.app.state.vector_store)
    return request.app.state.rag_pipeline


@router.post("/chat", response_model=RAGResponse)
@limiter.limit(f"{settings.RATE_LIMIT_PER_MINUTE}/minute")
async def chat(
    request: Request,
    body: ChatRequest,
    rag: RAGPipeline = Depends(get_rag_pipeline),
):
    """
    Standard Q&A endpoint. Returns full answer with source attribution.

    Example request:
    {
        "question": "What's the best laptop under $1000?",
        "session_id": "user-abc123",
        "filters": {"category": "laptops"}
    }
    """
    try:
        response = await rag.query(
            question=body.question,
            chat_history=body.chat_history,
            session_id=body.session_id,
        )
        response.session_id = body.session_id

        # Log to metrics collector
        request.app.state.metrics.log_query(
            session_id=body.session_id,
            question=body.question,
            rewritten_query=response.rewritten_query,
            latency_ms=response.latency_ms,
            source_count=len(response.sources),
        )

        return response

    except Exception as e:
        logger.exception(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/chat/stream")
@limiter.limit(f"{settings.RATE_LIMIT_PER_MINUTE}/minute")
async def chat_stream(
    request: Request,
    body: ChatRequest,
    rag: RAGPipeline = Depends(get_rag_pipeline),
):
    """
    Streaming endpoint using Server-Sent Events (SSE).
    Tokens are streamed as they are generated.
    """

    async def event_generator():
        try:
            async for token in rag.stream_query(
                question=body.question,
                chat_history=body.chat_history,
            ):
                payload = json.dumps({"token": token})
                yield f"data: {payload}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
