export async function getIP() {
    const ip = await fetch("https://ipapi.co/json");
    return (await ip.json()).ip as string;
}

export function LsKey(key: string) {
    return `@aisle-${key}`
}
