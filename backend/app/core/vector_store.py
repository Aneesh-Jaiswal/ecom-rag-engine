from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging
from typing import List, Optional
from app.core.config import settings

logger = logging.getLogger(__name__)

class VectorStoreManager:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            openai_api_key=settings.OPENAI_API_KEY,
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )
        self._store = None

    async def initialize(self):
        self._store = Chroma(
            collection_name="ecom_products",
            embedding_function=self.embeddings,
            persist_directory=settings.CHROMA_PERSIST_DIR,
        )
        logger.info(f"ChromaDB initialized at {settings.CHROMA_PERSIST_DIR}")

    def get_retriever(self, k: int = 5) -> VectorStoreRetriever:
        return self._store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k},
        )

    async def ingest_products(self, products: List[dict]) -> int:
        documents = []
        for product in products:
            text = self._product_to_text(product)
            chunks = self.text_splitter.split_text(text)
            for i, chunk in enumerate(chunks):
                doc = Document(
                    page_content=chunk,
                    metadata={
                        "product_id": product["id"],
                        "name": product["name"],
                        "price": product.get("price", 0),
                        "category": product.get("category", ""),
                        "brand": product.get("brand", ""),
                        "rating": product.get("rating", 0),
                    },
                )
                documents.append(doc)
        await self._store.aadd_documents(documents)
        logger.info(f"Ingested {len(documents)} chunks from {len(products)} products")
        return len(documents)

    def _product_to_text(self, product: dict) -> str:
        specs_text = ""
        if specs := product.get("specs"):
            specs_text = "\n".join(f"- {k}: {v}" for k, v in specs.items())
        tags_text = ", ".join(product.get("tags", []))
        return f"""Product: {product["name"]}
Brand: {product.get("brand", "N/A")}
Category: {product.get("category", "N/A")}
Price: ${product.get("price", 0):.2f}
Rating: {product.get("rating", 0)}/5
Description: {product.get("description", "")}
Specifications:\n{specs_text}
Tags: {tags_text}""".strip()

    async def similarity_search(self, query: str, k: int = 5, filters: Optional[dict] = None) -> List[Document]:
        return await self._store.asimilarity_search(query, k=k)

    async def get_collection_stats(self) -> dict:
        count = -1
        try:
            if hasattr(self._store, "_collection"):
                count = self._store._collection.count()
        except Exception:
            pass
        return {"total_chunks": count, "backend": settings.VECTOR_STORE}
