from fastapi import APIRouter

from . import route_users
from . import route_emailsend
from . import route_token

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_emailsend.router, prefix="/emails", tags=["email"])
api_router.include_router(route_token.router, prefix="/createToken", tags=["token"])