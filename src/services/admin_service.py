from services.exceptions import treat_exception
from repositories.user_repository import UserRepo
from repositories.admin_repository import AdminRepo


class AdminService():

    def __init__(self) -> None:
        self._admin_repo = AdminRepo()
        self._position_manager = UserRepo()

    def create_user(self, user):
        try:
            self._admin_repo.insert_user(user)
        except Exception as error:
            treat_exception(error, 'AdminService')

    def delete_user(self, codcli):
        try:
            self._admin_repo.delete_user(codcli)
        except Exception as error:
            treat_exception(error, 'AdminService')

    def get_all_accounts(self):
        try:
            all_accounts = self._admin_repo.select_all_users()
            return all_accounts
        except Exception as error:
            treat_exception(error, 'AdminService')

    def get_accounts_positions(self, codcli):
        try:
            accounts_positions = self._admin_repo.select_user_positions(codcli)
        except Exception as error:
            treat_exception(error, 'AdminService')
        return accounts_positions

    def delete_all_user_positions(self, codcli):
        try:
            self._admin_repo.delete_all_user_positions(codcli)
        except Exception as error:
            treat_exception(error, 'AdminService')