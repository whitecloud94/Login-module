from fastapi import FastAPI

from core.config import settings

from db.session import engine   #new
from db.base_class import Base  #new


def create_tables():           #new
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VER)
	create_tables()       #new
	return app

app = start_application()