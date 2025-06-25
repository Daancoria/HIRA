// pages/ChatHistoryPage.tsx
import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import styles from './ChatHistoryPage.module.css'

interface Message {
  sender: 'user' | 'bot'
  text: string
  timestamp?: string
}

interface ChatSession {
  id: string
  date: string
  messages: Message[]
}

export default function ChatHistoryPage() {
  const [sessions, setSessions] = useState<ChatSession[]>([])
  const navigate = useNavigate()

  useEffect(() => {
    try {
      const saved = localStorage.getItem('chatMessages')
      if (saved) {
        const parsedMessages: Message[] = JSON.parse(saved)
        const session: ChatSession = {
          id: 'session-1',
          date: new Date().toLocaleDateString(),
          messages: parsedMessages,
        }
        setSessions([session])
      }
    } catch (err) {
      console.error('Failed to load chat history:', err)
      setSessions([])
    }
  }, [])

  const viewSession = (sessionId: string) => {
    navigate(`/chat-history/${sessionId}`)
  }

  return (
    <div className={styles.container}>
      <h2 style={{ marginBottom: 20 }}>📜 Chat History</h2>

      {sessions.length === 0 ? (
        <p>No saved sessions found.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {sessions.map((session, index) => (
            <li
              key={session.id}
              className={styles.sessionItem}
              onClick={() => viewSession(session.id)}
            >
              <div className={styles.sessionTitle}>
                Session {index + 1} – {session.date}
              </div>
              <div className={styles.sessionMeta}>
                {session.messages.length} messages
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
