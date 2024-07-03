import React from "react"

type ButtonElementsProps = {
    text: string,
    className?: string,
    onClick?: React.MouseEventHandler<HTMLDivElement>
}
export default function Button(props: ButtonElementsProps) {
    return <div 
        className={
            "bg-alter rounded-[999px] h-[2.5rem] flex justify-center items-center font-bold cursor-pointer"
            + " "
            + props.className ?? ""
        }
        onClick={props.onClick}
    >
        {props.text}
    </div>
}
