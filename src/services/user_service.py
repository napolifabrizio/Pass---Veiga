from repositories.pass_manager_repository import PassManagerRepo
from repositories.user_repository import UserRepo
from crpt import Crypt

class UserService():

    def __init__(self) -> None:
        self._crypt = Crypt()
        self._user_repo = UserRepo()
        self._pass_manager = PassManagerRepo()

    def get_my_passwords(codcli):
        my_passwords = PassManagerRepo.get_account_passwords(codcli)
        return my_passwords

    def add_password(self, password):
        if token := self._crypt.cripto(password):
            PassManagerRepo.post_password(token)
            return True
        return False

    def delete_my_account(self, codcli):
        try:
            self._pass_manager.delete_all_passwords(codcli)
            self._user_repo.delete_user(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')


