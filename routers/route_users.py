from fastapi import APIRouter, Depends
from datetime import datetime

from sqlalchemy.orm import Session

from db.session import get_db

from db.repository.users import create_new_user, update_user_activation

from schemas.users import UserCreate, ShowUser


router = APIRouter()

@router.post("/", response_model=ShowUser)
async def create_user(user: UserCreate, db:Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.post("/activation",)
async def user_activation(id: int, token:str,
                         active: str, db:Session = Depends(get_db)):
    is_active = update_user_activation(id, db)
    return is_active