# main.py
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User, UpdateUser
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()
db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


@app.get("/")
async def root(msg: str = ''):
    msg = msg or "Hello world"
    return {"greeting": msg}


@app.post("/api/v1/users", tags=['Users'])
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.get("/api/v1/users", tags=['Users'])
async def get_users():
    return db


@app.delete("/api/v1/users/{user_id}", tags=['Users'])
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
        return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {user_id} not found."
    )


@app.put("/api/v1/users/{user_id}", tags=['Users'])
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
        return user.id
    raise HTTPException(status_code=404,
                        detail=f"Could not find user with id: {user_id}")
