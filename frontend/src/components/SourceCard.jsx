export default function SourceCard({ source, index }) {
  const scorePercent = Math.round((source.score || 0) * 100);
  const scoreColor = scorePercent > 85 ? "#34d399" : scorePercent > 70 ? "#fbbf24" : "#f87171";

  return (
    <div className="source-card">
      <div className="source-header">
        <div className="source-index">#{index + 1}</div>
        <div className="source-name">{source.product_name}</div>
        <div className="source-score" style={{ color: scoreColor }}>
          {scorePercent}%
        </div>
      </div>
      <div className="source-category">{source.category}</div>
      <div className="source-excerpt">{source.content.slice(0, 120)}…</div>
    </div>
  );
}
