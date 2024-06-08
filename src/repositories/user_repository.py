from config.connection import UserTable
from repositories.father import Father


class UserRepo(Father):

    def post_user(self, user: UserTable):
        try:
            with self.session(self.engine) as session:
                session.add(user)
                session.commit()
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')
        return True

    def get_account(self, codcli):
        with self.session(self.engine) as session:
            try:
                statement = self.select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement).one()
                print(result)
                return result
            except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')

    def delete_user(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(UserTable).where(UserTable.codcli == codcli)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()
