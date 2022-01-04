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
    user_id = db.query(Users.id).filter(Users.id == id).first()
    token = db.query(Token).filter(Token.user_id == user_id).first()
    return token