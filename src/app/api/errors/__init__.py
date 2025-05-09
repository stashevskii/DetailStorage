from .http.detail import NotFoundDetailHttpException, DetailAlreadyExistsHttpException
from .http.user import (
    NotFoundUserHttpException,
    UserAlreadyExistsHttpException,
    UserWithThisEmailAlreadyExistsHttpException,
    UserWithThisUsernameAlreadyExistsHttpException
)
from .register import register_exceptions_handler
from .template import ExceptionResponseTemplate

__all__ = [
    "NotFoundDetailHttpException",
    "DetailAlreadyExistsHttpException",
    "NotFoundUserHttpException",
    "UserAlreadyExistsHttpException",
    "UserWithThisEmailAlreadyExistsHttpException",
    "UserWithThisUsernameAlreadyExistsHttpException",
    "register_exceptions_handler",
    "ExceptionResponseTemplate",
]
