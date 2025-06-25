import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ChatbotPage from './pages/ChatbotPage';
import ErrorBoundary from './components/ErrorBoundary';
import './index.css';
import ChatHistoryPage from './pages/ChatHistoryPage';

// Route guard for authenticated pages
function ProtectedRoute() {
  const { user } = useAuth();
  return user ? <Outlet /> : <Navigate to="/login" />;
}

export default function App() {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light');

  useEffect(() => {
    document.body.classList.toggle('darkmode', theme === 'dark');
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <ErrorBoundary>
      <AuthProvider>
        <Router>
          {/* 🌗 Theme Toggle Button */}
          <button
            onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
            className="theme-toggle"
            style={{
              position: 'fixed',
              top: 20,
              right: 20,
              zIndex: 1000,
              padding: '8px 14px',
              borderRadius: 10,
              border: 'none',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: 500,
              backgroundColor: theme === 'dark' ? '#2c2c2c' : '#e0e0e0',
              color: theme === 'dark' ? '#f1f1f1' : '#111',
              boxShadow: '0 2px 6px rgba(0,0,0,0.1)'
            }}
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? '🌙 Night' : '☀️ Light'}
          </button>

          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route element={<ProtectedRoute />}>
              <Route path="/chat" element={<ChatbotPage />} />
            </Route>
            <Route path="/chat-history/:sessionId" element={<ChatHistoryPage />} />
            <Route path="*" element={<Navigate to="/login" />} />
          </Routes>
        </Router>
      </AuthProvider>
    </ErrorBoundary>
  );
}
