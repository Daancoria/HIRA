import React, { useRef, useEffect } from 'react'
import styles from './ChatInput.module.css'

interface ChatInputProps {
  value: string
  onChange: (text: string) => void
  onSend: () => void
  isLoading?: boolean
}

export default function ChatInput({
  value,
  onChange,
  onSend,
  isLoading,
}: ChatInputProps) {
  const inputRef = useRef<HTMLInputElement | null>(null)

  useEffect(() => {
    inputRef.current?.focus()
  }, [])

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !isLoading && value.trim()) {
      onSend()
    }
  }

  const isDisabled = !value.trim() || isLoading

  return (
    <div className={styles.inputRow}>
      <div className={styles.inputContainer}>
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
          disabled={isLoading}
        />
        <div className={styles.charCount}>{value.length}/300</div>
      </div>

      <button
        onClick={onSend}
        disabled={isDisabled}
        className={`${styles.button} ${isDisabled ? styles.disabled : ''}`}
        aria-label="Send message"
      >
        Send
      </button>
    </div>
  )
}
