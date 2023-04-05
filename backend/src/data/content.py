from typing import Optional

from sqlmodel import SQLModel, Field


class Content(SQLModel, table=True):
    name: Optional[str] = Field(default="", primary_key=True)
