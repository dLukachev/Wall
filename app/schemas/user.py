from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    nickname: str
    name: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}

class RegisterResponse(BaseModel):
    user: UserRead
    access_token: str
    token_type: str

    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    nickname: str
    password: str