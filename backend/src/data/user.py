from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from .dormitory import Dormitory


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    login: str
    first_name: str
    last_name: str
    email: str = Field(unique=True)
    hashed_password: str
    vk_id: Optional[str] = None
    gmail_id: Optional[str] = None
    reviews: List["Review"] = Relationship(back_populates="user")
    favorites: List["FavoriteDormitory"] = Relationship(back_populates="user")
