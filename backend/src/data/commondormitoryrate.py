from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class CommonDormitoryRate(SQLModel, table=True):
    __tablename__ = "common_dormitory_rate"

    id: Optional[int] = Field(default=None, primary_key=True)
    dormitory_id: int = Field(foreign_key="dormitory.id")
    dormitory: Optional["Dormitory"] = Relationship(back_populates="rate")
    total: float
    count: int = 0
