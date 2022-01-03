from fastapi import status, HTTPException

from sqlalchemy.orm import Session


from schemas.token import TokenCreate
from db.models.users import Users



def create_token(email:str, token:TokenCreate , db:Session):
    user_id = db.query(Users).filter(Users.email == email).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not exist user.")
    token = TokenCreate(
        token=token,
        user_id=user_id
    )
    