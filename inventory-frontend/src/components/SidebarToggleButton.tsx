
export interface SidebarToggleProps{
    onToggleSidebar: () => void;
    btnLabel: React.RefAttributes<SVGSVGElement> | string;
}

export const SidebarToggleButton: React.FC<SidebarToggleProps> = ( { onToggleSidebar, btnLabel }) => {
    return (
        <button
            className="text-[#c0c0c0] text-xl arimo rounded-full p-2 hover:bg-[#3d3939] active:bg-[#524e4e] cursor-pointer"
            onClick={onToggleSidebar}
            type="button"
        >
            {btnLabel}
        </button>
    )
}