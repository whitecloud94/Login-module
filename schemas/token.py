from pydantic import BaseModel, EmailStr

# from typing import List

class Token(BaseModel):
    email: EmailStr
    datetime: str

class TokenCreate(BaseModel):
    token : str

class AccessToken(BaseModel):
    access_token: str
    token_type: str