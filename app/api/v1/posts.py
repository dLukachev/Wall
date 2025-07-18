from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.api.deps import get_db

from app.schemas.posts import PostBase, PostRead
from app.crud.create_post import create_post
from app.crud.get_post import get_post
from app.crud.edit_post import update_post
from app.crud.delete_post import delete_post
from app.schemas.posts import PostUpdate, PostRead

from app.utils.check_user import get_current_user

router = APIRouter()


@router.get('/posts')
def get_p(db: Session = Depends(get_db), limit: int = 20, offset: int = 0):
    posts = get_post(db, limit=limit, offset=offset)
    return {"posts": [PostRead.model_validate(post) for post in posts]}


@router.post('/posts')
def create_p(post_in: PostBase, 
             authorization: Optional[str] = Header(None), 
             db: Session = Depends(get_db)
):
    user = get_current_user(authorization, db)
    
    post = create_post(db, post_in, user.id)

    return {'post': PostBase.model_validate(post, from_attributes=True)}


@router.put('/posts/{post_id}', response_model=PostRead)
def update_p(
    post_id: int,
    post_in: PostUpdate,
    db: Session = Depends(get_db),
    authorization: Optional[str] = Header(None)
):
    get_current_user(authorization, db)
    updated_post = update_post(db, post_id, post_in)
    return PostRead.model_validate(updated_post)


@router.delete('/posts/{post_id}', status_code=204)
def delete_p(
    post_id: int,
    db: Session = Depends(get_db),
    authorization: Optional[str] = Header(None)
):
    user = get_current_user(authorization, db)
    result = delete_post(post_id, db, user)
    if not result:
        raise HTTPException(status_code=404, detail="Post not found")
    return None