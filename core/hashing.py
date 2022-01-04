from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

email_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    
    @staticmethod
    def get_hashed_password(password):
        return pwd_context.hash(password)



class Email_Hasher():
    @staticmethod
    def verify_code(plain_code, hashed_code):
        return email_context.verify(plain_code, hashed_code)

    @staticmethod
    def get_hashed_code(data):
        return email_context.hash(data)