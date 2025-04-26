from fastapi import Request
from fastapi.responses import JSONResponse


class ExceptionResponseTemplate:
    def __init__(self, request: Request, exc):
        self.request = request
        self.exc = exc

    def __str__(self):
        return JSONResponse(
            status_code=self.exc.status_code,
            content={
                "status_code": self.exc.status_code,
                "url": self.request.url.path,
                "method": self.request.method,
                "message": self.exc.detail,
                "headers": self.exc.headers
            },
            headers=self.exc.headers
        )
