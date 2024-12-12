from typing import Callable, Any, Optional
from functools import wraps


def repeat(_func: Optional[Callable] = None, *, quantity: int = 1) -> Callable:
    """Декоратор множественного вызова выводящей на экран функции.

    :param _func: Переданная функция
    :type _func: Optional[Callable]
    :param quantity: Кол-во вызовов
    :type quantity: int

    :rtype: Callable
    :return: Объект реализации обёртки
    """

    def repeat_decorator(func: Callable) -> Callable:
        """Декоратор обёртка параметра.

        :param func: Вызываемая функция, выводящая сообщение на экран
        :type func: Callable

        :rtype: Callable
        :return: Объект реализации внутренней обёртки
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            """Обёртка для декорируемой функции, осуществляющая множественный вызов переданной функции.

            :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
            :type args: Any
            :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
            :type kwargs: Any
            """

            for _ in range(quantity):
                func(*args, **kwargs)

        return wrapper

    if _func is None:
        return repeat_decorator
    return repeat_decorator(_func)


def do_twice(func: Callable) -> Callable:
    """Декоратор двойного вызова выводящей на экран функции.

    :param func: Вызываемая функция, выводящая сообщение на экран
    :type func: Callable

    :rtype: Callable
    :return: Двойной вызов переданной функции
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        """Обёртка для декорируемой функции, осуществляющая двойной вызов переданной функции.

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any
        """

        for _ in range(2):
            func(*args, **kwargs)

    return wrapper


@repeat(quantity=3)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')