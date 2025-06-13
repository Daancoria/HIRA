import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { getBotResponse } from '../services/chatbotService';
import styles from './ChatbotPage.module.css';
import MessageBubble from '../components/MessageBubble';
import FileUploader from '../components/FileUploader';
import ChatInput from '../components/ChatInput';

interface Message {
  sender: 'user' | 'bot';
  text: string;
  timestamp?: string;
}

export default function ChatbotPage() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [uploadedFileName, setUploadedFileName] = useState<string | null>(null);
  const [insights, setInsights] = useState<string[]>([]);
  const [showHelp, setShowHelp] = useState(false);
  const chatEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!user) {
      navigate('/login', { replace: true });
    }
  }, [user, navigate]);

  useEffect(() => {
    const saved = localStorage.getItem('chatMessages');
    if (saved) {
      try {
        setMessages(JSON.parse(saved));
      } catch {
        console.warn('Failed to parse saved chat history.');
      }
    } else {
      setMessages([
        {
          sender: 'bot',
          text: 'Hi! I’m HIRA. Ask me anything about your team’s KPIs.',
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        }
      ]);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('chatMessages', JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const userMsg: Message = { sender: 'user', text: input, timestamp: now };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const reply = await getBotResponse(input);
      const botReply: Message = { sender: 'bot', text: reply, timestamp: now };
      setMessages(prev => [...prev, botReply]);

      const newInsights: string[] = [];
      const keywords = [
        { phrase: 'staffing gap', label: 'Staffing Gap Insight' },
        { phrase: 'FTE', label: 'FTE Insight' },
        { phrase: 'overtime', label: 'Overtime Alert' }
      ];

      keywords.forEach(({ phrase, label }) => {
        if (reply.toLowerCase().includes(phrase) && !insights.includes(label)) {
          newInsights.push(label);
        }
      });

      if (newInsights.length) {
        setInsights(prev => [...prev, ...newInsights]);
      }
    } catch (err: any) {
      console.error('Chatbot error:', err);
      const isNetworkError = err instanceof TypeError;
      const errorText = isNetworkError
        ? '⚠️ Network error. Please check your connection.'
        : '⚠️ Something went wrong. Please try again.';

      setMessages(prev => [
        ...prev,
        { sender: 'bot', text: errorText, timestamp: now }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('chatMessages');
    logout();
    navigate('/login');
  };

  const promptSuggestions =
    user?.role === 'Director'
      ? [
          'Show open positions by department',
          'Summarize staffing budget trends',
          'Compare FTE vs budgeted positions'
        ]
      : [
          'What are today’s staffing gaps?',
          'List departments with overtime',
          'Show unfilled shifts this week'
        ];

  return (
    <div className={styles.container}>
      {/* Role Banner */}
      <div
        style={{
          backgroundColor: user?.role === 'Director' ? '#0d6efd' : '#20c997',
          color: 'white',
          padding: '10px 16px',
          borderRadius: '6px',
          marginBottom: '12px',
          textAlign: 'center',
        }}
      >
        {user?.role === 'Director'
          ? '🎯 Director View: You can access budget and position control insights.'
          : '👥 Manager View: You can explore staffing gaps and scheduling insights.'}
      </div>

      {/* Header */}
      <div className={styles.header}>
        <h2>
          Welcome, {user?.name}
          <span
            style={{
              backgroundColor: user?.role === 'Director' ? '#0d6efd' : '#20c997',
              color: 'white',
              padding: '4px 10px',
              borderRadius: 12,
              fontSize: '0.8em',
              marginLeft: 8,
            }}
          >
            {user?.role}
          </span>
        </h2>
        <button onClick={handleLogout} className={styles.logoutButton}>Logout</button>
      </div>

      {/* Chat tools: Clear + Export */}
      <div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
        <button
          onClick={() => {
            setMessages([]);
            localStorage.removeItem('chatMessages');
          }}
          style={{
            backgroundColor: '#f8d7da',
            color: '#721c24',
            border: 'none',
            borderRadius: 6,
            padding: '6px 12px',
            cursor: 'pointer',
          }}
        >
          🗑️ Clear Chat
        </button>

        <button
          onClick={() => {
            const blob = new Blob([JSON.stringify(messages, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'chat-history.json';
            a.click();
          }}
          style={{
            backgroundColor: '#d1ecf1',
            color: '#0c5460',
            border: 'none',
            borderRadius: 6,
            padding: '6px 12px',
            cursor: 'pointer',
          }}
        >
          📥 Export Chat
        </button>
      </div>

      {/* Insight Summary */}
      {insights.length > 0 && (
        <div style={{
          background: '#fff3cd',
          border: '1px solid #ffeeba',
          padding: '12px',
          borderRadius: 8,
          marginBottom: 12
        }}>
          <strong>📊 Insight Summary:</strong>
          <ul style={{ marginTop: 8, paddingLeft: 20 }}>
            {insights.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Chat messages */}
      <div className={styles.chatbox}>
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} message={msg} />
        ))}

        {loading && (
          <div className={styles.messageBot}>
            <span style={{ fontStyle: 'italic', color: '#6c757d' }}>
              HIRA is typing<span className={styles.dots}>...</span>
            </span>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      {/* Prompt suggestions */}
      <div style={{ marginBottom: 12 }}>
        <div style={{ fontWeight: 500, marginBottom: 6 }}>💡 Suggestions:</div>
        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
          {promptSuggestions.map((text, idx) => (
            <button
              key={idx}
              onClick={() => setInput(text)}
              style={{
                background: '#e2e3e5',
                border: 'none',
                padding: '6px 12px',
                borderRadius: 12,
                cursor: 'pointer',
                fontSize: '0.9em'
              }}
            >
              {text}
            </button>
          ))}
        </div>
      </div>

      {/* File uploader */}
      <FileUploader onUploadSuccess={setUploadedFileName} />
      {uploadedFileName && (
        <div style={{ fontSize: '0.9em', marginTop: 6, color: '#555' }}>
          ✅ Uploaded: <strong>{uploadedFileName}</strong>
        </div>
      )}

      {/* Chat input */}
      <ChatInput
        value={input}
        onChange={setInput}
        onSend={sendMessage}
        isLoading={loading}
      />

      {/* Help modal */}
      {showHelp && (
        <div
          onClick={() => setShowHelp(false)}
          role="dialog"
          aria-modal="true"
          aria-label="How to Use HIRA"
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            backgroundColor: 'rgba(0, 0, 0, 0.6)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 1000
          }}
        >
          <div
            onClick={(e) => e.stopPropagation()}
            style={{
              background: '#fff',
              padding: '24px',
              borderRadius: 10,
              width: '90%',
              maxWidth: 500,
              position: 'relative',
              boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
            }}
          >
            <button
              onClick={() => setShowHelp(false)}
              aria-label="Close Help"
              style={{
                position: 'absolute',
                top: 8,
                right: 12,
                background: 'transparent',
                border: 'none',
                fontSize: '1.5rem',
                cursor: 'pointer',
                lineHeight: 1
              }}
            >
              &times;
            </button>
            <h3 style={{ marginBottom: 10 }}>🧭 How to Use HIRA</h3>
            <p style={{ marginBottom: 8 }}>
              Upload your staffing file (<code>.csv</code>, <code>.xls</code>, or <code>.pdf</code>),
              then ask questions like:
            </p>
            <ul style={{ paddingLeft: 20 }}>
              <li>“What are today’s staffing gaps?”</li>
              <li>“Show me overtime by department.”</li>
              <li>“Compare actual vs budgeted FTEs.”</li>
            </ul>
          </div>
        </div>
      )}

      {/* Floating Help Button */}
      <button
        onClick={() => setShowHelp(true)}
        aria-label="Help"
        style={{
          position: 'fixed',
          bottom: 80,
          right: 20,
          background: '#0d6efd',
          color: '#fff',
          border: 'none',
          borderRadius: '50%',
          width: 44,
          height: 44,
          fontSize: '1.2em',
          cursor: 'pointer',
          zIndex: 1000
        }}
      >
        ?
      </button>
    </div>
  );
}
