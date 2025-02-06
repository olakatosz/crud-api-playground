from typing import Union
from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    name: str
    job: str


users_db: Dict[int, dict] = {}
user_id_counter = 1

app = FastAPI()


@app.get("/users")
def get_users():
    return users_db


@app.post("/users")
def create_user(user: User):
    global user_id_counter
    users_db[user_id_counter] = {
        "id": user_id_counter, "name": user.name, "job": user.job}
    user_id_counter += 1
    return users_db[user_id_counter - 1]


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in users_db:
        users_db[user_id] = {"id": user_id, "name": user.name, "job": user.job}
        return users_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users_db:
        del users_db[user_id]
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/reset-users")
def reset_users():
    global users_db, user_id_counter
    users_db = {}
    user_id_counter = 1
    return {"message": "Test database reset"}
