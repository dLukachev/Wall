from sqlalchemy.orm import Session
from app.models.posts import Post
from app.schemas.posts import PostBase
import datetime

def create_post(db: Session, post_in: PostBase, user_id: int) -> Post:
    db_post = Post(
        title = post_in.title,
        content = post_in.content,
        created_at = datetime.datetime.now(datetime.UTC),
        user_id=user_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post