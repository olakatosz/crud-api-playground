from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    name: str
    job: str


class UserStore:
    def __init__(self):
        self.users_db: Dict[int, dict] = {}
        self.user_id_counter = 1

    def get_users(self):
        return self.users_db

    def create_user(self, user: User):
        user_id = self.user_id_counter
        self.users_db[user_id] = {"id": user_id,
                                  "name": user.name, "job": user.job}
        self.user_id_counter += 1
        return self.users_db[user_id]

    def update_user(self, user_id: int, user: User):
        if user_id in self.users_db:
            self.users_db[user_id] = {"id": user_id,
                                      "name": user.name, "job": user.job}
            return self.users_db[user_id]
        raise HTTPException(status_code=404, detail="User not found")

    def get_user(self, user_id: int):
        if user_id in self.users_db:
            return self.users_db[user_id]
        raise HTTPException(status_code=404, detail="User not found")

    def delete_user(self, user_id: int):
        if user_id in self.users_db:
            del self.users_db[user_id]
            return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")

    def reset_users(self):
        self.users_db.clear()
        self.user_id_counter = 1
        return {"message": "Test database reset"}


user_store = UserStore()
app = FastAPI()


@app.get("/users")
def get_users():
    return user_store.get_users()


@app.post("/users")
def create_user(user: User):
    return user_store.create_user(user)


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return user_store.update_user(user_id, user)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_store.get_user(user_id)


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_store.delete_user(user_id)


@app.delete("/reset-users")
def reset_users():
    return user_store.reset_users()
