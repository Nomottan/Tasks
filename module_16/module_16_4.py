from fastapi import FastAPI, HTTPException
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


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        user = [us for us in users if us.id == user_id]
        user = user[0]
        user.username = username
        user.age = age
        return f"User {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")



@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        user = [us for us in users if us.id == user_id]
        user = user[0]
        users.pop(user)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
