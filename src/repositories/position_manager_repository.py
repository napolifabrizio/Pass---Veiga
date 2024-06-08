from config.connection import PositionTable
from repositories.father import Father
from repositories.user_repository import UserRepo


class PositionManagerRepo(Father):

    def __init__(self) -> None:
        self._user_repo = UserRepo()
        super().__init__()

    def get_account_passwords(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement).all()
            except:
                return 'Não encontrado :('
        return result

    def post_password(self, password: PositionTable):
        if not UserRepo.get_account(password.codcli):
            return "Usuário não existe"
        with self.session(self.engine) as session:
            session.add(password)
            session.commit()
        return True

    def put_password(self, id_password, new_password):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.id == id_password)
            result = session.exec(statement)
            old_password = result.one()

            if new_password.name != None:
                old_password.name = new_password.name
            if new_password.password != None:
                old_password.password = new_password.password

            session.add(old_password)
            session.commit()
            session.refresh(old_password)

        return True

    def delete_password(self, id_password):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.id == id_password)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()

    def delete_all_passwords(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
            result = session.exec(statement)
            passwords = result.all()
            for password in passwords:
                session.delete(password)
            session.commit()