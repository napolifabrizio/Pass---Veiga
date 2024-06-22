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

    def select_my_key(self, id_user):
            try:
                with self.session(self.engine) as session:
                    statement = self.select(KeyUser).where(KeyUser.id_user == id_user)
                    result = session.exec(statement).one()
                    if result:
                        return result.key_user
                return False
            except Exception as error:
                print(f'Um erro desconhecido aconteceu no KeyUserRepo: {error}')

class KeyPositionRepo(Father):

    def __init__(self) -> None:
        super().__init__()