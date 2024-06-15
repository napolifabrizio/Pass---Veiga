from config.connection import UserTable
from repositories.father import Father


class UserRepo(Father):

    def insert_user(self, user: UserTable):
        try:
            with self.session(self.engine) as session:
                session.add(user)
                session.commit()
                return_user = self.get_account(user.codcli)
            return return_user
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')
        return False

    def login(self, email, password):
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
        return False


    def get_account(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement).one()
                print(result)
                return result
            except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_my_user(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(UserTable).where(UserTable.codcli == codcli)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()
