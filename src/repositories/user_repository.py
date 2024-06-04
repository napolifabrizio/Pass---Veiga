from sqlmodel import Session, select

from config.connection import engine, UserTable

class UserRepo():

    @staticmethod
    def post_user(user: UserTable):
        with Session(engine) as session:
            session.add(user)
            session.commit()
        return True

    @staticmethod
    def get_account(codcli):
        with Session(engine) as session:
            try:
                statement = select(UserTable).where(UserTable.codcli == codcli)
                result = session.exec(statement).one()
            except:
                return 'Não encontrado :('
        print(result)
        return result