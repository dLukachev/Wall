from fastapi import FastAPI
from api.v1.users import router

app = FastAPI()

app.include_router(r)