export class YdApi {
    baseUrl = ''

    get(path: string) {
        console.log(this.baseUrl + path)
        return fetch(this.baseUrl + path, {
            method: 'GET'
        })
    }

    post(path: string, data: any) {
        return fetch(this.baseUrl + path, {
            method: 'POST',
            body: data
        })
    }
}

export const ydApi = new YdApi()
