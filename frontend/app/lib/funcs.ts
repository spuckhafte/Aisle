import { ZodError } from "zod";

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
