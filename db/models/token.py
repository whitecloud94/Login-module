from sqlalchemy import (Column,
    Integer, 
    Boolean, 
    Date, 
    String, 
    func
 )
 
from sqlalchemy.sql.schema import ForeignKey

from datetime import timedelta

from db.base_class import Base

class Token(Base):
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String,unique=True, nullable=False)
    expiration_date = Column(Date, nullable=False, default=func.now() + timedelta(minutes=15))
    expired = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    create_date = Column(Date, nullable=False, default=func.now())