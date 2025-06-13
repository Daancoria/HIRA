import { render, screen } from '@testing-library/react';
import FileUploader from '../components/FileUploader';

test('renders file uploader input', () => {
  render(<FileUploader onUploadSuccess={() => {}} />);
  const fileInput = screen.getByLabelText(/upload kpi file/i); 
  expect(fileInput).toBeInTheDocument();
});
