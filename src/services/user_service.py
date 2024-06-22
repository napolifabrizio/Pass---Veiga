from fastapi import HTTPException, status

from config.connection import PositionTable
from repositories.user_repository import UserRepo
from repositories.keys_repository import KeyPositionRepo, KeyUserRepo
from services.exceptions import treat_exception
from services.crpt_service import CryptService


class UserService():

    def __init__(self) -> None:
        self._crypt = CryptService()
        self._userRepo = UserRepo()
        self._keyUserRepo = KeyUserRepo()

# -------------------- User -------------------- #

    def create_my_account(self, user):
        try:
            key = self._crypt.key
            user.password = self._crypt.cripto(user.password, key)
            self._keyUserRepo.insert_key_position(key)
            return self._userRepo.insert_my_user(user)
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def login(self, user_login):
        try:
            key = self._keyUserRepo.select_my_key(user_login.codcli)
            user_login.password = self._crypt.cripto(user_login.password, key)
            return self._userRepo.login(user_login.email, user_login.password)
        except Exception as error:
            treat_exception(error, 'UserService')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credenciais inválidas.")

    def delete_my_account(self, codcli):
        try:
            if not (self._userRepo.delete_all_my_positions(codcli) and self._userRepo.delete_my_user(codcli)):
                return False
            self._userRepo.delete_all_my_positions(codcli)
            self._userRepo.delete_my_user(codcli)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')

# ------------------- Positions -------------------- #

    def get_my_positions(self, codcli):
        try:
            show_positions = []
            my_positions = self._userRepo.select_my_positions(codcli)
            if not my_positions:
                return False
            for position in my_positions:
                position.password = self._crypt.decrypt(position.password, position.key)
                show_positions.append(
                    {
                        "id_position":position.id_position,
                        "service_name": position.service_name,
                        "service_email": position.service_email,
                        "password": position.password
                    }
                )
            return show_positions
        except Exception as error:
            treat_exception(error, 'UserService')

    def create_position(self, position: PositionTable):
        try:
            position.key = self._crypt.key
            position.password = self._crypt.cripto(position.password, position.key)
            if not self._userRepo.insert_position(position):
                return False
            self._userRepo.insert_position(position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')

    def update_my_position(self, id_position, new_position):
        try:
            if not self.get_my_position(id_position):
                return False
            if new_position.password:
                old_position_key = self.get_my_position(id_position).key
                new_position.password = self._crypt.cripto(new_position.password, old_position_key)
            self._userRepo.update_my_position(id_position, new_position)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')

    def get_my_position(self, id_position):
        try:
            if not self._userRepo.select_my_position(id_position):
                return False
            my_position = self._userRepo.select_my_position(id_position)
            my_position.password = self._crypt.decrypt(my_position.password, my_position.key)
            return my_position
        except Exception as error:
            treat_exception(error, 'UserService')
        return False

    def delete_my_position(self, id_password):
        try:
            if not self._userRepo.delete_my_position(id_password):
                return False
            self._userRepo.delete_my_position(id_password)
            return True
        except Exception as error:
            treat_exception(error, 'UserService')
        return False
