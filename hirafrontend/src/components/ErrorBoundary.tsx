import React, { Component, ReactNode } from 'react';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  errorInfo?: string | null;
}

class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(_: Error): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error('Uncaught error:', error, info);
    this.setState({ errorInfo: info.componentStack });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: 24, textAlign: 'center', color: '#dc3545' }}>
          <h2>⚠️ Something went wrong.</h2>
          <p>Please refresh the page or contact support.</p>
          <pre style={{ fontSize: '0.8em', color: '#6c757d' }}>{this.state.errorInfo}</pre>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
