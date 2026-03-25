# ⚡ ShopBot AI — E-Commerce Product Q&A Engine

> Production-grade RAG pipeline for intelligent product discovery.
> Built with LangChain · FastAPI · React · ChromaDB/Pinecone · Docker · MLflow

![Architecture](https://img.shields.io/badge/Stack-LangChain%20%7C%20FastAPI%20%7C%20React-6ee7f7?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11-a78bfa?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-34d399?style=flat-square)

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────┐
│           FastAPI Backend               │
│                                         │
│  Query Rewriting (LLM)                  │
│       │                                 │
│  Hybrid Retriever                       │
│  (Dense + ChromaDB/Pinecone)            │
│       │                                 │
│  Contextual Compression (Reranking)     │
│       │                                 │
│  GPT-4o Generation (LCEL chain)         │
│       │                                 │
│  Source Attribution + Metadata          │
└─────────────────────────────────────────┘
    │
    ▼
React Frontend  ←──→  Analytics Dashboard
                              │
                         MLflow + LangSmith
```

## 🚀 Quick Start

### 1. Clone & configure
```bash
git clone https://github.com/you/ecom-rag-engine.git
cd ecom-rag-engine
cp backend/.env.example backend/.env
# Edit backend/.env and add your OPENAI_API_KEY
```

### 2. Run with Docker Compose
```bash
docker compose up --build
```

### 3. Seed the product catalog
```bash
python scripts/seed_products.py
```

### 4. Open the app
| Service | URL |
|---|---|
| Chat UI | http://localhost:3000 |
| API Docs | http://localhost:8000/docs |
| MLflow UI | http://localhost:5001 |

---

## 📁 Project Structure

```
ecom-rag-engine/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app + lifespan
│   │   ├── api/routes/
│   │   │   ├── chat.py           # /chat + /chat/stream (SSE)
│   │   │   ├── products.py       # /products/ingest + /search
│   │   │   ├── health.py         # /health
│   │   │   └── analytics.py      # /analytics
│   │   ├── core/
│   │   │   ├── config.py         # Pydantic settings
│   │   │   ├── rag_pipeline.py   # LangChain RAG chain ⭐
│   │   │   ├── vector_store.py   # Chroma/Pinecone abstraction
│   │   │   └── metrics.py        # In-memory analytics
│   │   └── models/schemas.py     # Pydantic request/response models
│   ├── tests/test_api.py         # pytest test suite
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── pages/ChatPage.jsx    # Main chat interface
│       ├── pages/AnalyticsPage.jsx
│       └── components/           # MessageBubble, SourceCard, etc.
│
├── ml/evaluation/
│   └── evaluate_rag.py           # RAGAS evaluation + MLflow logging
│
├── scripts/seed_products.py      # Product catalog seeder
├── infra/docker/                 # Multi-stage Dockerfiles
├── .github/workflows/ci.yml      # CI/CD with quality gates
└── docker-compose.yml
```

---

## 🔑 Key Technical Decisions

### RAG Pipeline Design
| Component | Choice | Reason |
|---|---|---|
| LLM | GPT-4o | Best reasoning for product comparisons |
| Embeddings | text-embedding-3-small | Cost-efficient, high quality |
| Vector DB | ChromaDB (dev) / Pinecone (prod) | Swappable via ENV var |
| Reranking | LLMChainExtractor | Contextual compression reduces noise |
| Caching | Redis semantic cache | Avoids re-calling LLM for duplicate queries |
| Tracing | LangSmith | Full chain observability |

### MLOps Pipeline
- **RAGAS** evaluates faithfulness, relevancy, precision, recall
- **MLflow** tracks every eval run as an experiment
- **CI/CD quality gates** block deploys if RAGAS scores drop below thresholds

---

## 🧪 Running Tests

```bash
cd backend
pip install pytest pytest-asyncio httpx
pytest tests/ -v --cov=app
```

## 📊 Running RAG Evaluation

```bash
# Make sure backend is running first
python ml/evaluation/evaluate_rag.py
# Open MLflow UI: http://localhost:5001
```

---

## 💡 Interview Talking Points

1. **Why RAG over fine-tuning?** RAG is updatable (new products without retraining), cheaper, and provides source attribution.

2. **How does query rewriting help?** Users say "cheap laptop for school" — the rewriter expands this to include relevant specs and synonyms, boosting retrieval recall.

3. **Chroma vs Pinecone tradeoff?** Chroma is zero-cost and local for dev. Pinecone is managed, scales to billions of vectors, with automatic replication.

4. **How do you measure RAG quality?** RAGAS framework: faithfulness (no hallucination), answer relevancy, context precision/recall.

5. **What's the caching strategy?** Redis caches LLM responses for semantically similar queries, reducing latency from ~1.5s → ~50ms on cache hits.

---

## 📄 License

MIT
