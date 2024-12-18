from time import time
from typing import Callable, Any
from functools import update_wrapper


class LoggerDecorator:
    """Класс-декоратор, производит логирование переданной функции."""

    __func: Callable[..., Any]

    def __init__(self, func: Callable[..., Any]) -> None:
        update_wrapper(self, func)
        self.__func = func

    @property
    def func(self) -> Callable[..., Any]:
        return self.__func

    @func.setter
    def func(self, func: Callable[..., Any]) -> None:
        self.__func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('Вызов функции {}'.format(self.func.__name__))
        print('Аргументы: {0} {1}'.format(args, kwargs))
        started_time = time()
        results = self.func(*args, **kwargs)
        ended_time = time()
        func_time = ended_time - started_time
        print('Результат: {}'.format(results))
        print('Время выполнения функции: {} сек.'.format(func_time))
        return results


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
