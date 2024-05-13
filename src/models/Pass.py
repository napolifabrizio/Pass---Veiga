from pydantic import BaseModel

class Pass(BaseModel):

    name: str
    password: str