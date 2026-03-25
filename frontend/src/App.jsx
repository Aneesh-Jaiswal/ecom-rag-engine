import { useState } from "react";
import ChatPage from "./pages/ChatPage";
import AnalyticsPage from "./pages/AnalyticsPage";
import "./index.css";

export default function App() {
  const [page, setPage] = useState("chat");

  return (
    <div className="app">
      <nav className="nav">
        <div className="nav-brand">
          <span className="nav-logo">⚡</span>
          <span className="nav-title">ShopBot<span className="nav-ai">AI</span></span>
        </div>
        <div className="nav-links">
          <button
            className={`nav-link ${page === "chat" ? "active" : ""}`}
            onClick={() => setPage("chat")}
          >
            Chat
          </button>
          <button
            className={`nav-link ${page === "analytics" ? "active" : ""}`}
            onClick={() => setPage("analytics")}
          >
            Analytics
          </button>
        </div>
        <div className="nav-badge">RAG · LangChain · GPT-4o</div>
      </nav>

      <main className="main">
        {page === "chat" ? <ChatPage /> : <AnalyticsPage />}
      </main>
    </div>
  );
}
