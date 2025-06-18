import React, { createContext, useContext, useState, useEffect } from 'react';
import { auth } from "../config/firebase";
import {
  onAuthStateChanged,
  signInWithEmailAndPassword,
  signOut,
  createUserWithEmailAndPassword,
  User as FirebaseUser
} from 'firebase/auth';

type Role = 'Manager' | 'Director';

interface User {
  name: string;
  role: Role;
}

interface AuthContextType {
  user: User | null;
  register : (email: string, password: string, name: string, role: Role) => Promise<void>;
  login: (email: string, password: string, role: Role, name: string) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser: FirebaseUser | null) => {
      if (firebaseUser) {
        setUser((prevUser) => ({
          ...(prevUser || { name: 'Unknown' }),
          role: 'Manager'
        }));
      } else {
        setUser(null);
      }
    });

    return () => unsubscribe();
  }, []);

  const register = async (email: string, password: string, name: string, role: Role) => {
    await createUserWithEmailAndPassword(auth, email, password);

    // This is me adding a post for backend to create a user record
    await fetch('http://localhost:5001/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, role }),
    });

    setUser({ name, role });
  };

  const login = async (email: string, password: string, role: Role, name: string) => {
    await signInWithEmailAndPassword(auth, email, password);
    setUser({ name, role });
  };

  const logout = async () => {
    await signOut(auth);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, register, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
