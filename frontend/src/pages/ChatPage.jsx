import { useState, useRef, useEffect } from "react";
import MessageBubble from "../components/MessageBubble";
import SourceCard from "../components/SourceCard";
import TypingIndicator from "../components/TypingIndicator";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

const SUGGESTIONS = [
  "Best laptop under $1000 for college?",
  "Noise-cancelling headphones comparison",
  "4K TV with HDMI 2.1 for gaming?",
  "Standing desk with memory presets",
  "Coffee maker with thermal carafe",
];

export default function ChatPage() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hi! I'm ShopBot 🛒 — your AI shopping assistant. Ask me anything about our product catalog: comparisons, specs, recommendations, or deals. I'll find the best match for you!",
      sources: [],
      latency: null,
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [streamingText, setStreamingText] = useState("");
  const [activeSources, setActiveSources] = useState([]);
  const bottomRef = useRef(null);
  const inputRef = useRef(null);
  const sessionId = useRef(`session-${Date.now()}`);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, streamingText]);

  const sendMessage = async (text) => {
    const question = text || input.trim();
    if (!question || loading) return;

    setInput("");
    setActiveSources([]);
    const history = messages
      .filter((m) => m.role !== "system")
      .map((m) => ({ role: m.role, content: m.content }));

    setMessages((prev) => [...prev, { role: "user", content: question }]);
    setLoading(true);
    setStreamingText("");

    try {
      const res = await fetch(`${API}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question,
          session_id: sessionId.current,
          chat_history: history,
        }),
      });

      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.answer,
          sources: data.sources || [],
          latency: data.latency_ms,
          rewritten: data.rewritten_query,
        },
      ]);
      setActiveSources(data.sources || []);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Sorry, something went wrong. Please check the API connection and try again.",
          sources: [],
          isError: true,
        },
      ]);
    } finally {
      setLoading(false);
      setStreamingText("");
      inputRef.current?.focus();
    }
  };

  const handleKey = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-layout">
      {/* Messages */}
      <div className="messages-area">
        <div className="messages-inner">
          {messages.map((msg, i) => (
            <MessageBubble key={i} message={msg} />
          ))}
          {loading && !streamingText && <TypingIndicator />}
          {streamingText && (
            <MessageBubble
              message={{ role: "assistant", content: streamingText + "▌" }}
              isStreaming
            />
          )}
          <div ref={bottomRef} />
        </div>
      </div>

      {/* Sources Panel */}
      {activeSources.length > 0 && (
        <div className="sources-panel">
          <div className="sources-title">
            <span className="sources-icon">🔍</span>
            Retrieved Sources ({activeSources.length})
          </div>
          <div className="sources-grid">
            {activeSources.map((src, i) => (
              <SourceCard key={i} source={src} index={i} />
            ))}
          </div>
        </div>
      )}

      {/* Suggestions */}
      {messages.length <= 1 && (
        <div className="suggestions">
          {SUGGESTIONS.map((s, i) => (
            <button key={i} className="suggestion-chip" onClick={() => sendMessage(s)}>
              {s}
            </button>
          ))}
        </div>
      )}

      {/* Input */}
      <div className="input-area">
        <div className="input-wrapper">
          <textarea
            ref={inputRef}
            className="input-box"
            placeholder="Ask about products, comparisons, specs…"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKey}
            rows={1}
            disabled={loading}
          />
          <button
            className={`send-btn ${loading ? "loading" : ""}`}
            onClick={() => sendMessage()}
            disabled={loading || !input.trim()}
          >
            {loading ? (
              <span className="spinner" />
            ) : (
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            )}
          </button>
        </div>
        <div className="input-hint">
          Powered by GPT-4o · LangChain RAG · ChromaDB
        </div>
      </div>
    </div>
  );
}
