import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<'Manager' | 'Director'>('Manager');

  const handleLogin = async () => {
    if (!name.trim() || !email.trim() || !password.trim()) {
      return alert('Please enter name, email, and password.');
    }
    try {
      await login(email, password, role, name);
      navigate("/chat");
    } catch (err: any) {
      console.error('Login failed:', err);
      alert('Login failed. Please check your credentials.');
    }
  };
  const handleRegisterButton = () => {
    navigate('/register');
  };

  return (
    <div style={{ maxWidth: 400, margin: '100px auto', textAlign: 'center' }}>
      <h2>Login to HIRA</h2>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ width: '100%', padding: 10, marginBottom: 10 }}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{ width: '100%', padding: 10, marginBottom: 10 }}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: '100%', padding: 10, marginBottom: 10 }}
      />
      <select
        value={role}
        onChange={(e) => setRole(e.target.value as 'Manager' | 'Director')}
        style={{ width: '100%', padding: 10 }}
      >
        <option value="Manager">Manager</option>
        <option value="Director">Director</option>
      </select>
      <button onClick={handleLogin} style={{ marginTop: 20, padding: '10px 20px' }}>
        Login
      </button>
      <button onClick={handleRegisterButton} style={{ marginTop: 20, padding: '10px 20px' }}>
        Register
      </button>
    </div>
  );
}

