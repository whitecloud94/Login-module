from fastapi import (APIRouter, 
    Depends,
    BackgroundTasks,
)
from fastapi.exceptions import HTTPException

from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from core.config import mail_conf
from schemas.email import EmailSchema

from db.session import get_db
from db.models.users import Users
from db.models.token import Token
from db.repository.users import get_user_by_email
from db.repository.token import get_token_by_user_id

router = APIRouter()


@router.post("/SendEmailBackround")
async def send_in_background(background_tasks: BackgroundTasks, email: EmailSchema, db:Session = Depends(get_db)) -> JSONResponse:
    user = get_user_by_email(email.email, db)
    token = get_token_by_user_id(id=user.id, db=db)
    token = token.token
    email = user.email
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="email not found.")
    
    message = MessageSchema(
        subject="이메일 인증 테스트",
        recipients=email.dict().get("email"),
        body=f"http://127.0.0.1/emails/confirmation?token={token}",
        )

    fm = FastMail(mail_conf)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={"message": "email has been sent successfully."})







@router.post("/confirmation_token")
async def user_confirmation(token:str, db: Session=Depends(get_db)):

    pass