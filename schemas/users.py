# 유저 스키마.
from pydantic import BaseModel, EmailStr


#새로운 유저가 가입할 때 요구받는 인자.
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True