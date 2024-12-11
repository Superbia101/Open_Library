from typing import Callable, Any
from collections.abc import Iterator
from contextlib import contextmanager
import time


def timed(func: Callable, *args: Any, n_iter: int = 100) -> float:
    """Считает минимальное время выполнения переданной функции.

    :param func: Переданная функция
    :type func: Callable
    :param args: Аргументы функции
    :type args: Any
    :param n_iter: Кол-во подсчётов
    :type n_iter: int

    :rtype: float
    :return: Минимальное время выполнения переданной функции
    """

    acc = float("inf")  # бесконечно большое значение

    for i in range(n_iter):  # подсчёты
        time_start = time.perf_counter()  # время до
        func(*args)
        time_finish = time.perf_counter()  # время после
        acc = min(acc, time_finish - time_start)  # мин время выполнения функции (разность после функции и до)

    return acc


@contextmanager
def timer() -> Iterator:
    """Функция таймер в качестве контекст-менеджера. Работает с оператором with и замерять время работы вложенного кода.

    :return: Возвращает время между запросами
    """

    start = time.time()

    try:
        yield

    finally:
        print(time.time() - start)


with timer() as t1:
    pass
