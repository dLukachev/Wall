from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
import datetime

# Модель поста
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    img = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('app.models.users.User', back_populates='posts')