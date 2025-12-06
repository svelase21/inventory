import { type SidebarToggleProps, SidebarToggleButton } from "./SidebarToggleButton"

export const Navbar: React.FC<SidebarToggleProps> = ( { onToggleSidebar, btnLabel }) => {
    return(
        <>
            <nav className="flex-1 bg-[#242021] px-2 py-2 overflow-y-auto overflow-x-hidden border-b border-[#3d3939] shadow-xs">
                <SidebarToggleButton onToggleSidebar={onToggleSidebar} btnLabel={btnLabel}/>
            </nav>
        </>
    )
}