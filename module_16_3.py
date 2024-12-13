from fastapi import FastAPI, Path
from typing import Annotated

users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()


@app.get("/users")
async def get_all() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_one(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                   , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    new_key = str(max(int(key) for key in users.keys()) + 1 if users else 1)
    users[new_key] = f"Имя: {username}, возраст: {age}"
    return f"User {new_key} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_one(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]
                  , username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                  , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def del_one(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    users.pop(str(user_id), None)
    return f"User {user_id} has been deleted"


