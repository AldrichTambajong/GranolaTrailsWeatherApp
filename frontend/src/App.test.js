import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Login.js on App', () => {
  render(<App />);
  const linkElement = screen.getByText(/Sign Up/i);
  expect(linkElement).toBeInTheDocument();
});
