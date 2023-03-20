import {BaseModel} from "../shared/data/models/BaseModel";
import {Entity} from "../shared/data/decorators/Entity";
import {API} from "../shared/api/models/API";
import {Column} from "../shared/data/decorators/Column";


@Entity()
export class User extends BaseModel {
    api: API<User> = new API('users')

    @Column()
    name!: string
}
