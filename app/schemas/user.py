from pydantic import BaseModel
from datetime import datetime

# Базовая схема для пользователя
class UserBase(BaseModel):
    nickname: str
    name: str

# Схема для создания пользователя
class UserCreate(UserBase):
    password: str

# Схема для чтения пользователя
class UserRead(UserBase):
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}

# Схема для регистрации пользователя
class RegisterResponse(BaseModel):
    user: UserRead
    access_token: str
    token_type: str

    model_config = {"from_attributes": True}

# Схема для входа в систему
class UserLogin(BaseModel):
    nickname: str
    password: str