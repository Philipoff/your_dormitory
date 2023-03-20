from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class CommonDormitoryRate(SQLModel, table=True):
    __tablename__ = "common_dormitory_rate"

    id: Optional[int] = Field(default=None, primary_key=True)
    dormitory_id: Optional["Dormitory"] = Relationship(
        sa_relationship_kwargs={'uselist': False},
        back_populates="common_dormitory_rate"
    )
    total: float
    count: int = 0
    