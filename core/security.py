from datetime import date, datetime, timedelta
from typing import Optional
from jose import jwt, JWTError

from .config import settings


def create_access_token(data: dict, expire_delta:Optional[timedelta]= None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else :
        expire = datetime.utcnow() + timedelta(settings.ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_verification_token(data:dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt