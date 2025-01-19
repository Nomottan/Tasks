from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_user() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(ge=0, le=100, description="Enter your id", example="1")) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


@app.get("/user/{username}/{age}")
async def get_user(username: Annotated[
    str, Path(
        min_length=5, max_length=20, description="Enter your name", example="itsname"
    )], age: Annotated[
    int, Path(ge=0, le=100, description="Enter your id", example="1"
    )]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
