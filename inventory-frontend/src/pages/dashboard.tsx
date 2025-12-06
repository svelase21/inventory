import { useState } from "react"
import { Sidebar } from "../components/Sidebar"
import { Navbar } from "../components/Navbar"
import { AlignJustifyIcon } from "lucide-react"

export const Dashboard = () => {
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(true)

  return (
    <div className='flex min-h-screen bg-[#242021]'>
      <Sidebar isOpen={sidebarOpen}/>
      <div>
        <Navbar onToggleSidebar={() => setSidebarOpen(!sidebarOpen)} btnLabel={<AlignJustifyIcon/>}/>
      </div>
    </div>
  )
}
