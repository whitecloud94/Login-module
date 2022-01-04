from fastapi import APIRouter, Depends
from datetime import datetime

from sqlalchemy.orm import Session

from db.session import get_db

from db.repository.users import create_new_user


from schemas.users import UserCreate, ShowUser


router = APIRouter()

@router.post("/", response_model=ShowUser)
async def create_user(user: UserCreate, db:Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
