import React from 'react';
import styles from '../pages/ChatbotPage.module.css';

// Message interface for the chat bubble
interface Message {
  sender: 'user' | 'bot';
  text: string;
  timestamp?: string;
}

// Props for the MessageBubble component
interface Props {
  message: Message;
}

// MessageBubble component displays a single chat message
export default function MessageBubble({ message }: Props) {
  // Choose alignment class based on sender
  const alignmentClass =
    message.sender === 'user' ? styles.messageUser : styles.messageBot;

  return (
    <div className={`${styles.message} ${alignmentClass} ${styles.fadeIn}`}>
      {/* Message text */}
      <div>{message.text}</div>
      {/* Optional timestamp */}
      {message.timestamp && (
        <div style={{ fontSize: '0.75em', color: '#6c757d', marginTop: 2 }}>
          {message.timestamp}
        </div>
      )}
    </div>
  );
}
