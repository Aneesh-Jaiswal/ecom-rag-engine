"""
E-Commerce Product Q&A Engine
FastAPI Backend with LangChain + RAG Pipeline
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
import logging
import time

from app.api.routes import chat, products, health, analytics
from app.core.config import settings
from app.core.vector_store import VectorStoreManager
from app.core.metrics import MetricsCollector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle."""
    logger.info("🚀 Starting E-Commerce RAG Engine...")
    # Initialize vector store on startup
    vs_manager = VectorStoreManager()
    await vs_manager.initialize()
    app.state.vector_store = vs_manager
    app.state.metrics = MetricsCollector()
    app.state.start_time = time.time()
    logger.info("✅ Vector store initialized successfully")
    yield
    logger.info("🛑 Shutting down...")


app = FastAPI(
    title="E-Commerce Product Q&A Engine",
    description="Production-grade RAG pipeline for product intelligence",
    version="1.0.0",
    lifespan=lifespan,
)

# Middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])
app.include_router(products.router, prefix="/api/v1", tags=["Products"])
app.include_router(analytics.router, prefix="/api/v1", tags=["Analytics"])


@app.get("/")
async def root():
    return {
        "service": "E-Commerce Product Q&A Engine",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs",
    }
