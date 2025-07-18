from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    img: str

class PostRead(PostBase):
    id: int
    created_at: datetime
    user_id: int
    img: str

    model_config = {"from_attributes": True}

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    img: Optional[str] = None