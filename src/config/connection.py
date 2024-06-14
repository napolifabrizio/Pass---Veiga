from sqlmodel import SQLModel, create_engine, Field
from typing import Optional, Union

class UserTable(SQLModel, table=True):

    codcli: Optional[int] = Field(primary_key=True)
    name: Union[str, None]
    email: str
    password: Union[str, None]
    is_admin: bool

class PositionTable(SQLModel, table=True):

    id_position: Optional[int] = Field(primary_key=True)
    codcli: int = Field(foreign_key="usertable.codcli")
    name: Union[str, None]
    password: Union[bytes, None]
    key: bytes

engine = create_engine("sqlite:///database.sqlite")

SQLModel.metadata.create_all(engine)

