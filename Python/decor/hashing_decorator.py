from typing import Callable, Any
from functools import wraps


def hashing_decorator(func: Callable) -> Callable:
    """Декоратор для кеширования результатов выполнения функции, которая принимает одно целое число
    и возвращает целое число.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Callable
    :return: Результат работы декоратора (ссылка на объект реализации функции-обёртки)
    """

    dict_fib_num = {}

    @wraps(func)
    def wrapper(number: int) -> int:
        """Обёртка для декорируемой функции, осуществляющая подсчёт времени выполнения переданной функции.

        :param number: Целое число, для которого необходимо получить результат.
        :type number: int

        :rtype: int
        :return: Результат выполнения функции. Если функция уже вызывалась с данным аргументом, результат берётся из кеша.
        """

        if number not in dict_fib_num:
            dict_fib_num[number] = func(number)
        return dict_fib_num[number]

    return wrapper


@hashing_decorator
def fibonacci(number: int) -> int:
    """Рекурсивная функция вычисления чисел Фибонначи.

    :param number: Номер числа
    :type number: int

    :rtype: int
    :return: Число ряда Фибонначи по переданным номером
    """

    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
