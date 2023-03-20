import {getAuthToken} from "./tokenStorage";

export async function checkAuth() {
    return !!getAuthToken();
}
