import { render, screen } from '@testing-library/react';
import ChatInput from '../components/ChatInput';

test('renders chat input and send button', () => {
  render(<ChatInput value="Hello" onChange={() => {}} onSend={() => {}} />);
  expect(screen.getByPlaceholderText(/type a message/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /send/i })).toBeInTheDocument();
});
