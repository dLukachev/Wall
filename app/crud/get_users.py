from sqlalchemy.orm import Session
from app.models.users import User

def get_users(db: Session):
    return db.query(User).all() 