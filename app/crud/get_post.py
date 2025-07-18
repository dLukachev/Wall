from sqlalchemy.orm import Session
from app.models.posts import Post
from sqlalchemy import desc

def get_post(db: Session):
    return db.query(Post).order_by(desc(Post.created_at)).all()