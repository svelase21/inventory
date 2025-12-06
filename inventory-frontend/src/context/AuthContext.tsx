import { createContext } from "react";

// User interface
export interface User {
    id: number;
    username: string;
    user_type: string
}

// Define context with an interface
interface AuthContextType {
    token: string | null;
    user: User | null;
    loading: boolean;
    login: (token: string, user: User) => void;
    logout: () => void;
}

// Create provider
export const AuthContext = createContext<AuthContextType | undefined>(undefined);