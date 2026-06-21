from sqlmodel import SQLModel, Field
from typing import Optional

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    witer_id: int = Field(foreign_key=True)
    abstract:str
    content: str