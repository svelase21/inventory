import type React from "react";
import FloatingInput from "./FloatingLabelInput";
import { useState } from "react";
import { Link } from "react-router";
import UserCircle from "../assets/user-circle.svg";
import EyeOffIcon from "./EyeOffIcon";
import EyeIcon from "./EyeIcon";
import { useNavigate } from "react-router";
import { UseAuth } from "../hooks/UseAuth";
import apiClient from "../api/ApiClient";
import { TailSpin } from "react-loader-spinner";

export const Login: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);

  const [inputStatus, setInputStatus] = useState<"warning" | "error" | "correct" | "neutral">("neutral")

  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState("")

  const navigate = useNavigate();
  const { login } = UseAuth();
  const apiUrl = import.meta.env.VITE_API_URL;
 
  const togglePasswordVisibility = () => {
    setShowPassword((prev) => !prev);
  }
  

  // Create EyeIcon button
  const passwordIcon = (
    <button
      type="button"
      onClick={togglePasswordVisibility}
      className="text-gray-500 hover:text-gray-700"
      aria-label={showPassword ? "Hide password" : "Show password"}
    >
      {showPassword ? (
        <EyeOffIcon className="w-5 h-5" />
      ) : (
        <EyeIcon className="w-5 h-5" />
      )}
    </button>
  );

  const handleSumbit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    

    try {
        const response = await fetch(`${apiUrl}/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({username, password}),
      });

      const data = await response.json();

      if (data.access_token) {
          localStorage.setItem("access_token", data.access_token);
          const resAuthMe = await apiClient.get("/auth/me");

          if (resAuthMe.data){
            login(data.access_token, resAuthMe.data)
          }
          
          navigate("/home")
      }

      if (!response.ok) {
        setInputStatus("error")
        setError(data.detail)
        throw new Error(`HTTP error! status: ${response.status} body: ${data.detail}`);
      }

      

    } catch (err) {
      console.log(err)
      throw err;
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      {loading ? <div className="absolute bg-[#1f1c1c]/75 bg-opacity-20 min-w-screen z-20">
        <div className="flex items-center justify-center min-h-screen">
          <TailSpin
                    height="90"
                    width="90"
                    color="#00c8b2"
                    ariaLabel="tail-spin-loading"
                    visible={loading}
                />
        </div>
      </div>
      :
      null
      }
      
      <div className="grid min-h-screen justify-center items-center bg-[#242021]">
        <div className="bg-[#2e2e2e] shadow-2xl rounded-xl p-5 md:w-140 md:h-152 w-[20rem] h-120">
            <h1 className="text-3xl font-bold text-white text-center arimo-bold">Log in to account</h1>
            <div className="flex justify-center pt-5">
              <img src={UserCircle} alt="user_circle" className="h-auto md:w-64 w-32"/>
            </div>
            <form onSubmit={handleSumbit} className="pt-5 space-y-5">
                <FloatingInput 
                  id="user_name" label="Username" type="text" value={username}
                  required onChange={(e) => {
                    setUsername(e.target.value);
                    setInputStatus("neutral");
                    setError("");
                  }}
                  status={inputStatus}
                />
                <FloatingInput
                  id="user_password" label="Password" type={showPassword ? "text" : "password"}
                  value={password} required
                  onChange={(e) => {
                    setPassword(e.target.value);
                    setInputStatus("neutral");
                    setError("");
                  }}
                  endIcon={passwordIcon} status={inputStatus} spanText={error}
                />
                  
                <div className="text-center">
                  <button className="bg-[#00c8b2] arimo w-full rounded-xl py-3 focus:outline-none border border-transparent focus:border-white  hover:bg-[#1fb4a5] active:bg-[#2caa9e] active:border-[#1c8175]" type="submit">Sign In</button>
                </div>
            </form>
            <div className="text-center pt-5">
              <span className="arimo text-white">Don't you have an account? </span>
              <Link className="arimo text-[#299bef]" to="/register">Register</Link>
              
            </div>
        </div>
      </div>
    </>
  )
}
