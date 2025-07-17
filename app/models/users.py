from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    posts = relationship('Post', back_populates='user', cascade='all, delete-orphan')