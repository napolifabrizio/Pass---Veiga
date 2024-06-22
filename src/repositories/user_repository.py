from config.connection import PositionTable, UserTable
from repositories.father import Father

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
                return_user = self.select_my_user(user.codcli)
            return return_user
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')
                return False

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
                    "is_admin": user_login.is_admin,
                    "email":user_login.email,
                    "name":user_login.name,


                }
            return False
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def select_my_user(self, codcli):
            try:
                with self.session(self.engine) as session:
                    statement = self.select(UserTable).where(UserTable.codcli == codcli)
                    result = session.exec(statement).one()
                    if result:
                        return result
                return False
            except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_my_user(self, codcli):
        try:
            with self.session(self.engine) as session:
                statement = self.select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement)
                if not result:
                     return False
                password = result.one()
                session.delete(password)
                session.commit()
            return True
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

# ------------------ Position ------------------ #
    def select_my_positions(self, codcli):
        try:
            with self.session(self.engine) as session:
                    statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                    result = session.exec(statement).all()
            if not result:
                 return False
            return result
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def select_my_position(self, id_position):
        try:
            with self.session(self.engine) as session:
                    statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                    result = session.exec(statement).one()
            if not result:
                 return False
            return result
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def insert_position(self, position: PositionTable):
        try:
            if not self.select_my_user(position.codcli):
                return False
            with self.session(self.engine) as session:
                session.add(position)
                session.commit()
            return True
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def update_my_position(self, id_position, new_position):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                result = session.exec(statement)
                if not result:
                    return False
                old_position = result.one()

                if new_position.service_email != None:
                    old_position.service_email = new_position.service_email
                if new_position.service_name != None:
                    old_position.service_name = new_position.service_name
                if new_position.password != None:
                    old_position.password = new_position.password

                session.add(old_position)
                session.commit()
                session.refresh(old_position)
            return True
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_my_position(self, id_position):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.id_position == id_position)
                result = session.exec(statement)
                if not result:
                    return False
                position = result.one()
                session.delete(position)
                session.commit()
            return True
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_all_my_positions(self, codcli):
        try:
            with self.session(self.engine) as session:
                statement = self.select(PositionTable).where(PositionTable.codcli == codcli)
                result = session.exec(statement)
                if not result:
                    return False
                positions = result.all()
                for position in positions:
                    session.delete(position)
                session.commit()
            return True
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')