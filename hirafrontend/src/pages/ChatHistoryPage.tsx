import React, {useEffect, useState} from 'react';
import {useNavigate} from 'react-router-dom';
import styles from './ChatHistoryPage.module.css'; // Assuming you have a CSS module for styles

interface Message {
    sender: "user" | "bot";
    text: string;
    timestamp?: string;
}

interface ChatSession {
    id: string;
    date: string;
    messages: Message[];
}

export default function ChatHistoryPage() {
    const [sessions, setSessions] = useState<ChatSession[]>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const saved = localStorage.getItem('chatMessages');
        if (saved) {
            setSessions([
                {
                    id: 'session-1',
                    date: new Date().toLocaleDateString(),
                    messages: JSON.parse(saved)
                }
            ]);
        }
    }, []);

    const viewSession = (sessionId: string) => {
        navigate(`/chat-history/${sessionId}`);
    };

    return (
        <div className={styles.container}>
          <h2 style={{ marginBottom: 20 }}>📜 Chat History</h2>
          {sessions.length === 0 ? (
            <p>No saved sessions found.</p>
          ) : (
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {sessions.map((session, index) => (
                <li key={session.id} style={{
                  marginBottom: 12,
                  padding: 12,
                  background: '#f8f9fa',
                  borderRadius: 8,
                  cursor: 'pointer',
                  border: '1px solid #dee2e6'
                }} onClick={() => viewSession(session.id)}>
                  <strong>Session {index + 1}</strong> – {session.date}<br />
                  <small>{session.messages.length} messages</small>
                </li>
              ))}
            </ul>
          )}
        </div>
      );
    }

