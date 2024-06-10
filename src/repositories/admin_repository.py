import traceback

from config.connection import PositionTable, UserTable
from repositories.father import Father
from repositories.position_manager_repository import PositionManagerRepo
from repositories.user_repository import UserRepo

class AdminRepo(Father):

    def __init__(self) -> None:
        self._user_repo = UserRepo()
        self._position_manager = PositionManagerRepo()
        super().__init__()

    def insert_user(self, user: UserTable):
        with self.session(self.engine) as session:
            session.add(user)
            session.commit()
        return True

    def select_all_accounts(self):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable)
            result = session.exec(statement).all()
        return result

    def select_account_positions(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement).all()
            except:
                return 'Não encontrado :('
        return result

    def delete_all_user_positions(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
            result = session.exec(statement)
            positions = result.all()
            for position in positions:
                session.delete(position)
            session.commit()

    def delete_user(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(UserTable).where(UserTable.codcli == codcli)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()