from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import (Depends, APIRouter,
    HTTPException,
    status)
from sqlalchemy.orm import Session

from db.session import get_db
from core.config import settings
from core.security import create_access_token
from core.hashing import Hasher
from schemas.token import AccessToken
from db.repository.login import get_user



router = APIRouter()

def authenticate_user(username: str, password: str,db: Session):
    user = get_user(username=username,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=AccessToken)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_TIME)
    access_token = create_access_token(
        data={"sub": user.email}, expire_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}