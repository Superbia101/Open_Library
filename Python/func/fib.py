"""Число из последовательности Фибоначчи."""
"""num = int(input("Ведите число: "))
a, b = 1, 1

for _ in range(2, num):
    a, b = a + b, a

print(a)"""


def fib_rek(n: int) -> int:
    """Функция расчитывает рекурсивно, n-е число из последовательности Фибоначчи

    :param n: Порядковый номер числа
    :type n: int

    :raise AssertionError: n < 0

    :rtype: int
    :return: Число Фибоначи под номером n
    """

    assert n >= 0, 'Неверное значение параметра!'
    return n if n <= 1 else fib_rek(n - 1) + fib_rek(n - 2)


# print(fib_rek(8))


def fib_rek1(n: int) -> int:
    """Функция расчитывает, рекурсивно со словарём, n-е число из последовательности Фибоначчи

    :param n: Порядковый номер числа
    :type n: int

    :raise AssertionError: n < 0

    :rtype: int
    :return: Число Фибоначи под номером n
    """

    global cache
    cache = {}
    
    assert n >= 0, 'Неверное значение параметра!'
    
    if n not in cache:
        cache[n] = n if n <= 1 else fib_rek1(n - 1) + fib_rek1(n - 2)

    return cache[n]


# print(fib_rek1(20))


# через декоратор
def memo(f):
    def inner(n):
        cache = {}
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


print(memo(fib_rek1)(20))

# более эффективный алгоритм O(log(n)**2)
def qfib(n, with_next=False):    
    if n < 2:
        response = [n, 1]
    else:
        fa, fb = qfib(n//2, with_next=True)
        if n % 2 == 1:
            response = [fa**2 + fb**2,
                        fb * (fb + fa) + fa * fb,]
        else:
            response = [fa * (fb - fa) + fa * fb,
                        fa**2 + fb**2]
    if with_next:
        return response
    return response [0]


"""Даны целые числа (1 <= n <= 10**18) и (2 <= m <= 10**5), необходимо
найти остаток от деления n-го числа Фибоначчи на m."""

def fib_mod(n: int, m: int) -> int:
    """Функция находит отстаток от деления n-го числа Фибоначчи на m, используя период Пизано.

    :param n: Порядковый номер числа №1 - делимое
    :type n: int
    :param m: Порядковый номер числа №2 - делитель
    :type m: int

    :raise AssertionError: n <= 0 | m <= 0

    :rtype: int
    :return: Остаток от деления n-го числа Фибоначчи на m
    """

    assert n > 0 and m > 0, 'Неверное значение параметра!'
    
    a: int = 1
    b: int = 1
    list_mod: list[int] = [0, 1]
    
    while True:
        a, b = a + b, a
        list_mod.append(b % m)
        
        if list_mod[-2:] == [0, 1]:
            break
    
    return list_mod[n % (len(list_mod) - 2)]


# print(fib_mod(1598753, 25897))
