from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class DormitoryContent(SQLModel, table=True):
    __tablename__ = "common_content"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(foreign_key="content.name")
    dormitory_property_id: int = Field(foreign_key="dormitory_properties.id")
    dormitory_properties: Optional["DormitoryProperties"] = Relationship(back_populates="content")
