import traceback

from config.connection import PassManagerTable
from repositories.pass_manager_repository import PassManagerRepo
from repositories.user_repository import UserRepo
from services.crpt_service import CryptService

class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._user_repo = UserRepo()
        self._pass_manager = PassManagerRepo()

    def get_my_passwords(self, codcli):
        try:
            my_passwords = self._pass_manager.get_account_passwords(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())
        return my_passwords

    def add_password(self, password: PassManagerTable):
        try:
            print(password)
            password.password = self._crypt.cripto(password.password)
            self._pass_manager.post_password(password)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def update_password(self, id_password):
        try:
            self._pass_manager.put_password(id_password)
            return True
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def delete_password(self, id_password):
        try:
            self._pass_manager.delete_password(id_password)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def delete_my_account(self, codcli):
        try:
            self._pass_manager.delete_all_passwords(codcli)
            self._user_repo.delete_user(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def add_user(self, user):
        try:
            self._user_repo.post_user(user)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())




