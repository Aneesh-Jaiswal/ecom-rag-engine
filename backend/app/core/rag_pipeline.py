from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import logging
import time
from typing import AsyncGenerator, List
from app.core.config import settings
from app.core.vector_store import VectorStoreManager
from app.models.schemas import ChatMessage, RAGResponse, RetrievedChunk

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are ShopBot, an expert e-commerce assistant.
Use ONLY the retrieved product context to answer questions.
- Mention exact product names, prices, specs from the context
- Compare products when multiple options are available
- If no relevant products found, say so honestly
- Never make up product details"""


class RAGPipeline:
    def __init__(self, vector_store_manager: VectorStoreManager):
        self.vsm = vector_store_manager
        self.llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS,
            openai_api_key=settings.OPENAI_API_KEY,
        )
        self.retriever = self.vsm.get_retriever(k=settings.TOP_K_RETRIEVAL)
        logger.info("RAGPipeline initialized")

    async def query(self, question: str, chat_history: List = [], session_id: str = "default") -> RAGResponse:
        start = time.perf_counter()
        docs = await self.retriever.ainvoke(question)
        if docs:
            parts = [f"[{doc.metadata.get('name', 'Product')} - ${doc.metadata.get('price', 0)}]\n{doc.page_content}" for doc in docs]
            context = "\n\n".join(parts)
        else:
            context = "No matching products found."
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}"),
        ]
        response = await self.llm.ainvoke(messages)
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        sources = [
            RetrievedChunk(
                product_id=doc.metadata.get("product_id", ""),
                product_name=doc.metadata.get("name", "Unknown"),
                content=doc.page_content,
                score=round(0.95 - i * 0.05, 2),
                category=doc.metadata.get("category", ""),
            )
            for i, doc in enumerate(docs)
        ]
        return RAGResponse(
            answer=response.content,
            sources=sources,
            rewritten_query=question,
            latency_ms=latency_ms,
            model=settings.LLM_MODEL,
            session_id=session_id,
        )

    async def stream_query(self, question: str, chat_history: List = []) -> AsyncGenerator[str, None]:
        docs = await self.retriever.ainvoke(question)
        parts = [f"[{doc.metadata.get('name', 'Product')} - ${doc.metadata.get('price', 0)}]\n{doc.page_content}" for doc in docs]
        context = "\n\n".join(parts) if parts else "No matching products found."
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}"),
        ]
        async for chunk in self.llm.astream(messages):
            if chunk.content:
                yield chunk.content
