from typing import Callable
from functools import wraps


def map_exceptions(to_catch, to_raise):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for i, exc_type in enumerate(to_catch):
                    if isinstance(e, exc_type):
                        new_exc = to_raise[i]
                        raise new_exc

        return wrapper

    return decorator
