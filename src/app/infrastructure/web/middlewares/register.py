from fastapi import FastAPI

from .log_request import LogRequestMiddleware


def register_middlewares(app: FastAPI) -> None:
    app.add_middleware(LogRequestMiddleware)
