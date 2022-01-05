from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.users import get_user
from db.repository.token import create_token, token_verify
from db.models.token import Token

router = APIRouter()

def check_exist(data):
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{data} not exist.")
    else:
        return data


@router.post("/token")
async def create_new_token(email:str,db:Session = Depends(get_db)):
    user = get_user.get_user_by_email(email=email, db=db)
    check_exist(user)
    token = create_token(user,db)
    return token


@router.get("/confirmation_token")
async def user_confirmation(token:str, db: Session=Depends(get_db)):
    token = db.query(Token).filter(Token.token == token).filter(Token.expired == False).first()

    check_exist(token)

    user = get_user.get_user_by_id(token.user_id, db)
    verify = token_verify(email=user.email, is_active=user.is_active,
                        create_time=user.created_at, token=token.token)
    return verify


@router.post("/recreate_token")
async def recreate_token(email:str, db:Session = Depends(get_db)):
    user = get_user.get_user_by_email(email, db)
    check_exist(user)