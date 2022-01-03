from fastapi import (APIRouter, 
    Depends,
    BackgroundTasks,
)

from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema

from core.config import mail_conf
from schemas.email import EmailSchema


router = APIRouter()


@router.post("/SendEmailBackround")
async def send_in_background(
    background_tasks: BackgroundTasks,
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi mail module",
        recipients=email.dict().get("email"),
        body="Simple background task",
        )

    fm = FastMail(mail_conf)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={"message": "email has been sent successfully."})