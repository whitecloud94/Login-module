from fastapi import APIRouter, Depends
from datetime import datetime
from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from db.repository.token import token_verify

from db.session import get_db

from db.repository.users import create_new_user, update_user_activation

from schemas.users import UserCreate, ShowUser


router = APIRouter()

@router.post("/", response_model=ShowUser)
async def create_user(user: UserCreate, db:Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.post("/activation",)
async def user_activation(id: int, db:Session = Depends(get_db)):
    if token_verify:
        is_active = update_user_activation(id, db)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return is_active