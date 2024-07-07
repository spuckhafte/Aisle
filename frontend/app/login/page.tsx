"use client"

import Image from "next/image";
import { useEffect, useState } from "react"
import Input from "../ui/components/Input";
import Button from "../ui/components/Button";
import { rawFetch, storeInCookie } from "../lib/actions";
import { passwordSchema, usernameSchema } from "../lib/zchemas";
import { getZodError } from "../lib/funcs";
import { useRouter } from "next/navigation";

type SignupResponse = {
    token: string,
    err: string,
}

export default function Login() {
    const router = useRouter()

    const [username, setUsername] = useState("");
    const [usernameError, setUsernameError] = useState("");
    
    const [password, setPassword] = useState("");
    const [passwordError, setPasswordError] = useState("");

    const [triggerSignup, setTriggerSignup] = useState(0);

    useEffect(() => {
        if (!triggerSignup) return;
        
        try {
            usernameSchema.parse(username);
        } catch (e) {
            setUsernameError(getZodError(e));
            return;
        };

        try {
            passwordSchema.parse(password);
        } catch (e) {
            setPasswordError(getZodError(e));
            return;
        };
          

        const signup = async () => {
            const response = await rawFetch<SignupResponse>({
                type: "POST",
                query: {
                    path: "/signup",
                    payload: { username, password },
                }
            });

            if (!response) {
                console.log("no response from server");
                return
            }
            
            if (response.err && response.err.includes("(showcase)")) {
                setUsernameError(response.err.split("(showcase)")[1].trim());
            }

            if (response.err)
                return;

            await storeInCookie(response.token)
            router.replace("/");
        };
        
        signup();
    }, [triggerSignup]);

    useEffect(() => setUsernameError(""), [username]);
    useEffect(() => setPasswordError(""), [password]);

    return <div className="w-full h-[100vh] flex flex-col justify-center items-center">
        <div className="flex flex-col justify-center items-center w-[300px]">
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
