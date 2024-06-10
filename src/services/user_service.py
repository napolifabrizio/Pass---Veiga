import traceback

from config.connection import PositionTable
from services.crpt_service import CryptService
from repositories.position_manager_repository import PositionManagerRepo
from repositories.user_repository import UserRepo
from services.exceptions import treat_exception
class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._user_repo = UserRepo()
        self._position_manager = PositionManagerRepo()

    def create_my_account(self, user):
        try:
            self._user_repo.insert_user(user)
        except Exception as error:
            treat_exception(error, 'UserService')

    def delete_my_account(self, codcli):
        try:
            self._position_manager.delete_all_positions(codcli)
            self._user_repo.delete_my_user(codcli)
        except Exception as error:
            treat_exception(error, 'UserService')

    def get_my_positions(self, codcli):
        try:
            my_positions = self._position_manager.select_account_positions(codcli)
            for position in my_positions:
                position.password = self._crypt.decrypt(position.password, position.key)
        except Exception as error:
            treat_exception(error, 'UserService')
        return my_positions

    def create_position(self, position: PositionTable):
        try:
            position.key = self._crypt.key
            position.password = self._crypt.cripto(position.password, position.key)
            self._position_manager.insert_position(position)
        except Exception as error:
            treat_exception(error, 'UserService')

    def update_position(self, id_password, new_position):
        try:
            self._position_manager.update_position(id_password, new_position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')

    def delete_position(self, id_password):
        try:
            self._position_manager.delete_position(id_password)
        except Exception as error:
            treat_exception(error, 'UserService')
