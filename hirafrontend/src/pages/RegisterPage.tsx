import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../config/firebase';
import styles from './AuthPage.module.css';
type Role = 'Manager' | 'Director';
const RegisterPage: React.FC = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<Role>('Manager');
  const [error, setError] = useState('');
  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      // Optional: Store role in Firestore or use custom claims
      navigate('/login');
    } catch (err: any) {
      setError(err.message || 'Registration failed.');
    }
  };
  return (
    <div className={styles.container}>
      <h2>Create Your HIRA Account</h2>
      {error && <div className={styles.error}>{error}</div>}
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
        onChange={(e) => setRole(e.target.value as Role)}
      >
        <option value="Manager">Manager</option>
        <option value="Director">Director</option>
      </select>
      <button className={styles.button} onClick={handleRegister}>
        Register
      </button>
      <p className={styles.link} onClick={() => navigate('/login')}>
        Already have an account? Login
      </p>
    </div>
  );
};
export default RegisterPage;







