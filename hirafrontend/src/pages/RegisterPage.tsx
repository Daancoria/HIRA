import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../config/firebase';

// Optional: You can later store this in Firestore or user metadata
type Role = 'Manager' | 'Director';

export default function RegisterPage() {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<Role>('Manager');
  const [error, setError] = useState('');

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      // 🔒 You can add role handling to Firestore or custom claims here later
      navigate('/login');
    } catch (err: any) {
      setError(err.message || 'Registration failed.');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: '100px auto', textAlign: 'center' }}>
      <h2>Create Your HIRA Account</h2>

      {error && <div style={{ color: 'red', marginBottom: 10 }}>{error}</div>}

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
        onChange={(e) => setRole(e.target.value as Role)}
        style={{ width: '100%', padding: 10, marginBottom: 10 }}
      >
        <option value="Manager">Manager</option>
        <option value="Director">Director</option>
      </select>

      <button onClick={handleRegister} style={{ padding: '10px 20px' }}>
        Register
      </button>

      <p style={{ marginTop: 20 }}>
        Already have an account?{' '}
        <span
          onClick={() => navigate('/login')}
          style={{ color: '#007bff', cursor: 'pointer' }}
        >
          Login
        </span>
      </p>
    </div>
  );
}
