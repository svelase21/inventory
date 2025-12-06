import './App.css'
import './Fonts.css'
import { Login } from './components/Login'
import { Home } from "./pages/home"
import { Route, Routes, BrowserRouter } from 'react-router'
import { AuthProvider } from './context/AuthProvider'
import React from 'react'
import ProtectedRoute from './components/ProtectedRoute'
import { Dashboard } from './pages/dashboard'

function App() {

  return (
    <React.StrictMode>
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/auth" element={<Login/>}/>
            <Route path="/" element={<Dashboard/>}/>
            {/* private routes */}
            <Route element={<ProtectedRoute/>}>
              <Route path="/home" element={<Home/>}/>
            </Route>
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </React.StrictMode>
  )
}

export default App
