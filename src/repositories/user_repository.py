from sqlmodel import Session, select

from config.connection import engine, UserTable

class UserRepo():

    @staticmethod
    def post_user(user: UserTable):
        try:
            with Session(engine) as session:
                session.add(user)
                session.commit()
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')
        return True

    @staticmethod
    def get_account(codcli):
        with Session(engine) as session:
            try:
                statement = select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement).one()
            except Exception as error:
                print(f'Um erro desconhecido aconteceu no UserRepo: {error}')
        print(result)
        return result

    def delete_user(self, codcli):
        with self.session(self.engine) as session:
            statement = self.select(UserTable).where(UserTable.codcli == codcli)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()
