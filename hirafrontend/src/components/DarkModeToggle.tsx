import React, { useEffect, useState } from 'react'

export default function DarkModeToggle() {
  const [isDark, setIsDark] = useState<boolean>(() => {
    return localStorage.getItem('theme') === 'dark'
  })

  useEffect(() => {
    const root = document.documentElement
    if (isDark) {
      root.classList.add('darkmode')
      localStorage.setItem('theme', 'dark')
    } else {
      root.classList.remove('darkmode')
      localStorage.setItem('theme', 'light')
    }
  }, [isDark])

  const toggleTheme = () => {
    setIsDark((prev) => !prev)
  }

  return (
    <button
      onClick={toggleTheme}
      style={{
        position: 'fixed',
        bottom: 20,
        left: 20,
        padding: '10px 16px',
        fontSize: '14px',
        borderRadius: '6px',
        zIndex: 1000,
        backgroundColor: isDark ? '#f1f1f1' : '#333',
        color: isDark ? '#333' : '#f1f1f1',
        border: '1px solid var(--base-variant)',
        transition: 'all 0.2s ease',
      }}
    >
      {isDark ? '☀️ Light Mode' : '🌙 Dark Mode'}
    </button>
  )
}
