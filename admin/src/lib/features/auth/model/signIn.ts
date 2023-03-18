import {setAuthToken} from "./tokenStorage";

export const signIn = async (login: string, password: string) => {
    console.log(`send auth request ${login} ${password}`)
    setAuthToken('obtained token')
}
