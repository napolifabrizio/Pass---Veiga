from fastapi import FastAPI

from config.connection import PassTable, UserTable
from repositories.user_repository import UserRepo
from repositories.pass_repository import PassRepo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/get_all_accounts')
def get_all_accounts():
    passwords = PassRepo.get_all_accounts(PassTable)
    return passwords

@app.get('/get_account_passwords/{id_password}')
def get_account_passwords(id_password: int):
    password = PassRepo.get_account_passwords(id_password, PassTable)
    return password

@app.post('/insert_password')
def post_password(password: PassTable):
    PassRepo.post_password(password)
    return 'Password guardada!'

@app.put('/update_password/{id_item}')
def put_password(id_item: int, password: PassTable):
    PassRepo.put_password(id_item, password, PassTable)
    return 'Password atualizada'

@app.delete('/delete_password/{id_item}')
def delete_password(id_item: int):
    PassRepo.delete_password(id_item, PassTable)
    return 'Password deletada'

@app.post('/insert_user')
def post_user(user: UserTable):
    UserRepo.post_user(user)
    return 'User cadastrado!'