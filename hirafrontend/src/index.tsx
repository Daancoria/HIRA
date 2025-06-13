import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Import global styles
import App from './App'; // Import main App component

// Create a root for rendering the React app
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement // Get the root DOM element
);

// Render the App component inside React.StrictMode for highlighting potential problems
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
