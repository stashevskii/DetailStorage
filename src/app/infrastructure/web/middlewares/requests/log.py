from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, FastAPI
from starlette.responses import Response


class LogRequestMiddleware(BaseHTTPMiddleware):
    def __init__(self, *args, log, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = log

    def dispatch(self, request: Request, call_next: Callable) -> Response:
        self.log.info("Incoming %s request to %s", request.method, request.url.path)
        return call_next(request)


def register_log_request_middleware(app: FastAPI, log):
    app.add_middleware(LogRequestMiddleware, log=log)
