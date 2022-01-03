from pydantic import BaseModel
from typing import List
from pydantic import EmailStr

class EmailSchema(BaseModel):
    email: List[EmailStr]