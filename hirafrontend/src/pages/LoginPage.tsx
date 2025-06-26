import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import styles from './AuthPage.module.css';


const LoginPage: React.FC = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<'Manager' | 'Director'>('Manager');
  const handleLogin = async () => {
    if (!name || !email || !password) {
      alert('Please enter name, email, and password.');
      return;
    }
    try {
      await login(email, password, role, name);
      navigate('/chat');
    } catch (err) {
      console.error('Login failed:', err);
      alert('Login failed. Please check your credentials.');
    }
  };
  return (
    <div className={styles.container}>
      <h2>Login to HIRA</h2>
      <input
        className={styles.input}
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        className={styles.input}
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        className={styles.input}
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <select
        className={styles.select}
        value={role}
        onChange={(e) => setRole(e.target.value as 'Manager' | 'Director')}
      >
        <option value="Manager">Manager</option>
        <option value="Director">Director</option>
      </select>
      <button className={styles.button} onClick={handleLogin}>
        Login
      </button>
      <button
        className={styles.button}
        onClick={() => navigate('/register')}
      >
        Register
      </button>
    </div>
  );
};
export default LoginPage;









