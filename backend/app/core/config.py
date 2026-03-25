from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "EcomRAG Engine"
    ENV: str = Field(default="development", env="ENV")
    DEBUG: bool = Field(default=False, env="DEBUG")
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "*"]
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    LLM_MODEL: str = Field(default="gpt-4o", env="LLM_MODEL")
    EMBEDDING_MODEL: str = Field(default="text-embedding-3-small", env="EMBEDDING_MODEL")
    LLM_TEMPERATURE: float = 0.0
    LLM_MAX_TOKENS: int = 1024
    VECTOR_STORE: str = Field(default="chroma", env="VECTOR_STORE")
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    PINECONE_API_KEY: str = Field(default="", env="PINECONE_API_KEY")
    PINECONE_INDEX: str = Field(default="ecom-products", env="PINECONE_INDEX")
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 64
    TOP_K_RETRIEVAL: int = 4
    SIMILARITY_THRESHOLD: float = 0.3
    REDIS_URL: str = Field(default="redis://redis:6379", env="REDIS_URL")
    CACHE_TTL_SECONDS: int = 3600
    MLFLOW_TRACKING_URI: str = Field(default="http://mlflow:5000", env="MLFLOW_TRACKING_URI")
    LANGSMITH_API_KEY: str = Field(default="", env="LANGSMITH_API_KEY")
    LANGSMITH_PROJECT: str = "ecom-rag-engine"
    RATE_LIMIT_PER_MINUTE: int = 60
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
