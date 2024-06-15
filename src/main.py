from fastapi import FastAPI

from config.connection import UserTable, PositionTable
from services.user_service import UserService
from services.admin_service import AdminService

app = FastAPI()

user_service = UserService()
admin_service = AdminService()
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

@app.post("/user/login/{email}/{password}")
def post_login_user(email, password):
    return user_service.login(email, password)

@app.delete("/user/delete_my_account/{codcli}")
def delete_my_account(codcli):
    user_service.delete_my_account(codcli)
    return "Conta deletada!"

@app.get("/user/get_my_positions/{codcli}")
def get_my_positions(codcli):
    my_positions = user_service.get_my_positions(codcli)
    return my_positions

@app.post("/user/post_position")
def post_position(position: PositionTable):
    user_service.create_position(position)
    return "Position criado!"

@app.put("/user/put_position/{id_position}")
def put_position(id_position, position: PositionTable):
    user_service.update_position(id_position, position)
    return "Position atualizado!"

@app.delete("/user/delete_position/{id}")
def delete_position(id):
    user_service.delete_position(id)
    return "Position deletado!"

#--------------------------------------------------#
#                      Admin                       #
#--------------------------------------------------#

@app.post("/admin/post_user")
def post_user(user: UserTable):
    admin_service.create_user(user)
    return "User criado!"

@app.delete("/admin/delete_user/{codcli}")
def delete_user(codcli):
    admin_service.delete_user(codcli)
    return "Conta deletada!"

@app.get("/admin/get_user_positions/{codcli}")
def get_user_positions(codcli):
    positions = admin_service.get_accounts_positions(codcli)
    return positions

@app.get("/admin/get_all_positions")
def get_all_positions():
    positions = admin_service.get_all_accounts()
    return positions

@app.delete("/admin/delete_user_positions/{codcli}")
def delete_user_positions(codcli):
    admin_service.delete_all_user_positions(codcli)
    return "Positions deletados"
