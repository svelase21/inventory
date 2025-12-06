import { type ReactNode } from "react";
import type React from "react";

// Define props component
interface FloatingInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    id: string;
    label: string;
    endIcon?: ReactNode;
    status?: "warning" | "error" | "correct" | "neutral";
    spanText?: string;
}

// Create ClassMap
const statusStyles = {
    warning: {
        border: "border-yellow-600",
        text: "text-yellow-600"
    },
    error: {
        border: "border-red-600",
        text: "text-red-600"
    },
    correct: {
        border: "border-green-600",
        text: "text-green-600"
    },
    neutral: {
        border: "border-gray-600",
        text: "text-gray-600 "
    }
}

// Crate component
const FloatingInput: React.FC<FloatingInputProps> = ({ id, label, endIcon, status = "neutral", spanText, ...props }) => {
    // Add padding to right if exists an icon
    const inputPadding = endIcon ? "ps-2.5 pe-10" : "px-2.5";
    const inputStyle = statusStyles[status]

    return (
        <div className="relative">
            <input
                id={id}
                className={`block ${inputPadding} arimo px-2.5 pb-2.5 pt-4 w-full text-sm text-white bg-[#222021] 
                   rounded-lg border ${inputStyle.border} appearance-none
                   focus:outline-none focus:ring-0 focus:border-[#299bef] peer`}
                placeholder=" "
                // More atributes (type, value, onChange, ...)
                {...props}
            />
            <label
                htmlFor={id}
                className="absolute arimo text-sm text-gray-500 duration-300 transform 
                   -translate-y-4 scale-75 top-4 z-10 origin-left start-2.5
                   
                   // Border color
                   peer-focus:text-[#299bef]
                   
                   // Initial status
                   peer-placeholder-shown:scale-100
                   peer-placeholder-shown:translate-y-0
                   
                   // Float status
                   peer-focus:scale-75
                   peer-focus:-translate-y-4"
            >
                {label}
            </label>
            <span className={`${inputStyle.text}`}>{spanText}</span>

            {/* render icon */}
            {endIcon && (
                <div className="absolute top-7 end-3.5 -translate-y-1/2">
                    {endIcon}
                </div>
            )}
        </div>
    )
}

export default FloatingInput