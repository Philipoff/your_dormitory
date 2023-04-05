from datetime import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from dormitorycontent import DormitoryContent


class DormitoryProperties(SQLModel, table=True):
    __tablename__ = "dormitory_properties"

    id: Optional[int] = Field(default=None, primary_key=True)
    dormitory_id: Optional["Dormitory"] = Relationship(
        sa_relationship_kwargs={'uselist': False},
        back_populates="dormitory_properties"
    )
    floors: Optional[int] = Field(default=None)
    people_in_room: Optional[str] = Field(default=None)
    contacts: Optional[str] = Field(default=None)
    foundation_year: Optional[datetime] = Field(default=None)
    dormitory_type: str = Field(foreign_key="dormitory_type.name")
    content: List["DormitoryContent"] = Relationship(back_populates="dormitory_properties")
