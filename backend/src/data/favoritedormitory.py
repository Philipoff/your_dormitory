from typing import Optional

from sqlmodel import Field, SQLModel, Relationship


class FavoriteDormitory(SQLModel, table=True):
    __tablename__ = "favorite_dormitory"

    id: Optional[int] = Field(default=None, primary_key=True)
    dormitory_id: int = Field(foreign_key="dormitory.id")
    dormitory: Optional["Dormitory"] = Relationship(back_populates="favorites")
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="favorites")
