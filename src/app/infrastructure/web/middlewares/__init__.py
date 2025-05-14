from src.app.infrastructure.web.middlewares.log_request import register_log_request_middleware
from src.app.infrastructure.web.middlewares.process_time import register_process_time_middleware
from src.app.infrastructure.web.middlewares.cors import register_cors_middleware


def register_middlewares(app):
    register_cors_middleware(app)
    register_log_request_middleware(app)
    register_process_time_middleware(app)


__all__ = ["register_middlewares"]
