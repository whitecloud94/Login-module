from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from db.session import get_db
from db.repository.users import get_user
from db.repository.token import create_token


router = APIRouter()

@router.post("/test")
async def create_new_token(email:str,db:Session = Depends(get_db)):
    user = get_user.get_user_by_email(email=email, db=db)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"{email} is not exist.")
    token = create_token(user,db)
    return token