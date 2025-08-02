from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.posts import Post

# Удаление поста
def delete_post(id: int, db: Session, user):
    post = db.query(Post).filter_by(id=id).first()
    if not post or post.user_id != user.id:
        raise HTTPException(status_code=404, detail="The post was not found")
    db.delete(post)
    db.commit()
    return True
