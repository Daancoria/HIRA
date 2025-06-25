import React from 'react'
import styles from './MessageBubble.module.css'

interface Message {
  sender: 'user' | 'bot'
  text: string
  timestamp?: string
}

interface Props {
  message: Message
}

export default function MessageBubble({ message }: Props) {
  const alignmentClass =
    message.sender === 'user' ? styles.userBubble : styles.botBubble

  return (
    <div className={`${styles.bubble} ${alignmentClass}`}>
      <div className={styles.text}>{message.text}</div>
      {message.timestamp && (
        <div className={styles.timestamp}>{message.timestamp}</div>
      )}
    </div>
  )
}
