from cryptography.fernet import Fernet

class CryptService():

    def __init__(self) -> None:
        self._key = Fernet.generate_key()

    def cripto(self, password: str, key):
        password_encode = password.encode()
        token = Fernet(key).encrypt(password_encode)
        return token

    def decrypt(self, token, key):
        password = Fernet(key).decrypt(token)
        password = password.decode()
        return password

    @property
    def key(self):
        return self._key

