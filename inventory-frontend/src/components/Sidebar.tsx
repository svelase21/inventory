import { User2, Users2 } from "lucide-react"
import { motion, AnimatePresence, spring } from "motion/react"

export const Sidebar = ( { isOpen } ) => {
    const menuItems = [{
        admin: [
            {
                icon: User2, label: "Users", url: "/users" 
            },
            {
                icon: User2, label: "Users", url: "/users" 
            }
        ]
    }]

    return (
        <>
            {/* {isOpen && (
                <div className="absolute h-screen bg-white w-[17rem]"></div>
            )} */}
            <aside
                className={
                    `flex p-2 bg-[#2c2929] h-screen transition-all duration-400 ease-in-out shadow-sm
                    ${isOpen ? "w-[22rem]" : "w-[4rem]"}`
                }
            >
                <div className="flex-1 content-baseline">
                    <motion.h1
                        className={`text-white text-center arimo text-3xl pb-3 h-[3rem]`}
                        animate={isOpen ? {opacity: 1} : {opacity: 0}}
                        hidden={isOpen ? false : true}
                    >
                        Admin
                    </motion.h1>
                    
                    { menuItems.map((sideOp) => (
                        sideOp.admin.map((admin, index) => (
                            <div key={index} className={
                                    `flex ${isOpen ? "space-x-2" : "ml-2"} text-[#c0c0c0] hover:bg-[#3d3939] active:bg-[#524e4e] rounded-full p-2 cursor-pointer`
                                }
                            >
                                <admin.icon/>
                                <motion.span
                                    className={`${isOpen ? "" : "hidden"}`}
                                    animate={isOpen ? {opacity: 1} : {opacity: 0}}
                                >
                                    {admin.label}
                                </motion.span>
                            </div>
                        ))
                    )) }
                </div>
            </aside>
        </>
    )
}