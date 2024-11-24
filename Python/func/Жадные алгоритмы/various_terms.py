"""Жадные алгоритмы"""


def various_terms() -> None:
    """Функция находит и выводит максимальное кол-во различных слагаемых переданного числа."""

    num_list = []
    n = int(input('Число: '))

    for i in range(1, n + 1):
        if n - i >= i + 1:
            num_list.append(str(i))
            n -= i
        else:
            num_list.append(str(n))
            break

    print(len(num_list))
    print(' '.join(num_list))


various_terms()