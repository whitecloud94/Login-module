from fastapi import APIRouter

from . import route_users

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])