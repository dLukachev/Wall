from sqlalchemy.orm import Session
from app.models.users import User

# Получение всех пользователей
def get_users(db: Session):
    return db.query(User).all() 