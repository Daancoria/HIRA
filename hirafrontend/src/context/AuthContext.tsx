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
  register : (email: string, password: string) => Promise<void>;
  login: (email: string, password: string, role: Role, name: string) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (firebaseUser: FirebaseUser | null) => {
      if (firebaseUser) {
        // We'll use whatever name was provided during login
        // But if no name, fallback to email
        setUser((prevUser) => ({
          ...(prevUser || { name: 'Unknown' }), // retain previous user data or default name
          role: 'Manager' // set role to 'Manager'
        }));
      } else {
        setUser(null);
      }
    });

    return () => unsubscribe();
  }, []);

  const login = async (email: string, password: string, role: Role, name: string) => {
    await signInWithEmailAndPassword(auth, email, password);
    // Directly use the name from LoginPage
    setUser({ name, role });
  };
  const register = async (email: string, password: string) => {
    // create user
    await createUserWithEmailAndPassword(auth, email, password);
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
