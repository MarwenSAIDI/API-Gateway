from sqlmodel import SQLModel, Field
from typing import Optional

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    writer_id: int
    abstract:str
    content: str