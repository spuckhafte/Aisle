import { cookies } from "next/headers";
import { LsKey } from "./lib/funcs";
import { isLoggedIn } from "./lib/actions";
import { useRouter } from "next/router";
import { redirect } from "next/navigation";

export default async function Home() {
    const loginStatus = await isLoggedIn();

    if (!loginStatus)
        redirect("/login");

    return <div>
        Hello World
    </div>;
}
