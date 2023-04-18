from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from ....services.auth.models.auth import (
    RestRegister,
    RestLogin
)

from ....data.service import DatabaseService

from ....services.auth.jwt_processing import Auth

auth_router = APIRouter()


@auth_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    responses={400: {}, 401: {}, 403: {}},
)
async def register(request: Request, data: RestRegister):
    database: DatabaseService = request.app.state.database
    user = await database.get_user(email=data.email)

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist",
        )

    user = await database.register_user(
        email=data.email,
        login=data.login,
        password=data.password,
    )

    auth = Auth()
    access_token = auth.create_token(user.email)
    refresh_token = auth.create_refresh_token(user.email)
    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_router.post("/login")
async def login(request: Request, data: RestLogin):
    database: DatabaseService = request.app.state.database

    auth = Auth()
    user = await database.get_user(email=data.email)

    if user is None:
        return HTTPException(status_code=401, detail='Invalid email')
    if not auth.verify_password(data.password, user.hashed_password):
        return HTTPException(status_code=401, detail='Invalid password')

    access_token = auth.create_token(data.email)
    refresh_token = auth.create_refresh_token(data.email)

    return {"access_token": access_token, "refresh_token": refresh_token}
