from starlette.exceptions import HTTPException
from fastapi import FastAPI
from src.app.api.errors.template import ExceptionResponseTemplate


def register_exceptions_handler(app: FastAPI):
    app.exception_handler(HTTPException)(lambda request, exc: ExceptionResponseTemplate(request, exc).__str__())
