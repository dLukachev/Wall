from sqlalchemy.orm import Session
from app.models.users import User

def delete_all_users(db: Session):
    deleted_count = db.query(User).delete()
    db.commit()
    return deleted_count 