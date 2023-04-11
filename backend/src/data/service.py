from typing import Any, List, Optional, Sequence, Type

import bcrypt as bcrypt
from pydantic import EmailStr
from sqlalchemy import asc, desc, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.elements import UnaryExpression
from sqlmodel import SQLModel, select

from .user import User


def cast_order_by(model_class: Type[SQLModel], field: str) -> Optional[UnaryExpression]:
    sort_func = desc if field.startswith("-") else asc
    field = field.lstrip("-")

    if not hasattr(model_class, field):
        return None

    return sort_func(getattr(model_class, field))


class DatabaseService:
    def __init__(self, dsn: str):
        self.engine = create_async_engine(url=dsn, future=True)
        self.session: Optional[AsyncSession] = None

    async def start(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.create_all)

        self.session = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)()

    async def stop(self):
        await self.session.close()
        self.session = None

    async def _first(self, query) -> Optional[Any]:
        result = (await self.session.execute(query)).first()
        if result:
            return result[0]

    async def _all(self, query, unpack: bool = False) -> Sequence[Any]:
        results = (await self.session.execute(query)).all() or []
        if unpack:
            results = [result[0] for result in results]
        return results

    async def save(self, instance: SQLModel) -> SQLModel:
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)

        return instance

    # async def get_user(self, email: EmailStr) -> Optional[models.User]:
    #     query = select(models.User, models.Employee).where(
    #         models.User.employee_id == models.Employee.id,
    #         models.Employee.email == email,
    #     )
    #     result = (await self.session.execute(query)).first()
    #     if result:
    #         user, employee = result
    #         user.employee = employee
    #         return user

    async def register_user(self, email: EmailStr, login: str, first_name: str,
                            last_name: str, password: str) -> Optional[User]:
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        user = User(email=email, login=login, first_name=first_name, last_name=last_name,
                    hashed_password=hashed_password, reviews=[], favorites=[])
        print("123123123123")
        # await self.save(user)

        return user
