import { render, screen } from '@testing-library/react';
import ChatbotPage from '../pages/ChatbotPage';
import { AuthProvider } from '../context/AuthContext';
import { BrowserRouter } from 'react-router-dom';

window.HTMLElement.prototype.scrollIntoView = jest.fn();

test('renders chatbot page with welcome text', () => {
  render(
    <AuthProvider>
      <BrowserRouter>
        <ChatbotPage />
      </BrowserRouter>
    </AuthProvider>
  );

  expect(screen.getByText(/welcome/i)).toBeInTheDocument();
});
