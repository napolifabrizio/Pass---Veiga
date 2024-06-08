from sqlmodel import Session, select

from config.connection import engine

class Father():
    def __init__(self) -> None:
        self.session = Session
        self.select = select
        self.engine = engine