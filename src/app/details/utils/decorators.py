from typing import Callable, Any
from functools import wraps


def map_exceptions(to_catch, to_raise):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except to_catch:
                raise to_raise

        return wrapper
    return decorator
