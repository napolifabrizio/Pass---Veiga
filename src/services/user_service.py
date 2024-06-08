import traceback

from config.connection import PositionTable
from services.crpt_service import CryptService
from repositories.position_manager_repository import PositionManagerRepo
from repositories.user_repository import UserRepo

class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._user_repo = UserRepo()
        self._position_manager = PositionManagerRepo()

    def get_my_positions(self, codcli):
        try:
            my_positions = self._position_manager.get_account_positions(codcli)
            for position in my_positions:
                position.password = self._crypt.decrypt(position.password)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())
        return my_positions

    def add_position(self, position: PositionTable):
        try:
            position.password = self._crypt.cripto(position.password)
            self._position_manager.post_position(position)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def update_position(self, id_password):
        try:
            self._position_manager.put_position(id_password)
            return True
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def delete_position(self, id_password):
        try:
            self._position_manager.delete_position(id_password)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def delete_my_account(self, codcli):
        try:
            self._position_manager.delete_all_positions(codcli)
            self._user_repo.delete_user(codcli)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())

    def create_my_account(self, user):
        try:
            self._user_repo.post_user(user)
        except Exception as error:
            print(f'Aconteceu um erro desconhecido no UserService: {error}')
            print(traceback.format_exc())




