"use client"

import Image from "next/image";
import { useEffect, useState } from "react"
import Input from "../ui/components/Input";
import Button from "../ui/components/Button";
import { rawFetch } from "../lib/actions";

type SignupResponse = {
    
}

export default function Login() {
    const [username, setUsername] = useState("");
    const [usernameError, setUsernameError] = useState("");
    
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");

    const [triggerSignup, setTriggerSignup] = useState(0);

    useEffect(() => {
        if (!triggerSignup) return;
        
        const signup = async () => {
            const response = await rawFetch<SignupResponse>({
                type: "POST",
                query: {
                    path: "/signup",
                    payload: { username, password },
                }
            });

            console.log(response);
        };
        
        signup();
    }, [triggerSignup]);


    return <div className="w-full h-[100vh] flex flex-col justify-center items-center">
        <div className="flex flex-col justify-center items-center">
            <div className="flex flex-col justify-center items-center mb-4">
                <Image src="/logo.png" alt="logo" width={300} height={150}/>
                <div className="italic font-extrabold transform translate-y-[-15px]">
                    the musical expirience
                </div>
            </div>
            <div>
                <Input 
                    content={{
                        value: username,
                        set: setUsername,
                    }}
                    error={usernameError}
                    placeholder="username"
                    type="text"
                    className="mb-3"
                />
                <Input 
                    content={{
                        value: password,
                        set: setPassword,
                    }}
                    error={passwordError}
                    placeholder="password"
                    type="password"
                    className="mb-3"
               />
               <Button text="Log In" className="mb-3"/>
            </div>
            <div className="text-xs text-gray-400 font-semibold flex flex-col justify-center items-center">
                <span>Don't have an account yet?</span>
                <span className=" my-1">
                    <span 
                        className="text-alter underline cursor-pointer"
                        onClick={() => setTriggerSignup(prev => prev + 1)}
                    >Sign Up</span> 
                    {" "} with the above details instead
                </span>
            </div>
        </div>

    </div>
}
