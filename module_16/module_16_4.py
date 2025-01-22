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


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: str) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


# @app.put("/user/{user_id}/{username}/{age}")
# async def update_user(user_id: str, username: str, age: int) -> str:
#     user = list(filter(lambda users: user.id == user_id))
#     users[user_id] = f'Имя: {username}, возраст: {age}'
#     return f"User {user_id} is updated"
#
#
# @app.delete("/user/{user_id}")
# async def delete_user(user_id: str) -> str:
#     users.pop(user_id)
#     return f"User {user_id} has been deleted"
