import time
from functools import wraps
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                time_for_work = end - start
                success_message = (
                    f"'{func.__name__}' ok.\n"
                    f"Execution time: {time_for_work:.6f} seconds\n"
                )
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:  #
                        file.write(success_message)
                else:
                    print(success_message)
                return result
            except Exception as error:
                error_message = (
                    f"'{func.__name__}' error: {str(error)}.\n"
                    f"Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(error_message)
                else:
                    print(error_message)
                raise error

        return inner

    return wrapper


@log(filename="my_log.txt")  # Логи будут выводиться в файл
def add(x, y):
    return x + y

# @log()  # Логи будут выводиться в консоль
# def multipy(x, y):
#     if x == 0 or y == 0:
#         raise ValueError("Умножение на ноль")
#
#     return x * y
#
# print(multipy(1, 0))

# @log()  # Логи будут выводиться в консоль
# def add(x, y):
#     return x + y

# print(add(1, 0))
