from src.app.infrastructure.web.middlewares.requests.log import register_log_request_middleware
from src.app.infrastructure.web.middlewares.requests.process_time import register_process_time_middleware


def register_middlewares(app, log):
    register_log_request_middleware(app, log)
    register_process_time_middleware(app)

__all__ = ["register_middlewares"]
