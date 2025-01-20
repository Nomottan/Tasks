from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: str, age: str) -> str:
    curr_us = User()
    curr_us.id = len(users)
    curr_us.username = str(username)
    curr_us.age = int(age)
    users.append(curr_us)
    return f"{curr_us} is registered"
