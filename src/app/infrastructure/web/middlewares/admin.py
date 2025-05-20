from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, FastAPI, HTTPException, status
from fastapi.responses import Response, JSONResponse

from src.app.api.errors.auth import forbidden
from src.app.core.utils import get_logger
from src.app.infrastructure.config import config

log = get_logger(__name__)


class AdminMiddleware(BaseHTTPMiddleware):
    @staticmethod
    def __forbidden():
        log.warning("Unsuccessful try to use admin panel")
        return forbidden

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if not request.url.path.startswith(config.admin_router_config.prefix):
            return await call_next(request)

        try:
            if request.headers["X-Admin"] != config.admin_config.admin_password:
                return self.__forbidden()
        except KeyError:
            return self.__forbidden()

        log.info("Admitted to use admin panel")
        return await call_next(request)


def register_admin_middleware(app: FastAPI):
    app.add_middleware(AdminMiddleware)
