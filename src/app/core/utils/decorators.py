from typing import Callable, Any
from functools import wraps


def map_exceptions(ex: dict) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for to_catch, to_raise in ex.items():
                    if isinstance(e, to_catch):
                        raise to_raise

        return wrapper

    return decorator
