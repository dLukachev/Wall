from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
import datetime

# Модель стены
class Wall(Base):
    __tablename__ = 'wall'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # На чьей стене пост
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)  # Какой пост
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))  # Когда размещён на стене

    user = relationship('app.models.users.User', backref='wall_posts')
    post = relationship('app.models.posts.Post', backref='wall_entries')