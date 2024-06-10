import traceback

from repositories.position_manager_repository import PositionManagerRepo
from repositories.admin_repository import AdminRepo

class AdminService():

    def __init__(self) -> None:
        self._admin_repo = AdminRepo()
        self._position_manager = PositionManagerRepo()

    def create_user(self, user):
        try:
            self._admin_repo.insert_user(user)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no AdminService: {error}')
            print(traceback.format_exc())

    def delete_user(self, codcli):
        try:
            self._admin_repo.delete_user(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no AdminService: {error}')
            print(traceback.format_exc())

    def get_all_accounts(self):
        try:
            all_accounts = self._admin_repo.select_all_accounts()
            return all_accounts
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no AdminService: {error}')
            print(traceback.format_exc())

    def get_accounts_positions(self, codcli):
        try:
            accounts_positions = self._admin_repo.select_account_positions(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no AdminService: {error}')
            print(traceback.format_exc())
        return accounts_positions

    def delete_all_user_positions(self, codcli):
        try:
            self._admin_repo.delete_all_user_positions(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no AdminService: {error}')
            print(traceback.format_exc())