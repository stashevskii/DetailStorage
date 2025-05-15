from typing import Callable
from functools import wraps
from .logger import get_logger

log = get_logger(__name__)


def map_exceptions(ex: dict[Exception: Exception]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for to_catch, to_raise in ex.items():
                    if isinstance(e, to_catch):
                        log.info("Raising exception %s", to_raise.__name__)
                        raise to_raise

        return wrapper

    return decorator
