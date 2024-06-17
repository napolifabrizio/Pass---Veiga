from fastapi import HTTPException

from config.connection import PositionTable
from repositories.position_manager_repository import PositionManagerRepo
from repositories.user_repository import UserRepo
from services.exceptions import treat_exception
from services.crpt_service import CryptService

class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._user_repo = UserRepo()
        self._position_manager_repo = PositionManagerRepo()

    def create_my_account(self, user):
        try:
            return self._user_repo.insert_user(user)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def login(self, user_login):
        try:
            return self._user_repo.login(user_login.email, user_login.password)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def delete_my_account(self, codcli):
        try:
            self._position_manager_repo.delete_all_positions(codcli)
            self._user_repo.delete_my_user(codcli)
        except Exception as error:
            treat_exception(error, 'UserService')

    def get_my_positions(self, codcli):
        try:
            my_positions = self._position_manager_repo.get_account_positions(codcli)
            for position in my_positions:
                position.password = self._crypt.decrypt(position.password, position.key)
        except Exception as error:
            treat_exception(error, 'UserService')
        return my_positions

    def create_position(self, position: PositionTable):
        try:
            position.key = self._crypt.key
            position.password = self._crypt.cripto(position.password, position.key)
            self._position_manager_repo.insert_position(position)
        except Exception as error:
            treat_exception(error, 'UserService')

    def update_position(self, id_position, new_position):
        try:
            if new_position.password:
                old_position_key = self.get_my_position(id_position).key
                new_position.password = self._crypt.cripto(new_position.password, old_position_key)
            self._position_manager_repo.put_position(id_position, new_position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')

    def get_my_position(self, id_position):
        try:
            my_position = self._position_manager_repo.get_account_position(id_position)
            my_position.password = self._crypt.decrypt(my_position.password, my_position.key)
            return my_position
        except Exception as error:
            treat_exception(error, 'UserService')

    def delete_position(self, id_password):
        try:
            self._position_manager_repo.delete_position(id_password)
        except Exception as error:
            treat_exception(error, 'UserService')
