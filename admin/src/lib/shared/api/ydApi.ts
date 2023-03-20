import {API_URL} from "../config";
import {concatenatePath} from "../utils/concatenatePath";

export class YdApi {
    apiUrl = API_URL

    get(path: string) {
        return fetch(this.apiUrl + concatenatePath(path), {
            method: 'GET'
        })
    }

    post(path: string, data: any) {
        return fetch(this.apiUrl + concatenatePath(path), {
            method: 'POST',
            body: data
        })
    }
}

export const ydApi = new YdApi()
