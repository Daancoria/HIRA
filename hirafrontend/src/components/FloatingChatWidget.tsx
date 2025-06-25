import React, { useState, useRef, useEffect } from 'react'
import ChatInput from './ChatInput'
import styles from './FloatingChatWidget.module.css'
import { getBotResponse } from '../services/chatbotService'

interface ChatMessage {
  sender: 'user' | 'bot'
  text: string
}

export default function FloatingChatWidget() {
  const [isOpen, setIsOpen] = useState(false)
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const scrollRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    scrollRef.current?.scrollTo(0, scrollRef.current.scrollHeight)
  }, [messages])

  const handleSend = async () => {
    if (!inputValue.trim()) return

    const userMessage: ChatMessage = { sender: 'user', text: inputValue }
    setMessages((prev) => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)

    try {
      const reply = await getBotResponse(userMessage.text)
      setMessages((prev) => [...prev, { sender: 'bot', text: reply }])
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: '⚠️ Unable to get a response right now.' },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className={styles.floatingContainer}>
      <button className={styles.toggleButton} onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? '✖️' : '💬 HIRA'}
      </button>

      {isOpen && (
        <div className={styles.chatBox}>
          <div className={styles.header}>HIRA Assistant</div>

          <div className={styles.messages} ref={scrollRef}>
            {messages.map((msg, idx) => (
              <div
                key={idx}
                className={`${styles.message} ${
                  msg.sender === 'user' ? styles.userMsg : styles.botMsg
                }`}
              >
                {msg.text}
              </div>
            ))}
            {isLoading && <div className={styles.typing}>HIRA is typing...</div>}
          </div>

          <ChatInput
            value={inputValue}
            onChange={setInputValue}
            onSend={handleSend}
            isLoading={isLoading}
          />
        </div>
      )}
    </div>
  )
}
