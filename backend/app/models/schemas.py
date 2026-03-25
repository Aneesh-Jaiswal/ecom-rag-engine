"""
Pydantic Schemas — Request / Response models for all API endpoints.
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


# ── Enums ──────────────────────────────────────────────────────────────────────

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


# ── Chat ───────────────────────────────────────────────────────────────────────

class ChatMessage(BaseModel):
    role: MessageRole
    content: str
    timestamp: Optional[datetime] = None


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=1000)
    session_id: str = Field(default="default", max_length=64)
    chat_history: List[ChatMessage] = Field(default=[])
    filters: Optional[Dict[str, Any]] = None  # e.g. {"category": "laptops"}
    stream: bool = False

    @validator("question")
    def strip_question(cls, v):
        return v.strip()


class RetrievedChunk(BaseModel):
    product_id: str
    product_name: str
    content: str
    score: float
    category: str


class RAGResponse(BaseModel):
    answer: str
    sources: List[RetrievedChunk]
    rewritten_query: str
    latency_ms: float
    model: str
    session_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# ── Products ───────────────────────────────────────────────────────────────────

class ProductSpec(BaseModel):
    key: str
    value: str


class Product(BaseModel):
    id: str
    name: str
    brand: str
    category: str
    price: float = Field(..., ge=0)
    description: str
    specs: Dict[str, str] = {}
    tags: List[str] = []
    rating: float = Field(default=0.0, ge=0.0, le=5.0)
    review_count: int = Field(default=0, ge=0)
    in_stock: bool = True
    image_url: Optional[str] = None


class ProductIngestRequest(BaseModel):
    products: List[Product]


class ProductIngestResponse(BaseModel):
    ingested_count: int
    chunk_count: int
    message: str


class ProductSearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    k: int = Field(default=5, ge=1, le=20)
    category: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None


class ProductSearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    query: str
    total: int


# ── Analytics ─────────────────────────────────────────────────────────────────

class QueryLog(BaseModel):
    session_id: str
    question: str
    rewritten_query: str
    answer_length: int
    source_count: int
    latency_ms: float
    model: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AnalyticsResponse(BaseModel):
    total_queries: int
    avg_latency_ms: float
    avg_sources_used: float
    top_categories: List[Dict[str, Any]]
    queries_last_hour: int


# ── Health ─────────────────────────────────────────────────────────────────────

class HealthResponse(BaseModel):
    status: str
    uptime_seconds: float
    vector_store: str
    llm_model: str
    cache_enabled: bool
    version: str = "1.0.0"
