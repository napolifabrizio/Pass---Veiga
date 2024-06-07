from repositories.pass_repository import PassRepo
from crpt import Crypt

class PassController():

    def __init__(self) -> None:
        self._crypt = Crypt()

    def get_my_passwords(codcli):
        my_passwords = PassRepo.get_account_passwords(codcli)
        return my_passwords

    def add_password(self, password):
        if token := self._crypt.cripto(password):
            PassRepo.post_password(token)
            return True
        return False

