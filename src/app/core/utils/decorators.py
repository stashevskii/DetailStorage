from typing import Callable
from functools import wraps

from src.app.infrastructure.web.logger import get_logger

log = get_logger(__name__)


def map_exceptions(ex: dict) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for to_catch, to_raise in ex.items():
                    if isinstance(e, to_catch):
                        log.info("Raising exception %s", to_raise.__name__)
                        raise to_raise

        return wrapper

    return decorator
