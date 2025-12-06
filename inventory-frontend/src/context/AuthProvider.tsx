import { type ReactNode, useState, useEffect } from "react";
import { AuthContext, type User } from "./AuthContext";
import apiClient from "../api/ApiClient";
import { TailSpin } from "react-loader-spinner";

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [token, setToken] = useState<string | null>(localStorage.getItem("access_token"));
    const [user, SetUser] = useState<User | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    // UseEffect to load token from localStorage
    useEffect(() => {
        const checkUser = async () => {
            const storedToken = localStorage.getItem("access_token");

            if (storedToken) {
                try{
                    const response = await apiClient.get("/auth/me")

                    if (response.data) {
                        setToken(storedToken);
                        SetUser(response.data);        
                    }
                }
                    
                catch (error) {
                    console.error("Invalid Token: ", error)
                    localStorage.removeItem("access_token")
                }
            }
            setLoading(false);
        };
        checkUser()

    }, []);

    // Sign in function
    const login = (newToken: string, newUser: User) => {
        if (!localStorage.getItem("access_token")){
            localStorage.setItem("access_token", newToken);
        }
        setToken(newToken);
        SetUser(newUser);
    }

    // Logout function
    const logout = () => {
        localStorage.removeItem("access_token");
        setToken(null);
        SetUser(null);
    }

    // Loading
    if (loading) {
        return(
            <div className="bg-[#242021] flex items-center justify-center min-h-screen">
                <TailSpin
                    height="90"
                    width="90"
                    color="#00c8b2"
                    ariaLabel="tail-spin-loading"
                    visible={loading}
                />
            </div>
        )
    }

    return (
        <AuthContext.Provider value={{ token, user, loading, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}