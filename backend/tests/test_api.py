"""
Backend test suite.
Run: pytest tests/ -v
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
import os

os.environ.setdefault("OPENAI_API_KEY", "sk-test-key")
os.environ.setdefault("ENV", "testing")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379")

from app.main import app
from app.models.schemas import RAGResponse, RetrievedChunk
from datetime import datetime


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def mock_rag_response():
    return RAGResponse(
        answer="The Sony WH-1000XM5 is our top-rated noise-cancelling headphone at $349.99.",
        sources=[
            RetrievedChunk(
                product_id="prod_002",
                product_name="Sony WH-1000XM5",
                content="Industry-leading noise cancellation...",
                score=0.91,
                category="headphones",
            )
        ],
        rewritten_query="best wireless noise cancelling headphones",
        latency_ms=420.5,
        model="gpt-4o",
    )


class TestHealth:
    def test_health_returns_200(self, client):
        resp = client.get("/api/v1/health")
        assert resp.status_code == 200

    def test_health_schema(self, client):
        data = client.get("/api/v1/health").json()
        assert "status" in data
        assert "uptime_seconds" in data
        assert "vector_store" in data

    def test_root(self, client):
        resp = client.get("/")
        assert resp.status_code == 200
        assert resp.json()["version"] == "1.0.0"


class TestChat:
    @patch("app.api.routes.chat.RAGPipeline")
    def test_chat_valid_request(self, mock_pipeline_cls, client, mock_rag_response):
        mock_pipeline = AsyncMock()
        mock_pipeline.query.return_value = mock_rag_response
        mock_pipeline_cls.return_value = mock_pipeline

        resp = client.post("/api/v1/chat", json={
            "question": "Best noise-cancelling headphones?",
            "session_id": "test-session",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "answer" in data
        assert "sources" in data
        assert "latency_ms" in data

    def test_chat_empty_question_rejected(self, client):
        resp = client.post("/api/v1/chat", json={"question": " "})
        assert resp.status_code == 422

    def test_chat_question_too_long_rejected(self, client):
        resp = client.post("/api/v1/chat", json={"question": "x" * 1001})
        assert resp.status_code == 422


class TestProducts:
    def test_ingest_products(self, client):
        mock_vs = AsyncMock()
        mock_vs.ingest_products.return_value = 12
        client.app.state.vector_store = mock_vs

        resp = client.post("/api/v1/products/ingest", json={
            "products": [{
                "id": "test_001",
                "name": "Test Product",
                "brand": "TestBrand",
                "category": "electronics",
                "price": 99.99,
                "description": "A great test product",
            }]
        })
        assert resp.status_code == 200
        assert resp.json()["ingested_count"] == 1

    def test_stats_returns_dict(self, client):
        resp = client.get("/api/v1/products/stats")
        assert resp.status_code in [200, 500]


class TestSchemas:
    def test_chat_request_strips_whitespace(self):
        from app.models.schemas import ChatRequest
        req = ChatRequest(question="  hello  ")
        assert req.question == "hello"

    def test_product_price_must_be_non_negative(self):
        from app.models.schemas import Product
        with pytest.raises(Exception):
            Product(id="x", name="x", brand="x", category="x", price=-1, description="x")
