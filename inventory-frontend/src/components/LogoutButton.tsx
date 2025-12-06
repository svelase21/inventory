import { UseAuth } from "../hooks/UseAuth";
import { useNavigate } from "react-router";

const LogoutButton: React.FC = () => {
  const { logout } = UseAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    
    navigate('/login');
  };

  return (
    <button onClick={handleLogout}>
      Logout
    </button>
  );
};

export default LogoutButton;