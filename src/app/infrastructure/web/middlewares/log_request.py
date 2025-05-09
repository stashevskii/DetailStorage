from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import Response
from src.app.core.utils import get_logger

log = get_logger(__name__)


class LogRequestMiddleware(BaseHTTPMiddleware):
    def dispatch(self, request: Request, call_next: Callable) -> Response:
        log.info("Input %s request to %s", request.method, request.url.path)
        return call_next(request)
