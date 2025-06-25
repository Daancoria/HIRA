import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'

// 🌙 Apply theme before rendering
const savedTheme = localStorage.getItem('theme')
if (savedTheme === 'dark') {
  document.documentElement.classList.add('darkmode')
} else {
  document.documentElement.classList.remove('darkmode')
}

// Create root and render
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
)

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
