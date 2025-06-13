import { render, screen } from '@testing-library/react';
import MessageBubble from '../components/MessageBubble';

test('renders a bot message', () => {
  render(<MessageBubble message={{ sender: 'bot', text: 'Hello from bot', timestamp: '12:00' }} />);
  expect(screen.getByText(/hello from bot/i)).toBeInTheDocument();
});
