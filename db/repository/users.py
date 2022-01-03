from sqlalchemy.orm import Session
from datetime import datetime

from schemas.users import UserCreate
from schemas.token import Token
from db.models.users import Users
from core.hashing import Hasher
from core.security import create_verification_token

def create_new_user(user:UserCreate, db:Session):
    user = Users(
    username = user.username,
    email=user.email,
    hashed_password=Hasher.get_hashed_password(user.password),

    is_active=False,
    is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(email:str, db:Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user

def activation(id:str, db:Session):
    user = db.query(Users).filter(Users.id == id).first()
    user.is_active = True
    db.add(user)
    db.commit()
    return user