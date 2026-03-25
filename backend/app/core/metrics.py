"""
In-memory metrics collector.
In production, replace with Prometheus + Grafana.
"""

from collections import defaultdict, deque
from datetime import datetime, timedelta
from typing import List, Dict, Any
import threading


class MetricsCollector:
    def __init__(self):
        self._lock = threading.Lock()
        self._queries: deque = deque(maxlen=10_000)

    def log_query(self, session_id: str, question: str, rewritten_query: str,
                  latency_ms: float, source_count: int):
        with self._lock:
            self._queries.append({
                "session_id": session_id,
                "question": question,
                "rewritten_query": rewritten_query,
                "latency_ms": latency_ms,
                "source_count": source_count,
                "timestamp": datetime.utcnow(),
            })

    def get_summary(self) -> dict:
        with self._lock:
            queries = list(self._queries)

        if not queries:
            return {
                "total_queries": 0,
                "avg_latency_ms": 0.0,
                "avg_sources_used": 0.0,
                "top_categories": [],
                "queries_last_hour": 0,
            }

        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        recent = [q for q in queries if q["timestamp"] > one_hour_ago]

        return {
            "total_queries": len(queries),
            "avg_latency_ms": round(sum(q["latency_ms"] for q in queries) / len(queries), 2),
            "avg_sources_used": round(sum(q["source_count"] for q in queries) / len(queries), 2),
            "top_categories": [],
            "queries_last_hour": len(recent),
        }
