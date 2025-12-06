import { UseAuth } from "../hooks/UseAuth"
import { Navigate, Outlet } from "react-router"


const ProtectedRoute: React.FC = () => {
    const { token } = UseAuth()

    if (!token){
        return <Navigate to="/auth" replace/>
    }

    return <Outlet/>
}

export default ProtectedRoute