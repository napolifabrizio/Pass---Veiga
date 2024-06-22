from config.connection import KeyPosition, KeyUser
from repositories.father import Father

class KeyUserRepo(Father):

    def __init__(self) -> None:
        super().__init__()

    def insert_key_position(self, key_user: KeyUser):
        try:
            with self.session(self.engine) as session:
                    session.add(key_user)
                    session.commit()
        except Exception as error:
                print(f'Um erro desconhecido aconteceu no KeyUserRepo: {error}')
                return False

class KeyPositionRepo(Father):

    def __init__(self) -> None:
        super().__init__()