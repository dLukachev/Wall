from fastapi import FastAPI
from app.api.v1 import users
from app.api.v1 import posts

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)