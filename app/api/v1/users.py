from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.user import UserLogin, UserCreate, UserRead, RegisterResponse
from app.models.users import User
from app.crud.create_user import create_user
from app.crud.get_users import get_users
from app.crud.delete_users import delete_all_users
from app.api.deps import get_db

from app.utils.jwt import create_access_token
from app.utils.security import verify_password
from app.utils.jwt import decode_access_token

router = APIRouter()

@router.get("/users")
def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users(db)
    return {"users": [UserRead.model_validate(user) for user in users]}


@router.get("/check")
def get_current_user(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.split(" ")[1]
    try:
        payload = decode_access_token(token)
        nickname = payload.get("sub")
        if not nickname:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = db.query(User).filter_by(nickname=nickname).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        
        return UserRead.model_validate(user)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/register", response_model=RegisterResponse)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(nickname=user_in.nickname).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    
    user = create_user(db, user_in)
    access_token = create_access_token(data={"sub": user.nickname})

    return {"user": UserRead.model_validate(user), "access_token": access_token, "token_type": "bearer"}


@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(nickname=user_in.nickname).first()

    if not user or not verify_password(user_in.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect nickname or password")
    
    access_token = create_access_token(data={"sub": user.nickname})

    return {"access_token": access_token, "token_type": "bearer"}


@router.delete("/users")
def delete_all_users_endpoint(db: Session = Depends(get_db)):
    deleted_count = delete_all_users(db)
    return {"deleted": deleted_count}