from sqlalchemy.orm import Session
from app.models.posts import Post
from app.schemas.posts import PostUpdate

# Обновление поста
def update_post(db: Session, post_id: int, post_in: PostUpdate):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None
    for field, value in post_in.model_dump(exclude_unset=True).items():
        setattr(post, field, value)
    db.commit()
    db.refresh(post)
    return post