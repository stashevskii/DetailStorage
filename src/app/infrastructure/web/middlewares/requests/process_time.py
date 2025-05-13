from time import perf_counter
from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, FastAPI
from starlette.responses import Response


class ProcessTimeHeader(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start = perf_counter()
        response = await call_next(request)
        response.headers["X-Process-Time"] = f"{perf_counter() - start:.5f}"
        return response


def register_process_time_middleware(app: FastAPI):
    app.add_middleware(ProcessTimeHeader)
