from fastapi import FastAPI
from starlette.exceptions import HTTPException
from src.app.api.errors.detail import NotFoundDetailHttpException, DetailAlreadyExistsHttpException
from src.app.api.errors.user import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException,
    UserWithThisUsernameAlreadyExistsHttpException
)
from .response import ExceptionResponseTemplate


def register_exceptions_handler(app: FastAPI):
    app.exception_handler(HTTPException)(lambda request, exc: ExceptionResponseTemplate(request, exc).template)


__all__ = [
    "NotFoundDetailHttpException",
    "DetailAlreadyExistsHttpException",
    "NotFoundUserHttpException",
    "UserAlreadyExistsHttpException",
    "UserWithThisEmailAlreadyExistsHttpException",
    "UserWithThisUsernameAlreadyExistsHttpException",
    "register_exceptions_handler",
]
