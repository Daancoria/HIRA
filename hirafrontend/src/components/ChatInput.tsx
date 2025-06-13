import React, { useRef, useEffect } from 'react';
import styles from '../pages/ChatbotPage.module.css';

// Props for the ChatInput component
interface ChatInputProps {
  value: string; // Current input value
  onChange: (text: string) => void; // Handler for input change
  onSend: () => void; // Handler for sending message
  isLoading?: boolean; // Optional: disables input/button when loading
}

// ChatInput component for typing and sending chat messages
export default function ChatInput({ value, onChange, onSend, isLoading }: ChatInputProps) {
  const inputRef = useRef<HTMLInputElement | null>(null);

  // Focus the input field when the component mounts
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  // Handle Enter key to send message
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !isLoading && value.trim()) {
      onSend();
    }
  };

  return (
    <div className={styles.inputRow}>
      {/* Input field and character counter */}
      <div style={{ flexGrow: 1, display: 'flex', flexDirection: 'column' }}>
        <input
          ref={inputRef}
          type="text"
          maxLength={300}
          placeholder="Type a message..."
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          className={styles.input}
          aria-label="Chat message input"
        />
        <div className={styles.charCount}>{value.length}/300</div>
      </div>

      {/* Send button */}
      <button
        onClick={onSend}
        disabled={!value.trim() || isLoading}
        className={styles.button}
        aria-label="Send message"
        style={{
          opacity: (!value.trim() || isLoading) ? 0.6 : 1,
          cursor: (!value.trim() || isLoading) ? 'not-allowed' : 'pointer'
        }}
      >
        Send
      </button>
    </div>
  );
}
