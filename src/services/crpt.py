from cryptography.fernet import Fernet

class Crypt():

    def __init__(self) -> None:
        self._key = Fernet.generate_key()
        self._f = Fernet(self._key)

    def cripto(self, password: str):
        password = password.encode()
        token = self._f.encrypt(password)
        return token

    def decrypt(self, token):
        password = self._f.decrypt(token)
        password = password.decode()
        return password

