from typing import Optional

from sqlmodel import Field, SQLModel


class DormitoryType(SQLModel, table=True):
    __tablename__ = "dormitory_type"

    name: Optional[str] = Field(default="", primary_key=True)
