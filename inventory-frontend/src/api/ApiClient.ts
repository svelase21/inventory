import axios from "axios";

// Instance of Axios
const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// Configuration interceptor
apiClient.interceptors.request.use(
    (config) => {
        // Get JWT Token
        const token = localStorage.getItem("access_token");

        // Confirm if JWT Token exists
        if (token){
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default apiClient;