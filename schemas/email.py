from typing import List
from pydantic import BaseModel
from pydantic import EmailStr

class EmailSchema(BaseModel):
    email: List[EmailStr]