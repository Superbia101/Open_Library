"""Интервал чисел с 3-мя условиями: делится без остатка,
с остатком и сумма цифр < 10. по умолчанию создаёт нечётные от 0 до 1000."""


def my_funk(
    start: int = 0, finish: int = 1000, num1: int = 1, num2: int = 2, summa: int = 10
) -> list[int]:
    """Выводит числа в определённых границах, с условиями делимости с остатком и без,
    сумма цифр в которых меньше заданного.

    :param start: начало списка
    :type start: int
    :param finish: конец списка
    :type finish: int
    :param num1: значение условия делимости без остатка
    :type num1: int
    :param num2: значение условия делимости с остатком
    :type num2: int
    :param summa: значение условия границы суммы цифр
    :type summa: int

    :rtype: list[int]
    :return: list_num
    """

    list_num = [
        sum([int(str(i)[j]) for j in range(len(str(i)))]) < summa and i
        for i in range(start, finish + 1, num1)
        if i % num2 != 0
    ]

    # список чисел с 3-мя условиями, но лишними False
    for i in range(list_num.count(False)):  # удаляем лишние False
        list_num.remove(False)

    return list_num


if __name__ == "__main__":
    print(my_funk())
