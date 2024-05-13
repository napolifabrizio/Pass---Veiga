from sqlmodel import SQLModel, create_engine, Field
from typing import Optional

class PassTable(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    password: str

engine = create_engine("sqlite:///database.sqlite")

SQLModel.metadata.create_all(engine)

