# HIRA Chatbot Frontend

This project is the frontend interface for the **HIRA Chatbot**, a smart assistant designed to help healthcare managers and directors explore staffing insights.

## 🌟 Features

- 🔐 Login authentication with protected routes
- 💬 Chat interface with role-based prompt suggestions
- 📁 Upload staffing files (.csv, .xls, .pdf)
- 🌙 Light/Dark mode toggle with CSS variable theming
- 🧠 Insight summary panel (auto-generates based on keywords)
- 💾 Chat history persistence via localStorage
- 🔄 Export/clear chat history controls
- ❓ Onboarding/help modal for first-time users

## 🛠️ Tech Stack

- React + TypeScript
- React Router DOM v6+
- CSS Modules + CSS Variables for theming
- File upload handling via HTML5 APIs

## 🧪 Development Setup

```bash
npm install
npm start
```

Runs the app in development mode at `http://localhost:3000/`.

## 📦 Build for Production

```bash
npm run build
```

Builds the app for deployment to `/build`.

## 🗂 Project Structure

```bash
src/
  components/          # Reusable UI components (ChatInput, MessageBubble, etc.)
  context/             # AuthContext provider
  pages/               # Page views (ChatbotPage, LoginPage)
  services/            # Chatbot API integration
  App.tsx              # App router and theme toggle logic
  index.tsx            # Entry point
  index.css            # Global styles & CSS variable themes
```

## ✨ Theme Support

Light and Dark mode is controlled by a toggle in `App.tsx`, using the `darkmode` class on `<body>` and styled via `index.css`.

## ✅ Status

This frontend is production-ready. Integrate with a backend or deploy as a standalone static PWA.

---

© 2024 HIRA Project. All rights reserved.
