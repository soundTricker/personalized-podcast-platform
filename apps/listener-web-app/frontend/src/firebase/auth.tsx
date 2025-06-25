/**
 * Copyright 2025 Keisuke Tominaga a.k.a soundTricker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {useState, useEffect, createContext, useContext, ReactNode} from 'react';
import {initializeApp} from 'firebase/app';
import {
    getAuth,
    signInWithEmailAndPassword,
    createUserWithEmailAndPassword,
    signOut,
    onAuthStateChanged,
    GoogleAuthProvider,
    signInWithPopup,
    User,
    connectAuthEmulator,
    setPersistence,
    browserSessionPersistence
} from 'firebase/auth';
import {connectStorageEmulator, getStorage} from 'firebase/storage';
import {firebaseConfig} from './config';

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const storage = getStorage(app);
const googleProvider = new GoogleAuthProvider();

// Auth context type
type AuthContextType = {
    currentUser: User | null;
    loading: boolean;
    signInWithEmail: (email: string, password: string) => Promise<void>;
    signInWithGoogle: () => Promise<void>;
    signUpWithEmail: (email: string, password: string) => Promise<void>;
    logout: () => Promise<void>;
};

// Create auth context
const AuthContext = createContext<AuthContextType | null>(null);

// Auth provider props
type AuthProviderProps = {
    children: ReactNode;
};

// Auth provider component
export function AuthProvider({children}: AuthProviderProps) {
    const [currentUser, setCurrentUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    // Sign in with email and password
    const signInWithEmail = async (email: string, password: string) => {
        await setPersistence(auth, browserSessionPersistence);
        await signInWithEmailAndPassword(auth, email, password);
    };

    // Sign in with Google
    const signInWithGoogle = async () => {
        await setPersistence(auth, browserSessionPersistence);
        await signInWithPopup(auth, googleProvider);
    };

    // Sign up with email and password
    const signUpWithEmail = async (email: string, password: string) => {
        await setPersistence(auth, browserSessionPersistence);
        await createUserWithEmailAndPassword(auth, email, password);
    };

    // Logout
    const logout = async () => {
        await signOut(auth);
    };

    useEffect(() => {
        if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
            connectAuthEmulator(auth, "http://localhost:9099", {disableWarnings: true});
            connectStorageEmulator(storage, "localhost", 9299)
        }
    }, []);

    // Listen for auth state changes
    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            setCurrentUser(user);
            setLoading(false);
        });

        return unsubscribe;
    }, []);

    const value = {
        currentUser,
        loading,
        signInWithEmail,
        signInWithGoogle,
        signUpWithEmail,
        logout,
    };

    return (
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>
    );
}

// Custom hook to use auth context
export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}