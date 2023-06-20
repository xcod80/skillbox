import functools
from typing import Callable

def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    def decor(*args, **kwargs):
        @functools.wraps(func)
        def wrapper(func):
            print('Переданные арги и кварги в декоратор:', args, kwargs)
            result = func
            return result
        return wrapper
    return decor

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(func):
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)