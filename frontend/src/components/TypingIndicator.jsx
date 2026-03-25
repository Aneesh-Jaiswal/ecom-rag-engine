export default function TypingIndicator() {
  return (
    <div className="message-row assistant">
      <div className="avatar bot-avatar">🤖</div>
      <div className="bubble assistant-bubble typing-bubble">
        <span className="dot" />
        <span className="dot" />
        <span className="dot" />
      </div>
    </div>
  );
}
