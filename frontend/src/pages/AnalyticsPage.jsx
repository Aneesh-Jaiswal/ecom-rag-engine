import { useState, useEffect } from "react";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export default function AnalyticsPage() {
  const [data, setData] = useState(null);
  const [health, setHealth] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      fetch(`${API}/analytics`).then((r) => r.json()),
      fetch(`${API}/health`).then((r) => r.json()),
    ])
      .then(([analytics, healthData]) => {
        setData(analytics);
        setHealth(healthData);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="analytics-loading">Loading analytics…</div>;

  const stats = [
    { label: "Total Queries", value: data?.total_queries ?? 0, icon: "💬", color: "#6ee7f7" },
    { label: "Avg Latency", value: `${data?.avg_latency_ms ?? 0}ms`, icon: "⚡", color: "#a78bfa" },
    { label: "Avg Sources Used", value: data?.avg_sources_used ?? 0, icon: "📚", color: "#34d399" },
    { label: "Last Hour", value: data?.queries_last_hour ?? 0, icon: "🕐", color: "#fbbf24" },
  ];

  return (
    <div className="analytics-page">
      <div className="analytics-header">
        <h1 className="analytics-title">System Analytics</h1>
        <div className={`status-badge ${health?.status === "healthy" ? "healthy" : "error"}`}>
          ● {health?.status ?? "unknown"}
        </div>
      </div>

      {/* Stat Cards */}
      <div className="stat-grid">
        {stats.map((s, i) => (
          <div key={i} className="stat-card" style={{ "--accent": s.color }}>
            <div className="stat-icon">{s.icon}</div>
            <div className="stat-value">{s.value}</div>
            <div className="stat-label">{s.label}</div>
          </div>
        ))}
      </div>

      {/* System Info */}
      <div className="system-grid">
        <div className="system-card">
          <div className="system-card-title">🧠 Model Configuration</div>
          <div className="system-rows">
            <div className="system-row">
              <span>LLM Model</span><span className="mono">{health?.llm_model}</span>
            </div>
            <div className="system-row">
              <span>Vector Store</span><span className="mono">{health?.vector_store}</span>
            </div>
            <div className="system-row">
              <span>Cache</span>
              <span className={health?.cache_enabled ? "text-green" : "text-red"}>
                {health?.cache_enabled ? "Enabled" : "Disabled"}
              </span>
            </div>
            <div className="system-row">
              <span>Version</span><span className="mono">{health?.version}</span>
            </div>
          </div>
        </div>

        <div className="system-card">
          <div className="system-card-title">🏗️ RAG Architecture</div>
          <div className="pipeline-steps">
            {["Query Rewriting", "Hybrid Retrieval", "Contextual Compression", "LLM Generation", "Source Attribution"].map((step, i) => (
              <div key={i} className="pipeline-step">
                <div className="step-dot" />
                <span>{step}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Uptime */}
      <div className="uptime-card">
        <span>⏱ Uptime</span>
        <span className="mono">{Math.round((health?.uptime_seconds ?? 0) / 60)} minutes</span>
      </div>
    </div>
  );
}
