from typing import Callable, Any, Optional
from functools import wraps
from time import sleep


def delayer(_func: Optional[Callable] = None, *, time: int = 1) -> Callable:
    """Декоратор настраиваемого замедления функции.

    :param _func: Переданная функция
    :type _func: Optional[Callable]
    :param time: Кол-во секунд ожидания
    :type time: int

    :rtype: Callable
    :return: Объект реализации обёртки
    """

    def delayer_decorator(func: Callable) -> Callable:
        """Декоратор обёртка параметра.

        :param func: Вызываемая функция, выводящая сообщение на экран
        :type func: Callable

        :rtype: Callable
        :return: Объект реализации внутренней обёртки
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка для декорируемой функции, осуществляющая замедленный вызов переданной функции.

            :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
            :type args: Any
            :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
            :type kwargs: Any

            :rtype: Any
            :return: Результат, возвращаемый декорируемой функцией.
            """

            sleep(time)
            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return delayer_decorator
    return delayer_decorator(_func)


def slowing_five_seconds(func: Callable) -> Callable:
    """Декоратор, который замедляет выполнение декорируемой функции на 5 секунд.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Any
    :return: Результат работы декоратора (ссылка на объект реализации функции-обёртки)
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обёртка для декорируемой функции, осуществляющая задержку перед вызовом.

        Задерживает выполнение на 5 секунд, а затем вызывает оригинальную функцию с переданными ей аргументами.

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


@delayer(time=5)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
