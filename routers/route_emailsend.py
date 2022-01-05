from fastapi import (APIRouter, 
    Depends,
    BackgroundTasks,
    HTTPException,
    status
)

from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from core.config import mail_conf
from schemas.email import EmailSchema

from db.session import get_db
from db.models.users import Users
from db.models.token import Token
from db.repository.users import get_user
from db.repository.token import get_token_by_user_id, token_verify

router = APIRouter()


@router.post("/SendEmailBackround")
async def send_in_background(background_tasks: BackgroundTasks, email: EmailSchema, db:Session = Depends(get_db)) -> JSONResponse:
    user_email = email.email[0]
    user = get_user.get_user_by_email(user_email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="email not found.")
    token = get_token_by_user_id(id=user.id, db=db)
    token = token.token

    message = MessageSchema(
        subject="이메일 인증 테스트",
        recipients=email.dict().get("email"),
        body=f"http://127.0.0.1:8000/emails/confirmation_token?token={token}",
        )

    fm = FastMail(mail_conf)

    background_tasks.add_task(fm.send_message,message)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "email has been sent successfully."})