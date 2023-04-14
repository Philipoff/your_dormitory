from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from ....services.auth.models.auth import (
    RestRegister,
)

from ....data.service import DatabaseService

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
    # auth_user = await database.get_user(data.email)

    user = await database.register_user(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        login=data.login,
        password=data.password,
    )
    return user
