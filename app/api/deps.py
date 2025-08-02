from app.services.db import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

# Получение сессии базы данных
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()