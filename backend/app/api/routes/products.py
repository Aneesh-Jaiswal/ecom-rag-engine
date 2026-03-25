"""
Products API Routes
- POST /products/ingest  — bulk ingest product catalog
- POST /products/search  — semantic product search
- GET  /products/stats   — collection statistics
"""

from fastapi import APIRouter, Request, HTTPException
import logging

from app.models.schemas import (
    ProductIngestRequest,
    ProductIngestResponse,
    ProductSearchRequest,
    ProductSearchResponse,
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/products/ingest", response_model=ProductIngestResponse)
async def ingest_products(request: Request, body: ProductIngestRequest):
    """
    Bulk ingest product catalog into the vector store.
    Products are chunked, embedded, and stored with metadata.
    """
    try:
        vs = request.app.state.vector_store
        products_data = [p.model_dump() for p in body.products]
        chunk_count = await vs.ingest_products(products_data)

        return ProductIngestResponse(
            ingested_count=len(body.products),
            chunk_count=chunk_count,
            message=f"Successfully ingested {len(body.products)} products ({chunk_count} chunks)",
        )
    except Exception as e:
        logger.exception(f"Ingestion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products/search", response_model=ProductSearchResponse)
async def search_products(request: Request, body: ProductSearchRequest):
    """
    Semantic similarity search over the product catalog.
    Supports optional category filtering.
    """
    try:
        vs = request.app.state.vector_store
        filters = {}
        if body.category:
            filters["category"] = body.category

        docs = await vs.similarity_search(
            query=body.query,
            k=body.k,
            filters=filters or None,
        )

        results = [
            {
                "product_id": doc.metadata.get("product_id"),
                "name": doc.metadata.get("name"),
                "category": doc.metadata.get("category"),
                "price": doc.metadata.get("price"),
                "brand": doc.metadata.get("brand"),
                "rating": doc.metadata.get("rating"),
                "excerpt": doc.page_content[:200] + "...",
            }
            for doc in docs
        ]

        # Filter by price range if provided
        if body.min_price is not None:
            results = [r for r in results if (r["price"] or 0) >= body.min_price]
        if body.max_price is not None:
            results = [r for r in results if (r["price"] or 0) <= body.max_price]

        return ProductSearchResponse(
            results=results,
            query=body.query,
            total=len(results),
        )
    except Exception as e:
        logger.exception(f"Search error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products/stats")
async def collection_stats(request: Request):
    """Return vector store collection statistics."""
    vs = request.app.state.vector_store
    return await vs.get_collection_stats()
