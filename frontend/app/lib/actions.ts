"use server"

import { FetchMethods, FetchStructure } from "@/types";
import { getServerAddr, LsKey } from "./funcs";
import { cookies } from "next/headers";

export async function rawFetch<T, K extends FetchMethods = FetchMethods>(
    requestStructure: FetchStructure<K>,
    responseType: "json" | "text" = "json",
): Promise<T | null> {
    const SERVER_ADDR = getServerAddr();
    const serverTokenCookie = cookies().get(LsKey("server-token"))
    const serverToken = serverTokenCookie ? serverTokenCookie.value : "";
    
    const auth = {
        token: serverToken,
    };

    const header = new Headers();
    header.append("Authorization", JSON.stringify(auth));
    header.append("Content-Type", "application/json");

    try {
        return await (await fetch(SERVER_ADDR + "/" + requestStructure.query.path, {
            method: requestStructure.type,
            headers: header,
            body: JSON.stringify(requestStructure.query),
        }))[responseType]();
    } catch (e) {
        console.log(e);
        return null;
    }
}

export async function isLoggedIn() {
    const response = await rawFetch<string>({
        type: "POST",
        query: {
            path: "/is_logged_in",
            payload: ""
        }
    }, "text");

    return `${response}`.includes("true");
}

export async function storeInCookie(data: string) {
    cookies().set(LsKey("server-token"), data);
}
