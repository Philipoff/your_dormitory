from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from dormitory import Dormitory


class UniversityBranch(SQLModel, table=True):
    __tablename__ = "university_branch"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    university_id: int = Field(foreign_key="university.id")
    city_id: int = Field(foreign_key="city.id")
    is_branch: bool
    dormitories: List["Dormitory"] = Relationship(back_populates="university_branch")
