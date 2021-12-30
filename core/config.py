#DB configuration.

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


class settings:
    DB_SERVER : str = os.getenv("DB_URL")
    DB_USER : str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: str = os.getenv("DB_PORT")

    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"


settings = settings()