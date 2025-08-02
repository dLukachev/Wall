from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users
from app.api.v1 import posts

app = FastAPI()

# Разрешаем CORS для всех источников
# Так делать нельзя ни в коем случае, необходимо ограничить доступ к API только к некоторым необходимым адресам
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(users.router)
app.include_router(posts.router)