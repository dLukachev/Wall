from app.services.db import engine
from app.models.users import Base
from app.models.users import User
from app.models.posts import Post

Base.metadata.create_all(bind=engine)