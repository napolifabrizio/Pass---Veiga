from sqlmodel import SQLModel, create_engine, Field
from typing import Optional, Union

class UserTable(SQLModel, table=True):

    codcli: Optional[int] = Field(primary_key=True)
    email: str = Field(unique=True)
    name: Union[str, None]
    password: Union[bytes, None]
    is_admin: bool

class PositionTable(SQLModel, table=True):

    id_position: Optional[int] = Field(primary_key=True)
    codcli: int = Field(foreign_key="usertable.codcli")
    service_name: Union[str, None]
    service_email: Union[str, None]
    password: Union[bytes, None]

class KeyUser(SQLModel, table=True):

    id_user: int = Field(foreign_key="usertable.codcli")
    key_user: bytes

class KeyPosition(SQLModel, table=True):

    id_position: int = Field(foreign_key="positiontable.id_position")
    key_position: bytes

engine = create_engine("sqlite:///database.sqlite")

SQLModel.metadata.create_all(engine)

