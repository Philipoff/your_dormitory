from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from commondormitoryrate import CommonDormitoryRate
from dormitoryproperties import DormitoryProperties


# from review import Review


class Dormitory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Optional[str] = Field(default=None)
    rate: Optional["CommonDormitoryRate"] = Relationship(
        back_populates="dormitory"
    )
    properties: Optional["DormitoryProperties"] = Relationship(
        back_populates="dormitory"
    )
    reviews: List["Review"] = Relationship(back_populates="dormitory")
