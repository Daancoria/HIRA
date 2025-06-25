import React, { Component, ReactNode } from 'react'

interface Props {
  children: ReactNode
}

interface State {
  hasError: boolean
  errorInfo?: string | null
}

class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props)
    this.state = { hasError: false, errorInfo: null }
  }

  static getDerivedStateFromError(_: Error): State {
    return { hasError: true, errorInfo: null }
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error('Uncaught error:', error, info)
    this.setState({ errorInfo: info.componentStack })
  }

  handleReset = () => {
    window.location.reload()
  }

  render() {
    if (this.state.hasError) {
      return (
        <div
          style={{
            padding: '2rem',
            textAlign: 'center',
            color: '#dc3545',
            fontFamily: 'Segoe UI, sans-serif',
          }}
        >
          <h2>⚠️ Something went wrong.</h2>
          <p>Please try refreshing the page or contact support.</p>
          {this.state.errorInfo && (
            <pre
              style={{
                marginTop: '1rem',
                fontSize: '0.8em',
                color: '#6c757d',
                whiteSpace: 'pre-wrap',
              }}
            >
              {this.state.errorInfo}
            </pre>
          )}
          <button
            onClick={this.handleReset}
            style={{
              marginTop: '1.5rem',
              padding: '10px 20px',
              backgroundColor: '#007bff',
              color: '#fff',
              border: 'none',
              borderRadius: 6,
              cursor: 'pointer',
              fontSize: '1rem',
            }}
          >
            🔄 Try Again
          </button>
        </div>
      )
    }

    return this.props.children
  }
}

export default ErrorBoundary

