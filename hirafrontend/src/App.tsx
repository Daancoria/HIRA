import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import ChatHistoryPage from './pages/ChatHistoryPage'
import ChatbotPage from './pages/ChatbotPage'
import FloatingChatWidget from './components/FloatingChatWidget'
import DarkModeToggle from './components/DarkModeToggle'
import './index.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/chatbot" element={<ChatbotPage />} />
        <Route path="/history" element={<ChatHistoryPage />} />
      </Routes>

      {/* Floating assistant + theme toggle */}
      <FloatingChatWidget />
      <DarkModeToggle />
    </Router>
  )
}

export default App
