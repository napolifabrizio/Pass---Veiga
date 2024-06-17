from config.connection import PositionTable
from repositories.father import Father
from config.connection import UserTable

# O propósito dessa classe responde essa questão:
# O que o usuário pode fazer no banco de dados?

class UserRepo(Father):

    def __init__(self) -> None:
        super().__init__()

# ------------------ Usuário ------------------ #
    def insert_my_user(self, user: UserTable):
        try:
            with self.session(self.engine) as session:
                session.add(user)
                session.commit()
                return_user = self.get_account(user.codcli)
            return return_user
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def login(self, email, password):
        try:
            user_login = ''
            with self.session(self.engine) as session:
                statement = self.select(UserTable)
                users = session.exec(statement).all()
            for user in users:
                if email == user.email:
                    user_login = user
                    break
            if password == user_login.password:
                return {
                    "codcli": user_login.codcli,
                    "name": user_login.name
                }
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def select_my_user(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement).one()
                return result
            except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_my_user(self, codcli):
        try:
            with self.session(self.engine) as session:
                statement = self.select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement)
                password = result.one()
                session.delete(password)
                session.commit()
            return "Usuário deletado!"
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

# ------------------ Positions ------------------ #
    def select_my_positions(self, codcli):
        try:
            with self.session(self.engine) as session:
                    statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                    result = session.exec(statement).all()
            return result
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def select_my_position(self, id_position):
        try:
            with self.session(self.engine) as session:
                    statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                    result = session.exec(statement).one()
            return result
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def insert_position(self, position: PositionTable):
        try:
            if not self._user_repo.get_account(position.codcli):
                return "Usuário não existe"
            with self.session(self.engine) as session:
                session.add(position)
                session.commit()
            return True
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def update_my_position(self, id_position, new_position):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                result = session.exec(statement)
                old_position = result.one()

                if new_position.name != None:
                    old_position.name = new_position.name
                if new_position.password != None:
                    old_position.password = new_position.password

                session.add(old_position)
                session.commit()
                session.refresh(old_position)
            return "Position atualizado!"
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_my_position(self, id_position):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                result = session.exec(statement)
                position = result.one()
                session.delete(position)
                session.commit()
            return "Position deletada!"
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_all_my_positions(self, codcli):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement)
                positions = result.all()
                for position in positions:
                    session.delete(position)
                session.commit()
            return "Todas positions deletadas!"
        except Exception as error:
                raise(f'Um erro desconhecido aconteceu no UserRepo: {error}')