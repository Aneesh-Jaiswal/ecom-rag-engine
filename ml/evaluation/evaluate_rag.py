"""
RAG Evaluation Pipeline using RAGAS
Metrics: faithfulness, answer_relevancy, context_precision, context_recall

Run:
  python ml/evaluation/evaluate_rag.py
"""

import asyncio
import json
import mlflow
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
import httpx
import logging

logger = logging.getLogger(__name__)

# ── Ground Truth Test Set ──────────────────────────────────────────────────────
TEST_QUESTIONS = [
    {
        "question": "What is the best gaming laptop under $1200?",
        "ground_truth": "The ASUS ROG Strix G15 offers excellent gaming performance under $1200 with RTX 3070 graphics.",
    },
    {
        "question": "Do you have wireless noise-cancelling headphones?",
        "ground_truth": "Yes, we carry Sony WH-1000XM5 and Bose QuietComfort 45, both with industry-leading noise cancellation.",
    },
    {
        "question": "What coffee makers have a thermal carafe?",
        "ground_truth": "The Technivorm Moccamaster and Breville Precision Brewer both feature thermal carafes to keep coffee hot.",
    },
    {
        "question": "Is the iPhone 15 Pro available?",
        "ground_truth": "Yes, the iPhone 15 Pro is available in Black Titanium, White Titanium, Blue Titanium, and Natural Titanium.",
    },
    {
        "question": "What standing desks support over 300 lbs?",
        "ground_truth": "The Flexispot E7 Pro supports up to 355 lbs and features dual motor lift system.",
    },
]

API_BASE = "http://localhost:8000/api/v1"


async def collect_rag_outputs() -> list:
    """Hit the live API for each test question and collect answers + contexts."""
    results = []
    async with httpx.AsyncClient(timeout=60.0) as client:
        for item in TEST_QUESTIONS:
            resp = await client.post(
                f"{API_BASE}/chat",
                json={"question": item["question"], "session_id": "eval"},
            )
            resp.raise_for_status()
            data = resp.json()

            results.append({
                "question": item["question"],
                "answer": data["answer"],
                "contexts": [s["content"] for s in data["sources"]],
                "ground_truth": item["ground_truth"],
            })
            logger.info(f"✅ Collected: {item['question'][:50]}...")

    return results


def run_ragas_evaluation(results: list) -> dict:
    """Run RAGAS metrics on collected outputs."""
    dataset = Dataset.from_list(results)
    scores = evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall,
        ],
    )
    return scores


def log_to_mlflow(scores: dict, run_name: str = "rag-evaluation"):
    """Log evaluation scores to MLflow for experiment tracking."""
    with mlflow.start_run(run_name=run_name):
        for metric_name, value in scores.items():
            mlflow.log_metric(metric_name, float(value))

        mlflow.log_params({
            "test_set_size": len(TEST_QUESTIONS),
            "api_base": API_BASE,
        })

        # Save full results as artifact
        with open("/tmp/eval_results.json", "w") as f:
            json.dump(scores, f, indent=2)
        mlflow.log_artifact("/tmp/eval_results.json")

        logger.info(f"📊 MLflow run logged: {mlflow.active_run().info.run_id}")


async def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("🔬 Starting RAG Evaluation...")

    results = await collect_rag_outputs()
    scores = run_ragas_evaluation(results)

    print("\n" + "=" * 50)
    print("📊 RAGAS Evaluation Results")
    print("=" * 50)
    for k, v in scores.items():
        print(f"  {k:<30} {float(v):.4f}")
    print("=" * 50)

    log_to_mlflow(scores)
    return scores


if __name__ == "__main__":
    asyncio.run(main())
