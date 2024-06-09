import traceback

from config.connection import PositionTable, UserTable
from repositories.father import Father
from repositories.position_manager_repository import PositionManagerRepo
from repositories.user_repository import UserRepo

class AdminRepo(Father):

    def __init__(self) -> None:
        self._user_repo = UserRepo()
        self._position_manager = PositionManagerRepo()

    def create_user(self, user: UserTable):
        with self.session(self.engine) as session:
            session.add(user)
            session.commit()
        return True

    def get_all_accounts(self, table):
        with self.session(self.engine) as session:
            statement = self.select(table)
            result = session.exec(statement).all()
        return result

    def get_account_positions(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement).all()
            except:
                return 'Não encontrado :('
        return result

    def delete_all_positions_of_user(self, codcli):
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