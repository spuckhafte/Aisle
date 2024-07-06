export type FetchMethods = "GET" | "POST";
export type FetchPayload = {
    GET: {
        path: string
    },
    POST: {
        path: string
        payload: any
    }
}
export type FetchStructure<T extends FetchMethods> = {
    type: T
    query: FetchPayload[T]
}
