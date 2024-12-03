from typing import Callable, Any
import functools 

def do_twice(func: Callable) -> Callable:
    """Декоратор двойного вызова выводящей на экран функции.

    :param func: Вызываемая функция, выводящая сообщение на экран
    :type func: Callable

    :rtype: Callable
    :return: Двойной вызов переданной функции
    """

    @functools.wraps(func)
    def wrapped_func(*args: Any, **kwargs: Any) -> None:
        for _ in range(2):
            func(*args, **kwargs)

    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
