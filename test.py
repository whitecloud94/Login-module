from core.config import settings
from datetime import timedelta
access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_TIME))
print(access_token_expires)