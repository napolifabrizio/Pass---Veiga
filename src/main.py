from fastapi import FastAPI

from config.connection import PassManagerTable, UserTable
from repositories.user_repository import UserRepo
from repositories.pass_manager_repository import PassManagerRepo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#--------------------------------------------------#
#                      User                        #
#--------------------------------------------------#



#--------------------------------------------------#
#                   Accounts                       #
#--------------------------------------------------#
