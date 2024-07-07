import { ZodError } from "zod";

export async function getIP() {
    const ip = await fetch("https://ipapi.co/json");
    return (await ip.json()).ip as string;
}

export function getServerAddr() {
    return "http://localhost:5000";
}

export function LsKey(key: string) {
    return `@aisle-${key}`
}

export function getZodError(e: any): string {
    const err = e as ZodError;
    return JSON.parse(err.message)[0].message;
}
