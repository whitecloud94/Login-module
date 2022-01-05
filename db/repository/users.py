from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from starlette.status import HTTP_404_NOT_FOUND
from db.models.users import Users
from db.models.token import Token
from schemas.users import UserCreate
from schemas.email import EmailSchema
from core.hashing import Hasher,Email_Hasher

def create_new_user(user:UserCreate, db:Session):
    user = Users(
    username = user.username,
    email=user.email,
    hashed_password=Hasher.get_hashed_password(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

class get_user():
    
    @staticmethod
    def get_user_by_email(email:EmailSchema, db:Session):
        user = db.query(Users).filter(Users.email == email).first()
        return user

    @staticmethod
    def get_user_by_id(id:int, db:Session):
        user = db.query(Users).filter(Users.id == id).first()
        return user

def update_user_activation(id:int, db:Session):
    user = db.query(Users).filter(Users.id == id).first()
    token = db.query(Token).filter(Token.user_id == id).first()
    token.expired = True
    user.is_active = False
    db.add(token)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user