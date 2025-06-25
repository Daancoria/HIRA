// pages/ChatbotPage.tsx
import React from 'react'
import FloatingChatWidget from '../components/FloatingChatWidget'

export default function ChatbotPage() {
  return (
    <div style={{ padding: '2rem', height: '100vh', background: '#f9fafb' }}>
      <h1 style={{ fontSize: '1.75rem', marginBottom: '1rem' }}>
        HIRA Assistant
      </h1>
      <p style={{ marginBottom: '2rem' }}>
        You can interact with the floating assistant in the bottom right corner.
      </p>

      <p style={{ color: '#666', fontSize: '0.9rem' }}>
        Need help? Try asking: <em>“What is the premium pay percentage for ICU this month?”</em>
      </p>

      {/* Include the same chat widget in case this is a dedicated chatbot page */}
      <FloatingChatWidget />
    </div>
  )
}
