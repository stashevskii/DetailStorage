from fastapi import Request
from fastapi.responses import JSONResponse


def internal_server_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": "Internal server error"})


def not_found_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=404, content={"message": "Not found"})


def unprocessable_entity_error(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=422, content={"success": False, "message": "Unprocessable entity"})


exception_handlers = {500: internal_server_error, 404: not_found_error, 422: unprocessable_entity_error}
