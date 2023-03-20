from typing import Optional

from sqlmodel import Field, SQLModel


class FavoriteDormitory(SQLModel, table=True):
    __tablename__ = "favorite_dormitory"

    id: Optional[int] = Field(default=None, primary_key=True)
    dormitory_id: int = Field(foreign_key="dormitory.id")
    user_id: int = Field(foreign_key="user.id")
