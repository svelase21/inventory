import { useContext } from "react"
import { AuthContext } from "../context/AuthContext"

export const UseAuth = () => {
    const context = useContext(AuthContext); 
    if (context  === undefined) {
        throw new Error("UseAuth must go inside AuthProvider.")
    }
    return context;
}