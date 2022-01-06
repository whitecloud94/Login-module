from sqlalchemy.orm import Session

from db.models.users import Users

def get_user(username: str, db: Session):
    user = db.query(Users).filter(Users.email == username).first()
    return user