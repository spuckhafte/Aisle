"use server"

import { FetchMethods, FetchStructure } from "@/types";
import { getServerAddr, LsKey } from "./funcs";
import { cookies } from "next/headers";

export async function rawFetch<T, K extends FetchMethods = FetchMethods>(requestStructure: FetchStructure<K>): Promise<T | null> {
    const SERVER_ADDR = getServerAddr();
    const clientValidateCookie = cookies().get(LsKey("client-validate"))
    const authDetails = clientValidateCookie ? clientValidateCookie.value : "{}";

    const header = new Headers();
    header.append("Authorization", JSON.stringify(authDetails));
    header.append("Content-Type", "application/json");

    try {
        return await (await fetch(SERVER_ADDR + "/" + requestStructure.query.path, {
            method: requestStructure.type,
            headers: header,
            body: JSON.stringify(requestStructure.query),
        })).json();
    } catch (e) {
        console.log(e);
        return null;
    }
}
