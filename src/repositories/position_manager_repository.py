from config.connection import PositionTable
from repositories.father import Father
from repositories.user_repository import UserRepo


class PositionManagerRepo(Father):

    def __init__(self) -> None:
        self._user_repo = UserRepo()
        super().__init__()

    def get_account_positions(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement).all()
            except:
                return 'Não encontrado :('
        return result

    def insert_position(self, position: PositionTable):
        if not self._user_repo.get_account(position.codcli):
            return "Usuário não existe"
        with self.session(self.engine) as session:
            session.add(position)
            session.commit()
        return True

    def put_position(self, id_position, new_position):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.id == id_position)
            result = session.exec(statement)
            old_position = result.one()

            if new_position.name != None:
                old_position.name = new_position.name
            if new_position.password != None:
                old_position.password = new_position.password

            session.add(old_position)
            session.commit()
            session.refresh(old_position)

        return True

    def delete_position(self, id_position):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.id == id_position)
            result = session.exec(statement)
            position = result.one()
            session.delete(position)
            session.commit()

    def delete_all_positions(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
            result = session.exec(statement)
            positions = result.all()
            for position in positions:
                session.delete(position)
            session.commit()