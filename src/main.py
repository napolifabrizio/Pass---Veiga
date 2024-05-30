from fastapi import FastAPI

from config.connection import PassTable
from repositories.pass_repository import PassRepo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/get_passwords')
def get_passwords():
    passwords = PassRepo.get_passwords(PassTable)
    return passwords

@app.get('/get_password/{id_password}')
def get_passwords(id_password: int):
    password = PassRepo.get_password(id_password, PassTable)
    return password

@app.post('/insert')
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