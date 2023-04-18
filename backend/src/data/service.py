from typing import Any, List, Optional, Sequence, Type

import bcrypt as bcrypt
from pydantic import EmailStr
from sqlalchemy import asc, desc, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.elements import UnaryExpression
from sqlmodel import SQLModel, select

from .user import User


class DatabaseService:
    def __init__(self, dsn: str):
        self.engine = create_async_engine(url=dsn, future=True)
        self.session: Optional[AsyncSession] = None
        self.session = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)()

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

    async def get_user(self, email: EmailStr) -> Optional[User]:
        query = select(User).where(
            User.email == email,
        )
        result = (await self.session.execute(query)).first()
        if result:
            user = result[0]
            return user

    async def register_user(self, email: EmailStr, login: str, password: str) -> Optional[User]:
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        user = User(email=email, login=login, first_name=None, last_name=None,
                    hashed_password=hashed_password, reviews=[], favorites=[])
        await self.save(user)

        return user
