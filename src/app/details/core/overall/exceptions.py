from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


def internal_server_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": "Internal server error"})


def not_found_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=404, content={"message": "Not found"})


not_found_detail_exception = HTTPException(status_code=422, detail="Detail not found")

global_exception_handlers = {500: internal_server_error,
                             404: not_found_error}
