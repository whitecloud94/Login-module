#DB configuration.

from dotenv import load_dotenv, find_dotenv
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


settings = settings()


