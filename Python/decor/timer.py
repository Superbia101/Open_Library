from time import time
from typing import Callable, Any
import functools 


def timer(func: Callable) -> Callable:
    """Декоратор таймер. Возвращает результат работы переданной функции, выводи на экран её время работы.

    :param func: Переданная функция
    :type func: Callable

    :rtype: Any
    :return: Результат работы функции
    """

    @functools.wraps(func)
    def wrapped_func(*args: Any, **kwargs: Any) -> Any:
        started_time = time()
        result = func(*args, **kwargs)
        ended_time = time()
        func_time = ended_time - started_time
        print('Время выполнения функции: {} сек.'.format(func_time))

        return result
    return wrapped_func

@timer
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()
