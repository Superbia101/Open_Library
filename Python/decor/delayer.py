from typing import Callable, Any
from functools import wraps
from time import sleep


def delayer(func: Callable) -> Callable:
    """Декоратор, который замедляет выполнение декорируемой функции на 5 секунд.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Any
    :return: Результат работы декоратора (ссылка на объект реализации функции-обёртки)
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обёртка для декорируемой функции, осуществляющая задержку перед вызовом.

        Задерживает выполнение на 2 секунды, а затем вызывает оригинальную функцию с переданными ей аргументами.

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any

        :rtype: Any
        :return: Результат, возвращаемый декорируемой функцией.
        """

        sleep(5)
        return func(*args, **kwargs)

    return wrapper


@delayer
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
