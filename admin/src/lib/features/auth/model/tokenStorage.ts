import {get, writable} from "svelte/store";
import {ADMIN_TOKEN_LOCALSTORAGE_KEY} from "../config/consts";

export const token = writable<string | null>(null)

function loadTokenFromLocalStorage() {
    const savedToken = localStorage.getItem(ADMIN_TOKEN_LOCALSTORAGE_KEY)
    if (savedToken) {
        token.set(savedToken)
        return savedToken
    }
    return null
}

export function getAuthToken() {
    if (get(token)) {
        return get(token)
    }
    return loadTokenFromLocalStorage()
}

export function setAuthToken(newToken: string) {
    localStorage.setItem(ADMIN_TOKEN_LOCALSTORAGE_KEY, newToken)
    token.set(newToken)
}
