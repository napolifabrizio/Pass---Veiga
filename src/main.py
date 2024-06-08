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

@app.get("/user/get_my_passwords")
def user_post_password(codcli):
    user_service.get_my_passwords(codcli)
    return True

@app.post("/user/post_password")
def user_post_password(password: PositionTable):
    user_service.add_password(password)
    return "Senha guardada!"

@app.delete("/user/delete_my_account/{codcli}")
def delete_my_account(codcli):
    user_service.delete_my_account(codcli)
    return "Conta deletada!"

@app.post("/user/post_user")
def post_user(user: UserTable):
    user_service.add_user(user)
    return "User criado!"

#--------------------------------------------------#
#                      Admin                       #
#--------------------------------------------------#
