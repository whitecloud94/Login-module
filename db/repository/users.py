from sqlalchemy.orm import Session
from datetime import datetime
from db.models.users import Users
from schemas.users import UserCreate

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


def get_user_by_email(email:str, db:Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user
