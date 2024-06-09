from fastapi import FastAPI

from config.connection import UserTable, PositionTable
from services.user_service import UserService

app = FastAPI()

user_service = UserService()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#--------------------------------------------------#
#                      User                        #
#--------------------------------------------------#

@app.post("/user/post_user")
def post_user(user: UserTable):
    user_service.create_my_account(user)
    return "User criado!"

@app.delete("/user/delete_my_account/{codcli}")
def delete_my_account(codcli):
    user_service.delete_my_account(codcli)
    return "Conta deletada!"

@app.get("/user/get_my_positions/{codcli}")
def get_my_passwords(codcli):
    positions = user_service.get_my_positions(codcli)
    return positions

@app.post("/user/post_position")
def post_position(position: PositionTable):
    user_service.post_position(position)
    return "Position criado!"

@app.delete("/user/delete_position/{id}")
def delete_position(id):
    user_service.delete_position(id)
    return "Position deletado!"

#--------------------------------------------------#
#                      Admin                       #
#--------------------------------------------------#
