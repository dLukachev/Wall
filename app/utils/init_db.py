from app.services.db import engine
from app.models.base import Base

Base.metadata.create_all(bind=engine)