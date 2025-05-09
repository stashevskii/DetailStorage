from fastapi import Request
from fastapi.responses import JSONResponse
from src.app.infrastructure.web.logger import get_logger

log = get_logger(__name__)


class ExceptionResponseTemplate:
    def __init__(self, request: Request, exc):
        self.request = request
        self.exc = exc

    def __str__(self):
        log.error("HTTP error %s: %s", self.exc.status_code, self.exc.detail)
        return JSONResponse(
            status_code=self.exc.status_code,
            content={
                "status_code": self.exc.status_code,
                "url": self.request.url.path,
                "method": self.request.method,
                "message": self.exc.detail,
                "headers": self.exc.headers,
                "client": {
                    "host": self.request.client.host,
                    "port": self.request.client.port
                }
            },
            headers=self.exc.headers
        )
