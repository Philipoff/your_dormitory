import type {BaseModel} from "$lib/shared/data/models/BaseModel";
import {concatenatePath} from "$lib/shared/utils/concatenatePath";
import {ydApi} from "../ydApi";

export class API<T extends BaseModel> {
    path!: string

    constructor(path: string) {
        this.path = path
    }

    async fetch(id: string) {
        const _r = await ydApi.get(concatenatePath(this.path, 'get', id))
        return await _r.json()
    }
}
