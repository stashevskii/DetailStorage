from fastapi import FastAPI
from starlette.exceptions import HTTPException
from src.app.api.errors.detail import NotFoundDetailHttp, DetailAlreadyExistsHttp
from src.app.api.errors.user import (
    NotFoundUserHttp,
    UserAlreadyExistsHttp,
    DuplicateEmailHttp,
    DuplicateUsernameHttp
)
from .auth import InvalidCredentialsHttp
from .response import ExceptionResponseTemplate


def register_exceptions_handler(app: FastAPI):
    app.exception_handler(HTTPException)(lambda request, exc: ExceptionResponseTemplate(request, exc).template)


__all__ = [
    "NotFoundDetailHttp",
    "DetailAlreadyExistsHttp",
    "NotFoundUserHttp",
    "UserAlreadyExistsHttp",
    "DuplicateEmailHttp",
    "DuplicateUsernameHttp",
    "InvalidCredentialsHttp",
    "register_exceptions_handler",
]
