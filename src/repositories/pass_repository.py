from sqlmodel import Session, select

from repositories.user_repository import UserRepo

from config.connection import engine, PassTable, UserTable

class PassRepo():

    # ! Estudando utilidade
    # @staticmethod
    # def get_all_accounts(table):
    #     with Session(engine) as session:
    #         statement = select(table)
    #         result = session.exec(statement).all()
    #     return result

    @staticmethod
    def get_account_passwords(codcli):
        with Session(engine) as session:
            try:
                statement = select(PassTable).where(PassTable.codcli == codcli)
                result = session.exec(statement).all()
            except:
                return 'Não encontrado :('
        return result

    @staticmethod
    def post_password(password: PassTable):
        if UserRepo.get_account(password.codcli):
            return "Usuário não existe"
        with Session(engine) as session:
            session.add(password)
            session.commit()
        return True

    def put_password(id_password, new_password, table):
        with Session(engine) as session:
            statement = select(table).where(table.id == id_password)
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

    @staticmethod
    def delete_password(id_password, table):
        with Session(engine) as session:
            statement = select(table).where(table.id == id_password)
            result = session.exec(statement)
            password = result.one()
            session.delete(password)
            session.commit()