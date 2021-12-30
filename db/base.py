from typing import Any
from sqlalchemy.ext.declarative import declared_attr, as_declarative

@as_declarative
class Base:
    id: Any
    __name__: str


    # 클래스 이름으로 테이블네임 생성.
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()