import { ClientValidate } from "@/types";
import { atomWithStorage } from "jotai/utils";
import { LsKey } from "./funcs";


export const clientValidateAtom = atomWithStorage<ClientValidate>(LsKey("client-validate"), {});
