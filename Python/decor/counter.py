from typing import Callable, Any
from functools import wraps


def counter(func: Callable) -> Callable:
    """Декоратор для подсчёта и вывода количества вызовов переданной функции.

    Подсчитывает кол-во вызовов переданной функции, невзирая на различные её аргументы, выводит на экран.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Callable
    :return: Результат работы декоратора (ссылка на объект реализации функции-обёртки)
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обёртка для декорируемой функции, осуществляющая подсчёт кол-ва вызовов переданной функции.

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any

        :parameters 'name': Поля с именами переданных функций, хранящие значения счётчика.

        :rtype: Any
        :return: Результат, возвращаемый декорируемой функцией.
        """

        result = func(*args, **kwargs)
        name = func.__name__
        wrapper.name += 1
        print('Функция {0} вызывалась {1} раз.'.format(name, wrapper.name))

        return result

    name = func.__name__
    wrapper.name = 0

    return wrapper

@counter
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))

@counter
def farewell(name: str) -> None:
    print('Пока, {name}!'.format(name=name))


greeting("Том")
greeting("Том")
greeting("Jim")
farewell("Том")
greeting("Jim")
greeting("Том")
greeting("Jim")
farewell("Jim")
