from fastapi import HTTPException
from app.utils.jwt import decode_access_token
from app.models.users import User
from app.schemas.user import UserRead


def get_current_user(authorization, db):
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