from fastapi import HTTPException

from config.connection import PositionTable
from repositories.user_repository import UserRepo
from services.exceptions import treat_exception
from services.crpt_service import CryptService

class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._user_repo = UserRepo()

    def create_my_account(self, user):
        try:
            return self._user_repo.insert_my_user(user)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def login(self, email, password):
        try:
            return self._user_repo.login(email, password)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def delete_my_account(self, codcli):
        try:
            self._user_repo.delete_all_my_positions(codcli)
            self._user_repo.delete_my_user(codcli)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def get_my_positions(self, codcli):
        try:
            my_positions = self._user_repo.select_my_positions(codcli)
            for position in my_positions:
                position.password = self._crypt.decrypt(position.password, position.key)
            return my_positions
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def create_position(self, position: PositionTable):
        try:
            position.key = self._crypt.key
            position.password = self._crypt.cripto(position.password, position.key)
            self._user_repo.insert_position(position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def update_my_position(self, id_position, new_position):
        try:
            if new_position.password:
                old_position_key = self.get_my_position(id_position).key
                new_position.password = self._crypt.cripto(new_position.password, old_position_key)
            self._user_repo.update_my_position(id_position, new_position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def get_my_position(self, id_position):
        try:
            my_position = self._user_repo.select_my_position(id_position)
            my_position.password = self._crypt.decrypt(my_position.password, my_position.key)
            return my_position
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def delete_my_position(self, id_password):
        try:
            self._user_repo.delete_my_position(id_password)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')
        return False
