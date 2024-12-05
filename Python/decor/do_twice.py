from typing import Callable, Any
from functools import wraps

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

@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
