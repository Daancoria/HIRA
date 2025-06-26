import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import ChatHistoryPage from './pages/ChatHistoryPage';
import ChatbotPage from './pages/ChatbotPage';
import FloatingChatWidget from './components/FloatingChatWidget';
import DarkModeToggle from './components/DarkModeToggle';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import { AuthProvider } from './context/AuthContext';
import './index.css';
function AppRoutes() {
  const location = useLocation();
  const hideUI = location.pathname === '/' || location.pathname === '/register';
  return (
    <>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/chatbot" element={<ChatbotPage />} />
        <Route path="/history" element={<ChatHistoryPage />} />
      </Routes>
      {/* Show only when not on login/register */}
      {!hideUI && (
        <>
          <FloatingChatWidget />
          <DarkModeToggle />
        </>
      )}
    </>
  );
}
function App() {
  return (
    <AuthProvider>
      <Router>
        <AppRoutes />
      </Router>
    </AuthProvider>
  );
}
export default App;






















