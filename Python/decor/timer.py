from time import time
from typing import Callable, Any
from functools import wraps


def timer(func: Callable) -> Callable:
    """Декоратор таймер. Возвращает результат работы переданной функции, выводи на экран её время работы.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Callable
    :return: Результат работы декоратора (ссылка на объект реализации функции-обёртки)
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обёртка для декорируемой функции, осуществляющая подсчёт времени выполнения переданной функции.

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any

        :rtype: Any
        :return: Результат, возвращаемый декорируемой функцией.
        """

        started_time = time()
        result = func(*args, **kwargs)
        ended_time = time()
        func_time = ended_time - started_time
        print('Время выполнения функции: {} сек.'.format(func_time))

        return result

    return wrapper

@timer
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()
