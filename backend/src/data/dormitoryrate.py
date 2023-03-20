from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

class DormitoryRate(SQLModel, table=True):
    __tablename__ = "dormitory_rate"

    id: Optional[int] = Field(default=None, primary_key=True)
    review_id: Optional["Review"] = Relationship(
        sa_relationship_kwargs={'uselist': False},
        back_populates="dormitory_rate"
    )
    total: float
    purity: int
    staff: int
    cost: int
    location: int
