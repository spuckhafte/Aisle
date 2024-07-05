import React from "react"

type ButtonElementsProps = {
    text: string,
    className?: string,
    onClick?: React.MouseEventHandler<HTMLButtonElement>
    type?: "submit" | "reset" | "button"
}
export default function Button(props: ButtonElementsProps) {
    return <button 
        className={
            "bg-alter rounded-[999px] h-[2.5rem] flex justify-center items-center font-bold cursor-pointer w-full"
            + " "
            + props.className ?? ""
        }
        type={props.type}
        onClick={props.onClick}
    >
        {props.text}
    </button>
}
