from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base
from sqlalchemy.orm import relationship
import datetime

# Модель пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    password = Column(String(150), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    posts = relationship('app.models.posts.Post', back_populates='user', cascade='all, delete-orphan')