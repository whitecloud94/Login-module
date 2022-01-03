from pydantic import BaseModel
# from typing import List
from pydantic import EmailStr

class Token(BaseModel):
    email: EmailStr
    datetime: str

class TokenCreate(BaseModel):
    token : str
    user_id : int