from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.user import UserCreate
from app.utils.security import get_password_hash
import datetime

def create_user(db: Session, user_in: UserCreate) -> User:
    hash_password = get_password_hash(user_in.password)
    db_user = User(
        nickname = user_in.nickname,
        name = user_in.name,
        password = hash_password,
        created_at = datetime.datetime.now(datetime.UTC)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user