from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from .dormitoryrate import DormitoryRate


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="reviews")
    text: str
    dormitory_id: int = Field(foreign_key="dormitory.id")
    dormitory: Optional["Dormitory"] = Relationship(back_populates="reviews")
    dormitory_rate: Optional["DormitoryRate"] = Relationship(
        back_populates="review"
    )
