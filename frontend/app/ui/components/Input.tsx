"use client"

import React from "react"

type InputElementProps = {
    content: {
        value: string,
        set: React.Dispatch<React.SetStateAction<string>>,
    },
    placeholder?: string,
    error?: string,
    type?: React.HTMLInputTypeAttribute,
    className?: string,
}

export default function Input(props: InputElementProps) {
    return <div 
        className={ 
            "" 
            + " " 
            + props.className ?? "" 
        }
    >
        <input 
            className="bg-transparent outline-none rounded-[999px] border-[2px] border-solid border-gray-500 focus:border-alter h-[2.5rem] px-3" 
            placeholder={props.placeholder}
            type={props.type}
            value={props.content.value}
            onInput={e => props.content.set(e.currentTarget.value)}
        />
        <div className="text-xs pl-3 text-red-600 font-semibold">{ props.error }</div>
    </div>
}
