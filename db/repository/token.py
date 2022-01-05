from datetime import datetime
from sqlalchemy.orm import Session
from db.models.users import Users
from core.hashing import Email_Hasher
from db.models.token import Token


def create_token(user:Users, db:Session):
    user = user
    plain_data = user.email+str(user.is_active)+str(user.created_at)
    hash_code = Email_Hasher.get_hashed_code(plain_data)
    token = Token(
        token = hash_code,
        user_id = user.id
    )
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


def get_token_by_user_id(id:int, db:Session):
    token = db.query(Token).filter(Token.user_id == id).first()
    return token


def token_verify(email: str, token: str, is_active:bool, create_time:datetime):
    is_active = str(is_active)
    create_time = str(create_time)
    plain_code = email+is_active+create_time
    verify = Email_Hasher.verify_code(plain_code, token)
    return verify