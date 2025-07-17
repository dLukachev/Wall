from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead, RegisterResponse
from app.models.users import User
from app.crud.create_user import create_user
from app.api.deps import get_db

from app.utils.jwt import create_access_token

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": [UserRead.model_validate(user) for user in users]}


@router.post("/register", response_model=RegisterResponse)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(nickname=user_in.nickname).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    user = create_user(db, user_in)
    access_token = create_access_token(data={"sub": user.nickname})
    return {"user": UserRead.model_validate(user), "access_token": access_token, "token_type": "bearer"}


@router.delete("/users")
def delete_all_users(db: Session = Depends(get_db)):
    deleted_count = db.query(User).delete()
    db.commit()
    return {"deleted": deleted_count}