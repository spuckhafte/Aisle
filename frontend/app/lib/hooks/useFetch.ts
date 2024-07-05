import { ClientValidate, FetchMethods, FetchStructure } from "@/types";
import { useAtomValue } from "jotai";
import { useEffect, useState } from "react";
import { clientValidateAtom } from "../atoms";
import { getServerAddr, LsKey } from "../funcs";

export default function useFetch<T, K extends FetchMethods>(requestStructure: FetchStructure<K>) {
    const SERVER_ADDR = getServerAddr();

    const Res = useState<T | null>(null);
    const ResFailed = useState(false);
    const authDetails = useAtomValue(clientValidateAtom);

    const header = new Headers();
    header.append("Authorization", JSON.stringify(authDetails));
    header.append("Content-Type", "application/json");

    useEffect(() => {
        fetch(SERVER_ADDR + "/" + requestStructure.type, {
            method: requestStructure.type,
            headers: header,
            body: JSON.stringify(requestStructure.query),
        }).then(response => {
            ResFailed[1](!response.ok);
            return response.json();  
        }).then(res => Res[1](res)).catch(err => {
            console.log(err);
            ResFailed[1](true);
        });
    }, []);

    return [Res[0], ResFailed[0]] as [(T | null), boolean];
}


