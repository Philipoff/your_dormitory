from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    text: str
    dormitory_id: int = Field(foreign_key="dormitory.id")
    dormitory_rate: Optional["DormitoryRate"] = Relationship(
        back_populates="review"
    )