export default function MessageBubble({ message, isStreaming }) {
  const isUser = message.role === "user";

  return (
    <div className={`message-row ${isUser ? "user" : "assistant"}`}>
      {!isUser && (
        <div className="avatar bot-avatar">🤖</div>
      )}
      <div className={`bubble ${isUser ? "user-bubble" : "assistant-bubble"} ${message.isError ? "error-bubble" : ""}`}>
        <div className="bubble-text">{message.content}</div>
        {!isUser && message.latency && (
          <div className="bubble-meta">
            <span>⚡ {message.latency}ms</span>
            {message.rewritten && message.rewritten !== message.content && (
              <span title={`Rewritten: "${message.rewritten}"`}>🔁 query rewritten</span>
            )}
            {message.sources?.length > 0 && (
              <span>📚 {message.sources.length} sources</span>
            )}
          </div>
        )}
      </div>
      {isUser && (
        <div className="avatar user-avatar">👤</div>
      )}
    </div>
  );
}
