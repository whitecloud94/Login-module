from typing import Generator

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from core.config import settings

DATABASE_URL = settings.DB_URL

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False ,bind=engine)


def get_db() -> Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()