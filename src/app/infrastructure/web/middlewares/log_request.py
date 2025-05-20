from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, FastAPI
from starlette.responses import Response
from src.app.core.utils import get_logger

log = get_logger(__name__)


class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        log.info("Incoming %s request to %s", request.method, request.url.path)
        return await call_next(request)


def register_log_request_middleware(app: FastAPI):
    app.add_middleware(LogRequestMiddleware)
