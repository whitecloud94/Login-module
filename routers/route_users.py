from fastapi import APIRouter, Depends
from datetime import datetime

from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.users import create_new_user
from core.security import create_verification_token
from schemas.users import UserCreate, ShowUser
from schemas.token import Token

router = APIRouter()

@router.post("/", response_model=ShowUser)
async def create_user(user: UserCreate, db:Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    data = Token(
        email=user.email,
        datetime=datetime.utcnow()
    )
    token = create_verification_token(data)
    
    return user


@router.post("/test")
async def create_user():
    data = {"email" : 'user@example.com',
            "datetime": str(datetime.utcnow())}
    token = create_verification_token(data) 
    return token