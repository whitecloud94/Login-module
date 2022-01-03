#DB configuration.

from dotenv import load_dotenv, find_dotenv
from fastapi_mail import ConnectionConfig
import os

env_path = find_dotenv()
load_dotenv(env_path,verbose=True)

class settings:

    PROJECT_NAME: str = "2Factor 회원가입 테스트."
    PROJECT_VER: str = "0.0.0"

    DB_SERVER : str = os.getenv("DB_SERVER")
    DB_USER : str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: str = os.getenv("DB_PORT", 5432)

    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM : str = os.getenv("ALGORITHM")
    EMAIL_TOKEN_EXPIRE_TIME : str = os.getenv("EMAIL_TOKEN_EXPIRE_TIME")
    ACCESS_TOKEN_EXPIRE_TIME : str = os.getenv("ACCESS_TOKEN_EXPIRE_TIME")
    MAIL_USERNAME : str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD : str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM : str = os.getenv("MAIL_FROM")
    MAIL_PORT : str = os.getenv("MAIL_PORT")
    MAIL_SERVER : str = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME : str = os.getenv("MAIL_FROM_NAME")

mail_conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
)

settings = settings()


