export interface ClientValidate {
    token?: string
    ip?: string
}

type FetchMethods = "GET" | "POST";
type FetchPayload = {
    GET: {
        path: string
    },
    POST: {
        path: string
        payload: any
    }
}
type FetchStructure<T extends FetchMethods> = {
    type: T
    query: FetchPayload[T]
}
